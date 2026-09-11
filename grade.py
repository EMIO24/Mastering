"""Offline course grader. Run `python grade.py --help` for commands."""
import argparse
import hashlib
import json
import math
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def stamp():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def assignment(lesson):
    if not 1 <= lesson <= 40:
        raise ValueError('Lesson must be between 1 and 40.')
    week = (lesson - 1) // 3 + 1
    return ROOT / f'week-{week:02}' / 'assignments' / f'lesson-{lesson:02}'


def read_json(path, default=None):
    if not path.exists() and default is not None:
        return default
    return json.loads(path.read_text(encoding='utf-8-sig'))


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    temporary.replace(path)


def load_rubric(lesson):
    rubric = read_json(assignment(lesson) / 'rubric.json')
    criteria = rubric['criteria']
    if rubric['lesson'] != lesson or rubric['status'] not in ('ready', 'provisional'):
        raise ValueError(f'Invalid rubric metadata for lesson {lesson}.')
    if len({item['id'] for item in criteria}) != len(criteria):
        raise ValueError('Rubric criterion IDs must be unique.')
    if sum(item['points'] for item in criteria) != 100:
        raise ValueError('Rubric points must total 100.')
    for item in criteria:
        if item['mode'] not in ('auto', 'manual') or item['points'] <= 0:
            raise ValueError('Every criterion needs positive points and auto/manual mode.')
    entry = Path(rubric['entrypoint'])
    if entry.is_absolute() or '..' in entry.parts:
        raise ValueError('Entrypoint must be a relative path inside the assignment.')
    return rubric


def fingerprint(folder):
    """Tie marks to submission content, including written answers and rubric."""
    digest = hashlib.sha256()
    ignored = {'__pycache__', '.git', '.venv', 'venv', 'node_modules'}
    for path in sorted(folder.rglob('*')):
        if path.is_file() and not any(part in ignored for part in path.relative_to(folder).parts):
            digest.update(path.relative_to(folder).as_posix().encode('utf-8'))
            digest.update(b'\0')
            digest.update(path.read_bytes())
            digest.update(b'\0')
    return digest.hexdigest()


def engine_fingerprint():
    digest = hashlib.sha256()
    for path in (ROOT / 'grade.py', ROOT / 'grading' / 'worker.py', ROOT / 'grading' / 'week1.py'):
        if path.exists():
            digest.update(path.read_bytes())
    return digest.hexdigest()


def marks_path(lesson):
    return ROOT / 'grading' / 'marks' / f'lesson-{lesson:02}.json'


def report_path(lesson):
    return ROOT / 'grading' / 'reports' / f'lesson-{lesson:02}.json'


def automatic_checks(lesson, rubric, timeout):
    criteria = [c for c in rubric['criteria'] if c['mode'] == 'auto']
    if not criteria:
        return {}
    def failures(message):
        return {c['id']: {'passed': False, 'feedback': message} for c in criteria}
    source = assignment(lesson) / rubric['entrypoint']
    if not source.is_file():
        return failures(f'Missing entrypoint: {rubric["entrypoint"]}. Complete it or update rubric.json.')
    if rubric.get('engine') == 'prediction':
        # JSON answers are data, never imported or executed.
        try:
            answers = read_json(source)
            if not isinstance(answers, dict):
                raise ValueError('The submission must be a JSON object.')
        except (ValueError, OSError) as error:
            return failures(f'Cannot read submission.json: {error}')
        result = {}
        for item in criteria:
            value = answers.get(item['id'])
            expected = item['expected']
            passed = json.dumps(value, sort_keys=True) == json.dumps(expected, sort_keys=True)
            feedback = ('Correct worked-example prediction. Practical implementation still requires review.'
                        if passed else
                        'Missing or incorrect prediction. Trace the example and check JSON types, then retry.')
            result[item['id']] = {'passed': passed, 'feedback': feedback}
        return result
    # Relative paths and __file__ now refer to the disposable copy. This is
    # protection from ordinary assignment file writes, not a security sandbox.
    with tempfile.TemporaryDirectory(prefix='emio24-grade-') as temporary:
        work = Path(temporary)
        copied = work / 'submission'
        shutil.copytree(assignment(lesson), copied,
                        ignore=shutil.ignore_patterns('__pycache__', '.git', '.venv', 'venv', 'node_modules'))
        output = work / 'results.json'
        config = work / 'rubric.json'
        write_json(config, rubric)
        command = [sys.executable, '-I', str(ROOT / 'grading' / 'worker.py'),
                   str(copied / rubric['entrypoint']), str(config), str(output)]
        try:
            completed = subprocess.run(command, cwd=copied, stdin=subprocess.DEVNULL,
                                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                       timeout=timeout, check=False)
        except subprocess.TimeoutExpired:
            return failures(f'Timed out after {timeout:g}s. Check for an infinite loop or blocking input; no automatic marks awarded in this run.')
        if completed.returncode != 0 or not output.is_file():
            return failures(f'Worker exited without usable results (exit {completed.returncode}). Check import-time code or process exits.')
        result = read_json(output)
        if set(result) != {c['id'] for c in criteria}:
            return failures('Worker returned incomplete results.')
        return result


def build_report(lesson, timeout=15):
    folder = assignment(lesson)
    rubric = load_rubric(lesson)
    signature = fingerprint(folder)
    auto = automatic_checks(lesson, rubric, timeout)
    marks = read_json(marks_path(lesson), {})
    rows = []
    for item in rubric['criteria']:
        row = dict(item)
        if item['mode'] == 'auto':
            outcome = auto[item['id']]
            row.update(score=item['points'] if outcome['passed'] else 0,
                       state='passed' if outcome['passed'] else 'failed', feedback=outcome['feedback'])
        else:
            mark = marks.get(item['id'])
            if mark is None:
                row.update(score=None, state='pending', feedback='Manual review and evidence required.')
            elif mark.get('fingerprint') != signature:
                row.update(score=None, state='stale', feedback='Submission changed since this manual mark. Review again. Previous note: ' + mark.get('note', ''))
            elif (type(mark.get('score')) not in (int, float)
                  or not math.isfinite(mark['score']) or not 0 <= mark['score'] <= item['points']
                  or not str(mark.get('note', '')).strip()):
                raise ValueError(f'Invalid saved manual mark for {item["id"]}.')
            else:
                row.update(score=mark['score'], state='reviewed', feedback=mark['note'])
        rows.append(row)
    earned = sum(row['score'] or 0 for row in rows)
    pending = sum(row['points'] for row in rows if row['score'] is None)
    failed_gate = any(row.get('gate') and row['score'] != row['points'] for row in rows)
    # The diagnostic requires half the available marks in every section.
    section_ok = True
    if lesson == 1:
        for section in ('A', 'B', 'C', 'D', 'E'):
            group = [row for row in rows if row.get('section') == section]
            section_ok &= sum(row['score'] or 0 for row in group) >= sum(row['points'] for row in group) / 2
    if rubric['status'] == 'provisional':
        state = 'PROVISIONAL: REVIEW PENDING' if pending else 'PROVISIONAL: SCORED'
    elif pending:
        state = 'REVIEW PENDING'
    elif earned >= 80 and not failed_gate and section_ok:
        state = 'PASS'
    else:
        state = 'NEEDS PRACTICE'
    return dict(lesson=lesson, week=rubric['week'], rubric_status=rubric['status'],
                checked_at=stamp(), fingerprint=signature, engine=engine_fingerprint(),
                earned=earned, pending=pending, maximum=100, state=state, criteria=rows)


def markdown_report(report):
    lines = [f'# Lesson {report["lesson"]} feedback', '', f'**{report["state"]}**', '',
             f'Earned: **{report["earned"]:g}/100**. Awaiting manual review: **{report["pending"]:g} points**.', '',
             'Pending points are not failed points. A final grade requires all manual criteria to be reviewed.', '',
             f'Checked at: {report["checked_at"]}', '']
    for row in report['criteria']:
        score = 'pending' if row['score'] is None else f'{row["score"]:g}'
        lines += [f'## {row["id"]}: {score}/{row["points"]} ({row["state"]})', '',
                  row['description'], '', row['feedback'], '']
    return '\n'.join(lines)


def save_report(report):
    path = report_path(report['lesson'])
    write_json(path, report)
    path.with_suffix('.md').write_text(markdown_report(report), encoding='utf-8')


def saved_status(lesson):
    path = report_path(lesson)
    if not path.exists():
        return 'NOT CHECKED', '-', '-'
    report = read_json(path)
    marks = read_json(marks_path(lesson), {})
    changed_mark = any(mark.get('marked_at', '') > report['checked_at'] for mark in marks.values())
    if (report['fingerprint'] != fingerprint(assignment(lesson))
            or report.get('engine') != engine_fingerprint() or changed_mark):
        return 'STALE: RUN CHECK', '-', '-'
    return report['state'], f'{report["earned"]:g}/100', str(report['pending'])


def gradebook():
    lines = ['# Offline assignment gradebook', '',
             'PASS requires a ready rubric, completed manual review, at least 80/100, and required mastery gates. Provisional rubrics never produce PASS.', '',
             '| Week | Lesson | Status | Earned | Pending points |',
             '| --- | --- | --- | --- | --- |']
    for lesson in range(1, 41):
        state, earned, pending = saved_status(lesson)
        lines.append(f'| {(lesson-1)//3+1} | {lesson} | {state} | {earned} | {pending} |')
    target = ROOT / 'grading' / 'gradebook.md'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def selection(args):
    if getattr(args, 'lesson', None) is not None:
        assignment(args.lesson)
        return [args.lesson]
    if getattr(args, 'week', None) is not None:
        if not 1 <= args.week <= 14:
            raise ValueError('Week must be between 1 and 14.')
        return list(range((args.week-1)*3+1, min(args.week*3, 40)+1))
    return list(range(1, 41))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('check', 'status'):
        command = commands.add_parser(name, help='Run checks and save feedback' if name == 'check' else 'Show saved grades and stale results')
        group = command.add_mutually_exclusive_group()
        group.add_argument('--lesson', type=int)
        group.add_argument('--week', type=int)
        group.add_argument('--all', action='store_true', help='All 40 lessons (the default)')
        if name == 'check':
            command.add_argument('--timeout', type=float, default=15, help='Worker time limit in seconds per assignment (default 15, max 120)')
    rubric_cmd = commands.add_parser('rubric', help='Show criterion IDs, points, and grading instructions')
    rubric_cmd.add_argument('--lesson', type=int, required=True)
    mark = commands.add_parser('mark', help='Record an evidence-backed manual score; then recheck the lesson')
    mark.add_argument('--lesson', type=int, required=True)
    mark.add_argument('--criterion', required=True)
    mark.add_argument('--score', type=float, required=True)
    mark.add_argument('--note', required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == 'rubric':
            rubric = load_rubric(args.lesson)
            print(f'Lesson {args.lesson}: {rubric["status"]} rubric, 100 points')
            for row in rubric['criteria']:
                print(f'{row["id"]:22} {row["points"]:3} {row["mode"]:6} {row["description"]}')
            return 0
        if args.command == 'mark':
            rubric = load_rubric(args.lesson)
            row = next((row for row in rubric['criteria'] if row['id'] == args.criterion), None)
            if row is None or row['mode'] != 'manual':
                raise ValueError('Choose a manual criterion ID from the rubric command.')
            if not math.isfinite(args.score) or not 0 <= args.score <= row['points']:
                raise ValueError(f'Score must be between 0 and {row["points"]}.')
            if not args.note.strip():
                raise ValueError('Provide a note describing the evidence reviewed.')
            marks = read_json(marks_path(args.lesson), {})
            marks[args.criterion] = dict(score=args.score, note=args.note.strip(), marked_at=stamp(),
                                        fingerprint=fingerprint(assignment(args.lesson)))
            write_json(marks_path(args.lesson), marks)
            save_report(build_report(args.lesson))
            gradebook()
            print(f'Saved {args.criterion}: {args.score:g}/{row["points"]}. Updated lesson feedback and gradebook.')
            return 0
        lessons = selection(args)
        if args.command == 'check' and (not math.isfinite(args.timeout) or not 0 < args.timeout <= 120):
            raise ValueError('Timeout must be greater than 0 and at most 120 seconds.')
        incomplete = False
        for lesson in lessons:
            if args.command == 'check':
                report = build_report(lesson, args.timeout)
                save_report(report)
            state, earned, pending = saved_status(lesson)
            print(f'Lesson {lesson:02}: {state:28} Earned {earned:8} Pending {pending}')
            incomplete |= state != 'PASS'
            if args.command == 'check' and len(lessons) == 1:
                for row in report['criteria']:
                    if row['state'] in ('failed', 'stale'):
                        print(f'  {row["id"]}: {row["feedback"]}')
        if args.command == 'check':
            gradebook()
            print('Saved feedback in grading/reports/ and grading/gradebook.md')
            return 1 if incomplete else 0
        return 0
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(f'Checker error: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())

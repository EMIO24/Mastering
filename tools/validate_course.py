"""Check course coverage, grading metadata, links and standalone lesson examples."""
import contextlib
import importlib.util
import io
import json
import re
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import grade
from tools.build_course import LESSONS
from tools.detailed_assignments import DETAILS, REVIEW_FOCUS

errors = []
for n in range(1,41):
    folder = grade.assignment(n)
    brief = (folder/'README.md').read_text(encoding='utf-8-sig')
    numbers = [int(v) for v in re.findall(r'^## Exercise (\d+):', brief, re.M)]
    if numbers != list(range(1,11)):
        errors.append(f'Lesson {n}: exercise numbering {numbers}')
    rubric = grade.load_rubric(n)
    if rubric['status'] != 'ready':
        errors.append(f'Lesson {n}: rubric not ready')
    teaching = ROOT/f'week-{(n-1)//3+1:02}'/f'lesson-{n:02}'/'teaching.md'
    if not teaching.exists() or len(teaching.read_text(encoding='utf-8').split()) < 300:
        errors.append(f'Lesson {n}: missing or undersized teaching notes')
    if n >= 4 and len(rubric['criteria']) != 10:
        errors.append(f'Lesson {n}: expected 10 grading criteria')

# Every later practical task must retain its individually authored instructions.
if set(DETAILS) != set(range(4, 41)) or set(REVIEW_FOCUS) != set(range(4, 41)):
    errors.append('Incomplete detailed assignment coverage')
for item in LESSONS:
    number = item['number']
    brief = (grade.assignment(number) / 'README.md').read_text(encoding='utf-8-sig')
    bodies = DETAILS.get(number, [])
    if len(bodies) != 7:
        errors.append(f'Lesson {number}: expected seven individually authored practical briefs')
    for exercise, body in enumerate(bodies, 3):
        if body not in brief or '**Check:**' not in body or len(re.findall(r'^\d+\. ', body, re.M)) < 3:
            errors.append(f'Lesson {number} exercise {exercise}: detailed instructions/check missing')
    if REVIEW_FOCUS.get(number, 'MISSING') not in brief:
        errors.append(f'Lesson {number}: topic-specific verification guidance missing')

for path in ROOT.rglob('*.md'):
    if any(part in ('node_modules','.venv','.git','__pycache__') for part in path.parts):
        continue
    source=path.read_text(encoding='utf-8-sig')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', source):
        if target.startswith(('https://','http://','#','mailto:')):
            continue
        target=target.split('#')[0].replace('%20',' ')
        if target and not (path.parent/target).exists():
            errors.append(f'Broken link: {path.relative_to(ROOT)} -> {target}')

# Independently execute the standalone Python examples and compare known outcomes.
expected={4:'3 7',5:'Pen (NGN)',6:'cash:600\ntransfer:600',7:'600',10:'localhost 8000 /products',13:"[('Pen',)]",15:'5'}
for item in LESSONS:
    n=item['number']
    if n in expected:
        log=io.StringIO()
        with contextlib.redirect_stdout(log):
            exec(compile(item['code'],f'lesson-{n}-example','exec'), {'__name__':'__main__'})
        if log.getvalue().strip()!=expected[n]:
            errors.append(f'Lesson {n}: example output mismatch')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print('Validated: 40 lessons, 400 exercises, 40 ready rubrics totaling 100 each, local Markdown links, and 7 standalone Python examples.')

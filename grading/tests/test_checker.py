"""Regression tests for the checker, using temporary fictional submissions."""
import contextlib
import importlib.util
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path

COURSE = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('course_grader', COURSE / 'grade.py')
grade = importlib.util.module_from_spec(spec)
spec.loader.exec_module(grade)

# Function fixtures test the grader. They intentionally do not implement a CLI.
GOOD = '''
import csv
import json
from pathlib import Path

def stock_label(stock):
    return 'out' if stock == 0 else 'low' if stock <= 5 else 'available'
def inventory_value(records):
    return sum(p['price'] * p['stock'] for p in records)
def low_stock_names(records, threshold):
    return [p['name'] for p in records if p['stock'] <= threshold]
def find_product(records, product_id):
    return next((p for p in records if p['id'] == product_id), None)
def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Enter a whole number')
            continue
        if value > 0:
            return value
        print('Enter a positive number')
def sell_product(product, quantity):
    if type(quantity) is not int or quantity <= 0 or quantity > product['stock']:
        raise ValueError('Invalid quantity')
    product['stock'] -= quantity
    return product['price'] * quantity

def validate_inventory(records):
    if not isinstance(records, list):
        raise ValueError('Expected list')
    ids = set()
    for p in records:
        if not isinstance(p, dict) or not {'id','name','price','stock'}.issubset(p):
            raise ValueError('Missing fields')
        if type(p['id']) is not int or p['id'] <= 0 or p['id'] in ids:
            raise ValueError('Invalid ID')
        ids.add(p['id'])
        if not isinstance(p['name'], str) or not p['name'].strip():
            raise ValueError('Invalid name')
        for field in ('price','stock'):
            if type(p[field]) is not int or p[field] < 0:
                raise ValueError('Invalid number')
def load_inventory(path):
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    validate_inventory(data)
    return data

def save_inventory(path, records):
    validate_inventory(records)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.json.tmp')
    with open(temporary, 'w', encoding='utf-8') as f:
        json.dump(records, f)
    temporary.replace(path)

def export_csv(path, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ['id','name','price','stock']
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(records)
'''


class CheckerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='grader-test-')
        self.root = Path(self.temp.name)
        grade.ROOT = self.root
        (self.root / 'grading').mkdir()
        shutil.copy2(COURSE / 'grade.py', self.root / 'grade.py')
        for filename in ('worker.py', 'week1.py'):
            shutil.copy2(COURSE / 'grading' / filename, self.root / 'grading' / filename)
        for lesson in range(1, 41):
            folder = grade.assignment(lesson)
            folder.mkdir(parents=True)
            original = COURSE / folder.relative_to(self.root)
            shutil.copy2(original / 'rubric.json', folder / 'rubric.json')
            (folder / 'starter.py').write_text(GOOD, encoding='utf-8')

    def tearDown(self):
        grade.ROOT = COURSE
        self.temp.cleanup()

    def manual_full_marks(self, lesson):
        rubric = grade.load_rubric(lesson)
        marks = {c['id']: dict(score=c['points'], note='Demonstrated against fixture requirements',
                              marked_at=grade.stamp(), fingerprint=grade.fingerprint(grade.assignment(lesson)))
                 for c in rubric['criteria'] if c['mode'] == 'manual'}
        grade.write_json(grade.marks_path(lesson), marks)

    def run_cli(self, args):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return grade.main(args)

    def test_all_rubrics_total_100(self):
        for lesson in range(1, 41):
            self.assertEqual(sum(c['points'] for c in grade.load_rubric(lesson)['criteria']), 100)

    def test_correct_functions_and_pending_manual(self):
        for lesson, points in ((1, 40), (2, 65), (3, 35)):
            report = grade.build_report(lesson)
            self.assertEqual(report['earned'], points, report)
            self.assertEqual(report['pending'], 100-points)
            self.assertEqual(report['state'], 'REVIEW PENDING')

    def test_complete_review_passes(self):
        for lesson in (1, 2, 3):
            self.manual_full_marks(lesson)
            report = grade.build_report(lesson)
            self.assertEqual(report['state'], 'PASS', report)
            self.assertEqual(report['earned'], 100)

    def test_diagnostic_section_threshold(self):
        self.manual_full_marks(1)
        marks = grade.read_json(grade.marks_path(1))
        marks['types']['score'] = 0
        grade.write_json(grade.marks_path(1), marks)
        report = grade.build_report(1)
        self.assertEqual(report['earned'], 80)
        self.assertEqual(report['state'], 'NEEDS PRACTICE')

    def test_critical_gate_prevents_pass_at_90(self):
        path = grade.assignment(2) / 'starter.py'
        path.write_text(GOOD.replace("return product['price'] * quantity", 'return 0'), encoding='utf-8')
        self.manual_full_marks(2)
        report = grade.build_report(2)
        self.assertEqual(report['earned'], 90)
        self.assertEqual(report['state'], 'NEEDS PRACTICE')

    def test_unsafe_direct_write_fails(self):
        path = grade.assignment(3) / 'starter.py'
        path.write_text(GOOD.replace("temporary = path.with_suffix('.json.tmp')", 'temporary = path'), encoding='utf-8')
        report = grade.build_report(3)
        saving = next(c for c in report['criteria'] if c['id'] == 'saving')
        self.assertEqual(saving['state'], 'failed')

    def test_provisional_never_passes(self):
        path = grade.assignment(40) / 'rubric.json'
        rubric = grade.read_json(path)
        rubric['status'] = 'provisional'
        grade.write_json(path, rubric)
        grade.write_json(grade.assignment(40) / 'submission.json', {'exercise_02': True})
        self.manual_full_marks(40)
        report = grade.build_report(40)
        self.assertEqual(report['earned'], 100)
        self.assertEqual(report['state'], 'PROVISIONAL: SCORED')

    def test_later_predictions_and_manual_review(self):
        for lesson in range(4, 41):
            rubric = grade.load_rubric(lesson)
            expected = next(c['expected'] for c in rubric['criteria'] if c['mode'] == 'auto')
            grade.write_json(grade.assignment(lesson) / 'submission.json', {'exercise_02': expected})
            report = grade.build_report(lesson)
            self.assertEqual((report['earned'], report['pending'], report['state']),
                             (10, 90, 'REVIEW PENDING'))
            self.manual_full_marks(lesson)
            self.assertEqual(grade.build_report(lesson)['state'], 'PASS')

    def test_unfinished_later_work_never_auto_passes(self):
        grade.write_json(grade.assignment(4) / 'submission.json', {'exercise_02': None})
        report = grade.build_report(4)
        self.assertEqual((report['earned'], report['pending'], report['state']),
                         (0, 90, 'REVIEW PENDING'))

    def test_prediction_malformed_and_wrong_shape_are_feedback(self):
        path = grade.assignment(4) / 'submission.json'
        for text in ('{broken', '[]', 'null'):
            path.write_text(text, encoding='utf-8')
            report = grade.build_report(4)
            self.assertEqual(report['earned'], 0)
            row = next(c for c in report['criteria'] if c['mode'] == 'auto')
            self.assertIn('Cannot read', row['feedback'])

    def test_prediction_bool_is_not_integer(self):
        grade.write_json(grade.assignment(8) / 'submission.json', {'exercise_02': 1})
        self.assertEqual(grade.build_report(8)['earned'], 0)
        grade.write_json(grade.assignment(8) / 'submission.json', {'exercise_02': True})
        self.assertEqual(grade.build_report(8)['earned'], 10)

    def test_prediction_object_key_order_does_not_matter(self):
        path = grade.assignment(16) / 'rubric.json'
        rubric = grade.read_json(path)
        next(c for c in rubric['criteria'] if c['mode'] == 'auto')['expected'] = {'a': 1, 'b': 2}
        grade.write_json(path, rubric)
        grade.write_json(grade.assignment(16) / 'submission.json', {'exercise_02': {'b': 2, 'a': 1}})
        self.assertEqual(grade.build_report(16)['earned'], 10)

    def test_manual_marks_and_saved_report_become_stale(self):
        self.manual_full_marks(1)
        grade.save_report(grade.build_report(1))
        (grade.assignment(1) / 'answers.md').write_text('Changed answer', encoding='utf-8')
        self.assertEqual(grade.saved_status(1)[0], 'STALE: RUN CHECK')
        report = grade.build_report(1)
        self.assertEqual(report['pending'], 60)
        self.assertTrue(any(c['state'] == 'stale' for c in report['criteria']))

    def test_syntax_error_is_feedback(self):
        (grade.assignment(1) / 'starter.py').write_text('def broken(:', encoding='utf-8')
        report = grade.build_report(1)
        self.assertEqual(report['earned'], 0)
        self.assertTrue(any('SyntaxError' in c['feedback'] for c in report['criteria']))

    def test_timeout_is_reported(self):
        (grade.assignment(1) / 'starter.py').write_text('while True: pass', encoding='utf-8')
        report = grade.build_report(1, timeout=0.3)
        self.assertEqual(report['earned'], 0)
        self.assertTrue(any('Timed out' in c['feedback'] for c in report['criteria']))

    def test_copy_protects_original_assignment_files(self):
        folder = grade.assignment(3)
        (folder / 'data').mkdir()
        path = folder / 'data' / 'inventory.json'
        path.write_text('original learner file', encoding='utf-8')
        before = grade.fingerprint(folder)
        grade.build_report(3)
        self.assertEqual(grade.fingerprint(folder), before)
        self.assertEqual(path.read_text(encoding='utf-8'), 'original learner file')

    def test_missing_entrypoint(self):
        rubric_path = grade.assignment(1) / 'rubric.json'
        rubric = grade.read_json(rubric_path)
        rubric['entrypoint'] = 'not-submitted.py'
        grade.write_json(rubric_path, rubric)
        report = grade.build_report(1)
        self.assertEqual(report['earned'], 0)
        self.assertTrue(any('Missing entrypoint' in c['feedback'] for c in report['criteria']))

    def test_manual_mark_persists_and_invalid_marks_rejected(self):
        self.assertEqual(self.run_cli(['mark','--lesson','1','--criterion','types','--score','16','--note','Four predictions correct']), 0)
        self.assertEqual(grade.read_json(grade.marks_path(1))['types']['score'], 16)
        for score in ('21', '-1', 'nan', 'inf'):
            self.assertEqual(self.run_cli(['mark','--lesson','1','--criterion','types','--score',score,'--note','Evidence']), 2)
        self.assertEqual(self.run_cli(['mark','--lesson','1','--criterion','stock_zero','--score','3','--note','Evidence']), 2)
        self.assertEqual(self.run_cli(['mark','--lesson','1','--criterion','types','--score','10','--note',' ']), 2)

    def test_selection_and_reports(self):
        self.assertEqual(self.run_cli(['check','--week','14']), 1)
        self.assertTrue(grade.report_path(40).exists())
        self.assertFalse(grade.report_path(39).exists())
        self.assertTrue((self.root / 'grading' / 'gradebook.md').exists())
        self.assertEqual(self.run_cli(['check','--week','0']), 2)
        self.assertEqual(self.run_cli(['check','--lesson','41']), 2)


if __name__ == '__main__':
    unittest.main()

# Grade your assignments offline

The checker uses Python 3 and its standard library: no internet, account, API key or paid service. Run commands **from the course root**, the folder containing grade.py. Substitute `py` on Windows if needed.

```powershell
python grade.py check --lesson 1
python grade.py check --week 1
python grade.py check --all
python grade.py rubric --lesson 1
python grade.py status --all
```

Every lesson has exactly ten exercises and a 100-point rubric. Lessons 1-3 retain their original weighted diagnostic/project rubrics; some exercises share a criterion. Lessons 4-40 assign 10 points per exercise.

## What the checker grades

| Lessons | Automatic checks | Needs local human review |
| --- | --- | --- |
| 1 | Stock labels, totals, filtering, ID lookup, empty cases and non-mutation | Types, loops, collections and explanations |
| 2 | Input retries, lookup, successful sales, rejected-sale stock protection | Menu, message quality and explanations |
| 3 | Validation, loading, safe saving and CSV output | Drills, menu integration, sales, restart/failure demonstrations |
| 4-40 | Worked-example prediction in submission.json: 10 points | Terminology and practical code/configuration/design: 90 points |

The checker does **not** automatically verify Django/React implementations, Git operations, prose or deployment demonstrations. These have explicit acceptance cases and review criteria. A correct prediction is not a practical-code pass. Framework dependencies are separate from the checker; see [setup](../SETUP.md).

## Your first check

1. Complete the assignment files. Keep Week 1 function names and signatures.
2. For Lessons 4-40 replace `null` at `exercise_02` in submission.json with the requested JSON value. Strings use double quotes, Booleans use lowercase true/false, and lists use brackets. The lesson gives the required shape.
3. Run `python grade.py check --lesson N`, replacing N with the number.
4. Read `grading/reports/lesson-NN.md` for earned, failed and pending points. Fix your work and retry.

Reports stay local. `grading/gradebook.md` shows all 40 lessons. Unfinished starters produce failures and pending marks; this is expected, not an installation problem.

## Review practical work honestly

Use a tutor or carefully self-review. A self-reviewed grade is your assessment, not independent certification. Open the actual files and rerun the specified cases. A file merely existing earns no implementation marks.

For Lessons 4-40 Exercises 3-9 award 6 points for fulfilling stated requirements, 3 for demonstrated cases and 1 for explanation. Give partial marks for specific fulfilled requirements and note omissions. Exercises 1 and 10 have their own breakdowns in the brief.

List IDs, then record a reviewed result:

```powershell
python grade.py rubric --lesson 4
python grade.py mark --lesson 4 --criterion exercise_03 --score 8 --note "Reviewed product.py: all fields stored (6); one case demonstrated (2); independence explanation missing."
python grade.py check --lesson 4
```

The note is an example, not a score to copy. Record what you actually observed. Automatic criteria cannot be manually marked. Scores must be finite, within the maximum, and accompanied by nonempty evidence. Marks are stored under `grading/marks/`.

Week 1 IDs include `types`, `collections`, `menu` and `debug`. Consult its rubric; shared exercise marks must be combined once.

## Results

- **REVIEW PENDING:** Some manual work is unreviewed. Pending points are not failed points.
- **PASS:** At least 80/100, every manual criterion reviewed, and all required mastery gates satisfied. Lesson 1 also requires half the marks in every diagnostic section.
- **NEEDS PRACTICE:** Review is complete but the threshold or a gate was not met.
- **STALE: RUN CHECK:** Submission, rubric, grader or review changed after the saved report.
- **PROVISIONAL:** Reserved for future draft rubrics; the supplied 40 rubrics are ready.

Changing any assignment file invalidates its previous manual marks. Finish edits and checks before reviewing. This prevents old evidence being treated as proof of changed code.

Check exit codes: 0 means all selected lessons passed; 1 means practice/review remains; 2 means a checker input/configuration error. The status command only displays saved results and returns 0 on a valid invocation.

## Execution and verification

Week 1 runs Python in a disposable copy with a 15-second default timeout. Import-time interaction gets feedback and output is bounded. The copy protects ordinary relative assignment writes; it is not a security sandbox for untrusted code. Grade your own work. JSON answers are only read as data.

```powershell
python grade.py check --lesson 1 --timeout 10
python -m unittest discover -s grading/tests -v
python tools/validate_course.py
```

Regression tests use fictional submissions and do not award marks to your real work.

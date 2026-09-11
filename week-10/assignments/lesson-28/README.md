# Lesson 28 assignment: Testing the backend

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

Tests are repeatable quality checks at the shop. A fixture sets up known stock; an assertion compares what happened with what should happen. A passing check proves only the cases it actually examines.

Use the existing backend. Put tests in inventory/tests.py or its established tests/ package. The first pure-function test can use a small standalone total function; use Django/DRF facilities for database/request tests. Keep test data separate from working stock.

## Where to work and how to run it

Work in `week-10/assignments/lesson-28/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `project/inventory/tests.py` |
| 4 | `project/inventory/tests.py` |
| 5 | `project/inventory/tests.py` |
| 6 | `project/inventory/tests.py` |
| 7 | `project/inventory/tests.py` |
| 8 | `project/inventory/tests.py` |
| 9 | `project/inventory/tests.py` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Test case** | A repeatable check with setup, action and expected result. | one quality inspection. |
| **Assertion** | A condition that must hold for a test to pass. | the inspector’s comparison. |
| **Fixture** | Known data or environment used by a test. | the prepared sample shelf. |
| **Unit test** | A focused check of a small piece of behaviour. | testing one counter tool. |
| **Integration test** | A check of collaborating components. | rehearsing the whole checkout handoff. |

A **fixture** is known starting data, like a prepared sample shelf. A **boundary case** lies at the edge of a rule, such as requesting exactly the available stock. **Expected** is what the rule says should happen; **actual** is what you observed. A **criterion** is one part of the marking scheme. An **artefact** is a file or concrete result you created. **Demonstrate** means carry out the action and record its actual result, not merely say that it works.

## Exercise 1: Explain the five terms — 10 points

**Where:** Exercise 1 in `answers.md`.

1. Read the five topic terms above, then explain each in your own words.
2. Give an everyday analogy for each and map its parts explicitly. For example: “A function is like a service counter: arguments are the order and the returned value is the item handed back.” Use this form with this lesson's terms.
3. Explain one point where one of your analogies stops fitting the precise rule. Software cannot infer missing instructions through human judgement.

**Finished when:** all five terms have an accurate meaning and mapped analogy. Each earns 1 point for meaning and 1 for mapping. Manual criterion: `exercise_01`.

## Exercise 2: Predict and check the worked example — 10 points

**Where:** `exercise_02` in `submission.json`; reasoning in `answers.md`.

Use this exact example and the input/conditions in the question. This may be a code fragment or a message/query to trace. Use the setup above and the explanation below to place it correctly.

```python
import unittest

def total(price, quantity):
    return price * quantity

class TotalTests(unittest.TestCase):
    def test_sale(self):
        self.assertEqual(total(200, 3), 600)

if __name__ == "__main__":
    unittest.main()
```

**Question:** What expected numeric value does the assertion use?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

The assertion uses an independently known expected value. A test that calculates its expectation using the same broken logic can miss defects. Django TestCase adds database isolation; APIClient supports API request checks. Test both returned responses and persistent side effects.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Test a calculation - 10 points

**Where:** `project/inventory/tests.py`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Write a standard-library unittest for sale totals with 200*3=600, zero stock value and another price. Show the exact discovery command and results.

A test compares an independently known answer with the program's actual result.

1. Write a small sale-total function and a unittest.TestCase, using test_ method names.
2. Assert totals 200*3=600 and 50*4=200; add an empty inventory-value check returning 0.
3. Run the test file or Django inventory test suite, depending on where you placed it.
4. Record the test names and result.

**Check:** expectations are literal known values, not calculated by calling the same implementation again. A file that runs without importing/discovering any tests is not a passing test suite.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Test validation - 10 points

**Where:** `project/inventory/tests.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Add tests rejecting zero, negative, fractional and excessive sale quantities. Assert unchanged stock for every rejected case.

Rejected sales should be tested for both the error and unchanged stock.

1. Prepare a fresh Pen price 200/stock 4 for each case.
2. Use assertRaises(ValueError) for quantities 0, -1, 2.5 and 5, plus True if your direct-call contract rejects bool.
3. After each rejected call assert stock remains 4.
4. Add the boundary success quantity 4 and check total 800/stock 0.

**Check:** an implementation that raises after subtracting stock must fail your tests. Reusing a mutated fixture across cases can hide errors, so set up each case independently.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Test persistence - 10 points

**Where:** `project/inventory/tests.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Use a temporary database/file fixture and verify a saved product can be reloaded. Keep tests independent from your working inventory.

Persistence needs a new read, not merely the same object still sitting in memory.

1. Use a temporary directory/file or Django TestCase's isolated database.
2. Save a product, discard the local object reference, then reload by path or primary key.
3. Assert name, price and stock equal the expected values.
4. Ensure cleanup leaves your working inventory untouched and document the chosen test storage.

**Check:** the result comes from a storage read. Comparing an object with itself immediately after assignment proves neither file writing nor database persistence.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Test the API contract - 10 points

**Where:** `project/inventory/tests.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Use DRF APIClient for valid creation 201, invalid creation 400 and missing detail 404. Check response fields and row counts.

An API contract test checks transport and storage behaviour together.

1. Use DRF APIClient and appropriate test authentication to POST a valid Pen body.
2. Assert 201, expected fields, an assigned ID and exactly one added row.
3. POST stock -1 and assert 400 with no added row.
4. GET a verified absent detail and assert 404.

**Check:** every response assertion has the relevant database assertion. State the authentication setup; force_authenticate isolates API behaviour and does not test the real login/token flow.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Test access boundaries - 10 points

**Where:** `project/inventory/tests.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Create two users and prove one cannot read or change the other’s products. Include a direct request using a guessed valid ID.

Ownership tests should attempt the requests a hidden button would normally discourage.

1. Create A and B with separate products and authenticate as A.
2. List products and assert every returned record belongs to A, accounting for the pagination envelope.
3. Directly retrieve/update/delete B's known ID and assert the policy's denial status.
4. Refetch B's record to verify unchanged fields and existence.

**Check:** list and detail/write boundaries are all exercised. An assertion that a Delete button is absent does not prove the endpoint denies a crafted request.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Use a fake service - 10 points

**Where:** `project/inventory/tests.py`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Replace the external payment boundary with a fake returning success or failure. Check a failure does not deduct stock; no network calls should be needed.

A fake controls the payment boundary so success and failure are repeatable.

1. Inject a payment fake that records amounts and can raise a simulated refusal.
2. From fresh stock 4 sell quantity 2 at price 200 under success and refusal configurations.
3. Assert the attempted charge is 400 and stock decreases only after success.
4. Add an oversale case and assert no payment call occurs.

**Check:** the tests perform no network request. A recorded call proves attempted payment; the fake's configured result determines whether checkout may commit its stock change.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Prove a test detects a bug - 10 points

**Where:** `project/inventory/tests.py`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Temporarily introduce an incorrect comparison at the stock boundary in a disposable copy. Show a relevant test fails, restore the correct implementation and show it passes.

Prove that a useful test detects a realistic defect.

1. In a disposable copy temporarily change the sale boundary so buying exactly all available stock is rejected.
2. Run the relevant quantity-equals-stock test and save the failure output.
3. Restore the correct comparison and rerun the same test, then the affected suite.
4. Explain which requirement the failing assertion protects.

**Check:** you have a failing then passing run caused by the deliberate code change. Do not weaken the assertion just to get green output or leave the defective copy as your final implementation.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose two new test cases, one valid and one failure/boundary. Temporarily perturb relevant code in a disposable copy to explain what at least one assertion would detect. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 28
python grade.py rubric --lesson 28
```

The first checks the JSON prediction and writes `grading/reports/lesson-28.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-28/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

# Lesson 18 assignment: Django ORM queries

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

The ORM is a translator from Python requests to database queries. A QuerySet is often an order ticket waiting to be executed, not a bag of already loaded records.

Use the migrated Lesson 17 Product(name,price,stock) model. Seed Pen 200/4, Book 500/8 and Bag 4000/0 in a disposable database. Work in manage.py shell after importing Product from inventory.models. Save queries and actual output in query-notes.md.

## Where to work and how to run it

Work in `week-06/assignments/lesson-18/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `query-notes.md` |
| 4 | `query-notes.md` |
| 5 | `query-notes.md` |
| 6 | `query-notes.md` |
| 7 | `query-notes.md` |
| 8 | `query-notes.md` |
| 9 | `query-notes.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **ORM** | Object-relational mapping between code objects and database rows. | the Python-to-ledger translator. |
| **QuerySet** | A composable database query and its results when evaluated. | an order ticket. |
| **Lazy evaluation** | Deferring work until results are needed. | filling the order when collected. |
| **Lookup** | A field comparison used in a query. | the clerk’s selection rule. |
| **Aggregation** | Combining rows into summary values. | adding ledger totals. |

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
# Run in manage.py shell after creating the fixture
low = Product.objects.filter(stock__lte=4).order_by("id")
print(list(low.values_list("name", flat=True)))
```

**Question:** With Pen stock 4 and Book stock 8, inserted in that order, enter the names returned.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Import Product from inventory.models first. filter composes a query; list evaluates it. stock__lte means stock less than or equal to the supplied value. get expects exactly one row and raises exceptions for zero or multiple matches.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Seed a fixture - 10 points

**Where:** `query-notes.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Create Pen 200/4, Book 500/8 and Bag 4000/0 in a disposable database. Record primary keys and clear only your practice rows when repeating.

Prepare a fixture whose later query results are predictable.

1. In a disposable migrated database create Pen 200/4, Book 500/8 and Bag 4000/0 in that order.
2. Save their actual IDs in query-notes.md. Avoid adding duplicate fixtures every time you reopen the shell.
3. Query name, price and stock ordered by ID and record the rows.
4. Explain that Product.objects is the manager providing query operations.

**Check:** the exercise fixture has exactly three products with these values. Keep other practice records outside this fixture or clearly filter to it before calculating expected totals.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Filter and order - 10 points

**Where:** `query-notes.md`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Query stock <=4 ordered by stock then id. Expect Bag and Pen. Save Python and output, then check threshold 0.

Build a selection using a field lookup and explicit ordering.

1. Import Product in manage.py shell and filter with stock__lte=4.
2. Order by stock then id; display name/stock tuples.
3. Repeat with cutoff 0 and an empty-match cutoff such as -1.
4. Explain the double underscore as part of Django's lookup syntax, not a field named stock__lte.

**Check:** cutoff 4 gives Bag/0 then Pen/4; cutoff 0 gives Bag/0; -1 gives an empty QuerySet. Include equality at the boundary.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Retrieve safely - 10 points

**Where:** `query-notes.md`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Use get(pk=...) for Pen and catch Product.DoesNotExist for a missing ID. Explain why filter returns an empty QuerySet instead of raising for no match.

Use get when exactly one record is expected.

1. Fetch Pen using its recorded primary key and print its name.
2. Choose an absent key, verify it is absent, then attempt get and catch Product.DoesNotExist.
3. Compare with filter(pk=missing_key), which represents zero matching rows without that exception.
4. Explain that get can also fail if a nonunique condition matches multiple rows.

**Check:** valid get returns a Product object; missing get follows the documented exception path; missing filter is empty. Do not catch every exception and treat it as a missing product.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Update stock - 10 points

**Where:** `query-notes.md`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Use an F expression to increase Pen stock by 3, then refresh_from_db. Expect 7. Explain why an already loaded object can show an older value.

An F expression lets the database calculate from its current field value.

1. Import F from django.db.models. Load Pen into a Python variable while stock is 4.
2. Update its database stock using F("stock") + 3 through a filtered QuerySet.
3. Print the already loaded object's stock, then call refresh_from_db and print again.
4. Record both readings and explain the difference between a stored row and an earlier Python object snapshot.

**Check:** database stock becomes 7; refreshing makes the object show 7. A QuerySet update does not automatically refresh every previously loaded instance.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Calculate a summary - 10 points

**Where:** `query-notes.md`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Use ORM aggregation to calculate the total stock units after the update: 15. Define empty-queryset behaviour and demonstrate it.

Aggregate after the earlier update, not against the original fixture.

1. Import Sum from django.db.models and calculate the sum of stock over the three fixture products.
2. Extract the named aggregate result and compare with 7 + 8 + 0.
3. Run the aggregate over an empty filtered QuerySet.
4. Define a zero default for that empty result and demonstrate it without deleting products.

**Check:** total stock is 15, and your chosen empty-summary interface produces 0. Raw aggregate results can contain None; explain how your code turns that into the intended numeric default.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Observe query timing - 10 points

**Where:** `query-notes.md`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Use Django query capture in a test or shell to compare building a QuerySet with evaluating it. Save query counts and explain evaluation triggers.

A QuerySet can describe work before executing it.

1. In a Django test or shell import connection and CaptureQueriesContext.
2. Capture queries while merely constructing a filtered QuerySet; do not print or iterate it inside that first measurement.
3. In another capture block evaluate it with list(...), then inspect the SQL/count.
4. Evaluate the same already materialized QuerySet again and distinguish cached results from a newly created QuerySet.

**Check:** construction performs no select for its rows; initial evaluation does. Avoid asserting an unexplained total for a whole shell session containing unrelated database operations.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Limit returned data - 10 points

**Where:** `query-notes.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Fetch only names and stock with values() or values_list(), then compare output types with model instances. Show explicit ordering and explain when this projection helps.

A projection returns selected values instead of fully featured model instances.

1. Query the fixture with values("name","stock").order_by("id") and convert it to a list.
2. Repeat with values_list("name","stock") and compare the shapes.
3. Compare those entries with Product instances from an ordinary QuerySet.
4. Explain when a read-only report might need only these two fields.

**Check:** values entries are dictionaries; values_list entries are tuples; current stocks are 7,8,0. A dictionary result does not have a Product.save method just because it came from an ORM query.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new ORM filter/projection and an empty or stale-instance case. Record types, ordering and when database evaluation happens. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 18
python grade.py rubric --lesson 18
```

The first checks the JSON prediction and writes `grading/reports/lesson-18.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-18/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

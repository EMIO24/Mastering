# Lesson 17 assignment: Models and migrations

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A model describes the product ledger; a migration is a numbered renovation instruction for changing its structure. Editing the drawing alone does not renovate the database.

Copy the working Lesson 16 project with config/, inventory/, manage.py and registered settings/routes. Add Product here. Saving models.py alone does not create database tables.

## Where to work and how to run it

Work in `week-06/assignments/lesson-17/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `project/inventory/models.py` |
| 4 | `project/inventory/migrations/` |
| 5 | `answers.md` |
| 6 | `answers.md` |
| 7 | `project/inventory/models.py` |
| 8 | `migration-notes.md` |
| 9 | `rebuild-notes.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Model** | A Python class mapping stored entities to database fields. | the product-ledger design. |
| **Field** | A typed model attribute mapped to stored data. | a ruled ledger column. |
| **Migration** | A versioned operation changing schema or data. | a numbered renovation instruction. |
| **makemigrations** | The command generating migration files from model changes. | writing the renovation plan. |
| **migrate** | The command applying pending migrations. | carrying out the plan. |

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
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
```

**Question:** What stock value is declared as the default?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

This belongs in inventory/models.py in the previous project. Django supplies a primary key unless you define one. PositiveIntegerField allows zero. Generate and inspect a migration, then apply it; saving models.py by itself does not add database columns.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Define Product - 10 points

**Where:** `project/inventory/models.py`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Add name max_length=120, price and stock whole-naira/integer fields with stock default 0. Explain each field choice and add __str__.

Describe the stored product card as a Django model.

1. In inventory/models.py create Product(models.Model) with name CharField(max_length=120), price PositiveIntegerField and stock PositiveIntegerField(default=0).
2. Add __str__ returning the product name.
3. Explain that these integer fields allow zero and that whole-naira pricing is a deliberate course simplification.
4. Run `python manage.py check`; do not assume the table has been created yet.

**Check:** the class imports and system checks pass. Django supplies a primary key unless you define one. A model definition describes intended structure; migration steps make the database match it.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Generate a migration - 10 points

**Where:** `project/inventory/migrations/`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Run python manage.py makemigrations inventory. Open the generated file and identify CreateModel, field types and dependencies in notes.

Write the renovation instructions before applying them.

1. Run `python manage.py makemigrations inventory`.
2. Open the newly generated migration file; record its actual filename.
3. Identify dependencies, the CreateModel operation and the generated name/price/stock fields.
4. Explain what the migration's stock default means for new rows.

**Check:** a migration file exists containing the Product schema. Do not edit an existing migration that has already been applied merely to hide a changed model; later changes should produce another migration.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Apply the schema - 10 points

**Where:** `answers.md`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Run python manage.py migrate and showmigrations inventory. Save output showing the migration applied; explain the difference between generation and application.

Apply the pending schema changes to your local database.

1. Run `python manage.py showmigrations inventory` and note unchecked migrations.
2. Run `python manage.py migrate`, then showmigrations again.
3. Copy relevant output into answers.md and explain generation versus application.
4. Run migrate once more to observe the no-pending-work result.

**Check:** the Product migration is marked applied, and repeating migrate does not create a second Product table. Migration history tracks which versioned operations the database has already accepted.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Create a record - 10 points

**Where:** `answers.md`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** In manage.py shell create Pen price 200 stock 4. Close/reopen the shell and fetch the saved primary key. Record the persistent values.

Prove that a saved model instance survives leaving the shell.

1. Open manage.py shell and import Product from inventory.models.
2. Create Pen with price 200 and stock 4 using Product.objects.create; record its assigned primary key.
3. Exit the shell completely, reopen it, import Product again and fetch that exact key.
4. Print name, price and stock plus str(product).

**Check:** Pen/200/4 persists and str gives Pen. Do not assume the ID is 1 if your disposable database contains earlier records; use the actual saved key.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Add a field safely - 10 points

**Where:** `project/inventory/models.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Add optional description using blank=True and a suitable default. Generate/apply a second migration and show the existing Pen record remains usable.

Evolve the schema while keeping an existing row usable.

1. Add a description text field permitting an empty value, using blank=True and a suitable empty-string default.
2. Generate the next migration, inspect it, then apply it.
3. Fetch the earlier Pen by its recorded ID and inspect all old fields plus description.
4. Update description, save and refetch.

**Check:** Pen's name/price/stock are unchanged, initial description is empty, and the later description persists. blank concerns validation; it does not mean the same thing as database NULL.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Inspect SQL - 10 points

**Where:** `migration-notes.md`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Run sqlmigrate for your first migration and annotate table creation and primary-key SQL. Explain why generated SQL depends on the configured database backend.

Inspect what a migration asks the configured database to execute.

1. Run `python manage.py sqlmigrate inventory MIGRATION_NAME`, substituting your first Product migration's stem, such as 0001.
2. Identify table creation, primary key and the three authored fields in its SQL.
3. Record the database engine from settings and annotate any type differences from the Python model declarations.
4. Explain why another backend may produce different SQL for the same migration operations.

**Check:** the inspected SQL corresponds to the actual migration and configured backend. sqlmigrate displays SQL; it does not apply the migration by itself.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Rebuild from history - 10 points

**Where:** `rebuild-notes.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Use a disposable project/database copy and apply migrations from empty. Verify Product can be created. Keep committed migration files and record the rebuild commands.

Migration history should rebuild the schema from an empty database.

1. Copy project source, including migration files, into a disposable rebuild folder. Configure a separate empty database path; do not delete your working database.
2. Use the prepared environment and run migrate in that copy.
3. Create a Product and read it back, including description.
4. Record commands, database path and observed values in rebuild-notes.md.

**Check:** the schema rebuilds without copying a populated database. An empty database starts with no business records; successful schema reconstruction does not imply fixtures were migrated automatically.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new record after migration and a rebuild/schema-change case. Show the database path and migration state so existing data is not mistaken for reconstructed schema. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 17
python grade.py rubric --lesson 17
```

The first checks the JSON prediction and writes `grading/reports/lesson-17.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-17/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

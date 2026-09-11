# Lesson 13 assignment: SQL foundations

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A relational table is a carefully structured ledger. SQL describes which rows you want instead of making you walk through each page yourself. A table has no guaranteed display order without ORDER BY.

Use Python sqlite3 in practice.py and inventory.sqlite3 for persistent work. A :memory: database disappears when closed. Seed Pen 200/4, Book 500/8 and Bag 4000/0 with IDs 1/2/3. Avoid inserting duplicate fixtures when repeating a run.

## Where to work and how to run it

Work in `week-05/assignments/lesson-13/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

From this folder run `python practice.py`. Import sqlite3 in it. Read .sql text and use connection.executescript(...) for setup scripts; execute SELECT queries with connection.execute(...).fetchall() and print the rows. Commit successful persistent changes and close the connection.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `practice.py` |
| 4 | `practice.py` |
| 5 | `practice.py` |
| 6 | `practice.py` |
| 7 | `practice.py` |
| 8 | `practice.py` |
| 9 | `practice.py` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Database** | An organized persistent collection of data. | the ledger cabinet. |
| **Table** | Rows sharing a defined set of columns. | one structured ledger. |
| **Row** | One record in a table. | one ledger entry. |
| **SQL** | A language for relational data definition and manipulation. | instructions to the ledger clerk. |
| **Parameter** | A separately bound query value. | a filled form value rather than a rewritten instruction. |

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
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, stock INTEGER)")
db.executemany("INSERT INTO products VALUES (?, ?, ?)", [(1,"Pen",4),(2,"Book",8)])
rows = db.execute("SELECT name FROM products WHERE stock <= ? ORDER BY id", (4,)).fetchall()
print(rows)
```

**Question:** Enter the selected product names as a JSON list.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

The connection creates a temporary database for this example. The question mark binds 4 as data. fetchall returns tuples; selecting one column still produces a one-element tuple per row. Use a file path and commit for persistent exercises.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Create a ledger - 10 points

**Where:** `practice.py`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** In practice.py use sqlite3 to create a products table with id primary key, name, price and stock. Insert Pen 200/4, Book 500/8 and Bag 4000/0 using parameters.

Create a ledger with predictable starting records.

1. In practice.py import sqlite3 and connect to inventory.sqlite3 beside the script. Create products with id INTEGER PRIMARY KEY, name TEXT, price INTEGER and stock INTEGER.
2. Insert IDs 1/2/3: Pen 200/4, Book 500/8 and Bag 4000/0. Use ? placeholders and parameter tuples, not SQL string concatenation.
3. Commit and select all rows ordered by ID.

**Check:** exactly three rows match those values. Use a disposable database and make repeated setup deliberate; duplicate-key errors are not proof that seeding succeeded.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Read precise columns - 10 points

**Where:** `practice.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Select name and stock ordered by id. Save the SQL and returned rows; do not use SELECT * for this exercise.

Selecting particular columns gives the reader only the needed parts of each card.

1. Write SELECT for name and stock from products, with ORDER BY id.
2. Execute it and call fetchall(); print the returned tuples.
3. Record the SQL and output, then explain which tuple position represents each selected column.

**Check:** rows are `('Pen',4)`, `('Book',8)`, `('Bag',0)`. Do not use SELECT * for this task. Without ORDER BY, apparent insertion order is not a promised result order.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Filter stock - 10 points

**Where:** `practice.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Select stock <=4 ordered by stock then id. Expect Bag then Pen. Repeat for threshold 0 using a bound parameter.

Filter the ledger using a supplied cutoff.

1. Select name and stock where stock <= a bound parameter.
2. Order by stock ascending, then ID to break ties.
3. Execute with thresholds 4, 0 and -1 without rewriting the SQL string. Record each result.

**Check:** 4 gives Bag/0 then Pen/4; 0 gives Bag/0; -1 gives no rows. The equality case matters: Pen belongs at cutoff 4. Use a one-item tuple such as `(4,)` when binding a single sqlite3 parameter.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Update one row - 10 points

**Where:** `practice.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Change Pen stock to 7 with WHERE id=1. Show before/after rows and verify Book remains 8. Explain the effect of omitting WHERE.

Change one card without touching its neighbours.

1. Query all IDs/stocks before the update.
2. Update stock to 7 only where id equals the bound value 1. Commit.
3. Query all IDs/stocks again and explain the before/after difference.
4. Describe, without executing on useful data, what an UPDATE lacking WHERE would do.

**Check:** Pen is 7, Book remains 8 and Bag remains 0. This sets stock to 7; it does not add 7. The WHERE condition identifies the row, not its displayed position.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Delete deliberately - 10 points

**Where:** `practice.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Delete only the zero-stock Bag by ID. Show remaining row count 2. Work only on your disposable practice database.

Delete a verified practice record.

1. Fetch Bag and confirm ID 3 and stock 0 in your disposable database.
2. Delete using a parameterized condition on ID 3 and commit.
3. Query remaining IDs, count and a lookup for ID 3.

**Check:** count is 2, remaining IDs are 1 and 2, and Bag lookup returns no row. Repeat only with a restored fixture if you want to observe a successful deletion again. An already absent row should not cause another product to be deleted.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Aggregate value - 10 points

**Where:** `practice.py`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Use SUM(price * stock) after the update/delete. Expect 5400. Define and demonstrate a zero result for an empty table using COALESCE.

Combine all remaining rows into one inventory total.

1. Use the post-update/delete data: Pen 200/7 and Book 500/8.
2. Query SUM(price * stock), using COALESCE to choose zero when the aggregate is NULL.
3. Fetch the one value and compare with a handwritten calculation.
4. Run the same aggregate with a condition matching no rows; do not erase the fixture to check emptiness.

**Check:** total is `1400 + 4000 = 5400`; empty selection yields 0. Explain why SUM over no rows requires the explicit default.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Preserve data and queries - 10 points

**Where:** `practice.py`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Commit to inventory.sqlite3, close and reopen it, then show rows remain. Insert a name containing an apostrophe using parameters and demonstrate it reads back unchanged.

Prove both persistence and safe handling of punctuation.

1. Close and reopen inventory.sqlite3 and read the existing rows.
2. Insert an unused ID with name `Maker's Pen`, price 250 and stock 2 using bound parameters.
3. Commit, close, reopen and fetch that ID.
4. Explain why the apostrophe remains part of the data rather than changing the SQL instruction.

**Check:** Pen/Book persist and the new name reads back exactly. A :memory: connection cannot demonstrate persistence across a new connection; use the file database here.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new valid row/query and an empty-selection or punctuation-containing value. Show actual returned rows and the committed data afterward. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 13
python grade.py rubric --lesson 13
```

The first checks the JSON prediction and writes `grading/reports/lesson-13.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-13/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

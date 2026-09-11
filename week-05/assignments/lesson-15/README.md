# Lesson 15 assignment: Database design and transactions

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A transaction bundles stock deduction and sale recording into one sealed ledger update. Either the whole bundle is accepted or none is. A sketch of the ledger structure is its schema.

Use sqlite3 in practice.py with disposable design.sqlite3. Model suppliers(id,name,phone), products(id,sku,name,price,stock,supplier_id), sales(id), sale_lines(id,sale_id,product_id,quantity,unit_price). Choose/document SQL types and constraints. Start independent sale/failure checks with stock 5.

## Where to work and how to run it

Work in `week-05/assignments/lesson-15/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

From this folder run `python practice.py`. Import sqlite3 in it. Read .sql text and use connection.executescript(...) for setup scripts; execute SELECT queries with connection.execute(...).fetchall() and print the rows. Commit successful persistent changes and close the connection.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `schema-design.md` |
| 4 | `schema.sql and practice.py` |
| 5 | `schema.sql and practice.py` |
| 6 | `practice.py` |
| 7 | `practice.py` |
| 8 | `performance.md and practice.py` |
| 9 | `concurrency.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Schema** | The structure and constraints of a database. | the ledger blueprint. |
| **Normalization** | Organizing data to reduce harmful redundancy and anomalies. | keeping supplier details on one master card. |
| **Constraint** | A rule enforced by the database. | a ledger rule the clerk cannot bypass. |
| **Transaction** | A unit of database work committed or rolled back together. | one sealed update bundle. |
| **Index** | A structure that helps locate data efficiently. | the ledger’s lookup tabs. |

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
db.execute("CREATE TABLE stock (id INTEGER PRIMARY KEY, quantity INTEGER CHECK(quantity >= 0))")
with db:
    db.execute("INSERT INTO stock VALUES (1, 5)")
try:
    with db:
        db.execute("UPDATE stock SET quantity = quantity - 6 WHERE id = 1")
except sqlite3.IntegrityError:
    pass
print(db.execute("SELECT quantity FROM stock").fetchone()[0])
```

**Question:** What stock quantity is printed after the failed update?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

The first with commits the initial row. The second update violates CHECK and its transaction rolls back. Catching the error outside the with block lets the context manager observe failure. SQLite behaviour is useful practice but does not demonstrate PostgreSQL row locks.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Design the schema - 10 points

**Where:** `schema-design.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Draw products, suppliers, sales and sale_lines with keys and cardinalities. State which columns may be NULL and which are required.

A schema diagram is a buildable ledger blueprint.

1. Draw suppliers, products, sales and sale_lines with the starting setup's fields.
2. Mark primary/foreign keys and one-to-many relationships. State which fields may be NULL and the units of every numeric field.
3. Trace one sale containing Pen and Book through the diagram.
4. Explain why adding a third product to a sale should add a line, not another product column to sales.

**Check:** every relationship uses a named key and the sample sale fits the schema without changing its structure.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Remove an anomaly - 10 points

**Where:** `schema.sql and practice.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Show a duplicated supplier phone in three product rows. Move supplier details to a suppliers table and demonstrate one update changes the authoritative value.

Repeated supplier details can disagree after a partial update.

1. Sketch three products each storing the same supplier phone; change only one copy and explain the inconsistency.
2. Implement a suppliers row referenced by three products instead.
3. Update the phone on that supplier row, then join products to supplier details.
4. Record the SQL and all three results.

**Check:** every product displays the new phone from one authoritative value. Product stock remains on products because different products can have different counts even when they share a supplier.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Enforce business rules - 10 points

**Where:** `schema.sql and practice.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Write schema.sql with nonnegative stock/price checks, nonblank name validation at the application boundary, and unique product SKU. Demonstrate a duplicate SKU rejection.

Enforce critical rules even if someone bypasses a form.

1. Add nonnegative stock/price checks, unique SKU, primary keys and foreign keys in schema.sql. Validate nonblank names at the application boundary.
2. Insert Pen SKU PEN-001, price 200, stock 5.
3. Independently attempt a duplicate SKU and negative-stock row, rolling back each failed attempt.
4. Query the accepted data afterward and map each rule to its enforcing layer.

**Check:** only the valid row remains. State explicitly which rule is application validation and which is a database constraint; they are not automatically interchangeable.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Bundle a sale - 10 points

**Where:** `practice.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Implement a transaction that decreases stock and inserts a sale line. Starting stock 5, selling 2 commits stock 3 and one line.

A sale is one bundle of related database changes.

1. Start Pen at stock 5, price 200, with no sale records for this test.
2. Within one transaction reduce stock by 2 and create a sale with one line, quantity 2/unit_price 200.
3. Commit only after every statement succeeds.
4. Outside the transaction query stock, line count and sale total.

**Check:** stock 3, one new line, total 400. Do not commit between the stock deduction and line insertion: that would allow a half-recorded sale if the later statement failed.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Roll back a failure - 10 points

**Where:** `practice.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Cause line insertion to fail after the stock update in a disposable database. Show stock remains 5 and no sale line persists when starting from the original fixture.

Roll back the entire bundle when its second half fails.

1. Restore a fresh fixture with Pen stock 5 and no sale/line for this case.
2. In one transaction deduct stock, create a sale, then deliberately insert a line with an invalid foreign-key reference.
3. Let the error leave the transaction block and catch it outside.
4. Requery stock and sale/line counts.

**Check:** stock remains 5 and no new sale or line persists. Show the actual database state; catching an exception and printing “rolled back” is not sufficient evidence that the earlier deduction was undone.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Measure an index - 10 points

**Where:** `performance.md and practice.py`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Populate at least 1000 products and use EXPLAIN QUERY PLAN on SKU lookup before/after an appropriate index. Save plans; explain extra write/storage cost.

Inspect an actual lookup plan before claiming an index improves it.

1. Seed at least 1000 products and inspect EXPLAIN QUERY PLAN for a SKU lookup.
2. Note that a UNIQUE SKU already creates a lookup index in SQLite. For an unindexed SKU comparison, use a separate scratch table without that unique constraint.
3. Add an appropriate index to the scratch lookup and capture the second plan.
4. Confirm both queries return the same row and explain additional storage/write cost.

**Check:** evidence names the scan/index before and after. Do not claim a redundant index on an already unique key created an unindexed-to-indexed improvement.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Plan concurrent sales - 10 points

**Where:** `concurrency.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Trace two buyers attempting the last unit. Explain why reading then blindly writing loses correctness; propose an atomic conditional UPDATE and check its affected-row count.

Two shoppers can read the last unit before either records a sale.

1. Trace A and B each reading stock 1 and attempting to sell it with a naive read/overwrite approach.
2. Propose an atomic conditional update: decrement only where ID matches and stock is at least the requested quantity.
3. In a disposable script make two successive quantity-1 attempts, checking affected-row count before creating a sale.
4. Explain the concurrent rule and the limits of this sequential demonstration.

**Check:** first attempt affects one row; second affects zero and creates no sale; stock is 0. A sequential SQLite check does not demonstrate PostgreSQL row-lock behaviour.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new committed sale and a deliberately failed transaction. Query both stock and sale lines afterward to demonstrate atomicity. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 15
python grade.py rubric --lesson 15
```

The first checks the JSON prediction and writes `grading/reports/lesson-15.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-15/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

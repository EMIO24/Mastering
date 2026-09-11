# Lesson 14 assignment: Relationships and joins

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A sale line references a product card by its permanent number instead of copying all its current details. A join matches those references. Historical sale prices still need their own snapshot.

Use sqlite3 in practice.py and a disposable relationships.sqlite3. Define products(id,name,price), sales(id), sale_lines(id,sale_id,product_id,quantity,unit_price). References must point to existing rows. Start with Pen ID 1 price 200 and Book ID 2 price 500; add unsold Bag ID 3 later. Execute schema.sql/seed.sql through your script.

## Where to work and how to run it

Work in `week-05/assignments/lesson-14/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

From this folder run `python practice.py`. Import sqlite3 in it. Read .sql text and use connection.executescript(...) for setup scripts; execute SELECT queries with connection.execute(...).fetchall() and print the rows. Commit successful persistent changes and close the connection.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `schema.sql and practice.py` |
| 4 | `seed.sql` |
| 5 | `queries.sql and practice.py` |
| 6 | `queries.sql and practice.py` |
| 7 | `queries.sql and practice.py` |
| 8 | `practice.py` |
| 9 | `schema.sql and practice.py` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Primary key** | A column or columns uniquely identifying a row. | the permanent card number. |
| **Foreign key** | A constrained reference to another row key. | a valid card number on a sale line. |
| **One-to-many** | One record associated with several records. | one sale with several lines. |
| **JOIN** | Combining rows according to a condition. | matching sale slips with cards. |
| **NULL** | A marker for missing or unknown data. | a blank field whose value is unknown. |

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

```text
SELECT p.name, SUM(l.quantity) AS units
FROM products AS p
JOIN sale_lines AS l ON l.product_id = p.id
GROUP BY p.id, p.name
ORDER BY p.id;
```

**Question:** Pen has sale quantities 2 and 3. What is its SUM(quantity)?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

The ON condition connects each line to its product. GROUP BY collects matching lines before SUM. An inner join omits products with no sales; a left join can retain them. COUNT(*) after a left join counts the retained row, so count a non-null child key when counting children.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Create related tables - 10 points

**Where:** `schema.sql and practice.py`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Create products, sales and sale_lines with primary/foreign keys in SQLite. Enable PRAGMA foreign_keys = ON on the connection. Save schema.sql and a runnable loader.

A foreign key is a checked reference to another ledger's card number.

1. In schema.sql define products(id,name,price), sales(id), sale_lines(id,sale_id,product_id,quantity,unit_price), each with a primary key.
2. Make the two line references foreign keys, require positive quantities and nonnegative prices.
3. In practice.py connect to a disposable database, enable `PRAGMA foreign_keys = ON`, and execute the schema.

**Check:** all three tables exist and querying the pragma returns 1 on the connection used for inserts. Declaring a reference without enabling SQLite enforcement will not satisfy the later orphan-rejection check.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Insert a small history - 10 points

**Where:** `seed.sql`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Insert two products and two sales. Add Pen quantities 2 and 3 to separate sales, plus Book quantity 1. Save seed SQL and explain each relationship.

Seed a history small enough to verify by hand.

1. Insert Pen ID 1 price 200 and Book ID 2 price 500; create sales IDs 1 and 2.
2. Insert line IDs 1/2/3 as: sale1/Pen/quantity2/unit_price200; sale2/Pen/3/200; sale2/Book/1/500.
3. Commit and print all lines ordered by line ID. Keep the SQL in seed.sql.

**Check:** two products, two sales and three lines. Sale 1 totals 400; sale 2 totals 1100. Product ID identifies a product, while line ID identifies one particular receipt entry.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Join readable receipts - 10 points

**Where:** `queries.sql and practice.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Join lines to products and show sale ID, product name and quantity, ordered by sale ID then line ID. Verify names match the referenced IDs.

A join translates receipt references into readable product names.

1. Select sale ID, product name and quantity from sale_lines joined to products.
2. Match sale_lines.product_id to products.id in the ON clause.
3. Order by sale ID then line ID and execute from practice.py.
4. Explain the join condition using the card-number analogy.

**Check:** rows are `(1,'Pen',2)`, `(2,'Pen',3)`, `(2,'Book',1)`. Missing or incorrect join conditions can combine unrelated rows. Qualify column names with table names or aliases where they would otherwise be ambiguous.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Aggregate by product - 10 points

**Where:** `queries.sql and practice.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Produce Pen=5 and Book=1 units sold using GROUP BY. Explain why grouping by a name alone is unsafe if names can repeat.

Summarize units sold per product, across all sales.

1. Group the joined records by product ID and name.
2. Sum line quantity and order the summaries by product ID.
3. Compare with the seed rows rather than deriving the expectation from a second copy of your query.
4. Explain what would go wrong if two distinct products shared a name and you grouped only by name.

**Check:** Pen totals 5 units and Book 1. Sum quantities, not current prices; revenue is a different question.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Include unsold products - 10 points

**Where:** `queries.sql and practice.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Add Bag without a sale. Use LEFT JOIN and COALESCE so its units sold is 0. Show the difference from the inner join.

Keep products even when they have no sales.

1. Add Bag ID 3 price 4000 without a sale line.
2. Run your inner-join summary, then write a products LEFT JOIN sale_lines version.
3. Use COALESCE around SUM(quantity) and compare the two outputs.

**Check:** the inner join omits Bag; the left join shows Pen 5, Book 1, Bag 0. If counting lines, count a non-null child ID rather than COUNT(*), which also counts the retained parent row with no matching child.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Reject orphan lines - 10 points

**Where:** `practice.py`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Attempt a line with product_id 999 and show the foreign-key error. Roll back and verify no invalid row remains.

An orphan line refers to a card that does not exist.

1. Confirm product 999 is absent and line count is 3.
2. In a transaction attempt a new line for an existing sale but product_id 999.
3. Catch sqlite3.IntegrityError outside the transaction block, then query the attempted line and total count.

**Check:** the foreign-key failure leaves no new line and count remains 3. If insertion succeeds, inspect enforcement on the actual connection. Do not repair the test by creating product 999, because that removes the invalid condition you are trying to demonstrate.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Keep historical prices - 10 points

**Where:** `schema.sql and practice.py`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Store unit_price on sale_lines. Change the current product price and demonstrate that old receipt totals stay unchanged. Explain the intentional duplication.

Historical receipts must retain the price actually charged.

1. Calculate sale totals from line quantity times line unit_price.
2. Update today's Pen price from 200 to 300 and commit.
3. Recalculate historical totals from the same line fields.
4. Compare with the incorrect alternative of applying today's price to old quantities.

**Check:** sale 1 stays 400 and sale 2 stays 1100; today's Pen price is 300. Explain why unit_price on the sale line is an intentional snapshot, even though the product table also has a price field.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new related sale and an unsold/orphan case. Explain how join choice and foreign-key enforcement affect the observed result. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 14
python grade.py rubric --lesson 14
```

The first checks the JSON prediction and writes `grading/reports/lesson-14.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-14/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

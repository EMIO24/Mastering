# Lesson 15: Database design and transactions

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 14; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A transaction bundles stock deduction and sale recording into one sealed ledger update. Either the whole bundle is accepted or none is. A sketch of the ledger structure is its schema.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Schema | The structure and constraints of a database. | the ledger blueprint. |
| Normalization | Organizing data to reduce harmful redundancy and anomalies. | keeping supplier details on one master card. |
| Constraint | A rule enforced by the database. | a ledger rule the clerk cannot bypass. |
| Transaction | A unit of database work committed or rolled back together. | one sealed update bundle. |
| Index | A structure that helps locate data efficiently. | the ledger’s lookup tabs. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

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

The first with commits the initial row. The second update violates CHECK and its transaction rolls back. Catching the error outside the with block lets the context manager observe failure. SQLite behaviour is useful practice but does not demonstrate PostgreSQL row locks.

**Prediction:** What stock quantity is printed after the failed update?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Design the schema

Draw products, suppliers, sales and sale_lines with keys and cardinalities. State which columns may be NULL and which are required.

### Step 2: Remove an anomaly

Show a duplicated supplier phone in three product rows. Move supplier details to a suppliers table and demonstrate one update changes the authoritative value.

### Step 3: Enforce business rules

Write schema.sql with nonnegative stock/price checks, nonblank name validation at the application boundary, and unique product SKU. Demonstrate a duplicate SKU rejection.

### Step 4: Bundle a sale

Implement a transaction that decreases stock and inserts a sale line. Starting stock 5, selling 2 commits stock 3 and one line.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: The first with commits the initial row.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-15/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

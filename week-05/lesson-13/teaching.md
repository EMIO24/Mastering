# Lesson 13: SQL foundations

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 12; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A relational table is a carefully structured ledger. SQL describes which rows you want instead of making you walk through each page yourself. A table has no guaranteed display order without ORDER BY.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Database | An organized persistent collection of data. | the ledger cabinet. |
| Table | Rows sharing a defined set of columns. | one structured ledger. |
| Row | One record in a table. | one ledger entry. |
| SQL | A language for relational data definition and manipulation. | instructions to the ledger clerk. |
| Parameter | A separately bound query value. | a filled form value rather than a rewritten instruction. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, stock INTEGER)")
db.executemany("INSERT INTO products VALUES (?, ?, ?)", [(1,"Pen",4),(2,"Book",8)])
rows = db.execute("SELECT name FROM products WHERE stock <= ? ORDER BY id", (4,)).fetchall()
print(rows)
```

The connection creates a temporary database for this example. The question mark binds 4 as data. fetchall returns tuples; selecting one column still produces a one-element tuple per row. Use a file path and commit for persistent exercises.

**Prediction:** Enter the selected product names as a JSON list.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Create a ledger

In practice.py use sqlite3 to create a products table with id primary key, name, price and stock. Insert Pen 200/4, Book 500/8 and Bag 4000/0 using parameters.

### Step 2: Read precise columns

Select name and stock ordered by id. Save the SQL and returned rows; do not use SELECT * for this exercise.

### Step 3: Filter stock

Select stock <=4 ordered by stock then id. Expect Bag then Pen. Repeat for threshold 0 using a bound parameter.

### Step 4: Update one row

Change Pen stock to 7 with WHERE id=1. Show before/after rows and verify Book remains 8. Explain the effect of omitting WHERE.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: The connection creates a temporary database for this example.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-13/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

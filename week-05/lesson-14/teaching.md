# Lesson 14: Relationships and joins

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 13; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A sale line references a product card by its permanent number instead of copying all its current details. A join matches those references. Historical sale prices still need their own snapshot.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Primary key | A column or columns uniquely identifying a row. | the permanent card number. |
| Foreign key | A constrained reference to another row key. | a valid card number on a sale line. |
| One-to-many | One record associated with several records. | one sale with several lines. |
| JOIN | Combining rows according to a condition. | matching sale slips with cards. |
| NULL | A marker for missing or unknown data. | a blank field whose value is unknown. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```text
SELECT p.name, SUM(l.quantity) AS units
FROM products AS p
JOIN sale_lines AS l ON l.product_id = p.id
GROUP BY p.id, p.name
ORDER BY p.id;
```

The ON condition connects each line to its product. GROUP BY collects matching lines before SUM. An inner join omits products with no sales; a left join can retain them. COUNT(*) after a left join counts the retained row, so count a non-null child key when counting children.

**Prediction:** Pen has sale quantities 2 and 3. What is its SUM(quantity)?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Create related tables

Create products, sales and sale_lines with primary/foreign keys in SQLite. Enable PRAGMA foreign_keys = ON on the connection. Save schema.sql and a runnable loader.

### Step 2: Insert a small history

Insert two products and two sales. Add Pen quantities 2 and 3 to separate sales, plus Book quantity 1. Save seed SQL and explain each relationship.

### Step 3: Join readable receipts

Join lines to products and show sale ID, product name and quantity, ordered by sale ID then line ID. Verify names match the referenced IDs.

### Step 4: Aggregate by product

Produce Pen=5 and Book=1 units sold using GROUP BY. Explain why grouping by a name alone is unsafe if names can repeat.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: The ON condition connects each line to its product.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-14/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

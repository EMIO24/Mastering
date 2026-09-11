# Lesson 18: Django ORM queries

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 17; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

The ORM is a translator from Python requests to database queries. A QuerySet is often an order ticket waiting to be executed, not a bag of already loaded records.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| ORM | Object-relational mapping between code objects and database rows. | the Python-to-ledger translator. |
| QuerySet | A composable database query and its results when evaluated. | an order ticket. |
| Lazy evaluation | Deferring work until results are needed. | filling the order when collected. |
| Lookup | A field comparison used in a query. | the clerk’s selection rule. |
| Aggregation | Combining rows into summary values. | adding ledger totals. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
# Run in manage.py shell after creating the fixture
low = Product.objects.filter(stock__lte=4).order_by("id")
print(list(low.values_list("name", flat=True)))
```

Import Product from inventory.models first. filter composes a query; list evaluates it. stock__lte means stock less than or equal to the supplied value. get expects exactly one row and raises exceptions for zero or multiple matches.

**Prediction:** With Pen stock 4 and Book stock 8, inserted in that order, enter the names returned.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Seed a fixture

Create Pen 200/4, Book 500/8 and Bag 4000/0 in a disposable database. Record primary keys and clear only your practice rows when repeating.

### Step 2: Filter and order

Query stock <=4 ordered by stock then id. Expect Bag and Pen. Save Python and output, then check threshold 0.

### Step 3: Retrieve safely

Use get(pk=...) for Pen and catch Product.DoesNotExist for a missing ID. Explain why filter returns an empty QuerySet instead of raising for no match.

### Step 4: Update stock

Use an F expression to increase Pen stock by 3, then refresh_from_db. Expect 7. Explain why an already loaded object can show an older value.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Import Product from inventory.models first.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-18/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

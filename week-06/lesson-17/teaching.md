# Lesson 17: Models and migrations

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 16; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A model describes the product ledger; a migration is a numbered renovation instruction for changing its structure. Editing the drawing alone does not renovate the database.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Model | A Python class mapping stored entities to database fields. | the product-ledger design. |
| Field | A typed model attribute mapped to stored data. | a ruled ledger column. |
| Migration | A versioned operation changing schema or data. | a numbered renovation instruction. |
| makemigrations | The command generating migration files from model changes. | writing the renovation plan. |
| migrate | The command applying pending migrations. | carrying out the plan. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
```

This belongs in inventory/models.py in the previous project. Django supplies a primary key unless you define one. PositiveIntegerField allows zero. Generate and inspect a migration, then apply it; saving models.py by itself does not add database columns.

**Prediction:** What stock value is declared as the default?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Define Product

Add name max_length=120, price and stock whole-naira/integer fields with stock default 0. Explain each field choice and add __str__.

### Step 2: Generate a migration

Run python manage.py makemigrations inventory. Open the generated file and identify CreateModel, field types and dependencies in notes.

### Step 3: Apply the schema

Run python manage.py migrate and showmigrations inventory. Save output showing the migration applied; explain the difference between generation and application.

### Step 4: Create a record

In manage.py shell create Pen price 200 stock 4. Close/reopen the shell and fetch the saved primary key. Record the persistent values.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: This belongs in inventory/models.py in the previous project.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-17/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

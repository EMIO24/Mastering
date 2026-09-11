# Lesson 19: Django CRUD views

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 18; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

CRUD is the four basic actions at the ledger desk: create a card, read it, update it and delete it. Web views wrap these actions in requests, responses and access rules.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| CRUD | Create, read, update and delete operations. | the four ledger services. |
| URL parameter | A value extracted from a matched URL. | the card number on a request. |
| 404 | A response indicating the resource was not found. | no card at that address. |
| Redirect | A response telling the client to request another URL. | a direction to the next desk. |
| CSRF | Cross-site request forgery using a browser’s ambient credentials. | an outsider tricking a signed-in clerk into submitting a form. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
from django.shortcuts import get_object_or_404, render
from .models import Product

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "inventory/detail.html", {"product": product})
```

The URL pattern must capture pk and the template must exist. get_object_or_404 converts a missing row into a 404 response. Read-only GET views should not change data. State-changing browser forms use POST and Django CSRF protection.

**Prediction:** What HTTP status should a missing product detail return?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: List products

Implement a GET list view ordered by ID. Render name, price and stock; show a clear empty-state message for no rows.

### Step 2: Show one product

Add /products/<int:pk>/ and a detail template. Demonstrate a valid product and a missing ID returning 404.

### Step 3: Create safely

Add a POST creation view that validates nonblank name and nonnegative integer price/stock. Use a CSRF-protected HTML form; invalid input must create no row.

### Step 4: Update an existing record

Add edit GET/POST flows. Change stock 4 to 7 and redirect after success. A missing ID returns 404; invalid input preserves the stored row.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: The URL pattern must capture pk and the template must exist.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-19/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

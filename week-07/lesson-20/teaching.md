# Lesson 20: Forms and validation

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 19; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A Django form is a receiving clerk who checks raw paperwork before handing trusted fields to the ledger. Browser checks help the visitor, but the server clerk must still check everything.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Bound form | A form associated with submitted data. | paperwork filled by a visitor. |
| Validation | Checking and converting data against rules. | the receiving clerk’s inspection. |
| cleaned_data | Validated and converted form values. | the accepted fields. |
| ModelForm | A form derived from selected model fields. | a form designed from the ledger columns. |
| Field error | Feedback attached to a particular input. | a note next to the incorrect box. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
from django import forms

class StockForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

form = StockForm({"quantity": "3"})
print(form.is_valid())
print(form.cleaned_data["quantity"])
```

Run within the configured Django project. Raw HTTP form values are strings. IntegerField converts and validates them, so cleaned quantity is integer 3. Access cleaned_data after validation, and only use fields that passed validation.

**Prediction:** Enter the two printed values as a JSON list.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Build ProductForm

Create a ModelForm exposing only name, price and stock. Render field errors and preserve submitted input when validation fails.

### Step 2: Reject blank names

Strip name whitespace in clean_name and reject an all-space value. Demonstrate " Pen " becomes Pen and "   " creates no product.

### Step 3: Validate quantities

Create SaleForm with IntegerField(min_value=1). Demonstrate 3 accepted and 0, -1, "two" and "2.5" rejected with visible field errors.

### Step 4: Check related rules

Validate requested quantity against the selected product’s available stock. Starting stock 4, quantity 5 is rejected without changing the database.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Run within the configured Django project.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-20/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

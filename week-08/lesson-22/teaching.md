# Lesson 22: DRF serializers

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 21; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A serializer is a bilingual receiving clerk: it converts model data to simple response values and checks incoming values before creating or changing records. It is not itself the network connection.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Serializer | A component converting and validating representations. | the bilingual receiving clerk. |
| Deserialization | Turning an external representation into internal values. | translating an incoming form. |
| validated_data | Input values accepted by serializer validation. | the approved fields. |
| read_only | A field excluded from writable input. | an office-assigned box. |
| ModelSerializer | A serializer with model-derived fields and defaults. | a clerk using the ledger blueprint. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
from rest_framework import serializers

class SaleSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)

s = SaleSerializer(data={"quantity": "3"})
print(s.is_valid())
print(s.validated_data["quantity"])
```

Run in a Django project with DRF installed. Passing data= means incoming values need validation; passing an instance means representing existing data. is_valid performs checks before validated_data is consumed. This example converts the text quantity to integer 3.

**Prediction:** Enter the validated quantity as a JSON number.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Configure DRF

Add rest_framework to INSTALLED_APPS in your project and record the installed version. Keep dependency versions in requirements.txt.

### Step 2: Represent Product

Create ProductSerializer with explicit id, name, price and stock fields. Serialize Pen and show a JSON-compatible dictionary; serialize a list using many=True.

### Step 3: Validate incoming data

Instantiate with data= for valid Pen input and invalid negative stock. Call is_valid and record validated_data or field errors; invalid input must not save.

### Step 4: Protect assigned fields

Make id read-only. Supply an arbitrary id in input and demonstrate the client cannot choose an existing row’s primary key on creation.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Run in a Django project with DRF installed.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-22/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

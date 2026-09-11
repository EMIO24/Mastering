# Lesson 23: DRF API views

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 22; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

An API view is the dispatcher joining request handling, validation and response formatting. The serializer inspects the paperwork; the view decides when to use it and which response to send.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| APIView | DRF’s class-based request handling base. | the API service desk. |
| Response | A DRF response rendered according to content negotiation. | a receipt awaiting its final format. |
| request.data | Parsed request content exposed by DRF. | the opened order envelope. |
| Content negotiation | Choosing a supported response representation. | agreeing on the receipt format. |
| Generic view | A reusable implementation of common API operations. | a standard desk procedure. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})
```

Wire health into Django URLs. The decorator restricts methods and wraps the Django request with DRF behaviour. Returning a dictionary alone is insufficient; Response carries data for rendering. Use serializer errors with 400 and creation success with 201.

**Prediction:** Which status code should POST to this GET-only endpoint return?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: List through an API

Implement GET /api/products/ using ProductSerializer(many=True). Demonstrate populated and empty results, documenting whether pagination is enabled.

### Step 2: Create through an API

Implement POST using request.data, serializer validation and save. A valid product returns 201; invalid stock returns 400 and no extra row.

### Step 3: Read one product

Implement GET detail using a primary-key URL parameter. Return serialized data for an existing row and 404 for a missing one.

### Step 4: Update one product

Implement PUT or PATCH with the documented completeness rules. Demonstrate changing stock, preserving unrelated fields on PATCH, and rejecting a negative value.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Wire health into Django URLs.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-23/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

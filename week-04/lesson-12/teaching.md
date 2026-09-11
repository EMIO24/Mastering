# Lesson 12: REST API design

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 11; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

An API is a published service counter contract. Resource URLs are labelled counters such as products and sales. REST is an architectural style, not merely putting JSON on any URL.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| API | An interface through which software interacts. | the published counter contract. |
| Resource | A concept identified and manipulated through a representation. | a product record at a named counter. |
| Representation | Data describing a resource. | a copy of the product card. |
| Stateless request | A request understood without relying on stored client conversation context. | an order carrying the needed credentials and details. |
| Pagination | Dividing a collection into bounded result pages. | issuing a catalogue a few pages at a time. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```text
GET /api/products/?page=2

{"count":3,"next":null,"previous":"?page=1",
 "results":[{"id":3,"name":"Bag"}]}
```

A collection response wraps a page of records with navigation metadata. A client must read results rather than assuming the root is an array. Statelessness does not mean the server has no database; it concerns request context.

**Prediction:** How many product records are in this response page?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Specify resources

List products, customers and sales with collection/detail URLs. Use stable IDs, and explain why a sale deserves its own resource.

### Step 2: Write endpoint contracts

Create api-contract.md covering list, detail, create, update and delete products. Specify method, URL, request fields, success status and error status for each.

### Step 3: Define validation

Require nonblank name, integer price >=0 and integer stock >=0. Give one accepted JSON body and four rejected bodies with field-specific errors.

### Step 4: Paginate products

Design a page size of 2 for five sample products. Write all three response pages and correct next/previous values. Keep ordering explicit by ID.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: A collection response wraps a page of records with navigation metadata.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-12/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

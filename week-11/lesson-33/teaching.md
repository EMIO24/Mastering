# Lesson 33: Async JavaScript and APIs

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 32; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A promise is a collection ticket for work that may finish later. await pauses that async function until the ticket settles; it does not freeze every activity in the browser.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Promise | An object representing eventual completion or failure. | the collection ticket. |
| async | A function declaration/expression returning a promise. | a counter that issues tickets. |
| await | Pausing an async function until a promise settles. | waiting for your ticket at that counter. |
| fetch | A browser/JavaScript API for making requests. | sending the order. |
| Race condition | A result depending on the timing of competing operations. | older paperwork arriving after its replacement. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```javascript
async function loadProducts() {
  const response = await fetch("/api/products/");
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}
```

fetch commonly resolves even for HTTP 404 or 500, so inspect response.ok. Parsing JSON is another asynchronous operation. Surround calls with try/catch for request, status and parsing failures; distinguish loading, empty, success and error states.

**Prediction:** Does a fetch response with status 404 have ok equal to true? Enter a Boolean.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Trace scheduling

Log start, queue a resolved Promise callback, then log end. Predict and record the order in practice.js and explain why the callback follows synchronous code.

### Step 2: Fetch local products

Implement loadProducts using the example and your local API. Document whether it returns an array or paginated envelope and extract the intended records.

### Step 3: Show loading

Disable a load button while a request runs and display Loading. Restore the button in finally on both success and failure.

### Step 4: Handle HTTP errors

Call a missing local endpoint and a mocked 500 response. Check response.ok and display a useful status-based message without treating the error body as product data.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: fetch commonly resolves even for HTTP 404 or 500, so inspect response.ok.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-33/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

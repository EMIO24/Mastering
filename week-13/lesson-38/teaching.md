# Lesson 38: Frontend architecture

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 37; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A growing frontend is a shop with separate responsibilities: page counters coordinate tasks, reusable displays show information, and one delivery office handles API transport.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Separation of concerns | Assigning distinct responsibilities to code units. | different staff roles. |
| Custom Hook | A reusable function composing React Hooks. | a reusable stateful desk procedure. |
| API client | A module centralizing request behaviour. | the delivery office. |
| Single source of truth | One authoritative owner for a piece of state. | one official stock notebook. |
| Context | A React mechanism making a value available down a tree. | a shared notice accessible to descendants. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```javascript
// api/products.js
export async function listProducts(signal) {
  const response = await fetch("/api/products/", {signal});
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const body = await response.json();
  return body.results; // Contract: this endpoint is paginated.
}
```

Centralizing the transport contract means pages do not repeat envelope parsing and status handling. A custom Hook can own request state while a component owns display. Avoid putting every local input in global Context; scope state to its actual consumers.

**Prediction:** Which field contains the product array in the declared paginated contract?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Map the current app

Draw pages, reusable components, hooks and API modules. Identify duplicated request code and duplicated ownership of the same state.

### Step 2: Extract the API client

Implement list/get/create/update product functions with consistent status and JSON handling. Document exact inputs/outputs and the pagination envelope.

### Step 3: Create useProducts

Extract loading/data/error/retry behaviour into a custom Hook. Keep cancellation or stale-response protection and demonstrate two UI consumers using the same contract.

### Step 4: Separate display

Make ProductList accept products and callbacks as props without fetching internally. Render it against local empty and populated fixtures.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Centralizing the transport contract means pages do not repeat envelope parsing and status handling.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-38/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

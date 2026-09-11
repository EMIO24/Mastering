# Lesson 39: Full-stack integration

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 38; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

Integration is a full rehearsal from shop display to ledger and back. The browser proposes a sale; the server authorizes and validates it; the database commits it; the browser shows the confirmed result.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| End-to-end flow | A user operation spanning the system’s components. | the complete checkout rehearsal. |
| Contract mismatch | Disagreement about request or response structure. | two desks using different form versions. |
| Optimistic update | Showing an anticipated change before confirmation. | writing a provisional receipt. |
| Rollback | Restoring a prior valid state after failure. | cancelling the provisional entry. |
| Source of truth | The authoritative record used to resolve disagreement. | the official ledger. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```javascript
async function createSale(productId, quantity) {
  const response = await fetch("/api/sales/", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({product_id: productId, quantity})
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}
```

Add the authentication and CSRF handling required by your chosen session/token design; the snippet only shows the body contract. For the first implementation, show a sale as successful only after confirmation. A server transaction must protect stock regardless of client checks.

**Prediction:** Confirmed stock is 10 and a successful sale quantity is 3. What stock should the refreshed UI show?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Agree on one contract

Compare frontend field names, routes, pagination and statuses with the running API. Write a corrected contract and resolve at least one demonstrated mismatch.

### Step 2: Connect authentication

Implement the chosen login/logout flow and authenticated API transport. Demonstrate signed-out rejection, valid login and logout without recording credentials.

### Step 3: Load owned inventory

Fetch and display only the signed-in user’s products. Use two users and demonstrate no cross-user records appear.

### Step 4: Create and edit

Submit product forms to the API. Show successful changes appear after reload and server field errors remain visible without discarding the draft.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Add the authentication and CSRF handling required by your chosen session/token design; the snippet only shows the body contract.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-39/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

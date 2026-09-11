# Lesson 35: React state and controlled forms

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 34; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

State is a component’s remembered notebook. Each render sees a snapshot. Asking React to update it schedules a new snapshot; it does not rewrite the variable in the currently running handler.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| State | Data React retains between renders. | the component’s notebook. |
| Hook | A React function connecting components to features such as state. | a standard notebook service. |
| State setter | A function scheduling a state update. | a request for the next notebook page. |
| Controlled input | An input whose displayed value comes from state. | a form box synchronized with the notebook. |
| Lifting state | Moving shared state to a common ancestor. | one shared notebook for two counters. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```javascript
import {useState} from "react";

export function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => {
    setCount(c => c + 1);
    setCount(c => c + 1);
  }}>{count}</button>;
}
```

Functional updates receive the queued previous value, so one click adds 2. Two setCount(count + 1) calls in this handler would each use the same render snapshot. Keep Hooks at the top level of components or custom Hooks.

**Prediction:** Starting at 0, what count is displayed after one click?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Add a counter

Implement Counter and demonstrate the initial 0 and one-click 2 result. Compare functional setters with two snapshot-based setters in a separate demonstration.

### Step 2: Control a quantity field

Use state for an input value and onChange. Keep the raw text while editing; convert and validate on submit. Demonstrate empty, 3 and invalid text.

### Step 3: Build an add-product form

Control name, price and stock inputs. Reject blank name or negative/non-integer numbers with visible messages; successful submission calls a parent callback.

### Step 4: Update arrays immutably

Add a new product using a new array and update one product with map plus object spread. Show existing product data is preserved.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Functional updates receive the queued previous value, so one click adds 2.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-35/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

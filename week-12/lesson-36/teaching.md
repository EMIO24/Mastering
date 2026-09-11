# Lesson 36: React effects and data fetching

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 35; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

An Effect synchronizes the rendered application with an outside system, like arranging a delivery subscription after opening a counter. Cleanup cancels the old arrangement before a replacement or unmount.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Effect | Logic synchronizing a component with an external system. | the delivery arrangement. |
| Dependency array | Reactive values that determine resynchronization. | the details that require a new arrangement. |
| Cleanup | Logic stopping or undoing the previous synchronization. | cancelling the old arrangement. |
| Unmount | Removing a component from the rendered tree. | closing the counter. |
| Stale response | A completed request no longer matching current intent. | a delivery for an old order. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```javascript
useEffect(() => {
  const controller = new AbortController();
  fetch(url, {signal: controller.signal})
    .then(r => { if (!r.ok) throw new Error(`HTTP ${r.status}`); return r.json(); })
    .then(setData)
    .catch(e => { if (e.name !== "AbortError") setError(e.message); });
  return () => controller.abort();
}, [url]);
```

Import useEffect and supply url, setData and setError within a component. This snippet illustrates synchronization/cleanup; the assignment adds complete loading and stale-result handling. Effects are not needed to calculate a total from existing state. Development Strict Mode may run an extra setup/cleanup cycle.

**Prediction:** If url changes from /a to /b, should this Effect resynchronize? Enter a Boolean.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Fetch on mount

Create a product page using an Effect and local API URL. Display products after a successful response and record the initial and loaded UI.

### Step 2: Represent request states

Model loading, success, empty and error states explicitly. Provide a local mock for each and verify the right content is visible.

### Step 3: Respond to dependencies

Add a search query or category input used in the request URL. Include reactive dependencies and demonstrate changed input fetches the corresponding data.

### Step 4: Clean up requests

Use AbortController on cleanup and ignore cancellation errors. Navigate away during a delayed request and verify no obsolete update is applied.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Import useEffect and supply url, setData and setError within a component.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-36/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

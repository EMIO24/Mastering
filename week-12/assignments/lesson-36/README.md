# Lesson 36 assignment: React effects and data fetching

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

An Effect synchronizes the rendered application with an outside system, like arranging a delivery subscription after opening a counter. Cleanup cancels the old arrangement before a replacement or unmount.

Use the Lesson 35 React app and ProductPage.jsx. Use a real local API or labelled mocks with the same paginated contract: {count,next,previous,results}. A mocked success does not prove backend integration.

## Where to work and how to run it

Work in `week-12/assignments/lesson-36/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside frontend/ use the prepared dependencies and run `npm run dev`; open its printed URL. If starting fresh, while online run `npm create vite@latest frontend -- --template react` from the assignment folder, then `npm install` inside frontend/. Check its Node requirement and keep package-lock.json. JSX goes in src components, not a Python file or plain browser console. Offline work requires dependencies prepared in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `frontend/src/ProductPage.jsx` |
| 4 | `frontend/src/ProductPage.jsx` |
| 5 | `frontend/src/ProductPage.jsx` |
| 6 | `frontend/src/ProductPage.jsx` |
| 7 | `frontend/src/ProductPage.jsx` |
| 8 | `frontend/src/ProductPage.jsx` |
| 9 | `frontend/src/ProductPage.jsx` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Effect** | Logic synchronizing a component with an external system. | the delivery arrangement. |
| **Dependency array** | Reactive values that determine resynchronization. | the details that require a new arrangement. |
| **Cleanup** | Logic stopping or undoing the previous synchronization. | cancelling the old arrangement. |
| **Unmount** | Removing a component from the rendered tree. | closing the counter. |
| **Stale response** | A completed request no longer matching current intent. | a delivery for an old order. |

A **fixture** is known starting data, like a prepared sample shelf. A **boundary case** lies at the edge of a rule, such as requesting exactly the available stock. **Expected** is what the rule says should happen; **actual** is what you observed. A **criterion** is one part of the marking scheme. An **artefact** is a file or concrete result you created. **Demonstrate** means carry out the action and record its actual result, not merely say that it works.

## Exercise 1: Explain the five terms — 10 points

**Where:** Exercise 1 in `answers.md`.

1. Read the five topic terms above, then explain each in your own words.
2. Give an everyday analogy for each and map its parts explicitly. For example: “A function is like a service counter: arguments are the order and the returned value is the item handed back.” Use this form with this lesson's terms.
3. Explain one point where one of your analogies stops fitting the precise rule. Software cannot infer missing instructions through human judgement.

**Finished when:** all five terms have an accurate meaning and mapped analogy. Each earns 1 point for meaning and 1 for mapping. Manual criterion: `exercise_01`.

## Exercise 2: Predict and check the worked example — 10 points

**Where:** `exercise_02` in `submission.json`; reasoning in `answers.md`.

Use this exact example and the input/conditions in the question. This may be a code fragment or a message/query to trace. Use the setup above and the explanation below to place it correctly.

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

**Question:** If url changes from /a to /b, should this Effect resynchronize? Enter a Boolean.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Import useEffect and supply url, setData and setError within a component. This snippet illustrates synchronization/cleanup; the assignment adds complete loading and stale-result handling. Effects are not needed to calculate a total from existing state. Development Strict Mode may run an extra setup/cleanup cycle.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Fetch on mount - 10 points

**Where:** `frontend/src/ProductPage.jsx`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Create a product page using an Effect and local API URL. Display products after a successful response and record the initial and loaded UI.

An Effect starts synchronization after React renders the page.

1. Create ProductPage with data, loading and error state, and an Effect that requests the local product endpoint.
2. Check response.ok, parse JSON and extract results according to the documented page contract.
3. Render loading before completion and the product list after success.
4. Use a known Pen/Book response and inspect Network or a clearly labelled local mock log.

**Check:** the list appears from received data rather than a hard-coded success screen. Do not call fetch directly on every render, because state updates would keep starting new requests.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Represent request states - 10 points

**Where:** `frontend/src/ProductPage.jsx`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Model loading, success, empty and error states explicitly. Provide a local mock for each and verify the right content is visible.

A request has more than two useful display states.

1. Define visible loading, populated success, empty success and error branches.
2. Prepare deterministic responses for two products, zero products, a delayed response and a rejection.
3. Run each case from a clean state and record what is visible while pending and after settlement.
4. Decide explicitly whether old data stays visible during a refresh.

**Check:** empty data is not shown as a network failure, and an error does not leave a permanent spinner. Your screen policy handles transitions as well as the initial page load.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Respond to dependencies - 10 points

**Where:** `frontend/src/ProductPage.jsx`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Add a search query or category input used in the request URL. Include reactive dependencies and demonstrate changed input fetches the corresponding data.

Changing a request input should start the corresponding new synchronization.

1. Add a search/category input and derive the request URL from its current value.
2. Include the reactive values read by the Effect in its dependency list, keeping the request logic consistent with them.
3. Search for Pen, then Book using distinguishable mock/server results.
4. Inspect requests and explain why an empty dependency array would miss later changes.

**Check:** each changed input produces its intended data. Do not suppress a dependency warning without understanding which changing value the Effect reads.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Clean up requests - 10 points

**Where:** `frontend/src/ProductPage.jsx`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Use AbortController on cleanup and ignore cancellation errors. Navigate away during a delayed request and verify no obsolete update is applied.

Cleanup stops work belonging to a screen that has gone away.

1. Create an AbortController inside the Effect and pass its signal to fetch.
2. Return a cleanup function that aborts it; ignore AbortError while displaying real errors.
3. Start a delayed request, then hide/unmount ProductPage through a parent toggle before it finishes.
4. Reopen the page and confirm a fresh request works.

**Check:** the old request is cancelled or guarded from applying results after cleanup. In development Strict Mode, an extra setup/cleanup cycle is expected; code must tolerate it rather than disabling the check as a fix.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Prevent stale results - 10 points

**Where:** `frontend/src/ProductPage.jsx`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Delay query A longer than query B, request A then B, and prove B remains displayed when A finishes. Use cancellation or an active-request guard.

The last response to arrive is not necessarily the latest requested search.

1. Configure query A to finish after query B, then trigger A followed quickly by B.
2. Use cancellation plus an active/request-identity guard where necessary before setting data, error or loading state.
3. Observe B's completed result, then let A's delay expire.
4. Repeat with a mock that cannot actually cancel transport, to test the guard itself.

**Check:** A never replaces B and does not clear B's pending spinner early. Guarding only setData while obsolete catch/finally handlers still change state can leave another race.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Add retry - 10 points

**Where:** `frontend/src/ProductPage.jsx`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Provide a retry button after an error. Demonstrate failed -> loading -> success with a deterministic mock without forcing a full page reload.

Retry should create a new attempt with understandable state transitions.

1. Display a Retry button in the error branch.
2. Implement a retry counter/dependency or explicit reusable request trigger, keeping cancellation protection.
3. Configure the first attempt to fail and the next to return products.
4. Click Retry and record error → loading → success without reloading the entire browser page.

**Check:** the old error clears at the intended point, one current attempt controls the UI and repeated clicks follow your documented disabled/loading policy. Retry must not reuse an already aborted controller.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Remove unnecessary effects - 10 points

**Where:** `frontend/src/ProductPage.jsx`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Compute filtered visible products or inventory total directly from current data where appropriate. Explain why storing the derived value via another Effect risks unnecessary synchronization.

Use Effects for outside synchronization, not every calculation from existing data.

1. Find a filtered list or inventory total that depends only on current products and local filter state.
2. Calculate it during rendering instead of storing it through a second Effect.
3. Change a product quantity and the filter; compare results with manual expectations.
4. Explain which Effect remains necessary for network synchronization and why the derived calculation is different.

**Check:** derived display follows current inputs without an extra stale intermediate state. This does not prohibit measured memoization later; the goal is removing unnecessary duplicated state.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a successful resynchronization and an obsolete-response/unmount case. Record which request is permitted to change data, errors and loading. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 36
python grade.py rubric --lesson 36
```

The first checks the JSON prediction and writes `grading/reports/lesson-36.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-36/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

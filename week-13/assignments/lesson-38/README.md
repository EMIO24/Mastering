# Lesson 38 assignment: Frontend architecture

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A growing frontend is a shop with separate responsibilities: page counters coordinate tasks, reusable displays show information, and one delivery office handles API transport.

Use the working list/detail/form React app. Record current behaviour before extracting modules. The API client below expects the results field of a paginated response; reconcile it with your actual API contract.

## Where to work and how to run it

Work in `week-13/assignments/lesson-38/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside frontend/ use the prepared dependencies and run `npm run dev`; open its printed URL. If starting fresh, while online run `npm create vite@latest frontend -- --template react` from the assignment folder, then `npm install` inside frontend/. Check its Node requirement and keep package-lock.json. JSX goes in src components, not a Python file or plain browser console. Offline work requires dependencies prepared in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `architecture.md` |
| 4 | `frontend/src/api/products.js` |
| 5 | `frontend/src/hooks/useProducts.js` |
| 6 | `frontend/src/ProductList.jsx` |
| 7 | `frontend/src/SessionContext.jsx` |
| 8 | `frontend/src/ErrorMessage.jsx` |
| 9 | `regression-notes.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Separation of concerns** | Assigning distinct responsibilities to code units. | different staff roles. |
| **Custom Hook** | A reusable function composing React Hooks. | a reusable stateful desk procedure. |
| **API client** | A module centralizing request behaviour. | the delivery office. |
| **Single source of truth** | One authoritative owner for a piece of state. | one official stock notebook. |
| **Context** | A React mechanism making a value available down a tree. | a shared notice accessible to descendants. |

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
// api/products.js
export async function listProducts(signal) {
  const response = await fetch("/api/products/", {signal});
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const body = await response.json();
  return body.results; // Contract: this endpoint is paginated.
}
```

**Question:** Which field contains the product array in the declared paginated contract?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Centralizing the transport contract means pages do not repeat envelope parsing and status handling. A custom Hook can own request state while a component owns display. Avoid putting every local input in global Context; scope state to its actual consumers.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Map the current app - 10 points

**Where:** `architecture.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Draw pages, reusable components, hooks and API modules. Identify duplicated request code and duplicated ownership of the same state.

Map responsibilities before moving code between files.

1. Draw the current pages, display components, state owners and fetch calls in architecture.md.
2. Mark duplicate status handling, response parsing and duplicated copies of product state.
3. Propose specific destinations: api module for transport, custom Hook for request state, components for display.
4. Record one working list/detail/add/edit journey as the pre-change baseline.

**Check:** each proposed move addresses an identified responsibility. A folder named services is not architectural evidence unless you explain which behaviour belongs there and why.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Extract the API client - 10 points

**Where:** `frontend/src/api/products.js`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Implement list/get/create/update product functions with consistent status and JSON handling. Document exact inputs/outputs and the pagination envelope.

Give callers one consistent interface to product requests.

1. In src/api/products.js implement list/get/create/update functions with documented arguments and returned values.
2. Check response.ok and parse the expected body; handle an empty response only for operations that actually use one.
3. For list, extract results from the paginated envelope. Preserve status/field errors in a useful error representation.
4. Run one success and one failure through each relevant function using local API or labelled mocks.

**Check:** callers no longer duplicate envelope parsing. Do not discard field-level 400 errors into an uninformative success-shaped empty object.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Create useProducts - 10 points

**Where:** `frontend/src/hooks/useProducts.js`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Extract loading/data/error/retry behaviour into a custom Hook. Keep cancellation or stale-response protection and demonstrate two UI consumers using the same contract.

A custom Hook packages request state and lifecycle behaviour for reuse.

1. Create useProducts with data/loading/error plus a retry interface matching your page's needs.
2. Move request/cancellation logic from the page into the Hook; keep dependencies and stale-response protection.
3. Render two test consumers, each using the same documented return shape.
4. Demonstrate delayed success, error and retry.

**Check:** both consumers can use the Hook contract. Two Hook calls normally have independent state; extracting a Hook does not automatically create one shared global cache or prevent duplicate network calls.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Separate display - 10 points

**Where:** `frontend/src/ProductList.jsx`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Make ProductList accept products and callbacks as props without fetching internally. Render it against local empty and populated fixtures.

A display component should be usable with supplied data alone.

1. Refactor ProductList to receive products and event callbacks as props, without fetching internally.
2. Render it in a simple fixture page with [], then Pen/Book records.
3. Supply a selection callback and verify the selected ID.
4. Keep request-state presentation in the containing page/Hook boundary as you designed it.

**Check:** the list works with no live API and no hidden dependency on global session data. This fixture demonstrates display behaviour; it does not certify backend integration.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Scope shared state - 10 points

**Where:** `frontend/src/SessionContext.jsx`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Use Context for session information only where needed. Keep a single form’s draft state local and explain the boundary with a component tree.

Share state only as widely as its consumers require.

1. Put session identity/login/logout information in a SessionContext provider above the relevant pages.
2. Read it in navigation and protected-page UI.
3. Keep one product form's unsaved draft in that form rather than global Context.
4. Draw consumers and explain where each value is authoritative.

**Check:** login updates session consumers while editing a form does not overwrite global product/session data. Context distributes a value; it does not replace server-side authentication or authorization.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Centralize error presentation - 10 points

**Where:** `frontend/src/ErrorMessage.jsx`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Define a reusable error component with a message and optional retry action. Show network failure and field-validation feedback remain distinguishable.

Central error presentation should preserve the distinction between retryable failure and field correction.

1. Create ErrorMessage accepting a user-facing message and optional retry callback.
2. Show it for a simulated network failure and verify retry is actionable.
3. For a 400 form response, keep field-specific messages beside the relevant fields instead of hiding them all in a generic banner.
4. Test keyboard access and error visibility.

**Check:** users can retry a request failure and correct a stock error without losing draft inputs. Avoid showing raw server stack traces as the shared component's message.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Check architectural change - 10 points

**Where:** `regression-notes.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Repeat list/detail/add/edit flows after refactoring. Record behaviour before/after and verify API calls, permissions and stale-response handling remain correct.

Refactoring should retain behaviour, not merely compile with a new directory tree.

1. Repeat the baseline list/detail/add/edit journey after the moves.
2. Compare request URLs, request bodies, status handling and persisted values.
3. Repeat a permission denial and the slow-A/fast-B stale-response check.
4. Record any intended change explicitly and fix unintended differences.

**Check:** the same contracts still work and old responses cannot overwrite new intent. A successful build cannot replace these behavioural checks because the compiler does not know your business rules.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new flow through an extracted module and an error/stale-response case. Compare the observable contract before and after refactoring. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 38
python grade.py rubric --lesson 38
```

The first checks the JSON prediction and writes `grading/reports/lesson-38.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-38/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

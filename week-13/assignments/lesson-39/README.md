# Lesson 39 assignment: Full-stack integration

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

Integration is a full rehearsal from shop display to ledger and back. The browser proposes a sale; the server authorizes and validates it; the database commits it; the browser shows the confirmed result.

Keep backend in project/ and frontend in frontend/, with separate prepared dependencies. Run both locally and use your existing authentication approach consistently. Start each independent sale check with stock 10; the server owns authoritative stock.

## Where to work and how to run it

Work in `week-13/assignments/lesson-39/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Run backend and frontend from their own project/ and frontend/ directories. For Lesson 39 use the project interpreter with `python manage.py runserver` and use `npm run dev` in a second terminal. In Lesson 40 use `npm run build` and your selected production application server; document its exact command and configuration. The assignment checker does not start these services.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `api-contract.md` |
| 4 | `frontend/src/api/ and auth UI` |
| 5 | `frontend/src/ProductListPage.jsx` |
| 6 | `frontend/src/ProductForm.jsx` |
| 7 | `project/inventory/views.py and frontend/src/SaleForm.jsx` |
| 8 | `failure-notes.md` |
| 9 | `demo.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **End-to-end flow** | A user operation spanning the system’s components. | the complete checkout rehearsal. |
| **Contract mismatch** | Disagreement about request or response structure. | two desks using different form versions. |
| **Optimistic update** | Showing an anticipated change before confirmation. | writing a provisional receipt. |
| **Rollback** | Restoring a prior valid state after failure. | cancelling the provisional entry. |
| **Source of truth** | The authoritative record used to resolve disagreement. | the official ledger. |

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

**Question:** Confirmed stock is 10 and a successful sale quantity is 3. What stock should the refreshed UI show?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Add the authentication and CSRF handling required by your chosen session/token design; the snippet only shows the body contract. For the first implementation, show a sale as successful only after confirmation. A server transaction must protect stock regardless of client checks.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Agree on one contract - 10 points

**Where:** `api-contract.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Compare frontend field names, routes, pagination and statuses with the running API. Write a corrected contract and resolve at least one demonstrated mismatch.

Reconcile actual client/server behaviour before joining more features.

1. Inspect one real product-list response and a create request from the running API/client.
2. Compare paths, trailing slashes, authentication, field names, numeric types, pagination and status codes with api-contract.md.
3. Correct mismatches in the contract and implementation together.
4. If none exists, deliberately test a mismatched mock in a disposable client check and show the detected failure; do not invent a past bug.

**Check:** both sides agree on results versus raw arrays and ID/value types. Save a redacted actual request/response pair, not only an aspirational specification.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Connect authentication - 10 points

**Where:** `frontend/src/api/ and auth UI`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Implement the chosen login/logout flow and authenticated API transport. Demonstrate signed-out rejection, valid login and logout without recording credentials.

Use the chosen authentication mechanism consistently end to end.

1. Connect login UI to the existing session or token endpoint and centralize authenticated requests in the API client.
2. Include the required cookie/CSRF handling for session requests or Bearer token for token requests.
3. Test wrong credentials, correct login, protected access and logout.
4. Record screen states/statuses with secrets redacted.

**Check:** signed-out access is rejected, login enables only authorized requests and logout follows the documented expiry/revocation policy. A frontend Boolean named loggedIn is not proof the server authenticated the call.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Load owned inventory - 10 points

**Where:** `frontend/src/ProductListPage.jsx`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Fetch and display only the signed-in user’s products. Use two users and demonstrate no cross-user records appear.

Render the current user's permitted inventory, not a shared fixture.

1. Create two disposable users with distinct product names/IDs.
2. Log in as A and load the real product list; then log out and log in as B.
3. Clear or replace cached user-specific data when the identity changes.
4. Inspect the response and screen for the other user's records.

**Check:** each identity sees only its owned/permitted data, including after switching accounts in one browser session. Hiding another user's cards after receiving their data is not sufficient isolation.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Create and edit - 10 points

**Where:** `frontend/src/ProductForm.jsx`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Submit product forms to the API. Show successful changes appear after reload and server field errors remain visible without discarding the draft.

Submit drafts to the server and display its confirmed outcome.

1. Connect ProductForm create/edit callbacks to the API client, disabling duplicate submission while pending.
2. On success use returned data or refetch and verify the change survives a full reload.
3. On field-validation errors retain the draft and display the server's field messages.
4. Test Pen/200/4 creation, a stock edit and a rejected negative-stock submission.

**Check:** accepted data persists; rejected data does not create or change rows. Client validation improves feedback but must not suppress or misinterpret the server's validation result.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Record a sale - 10 points

**Where:** `project/inventory/views.py and frontend/src/SaleForm.jsx`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Create the sale endpoint and frontend form with quantity validation and an atomic stock update. From stock 10 sell 3; show total and stock 7 after refresh.

A confirmed sale requires an atomic stock change on the server.

1. Add a sales endpoint accepting product_id and positive integer quantity; scope the product to the caller.
2. Within a transaction validate/deduct stock with an appropriate conditional update or backend-supported locking rule, then record historical quantity/unit price.
3. Connect a sale form and show success only after the server confirms it.
4. From fresh stock 10/price 500 sell 3, reload, then independently try quantity 11 from stock 10.

**Check:** success total 1500/stock 7 persists; oversale creates no sale and leaves 10. A disabled browser button does not enforce concurrency correctness.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Recover from failures - 10 points

**Where:** `failure-notes.md`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Simulate a rejected oversale and interrupted request. Keep a coherent UI, do not display false success, and explain how retry avoids duplicate sales in your design.

A lost reply can leave the client uncertain even when the server committed the sale.

1. Test a rejected oversale and show field/business feedback without a success receipt.
2. Simulate a request failure before sending, then a lost response after a simulated or real committed operation; label simulations.
3. Explain how the UI refreshes/reconciles uncertain state before retrying, or use a server-validated idempotency key that returns the same recorded result for a repeated request.
4. Test the chosen retry policy twice against the same intended sale.

**Check:** stock is not deducted twice for one retried operation under your claimed policy. Do not blindly restore an old optimistic stock value when the server may already have committed.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Rehearse the complete journey - 10 points

**Where:** `demo.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Record register/create-user -> login -> add -> sell -> reload -> logout in demo.md. Include API/database evidence and a direct unauthorized access attempt.

Rehearse the complete user journey from an empty business account.

1. In demo.md record create/register user → login → add Notebook 500/10 → sell 3 → reload → logout.
2. Include actual API statuses, assigned IDs and confirmed stock 7/total 1500 without credentials.
3. Attempt direct access to another user's known record and record denial plus unchanged data.
4. List outstanding limitations discovered during the journey with reproducible steps.

**Check:** every screen action corresponds to a verified server/database outcome. A collection of separate mocked components is not evidence of this real full-stack journey.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new real persisted flow and a denied/uncertain sale case. Trace browser, API and database evidence, explicitly labelling any simulation. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 39
python grade.py rubric --lesson 39
```

The first checks the JSON prediction and writes `grading/reports/lesson-39.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-39/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

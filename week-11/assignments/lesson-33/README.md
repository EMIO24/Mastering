# Lesson 33 assignment: Async JavaScript and APIs

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A promise is a collection ticket for work that may finish later. await pauses that async function until the ticket settles; it does not freeze every activity in the browser.

Create a browser page with a labelled Load products button, status element and product-list element. main.js handles UI, api.js handles requests, mocks.js simulates local responses. Start your backend for real requests; otherwise label mocked evidence clearly.

## Where to work and how to run it

Work in `week-11/assignments/lesson-33/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Run plain scripts with `node practice.js` or load them in a browser page and use its Console. ES module files need `<script type="module" src="main.js"></script>`. Serve this folder with `python -m http.server 8080 --bind 127.0.0.1` and open `http://127.0.0.1:8080/`. Relative /api/ fetches need a backend/proxy at that origin; otherwise use an explicit local API URL with appropriate origin settings or a labelled mock.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `practice.js` |
| 4 | `api.js` |
| 5 | `index.html and main.js` |
| 6 | `api.js and main.js` |
| 7 | `mocks.js and main.js` |
| 8 | `main.js` |
| 9 | `mocks.js` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Promise** | An object representing eventual completion or failure. | the collection ticket. |
| **async** | A function declaration/expression returning a promise. | a counter that issues tickets. |
| **await** | Pausing an async function until a promise settles. | waiting for your ticket at that counter. |
| **fetch** | A browser/JavaScript API for making requests. | sending the order. |
| **Race condition** | A result depending on the timing of competing operations. | older paperwork arriving after its replacement. |

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
async function loadProducts() {
  const response = await fetch("/api/products/");
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}
```

**Question:** Does a fetch response with status 404 have ok equal to true? Enter a Boolean.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

fetch commonly resolves even for HTTP 404 or 500, so inspect response.ok. Parsing JSON is another asynchronous operation. Surround calls with try/catch for request, status and parsing failures; distinguish loading, empty, success and error states.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Trace scheduling - 10 points

**Where:** `practice.js`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Log start, queue a resolved Promise callback, then log end. Predict and record the order in practice.js and explain why the callback follows synchronous code.

Promise callbacks wait until the current synchronous code finishes.

1. In practice.js log start, schedule `Promise.resolve().then(...)` to log promise, then log end.
2. Predict the order before running it in Node or the browser console.
3. Record actual output and explain the callback as a task queued after the current stack.
4. Repeat after adding another synchronous log before end.

**Check:** original order is start, end, promise. A resolved promise does not make its .then callback run inline before the following synchronous statement.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Fetch local products - 10 points

**Where:** `api.js`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Implement loadProducts using the example and your local API. Document whether it returns an array or paginated envelope and extract the intended records.

Fetch data through the agreed API contract.

1. Define async loadProducts in api.js. Await fetch, reject !response.ok and await/return parsed JSON.
2. Decide whether the function returns the full page envelope or extracts results; document that choice and use it consistently in main.js.
3. Call the running local product endpoint, using an explicit URL/proxy if your static page is served on another port.
4. Display two known products, then an empty result using real fixtures or labelled mocks.

**Check:** the UI reads actual records, not undefined because it mapped the page object as an array. Record whether evidence came from a server or a mock.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Show loading - 10 points

**Where:** `index.html and main.js`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Disable a load button while a request runs and display Loading. Restore the button in finally on both success and failure.

A loading state tells the user an operation is in progress and prevents duplicate clicks.

1. Before calling loadProducts, disable the load button and set status text to Loading.
2. On success render the products or an empty message.
3. On failure display an error; in finally restore the enabled button.
4. Use a local delayed promise so the in-progress state lasts long enough to inspect.

**Check:** delayed request shows Loading, repeated clicks are blocked while pending, and both success/failure re-enable the button. Do not clear the state only on the happy path.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Handle HTTP errors - 10 points

**Where:** `api.js and main.js`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Call a missing local endpoint and a mocked 500 response. Check response.ok and display a useful status-based message without treating the error body as product data.

An HTTP error response is still a response that fetch can successfully receive.

1. Request a missing local endpoint and inspect its status.
2. In loadProducts check response.ok before accepting the body as product data.
3. Add a mock returning status 500/ok false, distinct from a rejected promise.
4. Show a useful status-based error and retain a retry/load option.

**Check:** 404 and 500 do not render error-body fields as products. A catch block alone is insufficient if you never turn an unsuccessful HTTP status into an application error.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Handle parsing and network failures - 10 points

**Where:** `mocks.js and main.js`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Use local mocks returning invalid JSON and rejecting fetch. Demonstrate both reach the error UI and clear loading state.

Network failure and unreadable JSON are different failure points.

1. In mocks.js create one fetch replacement rejecting with an Error and another resolving an ok response whose json() rejects.
2. Inject each into your loading path rather than changing global browser behaviour unnecessarily.
3. Run both from a clean UI state and record visible error text plus loading/button state.
4. Explain which failure occurred before a response and which while parsing one.

**Check:** both errors are handled, loading ends and retry is available. Do not claim a JSON parse failure proves the server could not be reached.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Cancel obsolete requests - 10 points

**Where:** `main.js`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Use AbortController for a replaced search request. Treat cancellation separately from a server failure; show an older response cannot replace newer search results.

Cancel a superseded search so an old delivery cannot overwrite the latest order.

1. Create an AbortController for each search and pass its signal into fetch.
2. Before starting the next search, abort the previous one.
3. Ignore AbortError as expected cancellation; still show genuine failures.
4. Use a slow query A and fast query B, requesting A then B. If a mock ignores abort, add a request-ID/active guard before committing results.

**Check:** B remains displayed after A would have finished; cancellation does not flash a server-error message. A stopped loading flag from an obsolete request must not incorrectly finish the current request's spinner.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Use deterministic mocks - 10 points

**Where:** `mocks.js`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Create mock success, empty, delayed and rejected responses locally. Record observed UI states for each so practice and review need no internet.

Deterministic mocks let another learner repeat the same screen states offline.

1. Create named scenarios for success with Pen/Book, empty results, delayed success, HTTP error, invalid JSON and network rejection.
2. Keep their response shape consistent with the real API contract, including ok/status/json where your loader expects them.
3. Provide a local selector or documented function call to choose each scenario.
4. Record each expected/actual UI state in answers.md.

**Check:** every scenario can be repeated without internet and is explicitly labelled simulated. Mock success proves client behaviour against the mock, not correctness of the Django endpoint.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a successful async request and an out-of-order or failed response. Document timing, mock/server source and final UI state. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 33
python grade.py rubric --lesson 33
```

The first checks the JSON prediction and writes `grading/reports/lesson-33.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-33/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

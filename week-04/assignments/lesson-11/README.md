# Lesson 11 assignment: HTTP requests and responses

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

HTTP is the order-and-receipt format at the counter. The method says the kind of action; the path names the resource; the status reports what happened. A receipt alone does not explain every business outcome.

This is an HTTP message-reading/design assignment. requests.http and responses.http are text documents; the worked response is not Python code. For the real browser observation, serve public/index.html locally. No working create/update API is required yet.

## Where to work and how to run it

Work in `week-04/assignments/lesson-11/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside public/ run `python -m http.server 8000 --bind 127.0.0.1`. Open `http://127.0.0.1:8000/`, open browser Developer Tools → Network, and reload. Stop the server with Ctrl+C. Write HTTP message examples in text files; they are not shell commands.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `requests.http` |
| 4 | `requests.http` |
| 5 | `responses.http` |
| 6 | `update-contract.md` |
| 7 | `repetition.md` |
| 8 | `network-notes.md` |
| 9 | `errors.json` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **HTTP method** | A request token expressing intended semantics. | the action on an order form. |
| **Header** | Metadata sent with a request or response. | delivery instructions. |
| **Body** | The message content. | the order details. |
| **Status code** | A numeric response classification. | the result stamp. |
| **Idempotent** | Having the same intended effect when repeated. | setting a shelf label to the same value twice. |

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

```text
HTTP/1.1 201 Created
Content-Type: application/json
Location: /products/4

{"id":4,"name":"Pen","stock":10}
```

**Question:** Enter the response status code as a number.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

The blank line separates headers from the body. 201 means creation succeeded; Location can identify the created resource. GET should be safe; PUT is intended to be idempotent; POST is not generally idempotent. An identical status on repeated requests is not the definition of idempotency.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Write a read request - 10 points

**Where:** `requests.http`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Write a complete GET /products/4 HTTP/1.1 request with Host in requests.http. Include the blank line and explain why the path is not the method.

An HTTP request starts with the action and target, followed by metadata.

1. In requests.http write `GET /products/4 HTTP/1.1`, then a Host header naming your local service, then a blank line.
2. Annotate a separate copy in answers.md: GET is the method, /products/4 is the path, HTTP/1.1 is the protocol version.
3. Explain why the Host value does not belong inside the path.
4. Keep this as a raw message illustration; it is not a Python program or a command to paste directly into PowerShell.

**Check:** the request has a start line, Host header and header/body separator. A read-only request describes fetching product 4 and must not imply changing its stock.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Write a create request - 10 points

**Where:** `requests.http`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Add a POST /products request with Content-Type application/json and name/price/stock body. Include a matching 201 response with Location.

A create request carries fields that the server needs to make a new record.

1. Add a conceptual POST /products request with Host and Content-Type: application/json headers, a blank line, and JSON containing name Pen, price 200 and stock 10.
2. Write a matching response starting `HTTP/1.1 201 Created`, with JSON content type and Location: /products/4.
3. Include response JSON with assigned id 4 and the accepted fields.
4. Explain that a real HTTP client supplies correct body framing such as Content-Length; this file focuses on the application contract.

**Check:** request and response bodies are valid JSON; ID assignment is attributed to the server. The 201 status communicates creation rather than merely any successful read.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Classify failures - 10 points

**Where:** `responses.http`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Write response examples for malformed input (400), missing authentication (401), forbidden access (403), missing resource (404), and server error (500). Explain a scenario for each.

Choose a response that explains which kind of failure happened.

1. In responses.http write five short response sketches for: malformed JSON, missing credentials, recognized user lacking permission, nonexistent product and an unexpected server exception.
2. Assign statuses 400, 401, 403, 404 and 500 respectively for this proposed API contract.
3. Give each a small JSON body with a safe code/message; include an appropriate authentication challenge for the 401 design.
4. Explain what the client should fix or retry in each scenario.

**Check:** 401 and 403 are not described as interchangeable. The 500 body contains no traceback or secret. Actual frameworks may choose a particular challenge/denial status based on authentication configuration; document your contract explicitly.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Compare updates - 10 points

**Where:** `update-contract.md`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Describe replacing a complete product with PUT versus changing stock with PATCH. Give request bodies and explicitly state your API’s required fields.

Replacing a complete card and changing one box on it have different input requirements.

1. Define the current product as id 4, name Pen, price 200, stock 10.
2. Write a PUT body containing all required writable fields and setting stock to 5. State whether omitted required fields are rejected.
3. Write a PATCH body containing only stock 5; explain that name and price remain unchanged under this contract.
4. List successful status/body behaviour for each and an invalid negative-stock response.

**Check:** both valid examples leave stock 5; PATCH preserves omitted fields. Your PUT requirements are explicit, not inferred from the fact that both methods can update records.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Trace repetition - 10 points

**Where:** `repetition.md`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Apply PUT stock=5 twice to stock 10, then compare two POST sale quantity=2 operations starting at 10. Record final stocks and explain idempotency.

Idempotency concerns intended state after repetition, not identical response text.

1. In repetition.md start a fictional product at stock 10.
2. Trace PUT stock=5 once and then repeat exactly the same request. Record stock after each step.
3. Reset to 10; trace two separate POST sale quantity=2 operations.
4. Explain why retrying an uncertain sale POST can create another sale unless the API has a specific duplicate-request mechanism.

**Check:** PUT trace is 10 → 5 → 5; sale trace is 10 → 8 → 6. Do not generalize a harmless repeated GET into proof that every HTTP request is safe to retry.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Inspect real local headers - 10 points

**Where:** `network-notes.md`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Use the local server from Lesson 10 and browser tools to save one request/response pair. Identify header/body boundaries and explain Content-Type.

Inspect one actual HTTP exchange, not only handwritten examples.

1. Serve a small index.html with the local Python server and open it in a browser.
2. In Network, select the main document request. Record URL/method, status, request headers and response headers.
3. Find the response body and identify a sentence from your file. Explain which visible fields are metadata and which are content.
4. Keep any handwritten raw HTTP example labelled as a representation of the exchange rather than an exact packet capture.

**Check:** your notes identify Content-Type and the HTML body separately. The browser may use a protocol display different from your HTTP/1.1 teaching sketch; report the version actually observed.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Design error content - 10 points

**Where:** `errors.json`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Define a JSON error body with code, message and field errors. Give an invalid-stock example, ensuring it provides no stack trace or secret values.

An error document should help a caller correct the order without exposing server internals.

1. In errors.json design a body with `code`, `message` and a `fields` object.
2. Use an attempted product stock of -1 and put field-specific feedback under stock.
3. In answers.md associate this body with status 400 and explain how a form could show the stock message beside its input.
4. Compare with a generic server-error body that gives no stack trace.

**Check:** errors.json parses as JSON, identifies the invalid field and gives a usable correction. Do not include comments, exception dumps, passwords or guessed internal file paths in the example response.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose one successful operation and one request-error scenario. Write the complete method/path/status/body consequences and explain which component handles the failure. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 11
python grade.py rubric --lesson 11
```

The first checks the JSON prediction and writes `grading/reports/lesson-11.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-11/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

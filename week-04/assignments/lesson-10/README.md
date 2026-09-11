# Lesson 10 assignment: How the web works

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A browser requesting a page resembles a customer sending an order to a shop address. DNS finds an address; the server handles the request. The analogy leaves out caches, proxies and repeated network connections.

Create public/index.html and work on your own machine. Start the local server from public/. localhost and 127.0.0.1 refer to the computer running the browser. Keep observations in text files beside public/. No public website is needed.

## Where to work and how to run it

Work in `week-04/assignments/lesson-10/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside public/ run `python -m http.server 8000 --bind 127.0.0.1`. Open `http://127.0.0.1:8000/`, open browser Developer Tools → Network, and reload. Stop the server with Ctrl+C. Write HTTP message examples in text files; they are not shell commands.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `request-flow.md` |
| 4 | `answers.md` |
| 5 | `public/index.html` |
| 6 | `network-notes.md` |
| 7 | `network-notes.md` |
| 8 | `public/index.html` |
| 9 | `architecture.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Client** | Software requesting a service. | the customer. |
| **Server** | Software handling requests. | the shop counter. |
| **DNS** | A system resolving domain names to records such as IP addresses. | an address directory. |
| **URL** | An address identifying a resource and access scheme. | a shop address plus department. |
| **Port** | A numbered network endpoint on a host. | a numbered service door. |

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

```python
from urllib.parse import urlparse

u = urlparse("http://localhost:8000/products?low=1")
print(u.hostname, u.port, u.path)
```

**Question:** Enter the host, port and path from the example as a JSON list.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

localhost refers to the local machine; port 8000 selects the listening service. /products is a path handled by that service. The query carries extra request information. Parsing a URL does not contact a server.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Draw one request - 10 points

**Where:** `request-flow.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Draw browser -> name resolution -> connection -> server -> response -> browser rendering. Explain each arrow and distinguish transferred HTML from displayed pixels.

A page request travels through several services before the browser displays anything.

1. In request-flow.md draw browser → name resolution → connection → server → response → rendering.
2. Under each arrow explain what moves or happens: finding an address, connecting to a listening port, sending HTTP, receiving bytes and interpreting HTML.
3. Use a fictional shop domain for the DNS explanation, then compare it with localhost, which is resolved locally.
4. Explain why receiving HTML and drawing pixels are separate operations.

**Check:** your diagram names both request and response directions. DNS finds address information; it does not return the shop's inventory page. Do not claim the diagram captures every cache/proxy detail.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Dissect addresses - 10 points

**Where:** `answers.md`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Break http://localhost:8000/products?low=1 into scheme, host, port, path and query in answers.md. Explain why localhost on a friend’s laptop is not your machine.

A URL gives both a location and instructions about which resource is requested.

1. Copy `http://localhost:8000/products?low=1` into answers.md.
2. Make a table separating scheme, hostname, port, path and query string.
3. Compare the URL with `http://localhost:8000/products?low=0`: identify what changed and what stayed the same.
4. Explain what localhost means if your friend opens this URL on a different computer.

**Check:** scheme http, host localhost, port 8000, path /products, query low=1. Your friend's browser contacts their own computer. The query is not part of the hostname or port.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Serve a page locally - 10 points

**Where:** `public/index.html`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Create public/index.html with an inventory heading and two products. From public run python -m http.server 8000 --bind 127.0.0.1; open http://127.0.0.1:8000/ and record the response.

Serve a real local page so the next exercises have observable network traffic.

1. Create public/index.html with an HTML title, an EMIO24 heading and a list containing Pen and Notebook with stock counts 4 and 8.
2. In a terminal change into public/ and run `python -m http.server 8000 --bind 127.0.0.1`.
3. Open `http://127.0.0.1:8000/` and confirm both products appear.
4. Record the command, URL and displayed content; keep the server running for later checks.

**Check:** the browser renders your file and the terminal logs a request. If the port is occupied, use another recorded port consistently; do not infer the right page from a browser cache alone.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Inspect the request - 10 points

**Where:** `network-notes.md`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Use browser Network tools to record request URL, method, status and content type for index.html. Explain each field using the shop analogy.

The browser's Network panel is the delivery receipt for each resource request.

1. Open Developer Tools and select Network. Reload your local index page.
2. Select the document request, not a favicon or extension request.
3. Record Request URL, method, status and response Content-Type in network-notes.md. Inspect Response to find your heading text.
4. Explain each field using the shop-order analogy.

**Check:** the document request uses GET, succeeds with 200 on an ordinary fresh response, and contains HTML. If you observe a cache-related status, disable cache while DevTools is open and reload, recording what actually changed.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Request a missing page - 10 points

**Where:** `network-notes.md`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Visit /missing.html and record the status. Compare a server returning an error response with stopping the server and getting a connection failure.

An HTTP error response differs from failing to reach any server.

1. With the local server running, visit `/missing.html`, a filename you have not created.
2. Record its status and response body from Network.
3. Stop the server with Ctrl+C and try a new uncached request to the same host/port.
4. Compare the browser error with the earlier 404 response, then restart the server for Exercise 8.

**Check:** the missing page gets a server response with status 404. The stopped-server case is a connection/network failure, not a 404 response from your server. Note any cached page instead of treating it as a live response.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Separate client and server - 10 points

**Where:** `public/index.html`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Add a local HTML button that changes visible text with JavaScript. Observe whether clicking creates a network request. Explain where that change executes.

Some UI actions happen entirely in the browser after the page has loaded.

1. Add a button labelled `Show stock` and a paragraph to index.html.
2. Attach a click handler that changes the paragraph to `Pen: 4 units` using textContent.
3. Reload, clear the Network log, then click the button.
4. Record both the changed screen text and whether your click generated a request. Distinguish unrelated browser traffic from your handler.

**Check:** the text changes without fetching new stock in this implementation. Explain that the displayed 4 was already available to browser JavaScript; it is not automatically current database stock.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Map a full-stack product - 10 points

**Where:** `architecture.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Draw React client, Django service and database with request/data arrows. Identify where stock is authoritative and why browser-visible stock can become stale.

Map the future app to the system you just observed.

1. In architecture.md draw React/browser, Django/API and database as separate boxes.
2. Trace a product-list request out and a data response back; label HTTP between browser/API and database queries between API/database.
3. Trace a proposed sale and identify where stock is validated and committed.
4. Describe a second customer buying an item while the first customer's page remains open.

**Check:** the database/server-side business process is authoritative; the browser can hold an outdated copy. Your arrows show how the UI would refresh rather than assuming two open pages share one in-memory variable.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose one page request and one missing-resource/connection case. Identify whether a server returned an HTTP response at all. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 10
python grade.py rubric --lesson 10
```

The first checks the JSON prediction and writes `grading/reports/lesson-10.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-10/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

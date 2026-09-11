# Lesson 27 assignment: Application security foundations

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

Security resembles protecting a shop through several controls: checked inputs, locked cabinets and limited keys. One locked door does not protect an open back entrance.

Use a disposable copy of the Lesson 26 app with fictional data. All security demonstrations target this local app. An origin includes scheme, host and port; record actual frontend/backend origins before configuring them.

## Where to work and how to run it

Work in `week-09/assignments/lesson-27/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `threat-model.md` |
| 4 | `project/inventory/tests.py` |
| 5 | `project/inventory/templates/inventory/` |
| 6 | `project/inventory/tests.py` |
| 7 | `project/config/settings.py and origins.md` |
| 8 | `project/config/settings.py and .env.example` |
| 9 | `project/config/settings.py and error-notes.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Threat model** | A description of assets, actors, trust boundaries and possible abuse. | the shop’s break-in map. |
| **Injection** | Untrusted data being interpreted as executable instructions. | an order form rewriting the clerk’s rules. |
| **XSS** | Untrusted script executing in a user’s browser context. | a forged notice running commands at reception. |
| **CORS** | Browser rules controlling cross-origin response access. | rules for which outside desks may read replies. |
| **Secret** | Sensitive material used to authenticate or protect systems. | a key rather than a public sign. |

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
# Bind values as data, never concatenate them into SQL.
cursor.execute("SELECT id FROM products WHERE name = %s", [user_input])
# This is Django cursor syntax; sqlite3 directly uses ? placeholders.
```

**Question:** Does CORS replace API authentication? Enter a Boolean.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Parameterized SQL separates instruction structure from input values. CORS is enforced by browsers and does not authenticate clients. Keep Django template escaping and CSRF protection enabled for relevant browser flows, and store deployment secrets outside committed code.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Map trust boundaries - 10 points

**Where:** `threat-model.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Draw browser, API, database and deployment configuration. List stock records, credentials and customer information as assets with one realistic abuse case each.

A threat model identifies what could be harmed and where untrusted input crosses a boundary.

1. Draw browser, API, database and deployment configuration in threat-model.md.
2. List stock, customer records and credentials as assets and identify who should access each.
3. Add an abuse scenario per boundary, such as another user's product ID or a forged stock value.
4. Map each scenario to an actual control and a local check you can perform.

**Check:** the document names assets, actor, entry point, potential harm and defence. “Use security” is not a testable control; specify validation, authentication or ownership enforcement as appropriate.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Demonstrate safe query input - 10 points

**Where:** `project/inventory/tests.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** In a local fixture search for a name containing quotes using bound parameters. Show it is treated as a name and cannot change query structure.

A query parameter is data, even when it contains punctuation that resembles SQL.

1. In a disposable fixture insert `Maker's Pen` using ORM creation or bound SQL parameters.
2. Search for it through the application's parameterized query path.
3. Search for a text value such as `' OR '1'='1` and record the ordinary no-match result unless that exact name exists.
4. Explain the difference between binding values and concatenating them into SQL instructions.

**Check:** the apostrophe name returns exactly and the second input does not select every product or alter the database. Use ? for direct sqlite3 and %s for Django cursor parameters; do not mix their conventions.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Verify escaping - 10 points

**Where:** `project/inventory/templates/inventory/`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Render the literal product name <script>alert(1)</script> in a local template. Confirm it displays as text rather than executing. Document why marking user text safe changes this.

User text should display as text rather than run as browser instructions.

1. Store a disposable product name `<script>alert(1)</script>`.
2. Render it through normal Django template escaping with a product-name variable.
3. Inspect displayed text and page source/DOM; record whether any script executes.
4. Explain why marking untrusted text safe would change the boundary. Do not leave an intentionally unsafe template in the working project.

**Check:** the name is visible as literal text and no alert runs. A safe JSON response alone does not prove every eventual HTML insertion is safe.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Check CSRF - 10 points

**Where:** `project/inventory/tests.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** With Django test client CSRF enforcement enabled, submit a session-authenticated write without a CSRF token and then with a valid token. Record expected rejection and success.

CSRF checks must be enabled in the test that claims to exercise them.

1. Use Django Client(enforce_csrf_checks=True) with an authenticated session.
2. POST a write without a CSRF token and record 403 plus unchanged data.
3. GET the actual form to receive a CSRF cookie and rendered token, then submit its token through the same client.
4. Verify the otherwise valid request succeeds and explain that it uses the browser session credential.

**Check:** no-token and valid-token requests differ as expected. A default Django test client disables CSRF checks, so it cannot establish this result. [Testing reference](https://docs.djangoproject.com/en/5.2/topics/testing/tools/).

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Configure origins - 10 points

**Where:** `project/config/settings.py and origins.md`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Document frontend/backend origins including ports. If separate origins are used, allow only the intended origins; demonstrate allowed and disallowed browser cases.

An origin is the browser's scheme/host/port combination, not simply a domain label.

1. Record your real frontend and API origins; ports 5173 and 8000 are different origins even on localhost.
2. If separate, configure your installed CORS middleware to allow only the intended frontend, placing it as its documentation requires.
3. Make browser requests from allowed and deliberately different local origins; inspect preflight/response headers and whether browser JavaScript can read the response.
4. Compare with a direct non-browser API request.

**Check:** allowed-origin browser reads work; disallowed reads are blocked under the policy. CORS does not replace authentication and does not prevent every client from sending a request.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Separate secrets - 10 points

**Where:** `project/config/settings.py and .env.example`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Read a dummy deployment secret from an environment variable; fail clearly if missing. Commit an example variable name with a placeholder and confirm actual .env is ignored.

Keep a deployment key outside committed source while documenting how to supply it.

1. Read a dummy variable such as EMIO24_DEMO_SECRET through os.environ in local settings.
2. Fail clearly if required configuration is absent, then run with a fake value supplied through the environment.
3. Create .env.example listing only the name and placeholder; confirm actual .env is ignored if you use one.
4. Explain that Django does not load a .env file automatically unless you configure a loader.

**Check:** missing and present cases behave differently; evidence contains neither real secrets nor their values. A placeholder file is documentation, not a populated production configuration.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Review production errors - 10 points

**Where:** `project/config/settings.py and error-notes.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** In local production-like settings disable debug output and test a controlled error. Show users receive a generic response while useful redacted detail is logged locally.

Users need a safe error page while operators need useful diagnostic records.

1. Use separate local production-like settings with DEBUG=False and the correct allowed local hosts.
2. Trigger a controlled exception through a test-only view in a disposable copy; configure logging to capture a redacted diagnostic.
3. Inspect response and log, then remove the deliberate failure route from the working app.
4. Record which details each audience receives.

**Check:** the response is generic and contains no traceback, settings or secrets; the log identifies the failure. A host-configuration 400 is not the controlled 500 you intended to test.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a working protected input path and a rejected/escaped malicious-looking input against your own local app. Explain the exact defence, not just the word secure. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 27
python grade.py rubric --lesson 27
```

The first checks the JSON prediction and writes `grading/reports/lesson-27.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-27/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

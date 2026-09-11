# Lesson 25 assignment: JWT authentication

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A signed access token resembles a tamper-evident visitor pass. A verifier checks its signature and expiry. The printed claims are usually readable; a signature is not encryption.

Use the authenticated-user model from the existing DRF project. Choose a maintained JWT integration compatible with your installed versions and follow its authentication-class and token-view setup. Record its package/version first. The illustrative claims below are not usable credentials.

## Where to work and how to run it

Work in `week-09/assignments/lesson-25/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `token-flow.md` |
| 4 | `project/config/settings.py and requirements.txt` |
| 5 | `project/config/urls.py` |
| 6 | `token-checks.md` |
| 7 | `token-checks.md` |
| 8 | `token-checks.md` |
| 9 | `token-storage.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **JWT** | A compact token format carrying claims. | the visitor pass format. |
| **Claim** | A statement stored in a token payload. | a printed field on the pass. |
| **Signature** | Cryptographic integrity/authenticity protection. | the tamper-evident seal. |
| **Access token** | A credential used to access a protected resource. | the short-lived entry pass. |
| **Refresh token** | A credential used to obtain new access tokens. | the renewal voucher. |

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
{"sub":"user-7","exp":2000,"iss":"emio24"}

# Illustrative claims only; this is not a signed token.
# A verifier rejects it when current time is >= exp.
```

**Question:** At time 2001, is a token expiring at 2000 expired? Enter a Boolean.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

A complete verification policy checks signature, allowed algorithm, expiry and applicable issuer/audience rules. Decoding a payload alone does not authenticate anyone. Use a maintained authentication library; never build cryptography from this teaching sketch.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Define the token flow - 10 points

**Where:** `token-flow.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Draw login -> access/refresh tokens -> authenticated API request -> expiry -> refresh. Identify which steps require credentials and which can fail.

A signed pass is readable but tamper-evident; it is not an encrypted secret document.

1. Draw login → access/refresh pair → Bearer-authenticated request → access expiry → refresh exchange.
2. Label which request carries a password, which carries an access token and which carries a refresh token.
3. Add failure branches for wrong credentials, invalid signature and expired access token.
4. Explain that decoding claims alone does not verify the signature or grant permission.

**Check:** the API authorizes a verified identity separately from checking token validity. The diagram never treats a refresh token as the normal credential for product requests.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Configure library authentication - 10 points

**Where:** `project/config/settings.py and requirements.txt`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Use a maintained JWT integration compatible with your installed Django/DRF versions. Record its exact version and configure access-token authentication without implementing signatures yourself.

Configure an existing verifier rather than implementing token cryptography.

1. Select a maintained compatible integration; the reference path for this course is djangorestframework-simplejwt. Record its installed version and dependency compatibility in requirements/settings notes.
2. Configure its JWTAuthentication class in DRF's authentication classes. Keep other explicitly needed classes and record their order.
3. Protect the intended endpoint with IsAuthenticated and run Django system checks.
4. Use the package's token views in Exercise 5; do not write signing code yourself.

**Check:** the selected class imports under the project interpreter. Follow the installed package's versioned documentation; do not assume a sample requirements list guarantees every Django version is officially supported. [Setup reference](https://django-rest-framework-simplejwt.readthedocs.io/en/stable/getting_started.html).

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Obtain disposable tokens - 10 points

**Where:** `project/config/urls.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Create token endpoints and request tokens for a local test user. Record statuses and claim names with credential/token values redacted.

Obtain test credentials through the token endpoint.

1. For Simple JWT, route TokenObtainPairView to /api/token/ and TokenRefreshView to /api/token/refresh/; both use .as_view().
2. Create a disposable user with Django's password APIs.
3. POST that user's username/password to the pair endpoint using JSON, then independently try a wrong password.
4. Record statuses and token field names, redacting actual credential/token values.

**Check:** valid credentials yield access and refresh strings; invalid credentials yield no usable pair. The decoded teaching payload in Exercise 2 is not a signed token and cannot be pasted in as one.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Call a protected endpoint - 10 points

**Where:** `token-checks.md`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Send an access token using Authorization: Bearer. Demonstrate a valid request and a missing/invalid credential rejection; record the configured status semantics.

Present the access pass in the request header.

1. Request your protected product endpoint using `Authorization: Bearer <access-token>`, replacing the placeholder only in the local request tool.
2. Repeat with no credential and with a deliberately malformed token.
3. Record statuses and confirm rejected calls expose no protected product data.
4. Document how the configured authentication-class order determines the unauthenticated response challenge/status.

**Check:** valid token succeeds; invalid/missing credentials do not. With JWTAuthentication first, expect its 401 challenge behaviour. Never treat a 200 public endpoint as proof that authentication was checked.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Check expiry - 10 points

**Where:** `token-checks.md`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Use a short lifetime in local test settings or the library’s time-testing support. Demonstrate an expired access token is rejected even though its payload can still be decoded.

Expiry must be enforced even though the printed payload remains readable.

1. Use local test settings with a short access lifetime, or the library's supported token/time testing APIs; keep production settings separate.
2. Obtain a fresh token and prove it works before expiry.
3. Advance the test time or wait beyond expiry, then make the same protected request.
4. Record time assumptions and response without saving the token value.

**Check:** the expired token is rejected. Do not simply edit the payload's exp and claim you tested expiry: editing a signed token also invalidates its signature and tests a different failure.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Refresh deliberately - 10 points

**Where:** `token-checks.md`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Exchange a valid refresh token for a new access token, then try an invalid refresh token. Document rotation/revocation settings and their logout implications.

A renewal voucher issues a new access pass under the configured policy.

1. POST a valid refresh token to /api/token/refresh/ and use the new access token on the protected endpoint.
2. Repeat the refresh call with a malformed refresh token and record rejection.
3. Inspect rotation/blacklist settings and document whether old refresh tokens remain usable.
4. Explain what logout means in your chosen configuration, including the remaining lifetime of already issued access tokens.

**Check:** valid renewal gives usable access; invalid renewal does not. Deleting a token in one browser is not proof it has been revoked everywhere.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Compare storage choices - 10 points

**Where:** `token-storage.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Compare memory and HttpOnly-cookie approaches for a browser client, including XSS/CSRF implications. Choose one for your app and document reload, refresh and logout behaviour.

Choose browser storage with an explicit reload/logout story.

1. Compare in-memory access storage with an HttpOnly-cookie design in token-storage.md.
2. For each, describe who can read/send the credential and the relevant XSS/CSRF concern.
3. Choose one for the later frontend and explain login, reload, expiry, refresh and logout.
4. If using cookies, describe credentialed requests and CSRF protection; if using memory, explain how reload signs out or securely renews.

**Check:** the design does not claim a signature encrypts payload data or that one storage choice removes all browser security concerns. Document a usable flow rather than only naming a storage API.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new valid token lifecycle step and an expiry/invalid-credential scenario. Do not copy token values into evidence; identify the verification rule tested. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 25
python grade.py rubric --lesson 25
```

The first checks the JSON prediction and writes `grading/reports/lesson-25.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-25/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

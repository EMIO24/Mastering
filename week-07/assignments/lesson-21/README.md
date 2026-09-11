# Lesson 21 assignment: Authentication and sessions

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

Authentication checks who is at the door; authorization decides which room they may enter. A session cookie is a reference to signed-in state, not permission to do everything.

Use the Lesson 20 project with default authentication/session middleware and migrations. Create disposable ordinary and privileged users. Keep passwords and cookie values out of evidence files.

## Where to work and how to run it

Work in `week-07/assignments/lesson-21/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `user-setup.md` |
| 4 | `project/config/urls.py and templates` |
| 5 | `project/inventory/views.py` |
| 6 | `project/config/urls.py and templates` |
| 7 | `project/inventory/views.py` |
| 8 | `session-notes.md` |
| 9 | `project/inventory/tests.py` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Authentication** | Establishing an identity. | checking an identity card. |
| **Authorization** | Deciding whether an identity may perform an action. | checking the room-access list. |
| **Session** | Server-side interaction state associated with a client identifier. | the desk’s record for a visitor ticket. |
| **Password hash** | A one-way password verification representation with a work factor. | a verification imprint rather than a readable password. |
| **Logout** | Ending the client’s authenticated session. | invalidating the visitor ticket. |

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
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def dashboard(request):
    return JsonResponse({"username": request.user.username})
```

**Question:** Is checking a signed-in user owns a product authentication or authorization? Enter the term.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Django authentication middleware populates request.user. login_required normally redirects anonymous browser visitors to login. It does not enforce product ownership or staff privileges. Use Django password APIs rather than storing or comparing plaintext passwords.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Create local users - 10 points

**Where:** `user-setup.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Create two disposable users through Django APIs or management commands. Use set_password/create_user; demonstrate check_password works without saving plaintext in notes.

Use Django's password tools rather than treating passwords as ordinary text fields.

1. In the project shell get the configured user model with get_user_model.
2. Create disposable ordinary and staff users with create_user, or use set_password followed by save.
3. Demonstrate check_password returns True for the chosen password and False for another value.
4. Record usernames/roles and Boolean outcomes, not password or stored-hash values.

**Check:** authentication checks work and no plaintext password was assigned directly to user.password. Setting is_staff is a role flag; the custom view must still check it when its contract requires staff access.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Add login - 10 points

**Where:** `project/config/urls.py and templates`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Use Django’s LoginView and a login template. Configure redirect paths. Show correct credentials reach a dashboard and incorrect credentials produce a useful error.

Login connects a verified identity with a browser session.

1. Add a /login/ route using Django LoginView and a registration/login.html template containing the form and csrf_token.
2. Set LOGIN_URL and a successful LOGIN_REDIRECT_URL pointing to your dashboard.
3. Try incorrect credentials, then valid credentials for the ordinary user.
4. Record response/redirect behaviour and the displayed outcome without copying credentials.

**Check:** incorrect credentials keep the user signed out with an error; valid credentials reach the intended page. A normal invalid-login form may return 200 with errors, rather than an HTTP authorization status.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Guard a view - 10 points

**Where:** `project/inventory/views.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Protect dashboard with login_required. Record the anonymous redirect and authenticated 200 response.

A protected dashboard should identify the visitor or send them to login.

1. Add login_required to the dashboard view and use request.user to show its username.
2. Request the route in a signed-out browser session and inspect the redirect, including the return-location parameter.
3. Sign in and request again.
4. Explain which middleware supplies request.user.

**Check:** signed-out access redirects to login; signed-in access returns 200 with the correct account name. This is identity protection, not yet a rule that one user owns every record displayed.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Implement logout - 10 points

**Where:** `project/config/urls.py and templates`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Use a CSRF-protected POST logout form. After logout, revisit dashboard and confirm authentication is required again.

Logout ends the browser's authenticated session through an intentional state-changing action.

1. Add a LogoutView route and a POST logout form containing csrf_token.
2. Configure its next page, such as /login/.
3. Sign in, confirm dashboard access, submit logout, then revisit dashboard.
4. Inspect behaviour from a direct GET to the logout URL too.

**Check:** after POST logout the dashboard requires login again. In the Django 5.2 baseline, LogoutView is not a state-changing GET link; use the form and document unsupported-method behaviour.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Separate privileges - 10 points

**Where:** `project/inventory/views.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Restrict product deletion to staff or an explicit permission. Show a signed-in ordinary user denied and a permitted user allowed.

Being signed in does not automatically grant destructive privileges.

1. Define a clear policy: product deletion requires is_staff or an explicit named permission, and state which you implement.
2. Enforce it in the delete view before any row is removed; hiding a button is optional UI assistance only.
3. Attempt a direct delete request as ordinary and privileged users with valid CSRF handling.
4. Compare status/redirect and row existence.

**Check:** ordinary user cannot delete; permitted user can. A signed-in denial should follow your documented response policy, such as 403, and preserve the record.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Inspect session behaviour - 10 points

**Where:** `session-notes.md`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Use browser tools to identify the session cookie without copying its value into your submission. Explain the roles of HttpOnly, Secure and SameSite.

Inspect the visitor ticket without exposing its secret value.

1. Sign in and open browser storage/cookie tools for the local site.
2. Record the session cookie's name, path and HttpOnly/Secure/SameSite settings, redacting its value.
3. Explain HttpOnly as restricting JavaScript access, Secure as requiring HTTPS transmission, and SameSite as controlling cross-site sending behaviour.
4. Compare development settings with intended production HTTPS settings.

**Check:** notes describe actual observed flags. Do not claim a Secure cookie works over an ordinary remote HTTP site or that these flags replace server-side permission checks.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Test identity boundaries - 10 points

**Where:** `project/inventory/tests.py`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Write tests for anonymous, normal and privileged users. Check both visible links and direct requests, proving hidden buttons alone do not enforce access.

Verify access rules with requests that do not rely on visible buttons.

1. In tests create ordinary and privileged users plus a product fixture.
2. Test anonymous dashboard access, ordinary authenticated dashboard access and the deletion rule for both roles.
3. Use separate client sessions or explicitly logout between cases; force_login can set up authenticated tests without testing password entry again.
4. Assert both response behaviour and whether the product remains.

**Check:** unauthorized cases never mutate data and allowed cases do. Include a separate real login test if you want to claim password authentication is tested; force_login bypasses it intentionally.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a successful session/permission action and a denied direct request. Distinguish password verification from role authorization. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 21
python grade.py rubric --lesson 21
```

The first checks the JSON prediction and writes `grading/reports/lesson-21.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-21/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

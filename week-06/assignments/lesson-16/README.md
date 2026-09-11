# Lesson 16 assignment: Django architecture and request flow

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

Django routes a visitor through a reception desk: the URL dispatcher selects a view, the view coordinates work, and a template formats the response. A model handles stored records.

Create a new Django project in project/. Its configuration package is config and its app is inventory. No Product model is required yet. The health endpoint returns JSON and the home page renders HTML.

## Where to work and how to run it

Work in `week-06/assignments/lesson-16/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `project/` |
| 4 | `project/config/settings.py and project/config/urls.py` |
| 5 | `project/inventory/views.py and project/inventory/urls.py` |
| 6 | `project/inventory/views.py and project/inventory/templates/inventory/home.html` |
| 7 | `project/inventory/urls.py` |
| 8 | `answers.md` |
| 9 | `request-flow.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Framework** | Reusable structure that calls your application code. | a staffed building where you fill assigned roles. |
| **Project** | Django configuration for a site. | the building’s central plan. |
| **App** | A reusable unit of Django functionality. | one department. |
| **View** | A callable handling a request and returning a response. | the selected service desk. |
| **Template** | A document pattern rendered with data. | a reusable receipt layout. |

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
# inventory/views.py
from django.http import JsonResponse

def health(request):
    return JsonResponse({"status": "ok"})

# inventory/urls.py
from django.urls import path
from .views import health
urlpatterns = [path("health/", health)]
```

**Question:** Enter the JSON response body for GET /health/ as an object.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Create an inventory app inside a Django project and include its URLs at the root to expose /health/. A request reaches the view only after URL resolution. JsonResponse converts the dictionary to JSON and sets its content type. runserver is a development server.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Create the project - 10 points

**Where:** `project/`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** With Django 5.2 available in your environment, run python -m django startproject config . in a new project folder and python manage.py startapp inventory. Save version and folder tree.

Create the building before adding its inventory department.

1. In a new project/ directory create a virtual environment and use its interpreter for all commands. Install the Django 5.2 baseline from your prepared packages or while online.
2. Run `python -m django startproject config .`, then `python manage.py startapp inventory`.
3. Run `python -m django --version` and `python manage.py check`.
4. Record the version and a tree showing manage.py, config/settings.py, config/urls.py and inventory/.

**Check:** Django's system check completes without errors. Do not run startproject over an existing project; copy its source instead if you already have the required structure.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Register the department - 10 points

**Where:** `project/config/settings.py and project/config/urls.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Add inventory to INSTALLED_APPS and create inventory/urls.py. Include it from config/urls.py. Explain project URLs versus app URLs.

Register the department and connect its URL directory.

1. Add inventory to INSTALLED_APPS in config/settings.py.
2. Create inventory/urls.py with imports for path and an initially empty urlpatterns list.
3. Import include in config/urls.py and include inventory.urls at the empty root prefix.
4. Run `python manage.py check` again. Explain that the root file delegates requests while the app file defines the department's routes.

**Check:** configuration imports without errors; no inventory route is expected to exist until you add one. Accidentally including the root URL module inside itself creates a routing loop.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Add health status - 10 points

**Where:** `project/inventory/views.py and project/inventory/urls.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Implement the shown health view and route. Request /health/ locally; expect status 200, JSON content type and status ok.

A health view is a small request/response check.

1. Add health(request) in inventory/views.py returning JsonResponse with status set to the text ok.
2. Import the view in inventory/urls.py and add `path("health/", health, name="health")`.
3. Start runserver and open http://127.0.0.1:8000/health/.
4. Inspect status, Content-Type and body in the browser Network panel.

**Check:** 200, application/json content type and `{"status":"ok"}`. This verifies the route/view responds; it does not prove a database or every other dependency is healthy.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Render HTML - 10 points

**Where:** `project/inventory/views.py and project/inventory/templates/inventory/home.html`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Add a home view and inventory/home.html template with an EMIO24 heading. Pass shop_name as context and verify it appears in the response.

Render a page by filling a reusable document with view data.

1. Create inventory/templates/inventory/home.html containing an h1 that displays the template variable shop_name.
2. Add a home view that calls render with that template and context `{"shop_name":"EMIO24"}`.
3. Add an empty-path route named home and open the root URL.
4. Change the context value to a temporary test name, reload and restore EMIO24.

**Check:** the heading follows context data without editing the template. A literal shop_name word is not a template variable; Django's template expression uses double braces.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Use route names - 10 points

**Where:** `project/inventory/urls.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Name the home and health routes and use reverse() to resolve them. Show both resolved paths without hard-coding the URLs in the calling code.

Named routes let callers ask for a destination without hard-coding its path.

1. Confirm your home and health URL patterns have those names.
2. Open `python manage.py shell`, import reverse from django.urls, and evaluate reverse("home") and reverse("health").
3. Record results and explain how reversing differs from handling an incoming request.
4. If you use a namespace, record the exact namespaced names and use them consistently.

**Check:** the unnamespaced setup resolves to `/` and `/health/`. A NoReverseMatch error means the requested name/arguments did not match your URL configuration, not that the browser is offline.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Handle a missing route - 10 points

**Where:** `answers.md`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Request /does-not-exist/ and record 404. Trace why your health view is not called. Distinguish routing failure from a Python exception inside a view.

A missing route never reaches an unrelated view.

1. Request http://127.0.0.1:8000/does-not-exist/ and inspect its status.
2. Compare it with a successful /health/ request.
3. In answers.md trace URL matching and explain why the health view is not chosen for the unknown path.
4. Explain how this differs from an exception raised after a valid route has already selected its view.

**Check:** the unmatched route returns 404. With local DEBUG enabled, Django may show route details; this is a development response, not a production error-page design.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Trace the architecture - 10 points

**Where:** `request-flow.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Annotate browser -> URL configuration -> view -> template/JsonResponse -> response with actual filenames. Explain where models will enter the flow next lesson.

Make a concrete map of the code that handled your request.

1. In request-flow.md trace the root page through config/urls.py, inventory/urls.py, the home view, home.html and the HTTP response.
2. Trace /health/ separately and show that it uses JsonResponse instead of an HTML template.
3. Label where request data enters and context/response data leaves.
4. Add where a Product model lookup could enter next lesson.

**Check:** every box names an actual file/function. Do not claim a model was queried by the current health view when it simply returns a fixed dictionary.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new valid route and a missing-route or missing-template case. Explain the exact stage reached before the failure. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 16
python grade.py rubric --lesson 16
```

The first checks the JSON prediction and writes `grading/reports/lesson-16.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-16/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

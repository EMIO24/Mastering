# Lesson 23 assignment: DRF API views

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

An API view is the dispatcher joining request handling, validation and response formatting. The serializer inspects the paperwork; the view decides when to use it and which response to send.

Use the Lesson 22 project with ProductSerializer working. Put API routes beneath /api/. Start with Pen 200/4 and Book 500/8. Check response status and database effects for every write test.

## Where to work and how to run it

Work in `week-08/assignments/lesson-23/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `project/inventory/views.py and project/inventory/urls.py` |
| 4 | `project/inventory/views.py and project/inventory/urls.py` |
| 5 | `project/inventory/views.py and project/inventory/urls.py` |
| 6 | `project/inventory/views.py and project/inventory/urls.py` |
| 7 | `project/inventory/views.py and project/inventory/urls.py` |
| 8 | `project/inventory/views.py and project/inventory/urls.py` |
| 9 | `project/inventory/generic_views.py` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **APIView** | DRF’s class-based request handling base. | the API service desk. |
| **Response** | A DRF response rendered according to content negotiation. | a receipt awaiting its final format. |
| **request.data** | Parsed request content exposed by DRF. | the opened order envelope. |
| **Content negotiation** | Choosing a supported response representation. | agreeing on the receipt format. |
| **Generic view** | A reusable implementation of common API operations. | a standard desk procedure. |

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
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})
```

**Question:** Which status code should POST to this GET-only endpoint return?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Wire health into Django URLs. The decorator restricts methods and wraps the Django request with DRF behaviour. Returning a dictionary alone is insufficient; Response carries data for rendering. Use serializer errors with 400 and creation success with 201.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: List through an API - 10 points

**Where:** `project/inventory/views.py and project/inventory/urls.py`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Implement GET /api/products/ using ProductSerializer(many=True). Demonstrate populated and empty results, documenting whether pagination is enabled.

A list API returns data instead of rendering an HTML product card.

1. Add GET /api/products/ using a DRF view and ProductSerializer with many=True over an ID-ordered QuerySet.
2. Return a DRF Response. State whether this version is an array or already uses a pagination envelope.
3. Request it with two products and with an empty isolated fixture.
4. Record status, content type and parsed body.

**Check:** status 200 and the correct records; empty results have the documented empty shape. Returning model objects or a QuerySet directly is not the serializer's simple-value representation.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Create through an API - 10 points

**Where:** `project/inventory/views.py and project/inventory/urls.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Implement POST using request.data, serializer validation and save. A valid product returns 201; invalid stock returns 400 and no extra row.

Creation must distinguish accepted input from a rejected form.

1. Add POST handling on the collection route, binding ProductSerializer with request.data.
2. Validate before saving. Return created representation with 201; return validation errors with 400.
3. Send Pen/200/4 as JSON, then independently stock -1.
4. Check database counts around both requests.

**Check:** valid request adds exactly one row and returns its assigned ID; invalid request adds none and identifies stock. request.data is parsed request content; do not manually assume every request body is a form-encoded dictionary.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Read one product - 10 points

**Where:** `project/inventory/views.py and project/inventory/urls.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Implement GET detail using a primary-key URL parameter. Return serialized data for an existing row and 404 for a missing one.

A detail route resolves one existing product or a missing-resource response.

1. Add /api/products/<int:pk>/ and fetch with get_object_or_404 or equivalent DRF behaviour.
2. Serialize the single instance without many=True and return it.
3. Request a known product and a verified absent ID with APIClient or your local request tool.
4. Confirm neither request changes row count or stock.

**Check:** known ID is 200 with one product object; absent ID is 404. Do not return 200 with an error string for a missing resource under this contract.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Update one product - 10 points

**Where:** `project/inventory/views.py and project/inventory/urls.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Implement PUT or PATCH with the documented completeness rules. Demonstrate changing stock, preserving unrelated fields on PATCH, and rejecting a negative value.

Use the update method's documented completeness rule.

1. Add PUT for complete writable fields and/or PATCH for partial changes; state which methods your view supports.
2. For PATCH bind the existing instance with partial=True. Validate before save.
3. Starting Pen 200/4, change only stock to 7; then try -1 in a separate request.
4. Refetch the product after each request.

**Check:** success returns 200 and stock 7 while name/price remain; invalid update returns 400 and leaves the successful state intact. Omitting instance= would create another row instead of updating the target.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Delete through an API - 10 points

**Where:** `project/inventory/views.py and project/inventory/urls.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Implement DELETE returning 204 with an empty body. Verify the row is gone and a subsequent detail request is 404.

Deletion has a successful empty response and a lasting database effect.

1. Add DELETE handling on the detail route.
2. Resolve the target or return 404, delete it, then return status 204 without a JSON body.
3. Delete a disposable known product and inspect response bytes plus row existence.
4. Request that detail again and repeat DELETE if desired.

**Check:** first deletion returns an empty 204; later lookup is 404. Calling response.json on an empty 204 is a client error; no JSON body is expected.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Exercise error paths - 10 points

**Where:** `project/inventory/views.py and project/inventory/urls.py`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Send an unsupported method and malformed JSON using local API tests. Record 405 and 400 behaviour and prove the database remains unchanged.

Exercise failures in parsing and method selection separately from field validation.

1. Send a method your configured route does not allow, such as POST to a GET-only health view.
2. Send syntactically broken JSON to the product create route with application/json content type.
3. Record statuses, body shapes and before/after product counts.
4. Compare these with the negative-stock serializer failure from Exercise 4.

**Check:** unsupported method is 405; malformed JSON is 400; neither writes a product. A 400 parser error occurs before normal field validation, so its message need not look like a stock field error.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Compare implementations - 10 points

**Where:** `project/inventory/generic_views.py`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Reimplement list/create with a DRF generic view in a separate module. Compare the serializer, queryset and permission configuration while retaining the same observable contract.

A generic view packages common request handling while you supply the model-specific choices.

1. In generic_views.py implement list/create using ListCreateAPIView with queryset, serializer_class and the same permission policy as your original view.
2. Wire it at a temporary comparison path, leaving one clearly documented final route.
3. Run the same populated/empty/valid-create/invalid-create cases against both implementations.
4. Compare status/body/database effects, allowing only documented pagination differences.

**Check:** the generic version honours the same validation and access contract. Less code is not proof of equivalent behaviour; demonstrate the actual cases.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new API success and a parser/method/validation failure. Keep their status meanings distinct and inspect persistent side effects. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 23
python grade.py rubric --lesson 23
```

The first checks the JSON prediction and writes `grading/reports/lesson-23.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-23/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

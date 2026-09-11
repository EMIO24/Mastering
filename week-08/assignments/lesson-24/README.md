# Lesson 24 assignment: ViewSets, routers and pagination

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A ViewSet groups related counter services; a router prints the directory mapping URLs and methods to those services. The directory does not decide who is allowed through the door.

Use the Lesson 23 API. Keep serializer validation and access rules when replacing views with a ViewSet. Use five products in stable ID order and page size 2.

## Where to work and how to run it

Work in `week-08/assignments/lesson-24/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `project/inventory/views.py` |
| 4 | `project/inventory/urls.py` |
| 5 | `route-matrix.md` |
| 6 | `project/config/settings.py` |
| 7 | `project/inventory/views.py` |
| 8 | `project/inventory/views.py` |
| 9 | `api-contract.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **ViewSet** | A class grouping resource actions. | one resource department. |
| **Router** | A generator of URL patterns for ViewSets. | the printed counter directory. |
| **Action** | A named operation on a ViewSet. | a service offered at the counter. |
| **basename** | The base used for generated route names. | the directory’s naming prefix. |
| **Pagination** | Bounding collection responses into pages. | handing out catalogue pages. |

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
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="product")
urlpatterns = router.urls
```

**Question:** Enter the generated list route name for basename product.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Define ProductViewSet with a queryset and serializer_class, then include these URLs beneath /api/. The list/create path is products/; detail actions include a lookup value. Route names such as product-list derive from basename, not necessarily the model class.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Create a ViewSet - 10 points

**Where:** `project/inventory/views.py`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Implement ProductViewSet using ModelViewSet, Product queryset and serializer. Preserve your existing validation rules.

A ViewSet groups operations for the same resource.

1. Define ProductViewSet(ModelViewSet) with an ID-ordered queryset and ProductSerializer.
2. Copy the existing view's permission policy explicitly rather than relying on accidental defaults.
3. Remove duplicated operation logic only after the replacement is wired and tested.
4. Identify which built-in actions handle list, retrieve, create, update, partial_update and destroy.

**Check:** the ViewSet can use the same serializer validation. Declaring the class alone exposes no route; Exercise 4 registers its URLs.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Register routes - 10 points

**Where:** `project/inventory/urls.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Register products with basename product under /api/. Use reverse for product-list and product-detail and record resolved URLs.

The router translates standard resource operations into named URLs.

1. In inventory/urls.py create a DefaultRouter and register products with basename product.
2. Include its URLs below /api/ from the project URL configuration.
3. In the shell use reverse for product-list and product-detail with a real pk.
4. Check you did not produce a doubled prefix such as /api/api/products/.

**Check:** list resolves to /api/products/ and detail to /api/products/ID/. basename determines route names; it is not automatically the same thing as the Python class name.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Verify CRUD routing - 10 points

**Where:** `route-matrix.md`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Record method/path/action mappings for list, create, retrieve, update, partial_update and destroy. Test one success and one missing detail.

Verify what each method does on collection and detail paths.

1. In route-matrix.md list GET/POST collection and GET/PUT/PATCH/DELETE detail with their corresponding ViewSet actions.
2. Create a disposable product, retrieve it, update stock, partially update its name and delete it.
3. Record each status and final database effect.
4. Request a missing detail and an unsupported method.

**Check:** successful operations follow 200/201/204 as applicable, missing detail is 404 and unsupported method is 405. A successful route reverse does not prove its action returns correct data.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Bound collection size - 10 points

**Where:** `project/config/settings.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Configure page-number pagination with page size 2. Seed five products and verify page lengths 2, 2, 1 with stable ID ordering.

Bound the catalogue into stable pages.

1. Configure PageNumberPagination and PAGE_SIZE=2 in DRF settings, retaining other settings.
2. Seed exactly five fixture products and ensure the ViewSet orders by ID.
3. Request pages 1,2,3 and record count/next/previous/results.
4. Follow next links from page 1 and compare all collected IDs.

**Check:** page lengths are 2,2,1, count is 5, and each ID appears once. Without stable ordering, paging observations can be inconsistent even when the page-size setting is correct.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Add a read-only action - 10 points

**Where:** `project/inventory/views.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Add a low-stock collection action using stock <= supplied threshold. Validate threshold input and ensure its result is serialized and paginated consistently.

A custom collection action still needs validation and pagination.

1. Add a GET collection action for low stock using a threshold query parameter; choose and document a default such as 5.
2. Convert threshold to an integer and reject malformed input with a 400 response.
3. Filter stock <= threshold and pass the result through the ViewSet pagination/serialization helpers.
4. Test stocks 0,2,4 with threshold 2 and then text "bad".

**Check:** valid results include stocks 0 and 2 in the normal page envelope; bad input returns 400. Returning a raw unpaginated QuerySet would break the collection contract.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Limit filtering - 10 points

**Where:** `project/inventory/views.py`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Support an explicit allowed set of ordering fields. Demonstrate stock ordering and document how an unsupported field is handled.

Allow only intended ordering choices.

1. Configure DRF's OrderingFilter or equivalent with allowed fields id, name and stock.
2. Define a stable default, such as id, and document how ties are resolved.
3. Request ascending stock and descending stock on fixtures with distinct counts.
4. Try an unsupported field and record whether your chosen implementation ignores it or returns an error.

**Check:** valid orderings arrange the same permitted records; unsupported input follows the documented policy. Do not promise a 400 if the configured filter actually falls back to default ordering.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Check the contract - 10 points

**Where:** `api-contract.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Update api-contract.md to match generated routes, trailing slashes and page envelope. Test a client reads results rather than assuming the root is a list.

Make the client contract match the router and page shape actually in use.

1. Update api-contract.md with exact collection/detail/custom-action paths, trailing-slash policy and allowed methods.
2. Include a real page response and identify results as the product array.
3. Show client pseudocode reading body.results, not mapping over the whole response object.
4. Repeat one list, create, invalid-create and missing-detail check using the documented paths.

**Check:** a reader can call each route without guessing prefixes or envelope shape. A client that expected an array must be updated when pagination wraps that array in an object.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new page/action request and an invalid parameter or missing-detail case. Preserve ordering, envelope shape and permission policy. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 24
python grade.py rubric --lesson 24
```

The first checks the JSON prediction and writes `grading/reports/lesson-24.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-24/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

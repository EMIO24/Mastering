# Lesson 19 assignment: Django CRUD views

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

CRUD is the four basic actions at the ledger desk: create a card, read it, update it and delete it. Web views wrap these actions in requests, responses and access rules.

Use the Lesson 18 project. Put templates under inventory/templates/inventory/ and route URLs to inventory/views.py. Build ordinary HTML browser flows here; JSON APIs come later.

## Where to work and how to run it

Work in `week-07/assignments/lesson-19/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `project/inventory/views.py and templates` |
| 4 | `project/inventory/urls.py and templates` |
| 5 | `project/inventory/views.py and templates` |
| 6 | `project/inventory/views.py and templates` |
| 7 | `project/inventory/views.py and templates` |
| 8 | `project/inventory/views.py` |
| 9 | `method-matrix.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **CRUD** | Create, read, update and delete operations. | the four ledger services. |
| **URL parameter** | A value extracted from a matched URL. | the card number on a request. |
| **404** | A response indicating the resource was not found. | no card at that address. |
| **Redirect** | A response telling the client to request another URL. | a direction to the next desk. |
| **CSRF** | Cross-site request forgery using a browser’s ambient credentials. | an outsider tricking a signed-in clerk into submitting a form. |

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
from django.shortcuts import get_object_or_404, render
from .models import Product

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "inventory/detail.html", {"product": product})
```

**Question:** What HTTP status should a missing product detail return?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

The URL pattern must capture pk and the template must exist. get_object_or_404 converts a missing row into a 404 response. Read-only GET views should not change data. State-changing browser forms use POST and Django CSRF protection.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: List products - 10 points

**Where:** `project/inventory/views.py and templates`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Implement a GET list view ordered by ID. Render name, price and stock; show a clear empty-state message for no rows.

Show the ledger as a readable HTML page.

1. Add a list view that retrieves Product rows ordered by ID and passes them to inventory/list.html.
2. Route GET /products/ to it and render name, price and stock for each row.
3. Use a template empty branch/message for no rows.
4. Test with Pen 200/4 and Book 500/8, then with an empty disposable database or an isolated test fixture.

**Check:** populated HTML shows both records; empty HTML clearly says there are no products. Loading this GET page must not create or update a row.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Show one product - 10 points

**Where:** `project/inventory/urls.py and templates`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Add /products/<int:pk>/ and a detail template. Demonstrate a valid product and a missing ID returning 404.

A detail page takes the desired card number from its URL.

1. Add `/products/<int:pk>/` and a view receiving pk.
2. Use get_object_or_404 to find the product and render inventory/detail.html with name, price and stock.
3. Link to details from the list using named URL patterns.
4. Visit a known key, then a verified absent key.

**Check:** known product returns 200 with correct fields; missing product returns 404. A product's primary key need not equal its position in the list or the first sample ID.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Create safely - 10 points

**Where:** `project/inventory/views.py and templates`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Add a POST creation view that validates nonblank name and nonnegative integer price/stock. Use a CSRF-protected HTML form; invalid input must create no row.

Accept a new card only after checking the submitted fields.

1. Add a GET page containing a POST form with labelled name, price and stock inputs and csrf_token.
2. On POST strip/check name, convert numeric text and reject non-integer or negative values before saving.
3. Create a product only after every field succeeds; show errors and the entered values after failure.
4. Submit Pen/200/4, then blank name and stock -1 as independent cases.

**Check:** the valid submission creates one row; invalid submissions create none. This lesson may use explicit validation; Lesson 20 refactors it into reusable Django forms.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Update an existing record - 10 points

**Where:** `project/inventory/views.py and templates`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Add edit GET/POST flows. Change stock 4 to 7 and redirect after success. A missing ID returns 404; invalid input preserves the stored row.

Editing should update the selected record, not accidentally add another.

1. Add edit GET/POST routes using the record's pk and load it or return 404.
2. Populate the GET form with existing data. On POST validate all editable fields before assigning/saving.
3. Change Pen stock 4 to 7 and redirect to its detail page after success.
4. Try an invalid negative stock and an absent ID.

**Check:** successful edit leaves row count unchanged and stock 7; invalid input preserves stored data; absent ID is 404. The form should display the user's rejected input alongside an explanation.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Confirm deletion - 10 points

**Where:** `project/inventory/views.py and templates`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** GET displays a confirmation only; POST performs deletion with CSRF protection. Show that simply opening the confirmation URL leaves the record present.

Opening a confirmation page must not delete anything.

1. Add a delete confirmation GET showing the selected product and a labelled POST confirmation form with csrf_token.
2. Perform deletion only in the accepted POST branch, then redirect to the list.
3. Fetch the confirmation page and inspect the database before clicking Confirm.
4. Submit confirmation and attempt the old detail URL.

**Check:** GET retains the row; POST removes it; old detail returns 404. A link that deletes immediately on GET violates this exercise even if its text says Delete.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Handle browser refresh - 10 points

**Where:** `project/inventory/views.py`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Use POST-redirect-GET after successful creation. Refresh the resulting page and demonstrate that it does not create a duplicate record.

Post-redirect-get prevents refreshing the result page from simply resending the same form.

1. After valid creation, return a redirect to the created product's detail or list page.
2. Submit a new product while watching the Network panel.
3. Record the POST response and following GET, then refresh the resulting page twice.
4. Compare row counts before submission, after submission and after refreshes.

**Check:** only one new row is created. This pattern handles ordinary browser refresh; it is not a complete duplicate-request prevention mechanism for repeated independent POSTs.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Audit method behaviour - 10 points

**Where:** `method-matrix.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Record a matrix of routes and supported methods. Demonstrate that GET requests never add, edit or delete products and unsupported methods get an appropriate response.

Document and verify each route's allowed methods.

1. In method-matrix.md list list/detail/create/edit/delete-confirmation URLs and supported methods.
2. For every GET, state why it is read-only and verify row counts/stocks remain unchanged.
3. Send an unsupported method to at least one restricted view, using a test client or local request tool.
4. Configure a 405 response for unsupported methods and record it.

**Check:** create/edit/delete mutations occur only on intended POST flows; GET confirmation remains harmless. Record expected and observed methods, statuses and data effects rather than checking only whether a page looks correct.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new accepted CRUD operation and an invalid/missing-record request. Check HTTP behaviour and row/field changes together. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 19
python grade.py rubric --lesson 19
```

The first checks the JSON prediction and writes `grading/reports/lesson-19.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-19/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

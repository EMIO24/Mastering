# Lesson 20 assignment: Forms and validation

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A Django form is a receiving clerk who checks raw paperwork before handing trusted fields to the ledger. Browser checks help the visitor, but the server clerk must still check everything.

Use the Lesson 19 browser CRUD project. A form receives raw submitted text; validation converts accepted fields before saving. Use a Product with stock 4 for the sale check. Browser input restrictions do not replace server validation.

## Where to work and how to run it

Work in `week-07/assignments/lesson-20/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `project/inventory/forms.py` |
| 4 | `project/inventory/forms.py` |
| 5 | `project/inventory/forms.py` |
| 6 | `project/inventory/forms.py` |
| 7 | `project/inventory/views.py` |
| 8 | `project/inventory/templates/inventory/` |
| 9 | `project/inventory/tests.py` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Bound form** | A form associated with submitted data. | paperwork filled by a visitor. |
| **Validation** | Checking and converting data against rules. | the receiving clerk’s inspection. |
| **cleaned_data** | Validated and converted form values. | the accepted fields. |
| **ModelForm** | A form derived from selected model fields. | a form designed from the ledger columns. |
| **Field error** | Feedback attached to a particular input. | a note next to the incorrect box. |

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
from django import forms

class StockForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

form = StockForm({"quantity": "3"})
print(form.is_valid())
print(form.cleaned_data["quantity"])
```

**Question:** Enter the two printed values as a JSON list.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Run within the configured Django project. Raw HTTP form values are strings. IntegerField converts and validates them, so cleaned quantity is integer 3. Access cleaned_data after validation, and only use fields that passed validation.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Build ProductForm - 10 points

**Where:** `project/inventory/forms.py`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Create a ModelForm exposing only name, price and stock. Render field errors and preserve submitted input when validation fails.

A ModelForm gives the receiving clerk a form based on selected ledger fields.

1. Create inventory/forms.py with ProductForm derived from forms.ModelForm.
2. In Meta set Product as model and explicitly list name, price and stock; do not expose every field automatically.
3. Update create/edit views to bind the form on POST and render it on GET.
4. Display labels, entered values and field errors in the template.

**Check:** valid Pen/200/4 saves; invalid stock shows an error and retains the submitted name. Explicit fields prevent future model additions from silently becoming editable inputs.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Reject blank names - 10 points

**Where:** `project/inventory/forms.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Strip name whitespace in clean_name and reject an all-space value. Demonstrate " Pen " becomes Pen and "   " creates no product.

A name made entirely of spaces is still unusable even though it is text.

1. Add clean_name to ProductForm. Read the cleaned field, strip surrounding whitespace and reject the empty result with forms.ValidationError.
2. Return the accepted normalized name.
3. Bind forms with names `" Pen "` and `"   "`, supplying valid price/stock in both.
4. Compare is_valid, cleaned_data and errors before saving anything.

**Check:** padded Pen is accepted as Pen; spaces-only is rejected and no row is created. Returning the cleaned value matters: the form needs the accepted value, not just a printed message.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Validate quantities - 10 points

**Where:** `project/inventory/forms.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Create SaleForm with IntegerField(min_value=1). Demonstrate 3 accepted and 0, -1, "two" and "2.5" rejected with visible field errors.

Quantity validation belongs in a reusable form, not only the browser input widget.

1. Define SaleForm with an IntegerField named quantity and min_value=1.
2. Bind separate forms with raw quantity text "3", "0", "-1", "two" and "2.5".
3. Call is_valid on each; only read accepted cleaned quantity after successful validation.
4. Render one invalid form in the browser with its field error visible.

**Check:** "3" becomes integer 3; the other inputs fail. A minimum HTML attribute alone is not proof the server will reject an invalid direct request.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Check related rules - 10 points

**Where:** `project/inventory/forms.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Validate requested quantity against the selected product’s available stock. Starting stock 4, quantity 5 is rejected without changing the database.

A quantity can be valid by itself but invalid for the selected product.

1. Pass a Product instance into SaleForm using a documented constructor argument, storing it before calling the parent form initializer.
2. After basic quantity validation, compare it with that product's stock and add a quantity error if excessive.
3. With fresh stock 4, bind quantities 4 and 5.
4. Keep validation separate from deduction; validating a form must not sell anything.

**Check:** 4 is allowed and 5 rejected, with database stock still 4 in both validation-only checks. A later concurrent sale still needs a database-level stock rule; this form reads a snapshot.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Use cleaned values - 10 points

**Where:** `project/inventory/views.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Refactor the view to use cleaned_data or form.save only after is_valid. Explain why directly using request.POST bypasses your validated values.

Use the clerk's accepted fields rather than returning to the unchecked paperwork.

1. In the view call is_valid before form.save or use of cleaned_data.
2. Remove direct assignments from request.POST to model fields after validation.
3. For a valid ProductForm save once; for invalid input render the same bound form without saving.
4. Demonstrate normalized name and numeric stock using a padded name and raw text numbers.

**Check:** stored name is stripped and stock is numeric; invalid stock does not alter the existing row. A successful is_valid call is wasted if the view then saves different unvalidated values.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Protect the form flow - 10 points

**Where:** `project/inventory/templates/inventory/`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Include csrf_token and a labelled submit button. Show GET renders an unbound form and invalid POST re-renders a bound form with errors.

A bound form remembers the visitor's attempted input and its errors.

1. On GET create an unbound ProductForm; on POST bind request.POST.
2. Render labels, field values, errors, a submit button and csrf_token inside the POST form.
3. Submit a valid name with invalid stock, then correct only stock and resubmit.
4. Inspect the initial form and the failed form state.

**Check:** GET has no submission errors; failed POST preserves entered values and explains stock; correction can succeed without retyping everything. Do not replace an invalid bound form with a fresh empty one before rendering.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Test bypassed browser rules - 10 points

**Where:** `project/inventory/tests.py`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Submit invalid values directly with Django’s test client rather than relying on HTML input restrictions. Record status, form errors and unchanged row count.

Test the server by bypassing the browser's friendly restrictions.

1. In inventory/tests.py create a Django TestCase with known initial row count.
2. Use its test client to POST blank name, negative stock and fractional stock directly to your create route.
3. Assert the chosen form-error response, an invalid form/visible error and unchanged row count.
4. Add a valid POST and verify exactly one record with expected values.

**Check:** tests pass under `python manage.py test inventory` without opening a browser. These validation tests do not prove CSRF enforcement because Django's ordinary test client disables that check by default.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new accepted form value and a cross-field or conversion failure. Show raw input, cleaned values/errors and unchanged data after rejection. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 20
python grade.py rubric --lesson 20
```

The first checks the JSON prediction and writes `grading/reports/lesson-20.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-20/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

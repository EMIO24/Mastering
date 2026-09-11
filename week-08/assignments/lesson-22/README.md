# Lesson 22 assignment: DRF serializers

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A serializer is a bilingual receiving clerk: it converts model data to simple response values and checks incoming values before creating or changing records. It is not itself the network connection.

Use the Lesson 21 project and add DRF. Run serializer experiments in manage.py shell; import Product and your serializer from their inventory modules. Use Pen name/price/stock values Pen/200/4.

## Where to work and how to run it

Work in `week-08/assignments/lesson-22/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `project/config/settings.py` |
| 4 | `project/inventory/serializers.py` |
| 5 | `serializer-checks.md` |
| 6 | `project/inventory/serializers.py` |
| 7 | `project/inventory/serializers.py` |
| 8 | `serializer-checks.md` |
| 9 | `serializer-checks.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Serializer** | A component converting and validating representations. | the bilingual receiving clerk. |
| **Deserialization** | Turning an external representation into internal values. | translating an incoming form. |
| **validated_data** | Input values accepted by serializer validation. | the approved fields. |
| **read_only** | A field excluded from writable input. | an office-assigned box. |
| **ModelSerializer** | A serializer with model-derived fields and defaults. | a clerk using the ledger blueprint. |

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
from rest_framework import serializers

class SaleSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)

s = SaleSerializer(data={"quantity": "3"})
print(s.is_valid())
print(s.validated_data["quantity"])
```

**Question:** Enter the validated quantity as a JSON number.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Run in a Django project with DRF installed. Passing data= means incoming values need validation; passing an instance means representing existing data. is_valid performs checks before validated_data is consumed. This example converts the text quantity to integer 3.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Configure DRF - 10 points

**Where:** `project/config/settings.py`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Add rest_framework to INSTALLED_APPS in your project and record the installed version. Keep dependency versions in requirements.txt.

Install the API tools into the same toolbox that runs Django.

1. Use the project interpreter to install djangorestframework from prepared artifacts or while online.
2. Add rest_framework to INSTALLED_APPS and record `python -m pip show djangorestframework` output without unrelated environment details.
3. Run manage.py check and import rest_framework in the project shell.
4. Record the resolved installed version in requirements.txt.

**Check:** the running project can import DRF; installing it for a different interpreter does not satisfy this. Keep existing Django settings instead of replacing the entire file with a fragment.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Represent Product - 10 points

**Where:** `project/inventory/serializers.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Create ProductSerializer with explicit id, name, price and stock fields. Serialize Pen and show a JSON-compatible dictionary; serialize a list using many=True.

A serializer turns a model card into simple values suitable for a response.

1. In inventory/serializers.py create ProductSerializer as a ModelSerializer with explicit id/name/price/stock fields.
2. In the project shell import it and serialize an existing Pen record using an instance argument.
3. Serialize two products with many=True and inspect .data.
4. Explain how a single representation differs from a list representation.

**Check:** one record has the four selected fields; the collection has one representation per record. .data is not automatically a transmitted HTTP response; a view handles that later.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Validate incoming data - 10 points

**Where:** `serializer-checks.md`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Instantiate with data= for valid Pen input and invalid negative stock. Call is_valid and record validated_data or field errors; invalid input must not save.

Incoming data takes the opposite path and must be checked before saving.

1. Instantiate ProductSerializer with data containing Pen/200/4, then call is_valid and inspect validated_data.
2. Repeat with stock -1 and inspect errors. Add a missing required name case.
3. Record product count before and after validation-only calls.
4. Explain the distinction between instance= for an existing record and data= for submitted values.

**Check:** valid input is accepted, invalid fields produce errors and validation alone creates no database row. Accessing .data before calling .save on a writable serializer can also affect the intended workflow; validate and save in the correct order.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Protect assigned fields - 10 points

**Where:** `project/inventory/serializers.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Make id read-only. Supply an arbitrary id in input and demonstrate the client cannot choose an existing row’s primary key on creation.

A server-assigned identifier should not become a client-controlled creation field.

1. Mark id read-only in ProductSerializer, keeping it visible in output.
2. Submit a valid creation body containing an arbitrary id already belonging to another product.
3. Validate/save and inspect the assigned ID and original row.
4. Record whether the read-only input is ignored, as in the normal serializer behaviour, rather than promising an automatic rejection.

**Check:** the client cannot overwrite the existing row or dictate its ID through creation. The response still includes the server-assigned identifier for later detail requests.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Add a field rule - 10 points

**Where:** `project/inventory/serializers.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Strip and validate name with validate_name. Show blank input rejected and padded valid input normalized.

Normalize and validate a name at the serializer boundary.

1. Add validate_name(self,value) that strips whitespace, rejects an empty result with serializers.ValidationError, and returns accepted text.
2. Submit padded Pen and spaces-only names with otherwise valid fields.
3. Inspect validated_data/errors, then save only the valid case and refetch it.
4. Compare behaviour with the browser form's name rule.

**Check:** stored name is Pen without surrounding spaces; blank input creates no record. The API needs its own validation even if an HTML form already rejects the same input.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Create and update - 10 points

**Where:** `serializer-checks.md`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Call save after successful validation to create then update a Product. Record row count and values; explain instance= versus data=.

Creation and update both use save, but the existing instance changes the operation.

1. Validate a new product body and call save without an instance; record the new row's key and count change.
2. Make another serializer with that instance and a complete updated body, validate and save.
3. Refetch the row and check its fields/count.
4. Use an invalid update body to confirm saving is not performed after validation failure.

**Check:** creation adds one row; updating it does not add another. Invalid input leaves the previously stored fields intact. Print successful return values only after validation succeeds.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Partial update - 10 points

**Where:** `serializer-checks.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Use partial=True to change stock alone. Show name remains unchanged. Compare the same incomplete input under full validation and record which fields are required.

A partial update can change one box while retaining the others.

1. Start with a persisted Pen price 200/stock 4.
2. Bind that instance with data containing only stock 7 and partial=True; validate/save.
3. Refetch all fields. Separately try the same incomplete input without partial=True and record missing required-field errors.
4. Explain which writable fields are required by your actual serializer.

**Check:** PATCH-style update keeps name Pen and price 200 while stock becomes 7. Full validation normally requires name and price here; do not invent a missing-stock error if your model default makes it optional.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new valid serialization/save case and a rejected writable-field case. Compare serializer output, errors and row count. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 22
python grade.py rubric --lesson 22
```

The first checks the JSON prediction and writes `grading/reports/lesson-22.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-22/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

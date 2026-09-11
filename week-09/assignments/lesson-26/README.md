# Lesson 26 assignment: Permissions and ownership

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

Signing in gets a visitor into reception; ownership checks decide which stockroom records that visitor may see or change. Hiding a door in the UI does not lock it.

Use the Lesson 25 API. Make user A with two products and user B with three. Add/migrate ownership before running scoped queries. Refer to users by labels in evidence, not credentials.

## Where to work and how to run it

Work in `week-09/assignments/lesson-26/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `project/inventory/models.py` |
| 4 | `project/inventory/views.py` |
| 5 | `project/inventory/tests.py` |
| 6 | `project/inventory/views.py and serializers.py` |
| 7 | `project/inventory/permissions.py` |
| 8 | `project/inventory/views.py` |
| 9 | `project/inventory/tests.py` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Permission** | A rule deciding whether an operation is allowed. | the room-access rule. |
| **Object-level permission** | Authorization concerning a particular record. | access to one specific cabinet. |
| **Queryset scoping** | Restricting queried records to those the user may access. | only bringing authorized cards to the desk. |
| **Least privilege** | Granting only access needed for a task. | issuing the fewest necessary keys. |
| **Tenant** | An isolated customer or organization sharing an application. | one business renting space in the building. |

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
# Inside an authenticated ProductViewSet
def get_queryset(self):
    return Product.objects.filter(owner=self.request.user)
```

**Question:** User A owns 2 products and user B owns 3. How many should A see in this queryset?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Add an owner relation to Product first. Filtering prevents other users’ records appearing in list results and ordinary detail lookup. Object permissions do not automatically filter every list item; creation also needs explicit ownership assignment from request.user.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Add ownership - 10 points

**Where:** `project/inventory/models.py`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Add an owner foreign key to Product and migrate. Plan how existing rows receive owners in a disposable fixture rather than silently assigning every real row.

Ownership connects each card to the business/user allowed to manage it.

1. Add Product.owner as a ForeignKey to the configured user model and choose a documented deletion policy.
2. In a disposable fixture assign existing rows intentionally before enforcing any required non-null owner constraint.
3. Generate/apply migrations and create A's two products and B's three products.
4. Query each record's owner and record IDs without credentials.

**Check:** every fixture row has its intended owner; migration did not silently assign all real records to one account. Ownership requires query/view rules as well as the model field.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Scope list results - 10 points

**Where:** `project/inventory/views.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Filter the queryset to request.user. Seed A with two products and B with three; demonstrate their lists contain 2 and 3 records respectively.

Scope the rows brought to the service desk before serializing them.

1. In the authenticated ViewSet implement get_queryset filtering owner=request.user.
2. Sign in as A and list products; repeat as B using a separate client/session.
3. Record returned IDs and pagination counts.
4. Make the anonymous request and check that your authentication policy blocks it.

**Check:** A sees only two owned records and B only three. Object-level permission checks are not a substitute for filtering a list response; do not retrieve everyone's data and hide cards only in the UI.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Block guessed IDs - 10 points

**Where:** `project/inventory/tests.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Have A request B’s detail, update and delete URLs directly. Verify no data exposure or mutation; document whether your scoped endpoint returns 404 or 403.

Guessing another user's valid ID must not bypass the list restriction.

1. Record one B-owned product ID and its fields.
2. As A request its detail, PATCH its stock and DELETE it directly.
3. Inspect the record as B afterward.
4. State your policy: a queryset scoped before lookup commonly returns 404 for an inaccessible ID; explicit object denial may return 403.

**Check:** all three attempts disclose no protected details or mutations and B's row remains unchanged. Verify state, not just an error-looking message in an otherwise successful response.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Assign owner server-side - 10 points

**Where:** `project/inventory/views.py and serializers.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Use perform_create(serializer.save(owner=request.user)) or equivalent. Submit B’s ID as A and show A cannot transfer ownership through writable input.

The server determines ownership during creation.

1. Make owner read-only or exclude it from writable serializer fields.
2. In perform_create save with owner=request.user.
3. As A submit a valid product body that also tries to supply B's owner ID.
4. Inspect the created row and both users' lists.

**Check:** it belongs to A, or the extra owner field is explicitly rejected under your policy; it must never become B's product. Validating that B's ID exists does not grant A permission to assign ownership to B.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Add a business role - 10 points

**Where:** `project/inventory/permissions.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Define staff read/write privileges explicitly and implement them. Demonstrate one allowed and one denied operation for an ordinary user and a staff user.

Define the privilege policy before writing a special-case bypass.

1. In permissions.py define whether staff may view all products and perform all operations, or a narrower documented set.
2. Implement both queryset visibility and write checks consistently with that choice.
3. Test ordinary A, ordinary B and staff against owned and unowned rows.
4. Record one allowed and one denied ordinary-user action plus the relevant staff behaviour.

**Check:** a role flag is not automatically a universal override. The matrix describes the actual implemented policy, including whether staff can transfer ownership.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Guard custom actions - 10 points

**Where:** `project/inventory/views.py`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Apply the same scope and permission rules to low-stock and sale actions. Show that a custom route cannot bypass another user’s inventory boundary.

Custom actions must use the same permission boundary as standard CRUD.

1. Audit low-stock and sale actions for direct unscoped Product.objects lookups.
2. Use get_queryset/get_object or equivalent scoped access before reading or modifying a product.
3. As A call the low-stock action and attempt a sale against B's product ID.
4. Inspect both users' inventory after the attempts.

**Check:** custom lists contain only permitted rows and the cross-owner sale changes neither stock nor sale history. A permission check on retrieve alone does not automatically protect custom code that bypasses it.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Build a permission matrix - 10 points

**Where:** `project/inventory/tests.py`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Write automated API tests covering anonymous/A/B/staff against list/detail/create/update/delete. Record expected status and database effect for each relevant case.

Turn the access matrix into repeatable API checks.

1. Create fixtures for anonymous, A, B and staff, with known owned records.
2. Test list/detail/create/update/delete outcomes appropriate to each role and ownership relationship.
3. Assert response status, returned IDs and database side effects, using fresh records for destructive cases.
4. Run `python manage.py test inventory` and record the matrix plus results.

**Check:** direct guessed-ID attacks and owner-spoofed creation are covered. If you use force_authenticate for permission tests, label them as permission tests; they do not validate JWT signature handling.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a permitted owner action and a cross-owner or spoofed-owner attempt. Check both response visibility and persisted ownership/stock. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 26
python grade.py rubric --lesson 26
```

The first checks the JSON prediction and writes `grading/reports/lesson-26.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-26/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

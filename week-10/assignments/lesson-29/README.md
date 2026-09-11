# Lesson 29 assignment: Query performance and caching

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

Performance work is timing the queue before changing the shop layout. Fetching one supplier per product is many trips to the same cabinet; a joined fetch can reduce those trips.

Use a disposable backend database. Add Supplier(name) and a Product supplier ForeignKey if missing, then migrate. Add a categories many-to-many or reverse sale-line relation for the collection task. Seed at least 100 products and several suppliers; record fixture size before measuring.

## Where to work and how to run it

Work in `week-10/assignments/lesson-29/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `performance.md` |
| 4 | `performance.md` |
| 5 | `project/inventory/views.py` |
| 6 | `project/inventory/views.py` |
| 7 | `project/inventory/views.py` |
| 8 | `project/inventory/views.py` |
| 9 | `project/inventory/views.py and tests.py` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Latency** | Elapsed time for an operation. | one customer’s waiting time. |
| **Throughput** | Operations completed per unit time. | customers served per minute. |
| **N+1 queries** | One initial query followed by a query per result. | one catalogue trip plus a supplier trip per card. |
| **Cache** | Stored reusable results. | a temporary copy at the counter. |
| **Invalidation** | Removing or updating cached results after changes. | replacing an outdated counter copy. |

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
# Product has a supplier ForeignKey.
products = Product.objects.select_related("supplier").order_by("id")
for product in products:
    print(product.name, product.supplier.name)
```

**Question:** A naive list does 1 product query plus 1 supplier query for each of 5 products. How many queries is that?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

select_related joins single-valued relationships such as foreign keys. prefetch_related uses separate queries and joins results in Python, fitting collections. Fewer queries do not guarantee faster execution for every workload; measure representative data and response correctness.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Create a baseline - 10 points

**Where:** `performance.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Seed at least 100 products with suppliers. Measure query count and elapsed time for a list endpoint with repeated trials; record fixture size and environment.

Measure a repeatable workload before changing the implementation.

1. Seed at least 100 products assigned to several suppliers in a disposable database.
2. Record fixture count, response page size, database engine and the exact list request.
3. Capture query count and elapsed time for repeated runs, distinguishing first/warm runs.
4. Save returned IDs/names as a correctness reference alongside timing.

**Check:** comparisons use the same data and workload. Do not compare an unpaginated 100-row response against a 2-row response and attribute every difference to query optimization.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Expose N+1 - 10 points

**Where:** `performance.md`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Render each product’s supplier name without eager loading. Capture query count and explain the repeated pattern.

N+1 means one list query followed by a lookup for each returned product.

1. Render/serialize supplier.name for each product without eager loading.
2. Capture queries around the complete evaluation, not just QuerySet construction.
3. Identify the initial product query and repeated supplier fetches.
4. For a controlled unpaginated five-product case, compare with the expected one-plus-five pattern, noting any extra unrelated queries separately.

**Check:** the evidence shows repeated supplier lookups. If your framework already eagerly loads or reuses values, report that instead of inventing six queries.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Join a foreign key - 10 points

**Where:** `project/inventory/views.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Apply select_related for supplier and measure again. Verify returned names and ordering are unchanged; report query counts before/after.

Join single-valued relationships before the display loop.

1. Add select_related("supplier") to the same queryset used by the measured response.
2. Rerun the identical request and capture query count/timing again.
3. Compare returned IDs, product names and supplier names with the baseline.
4. Explain which repeated trips to the database disappeared.

**Check:** the controlled product/supplier iteration normally uses one joined select; overall request counts may include authentication or pagination queries. Correctness must remain unchanged even if elapsed times vary on a small dataset.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Prefetch a collection - 10 points

**Where:** `project/inventory/views.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** For a many-to-many category relation or reverse sale lines, compare naive access with prefetch_related. Explain why select_related alone cannot serve that collection.

Collections need a different loading strategy from one foreign key.

1. Choose Product.categories or a reverse sale-line relation and seed at least two related entries for a product.
2. Access that collection for each product and capture the naive query pattern.
3. Add prefetch_related for the selected relationship and repeat exactly the same access.
4. Compare values and explain the separate child query combined in Python.

**Check:** related collections are complete and repeated per-product queries are reduced. A later differently filtered related-manager call may bypass the prefetched cache; measure the exact access your UI uses.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Bound output - 10 points

**Where:** `project/inventory/views.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Paginate a list and select only needed fields where appropriate. Compare payload size and query behaviour without dropping required response fields.

Bound both database work and the size of the response deliberately.

1. Configure a fixed page size and explicit ordering; request first and next pages on the same fixture.
2. Identify fields the client actually needs and remove only unnecessary response fields.
3. Measure serialized response bytes and query counts before/after, recording page sizes.
4. Confirm links/counts and required fields still match the contract.

**Check:** all intended records remain reachable and IDs do not repeat across stable pages. Fewer fields is not permission to drop a field the frontend depends on without updating its contract.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Cache a summary - 10 points

**Where:** `project/inventory/views.py`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Cache a stock summary with a documented key and expiry. Include owner/tenant in keys when relevant. Show users cannot receive each other’s cached totals.

A cached summary is a temporary copy that must respect ownership.

1. Calculate an owner's stock total and choose a cache key incorporating owner ID and summary version.
2. Give A and B different totals, for example 4 and 9, and request summaries as each.
3. Cache the result with a documented short expiry, then repeat requests to observe reuse.
4. Record backend/cache configuration and the uncached value used for comparison.

**Check:** A always gets 4 and B 9 in the fixture, including cached requests. A single global stock-summary key would leak or mix data between users.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Invalidate after a sale - 10 points

**Where:** `project/inventory/views.py and tests.py`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Sell an item and invalidate/update the relevant cache after a successful database commit. Demonstrate the next summary shows current stock and a failed sale does not publish a wrong total.

Publish a cache change only after the authoritative database transaction succeeds.

1. Begin with A's cached total 4. Sell one unit successfully and schedule invalidation using transaction.on_commit or equivalent post-commit logic.
2. Request the summary again and compare with the database total 3.
3. Repeat from a fresh fixture with a forced transaction failure.
4. Observe that no false success total is published for the rolled-back sale.

**Check:** committed sale refreshes to 3; failed sale remains 4. In Django TestCase, use supported commit-callback execution tools or a suitable transaction test; callbacks may not run when the outer test transaction never commits.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new measured query/cache success and a stale/cross-owner cache case. Compare correctness before making a performance claim. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 29
python grade.py rubric --lesson 29
```

The first checks the JSON prediction and writes `grading/reports/lesson-29.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-29/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

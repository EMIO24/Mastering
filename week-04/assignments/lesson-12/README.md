# Lesson 12 assignment: REST API design

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

An API is a published service counter contract. Resource URLs are labelled counters such as products and sales. REST is an architectural style, not merely putting JSON on any URL.

Write api-contract.md as a specification another programmer could implement; you are not building the server yet. Use five products with IDs 1 through 5, names Pen/Notebook/Bag/Pencil/Eraser and stocks 4/8/0/2/6. Use page size 2 and ID order unless an exercise says otherwise.

## Where to work and how to run it

Work in `week-04/assignments/lesson-12/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

No server command is needed. Walk each request/response through your contract, checking method, URL, fields, status and database effect. Save the scenario trace in answers.md.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `api-contract.md` |
| 4 | `api-contract.md` |
| 5 | `api-contract.md` |
| 6 | `api-contract.md` |
| 7 | `api-contract.md` |
| 8 | `api-contract.md` |
| 9 | `api-contract.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **API** | An interface through which software interacts. | the published counter contract. |
| **Resource** | A concept identified and manipulated through a representation. | a product record at a named counter. |
| **Representation** | Data describing a resource. | a copy of the product card. |
| **Stateless request** | A request understood without relying on stored client conversation context. | an order carrying the needed credentials and details. |
| **Pagination** | Dividing a collection into bounded result pages. | issuing a catalogue a few pages at a time. |

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
GET /api/products/?page=2

{"count":3,"next":null,"previous":"?page=1",
 "results":[{"id":3,"name":"Bag"}]}
```

**Question:** How many product records are in this response page?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

A collection response wraps a page of records with navigation metadata. A client must read results rather than assuming the root is an array. Statelessness does not mean the server has no database; it concerns request context.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Specify resources - 10 points

**Where:** `api-contract.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** List products, customers and sales with collection/detail URLs. Use stable IDs, and explain why a sale deserves its own resource.

Resource names should identify business records, not arbitrary screen buttons.

1. In api-contract.md list products, customers and sales, with `/api/products/`, `/api/customers/` and `/api/sales/` collection paths.
2. Add a detail pattern using an ID, such as `/api/products/7/`, for each.
3. State what each resource represents and which ID identifies it.
4. Explain why a completed sale needs its own record instead of only decreasing a product field.

**Check:** a sale can retain quantity, historical price and purchaser information even after current product details change. Use stable numeric IDs in this exercise; do not use list positions as persistent identity.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Write endpoint contracts - 10 points

**Where:** `api-contract.md`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Create api-contract.md covering list, detail, create, update and delete products. Specify method, URL, request fields, success status and error status for each.

Write a contract another developer can implement without guessing the operation.

1. Make a table for list, retrieve, create, full update, partial update and delete products.
2. For every row state method/path, writable fields, successful status/body and at least one failure.
3. Use 200 for reads/updates, 201 for creation and 204 with no body for deletion in this design.
4. Include one concrete request/response pair for creating Pen at 200/4.

**Check:** a reader knows whether collection results are paginated and whether a deleted response has a body. Missing records return 404 and invalid submitted fields return 400 under the stated contract.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Define validation - 10 points

**Where:** `api-contract.md`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Require nonblank name, integer price >=0 and integer stock >=0. Give one accepted JSON body and four rejected bodies with field-specific errors.

Parsing JSON only establishes its structure; validation establishes whether the shop accepts its values.

1. Define name as nonblank text, and price/stock as nonnegative whole-number values. Exclude Boolean values from the intended numeric contract.
2. Write a valid body with name Pen, price 200 and stock 4.
3. Write separate invalid examples: blank name, negative price, fractional stock and Boolean stock.
4. Give field-specific errors and state that rejected creation leaves the product count unchanged.

**Check:** all five examples are valid JSON, but only the first satisfies business rules. Label malformed JSON separately if you add it; it fails parsing before field validation.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Paginate products - 10 points

**Where:** `api-contract.md`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Design a page size of 2 for five sample products. Write all three response pages and correct next/previous values. Keep ordering explicit by ID.

Pagination divides a long catalogue into predictable pieces.

1. Use IDs 1–5 from the starting fixture, ordered ascending, with page size 2.
2. Write all three complete response objects using count, next, previous and results.
3. Put two product objects on pages 1 and 2 and one on page 3. Use null where no neighbouring page exists.
4. Explain that count is the whole matching collection size, not just the current page length.

**Check:** page IDs are [1,2], [3,4], [5]; count remains 5. Following next from the first page reaches every ID once, and the last next is null.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Filter and order - 10 points

**Where:** `api-contract.md`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Specify low-stock and name-search query parameters and allowed ordering fields. Give an example matching two records and define unknown parameter behaviour.

A filter chooses records; ordering arranges the chosen records.

1. Define `stock_lte` as an integer cutoff and `search` as case-insensitive name substring matching. Choose allowed ordering fields, such as id/name/stock.
2. With starting stocks 4/8/0/2/6, show `stock_lte=2` returning Bag and Pencil when ordered by ID.
3. Show `search=pen` matching Pen and Pencil under substring rules.
4. Specify invalid/unknown parameter behaviour and show one rejected or deliberately ignored example.

**Check:** your examples use the same documented matching rule; results keep the pagination envelope. Do not promise arbitrary database field ordering without defining what the API allows.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Model stock changes - 10 points

**Where:** `api-contract.md`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Design POST /sales/ with product ID and quantity. Specify insufficient-stock handling, unchanged stock after failure, and how clients learn the updated stock.

A sale request proposes a ledger change; the server decides whether it can commit it.

1. Specify POST /api/sales/ with product_id and positive integer quantity. The server obtains price from the product record, not a client-supplied total.
2. Start Pen at stock 4, price 200. Show a sale of 2 returning a sale ID, total 400 and updated stock 2.
3. From a fresh stock 4, show quantity 5 rejected with your chosen documented business-error status and no sale/stock change.
4. Explain how the client gets confirmed stock and what it should do when a request's outcome is uncertain.

**Check:** the response/error contract is explicit and does not let the browser authorize its own sale.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Review compatibility - 10 points

**Where:** `api-contract.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Add a new optional product field without removing existing fields. Compare that with renaming id, explain which clients break, and write a migration/versioning note.

A contract change can break code that already depends on it.

1. Add an optional description field to the product response and describe a client that ignores unknown fields.
2. Compare with renaming id to product_number and deleting id from the response.
3. Write a small before/after example showing why an existing client's `product.id` access breaks in the second case.
4. Propose a transition: retain the old field temporarily or introduce a documented version, with a migration plan for callers.

**Check:** you identify the affected consumer and a way to keep it working during change. Do not call every added field harmless if an existing consumer rejects unknown fields; state your compatibility assumption.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new resource/page scenario and an invalid request. Trace pagination or validation using your contract, including whether stored data would change. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 12
python grade.py rubric --lesson 12
```

The first checks the JSON prediction and writes `grading/reports/lesson-12.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-12/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

# Lesson 32 assignment: Modern JavaScript transformations

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

map sends every product card through a rewriting station; filter keeps selected cards; reduce combines cards into one summary. A spread copy duplicates the outer box, not every nested object.

Use objects with id/name/price/stock. For total 3500 use Pen 200/10, Book 500/3 and Bag 4000/0. The worked low-stock example has its own Pen stock 4 and Book stock 8 fixture; do not mix the two.

## Where to work and how to run it

Work in `week-11/assignments/lesson-32/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Run plain scripts with `node practice.js` or load them in a browser page and use its Console. ES module files need `<script type="module" src="main.js"></script>`. Serve this folder with `python -m http.server 8080 --bind 127.0.0.1` and open `http://127.0.0.1:8080/`. Relative /api/ fetches need a backend/proxy at that origin; otherwise use an explicit local API URL with appropriate origin settings or a labelled mock.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `practice.js` |
| 4 | `practice.js` |
| 5 | `practice.js` |
| 6 | `practice.js` |
| 7 | `practice.js` |
| 8 | `calculations.js and main.js` |
| 9 | `practice.js` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Arrow function** | A compact function expression with lexical this. | a short task instruction using its surrounding context. |
| **Destructuring** | Extracting values through a matching pattern. | unpacking labelled compartments. |
| **Spread** | Expanding iterable values or object properties. | emptying one outer box into another. |
| **map** | Creating an array from one result per input item. | rewriting every card. |
| **reduce** | Accumulating values into a result. | combining receipt lines into a total. |

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

```javascript
const products = [{name:"Pen",stock:4},{name:"Book",stock:8}];
const names = products.filter(p => p.stock <= 4).map(p => p.name);
console.log(names);
```

**Question:** Enter the resulting names array.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

filter selects the Pen object, then map extracts its name. Neither call changes the original array in this example, but the selected object references are shared. Copy the changed nested object too when making an immutable update.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Extract fields - 10 points

**Where:** `practice.js`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Use object destructuring to read name and stock from a product, with a default category. Demonstrate missing category versus a present category.

Destructuring unpacks named fields without repeatedly spelling the object path.

1. Create a product with name Pen and stock 4, omitting category.
2. Destructure name, stock and a default category such as General, then log them.
3. Repeat with category Stationery already present.
4. Compare missing category with category null and explain when the default applies.

**Check:** missing/undefined category uses General; present Stationery stays Stationery; null remains null. A destructuring default is not a replacement for every false-like value.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Transform without mutation - 10 points

**Where:** `practice.js`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Use map to add a displayLabel to copied products. Show original objects have no new displayLabel property.

map creates one output per card; copying the object prevents changing the original card.

1. Use Pen stock 4 and Book stock 8.
2. Map to new objects that retain all fields and add displayLabel, for example `Pen (4 units)`.
3. Log original and transformed arrays using JSON.stringify.
4. Change a transformed label and inspect the original record again.

**Check:** transformed entries have correct labels and original entries have no displayLabel property. Returning the same object after adding a property mutates it even though map creates a new outer array.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Filter low stock - 10 points

**Where:** `practice.js`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Implement lowStockNames(products,threshold) with filter/map. Check equality at 4, above threshold, and an empty array.

Chain selection and transformation to return just the names needed.

1. Implement lowStockNames(products,threshold) with filter followed by map.
2. Filter using stock <= threshold and map matching objects to name strings.
3. Test Pen stock 4, Book 8 and Bag 0 with cutoffs 4 and 0, then empty input.
4. Compare ordering with the original array.

**Check:** cutoff 4 returns ["Pen","Bag"], cutoff 0 ["Bag"], empty input []. Equality is included and the function returns names, not matching product objects.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Reduce totals - 10 points

**Where:** `practice.js`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Use reduce with initial value 0 to total price*stock. Test the 3500 fixture and empty input.

reduce combines several line values into one total.

1. Implement an inventory total using reduce with initial accumulator 0.
2. For each product add price times stock to the accumulator and return the next accumulated value from the callback.
3. Test fresh Pen 200/10, Book 500/3, Bag 4000/0 and an empty array.
4. Explain what the initial zero does when there are no items.

**Check:** results are 3500 and 0. Omitting a callback return can turn later accumulation into undefined/NaN; log a small two-item trace if your result is unexpected.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Update nested data - 10 points

**Where:** `practice.js`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Create state={products:[...]}; replace one product stock using object spread and map. Demonstrate both original stock and unrelated product values remain unchanged.

Copy every level that changes, while allowing unchanged objects to be shared.

1. Start with state={products:[Pen stock4, Book stock8]} using complete product objects with IDs.
2. Create nextState with a copied outer state, a mapped products array and a copied Pen object whose stock is 7.
3. Inspect old/new stock values and reference comparisons for state, array, Pen and Book.
4. Explain why a spread of only state leaves its nested products shared.

**Check:** old Pen stays 4, new Pen is 7; outer state/array/changed Pen have new references. Sharing unchanged Book is acceptable and demonstrates a targeted immutable update.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Export reusable functions - 10 points

**Where:** `calculations.js and main.js`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Move calculations to calculations.js with named exports and import from an ES module entry. Run with browser type=module or correctly configured Node modules and record the setup.

An ES module exposes named tools to another file.

1. Move inventoryValue and lowStockNames to calculations.js and export them by name.
2. Import both in main.js and log known fixture results.
3. In index.html load main.js with type="module" and serve the folder over local HTTP; alternatively configure Node's ES module mode deliberately.
4. Record your exact command/URL and any package.json module setting used.

**Check:** imported functions yield 3500 and the correct low-stock names. Opening an ES module page through file:// can introduce browser restrictions unrelated to your function logic.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Handle optional fields - 10 points

**Where:** `practice.js`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Read an optional supplier name with optional chaining and ?? fallback. Show absent supplier and an intentionally empty string; explain why || may behave differently.

Optional chaining protects missing paths; nullish fallback preserves intentionally empty values.

1. Prepare products with no supplier, supplier name Acme, and supplier name an empty string.
2. Read supplier?.name with a ?? fallback such as Unknown.
3. Compare with using || for the same inputs.
4. Explain whether empty supplier text should be preserved or rejected by a separate validation rule.

**Check:** ?? yields Unknown, Acme, then empty string; || uses its fallback for the empty string too. These operators do not prove the underlying data is valid; they define access/fallback behaviour.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new transformation and an empty/nested-copy case. Snapshot original and new values so shared references cannot hide a mutation. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 32
python grade.py rubric --lesson 32
```

The first checks the JSON prediction and writes `grading/reports/lesson-32.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-32/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

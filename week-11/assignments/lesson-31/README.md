# Lesson 31 assignment: JavaScript fundamentals

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

JavaScript values and control flow resemble Python’s stockroom tools, but the labels and rules differ. const locks a name’s binding; it does not freeze the contents of the box.

Create practice.js for plain JavaScript and index.html for the input/button task. Load the script from the HTML page. For inventory totals use Pen 200/10, Book 500/3 and Bag 4000/0.

## Where to work and how to run it

Work in `week-11/assignments/lesson-31/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Run plain scripts with `node practice.js` or load them in a browser page and use its Console. ES module files need `<script type="module" src="main.js"></script>`. Serve this folder with `python -m http.server 8080 --bind 127.0.0.1` and open `http://127.0.0.1:8080/`. Relative /api/ fetches need a backend/proxy at that origin; otherwise use an explicit local API URL with appropriate origin settings or a labelled mock.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `practice.js` |
| 4 | `practice.js` |
| 5 | `practice.js` |
| 6 | `practice.js` |
| 7 | `practice.js` |
| 8 | `practice.js` |
| 9 | `index.html and practice.js` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Binding** | An association between a name and a value. | a label pointing to a box. |
| **const** | A declaration whose binding cannot be reassigned. | a fixed label attachment. |
| **let** | A block-scoped reassignable declaration. | a label you may move within one room. |
| **Object** | A collection of properties. | a named product card. |
| **Strict equality** | Equality comparison without type coercion. | comparing labels without automatic conversion. |

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
const product = {name: "Pen", stock: 4};
product.stock += 2;
console.log(product.stock);
console.log("6" === 6);
```

**Question:** Enter the two logged values as a JSON list.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

The const binding still points to the same object, whose stock property changes to 6. Strict equality compares the string and number as different types. Run plain JavaScript in Node or a browser console; JSX comes later.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Use declarations - 10 points

**Where:** `practice.js`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** In practice.js declare shopName with const and stock with let. Update stock, then demonstrate a caught reassignment error for a const binding in a separate example.

const fixes a binding; let allows that binding to be reassigned.

1. In practice.js declare shopName with const and stock with let, then increase stock from 4 to 6.
2. Print both values.
3. In a separate try/catch block attempt to reassign shopName and print the caught error's name.
4. Compare with changing a property of a const-bound product object.

**Check:** stock becomes 6; const reassignment throws TypeError; changing an object's stock property is still possible. Binding immutability is not the same as freezing the object's contents.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Convert input - 10 points

**Where:** `practice.js`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Convert "200" and "3" to numbers and calculate 600. Check Number.isFinite after conversion and reject a nonnumeric value; explain why empty text needs an explicit rule.

Input text needs conversion and a business rule before arithmetic.

1. Write a helper or short routine accepting price text "200" and quantity text "3".
2. Reject empty/whitespace-only input explicitly, then convert with Number and check Number.isFinite.
3. Multiply accepted values and display the result.
4. Try "two" and empty text as invalid alternatives.

**Check:** valid inputs produce 600; invalid input produces your documented error/message, not NaN as a customer total. Number("") is zero, which is why the explicit empty-input rule is necessary.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Classify stock - 10 points

**Where:** `practice.js`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Implement stockLabel(stock) returning out for 0, low for 1 through 5 and available above 5. Demonstrate 0,1,5,6.

Return one label for each stock range.

1. Define stockLabel(stock), assuming nonnegative integer input.
2. Return the exact strings out for 0, low for 1 through 5, and available above 5.
3. Log calls for 0,1,5,6 and compare with the expected sequence.
4. Explain why the equality at 5 belongs to the low branch.

**Check:** logs are out, low, low, available. Do not use console.log as a substitute for returning the label: another function needs the returned string.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Represent products - 10 points

**Where:** `practice.js`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Create an array of three product objects with id, name, price and stock. Update only the second product and show all records before/after.

Use objects for individual cards and an array for the shelf.

1. Create three objects with id/name/price/stock: Pen 200/10, Book 500/3 and Bag 4000/0, IDs 1/2/3.
2. Put them in products and log a snapshot using JSON.stringify.
3. Change only the second product's stock from 3 to 8, then log another snapshot.
4. Explain zero-based position 1 versus product ID 2.

**Check:** only Book's stock changes. Browser consoles may display live object references later, so stringified snapshots make the before/after evidence unambiguous.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Sum inventory - 10 points

**Where:** `practice.js`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Implement inventoryValue(products) returning the sum of price*stock and 0 for empty input. Use Pen 200/10 and Book 500/3 to expect 3500.

Compute a total from the supplied records, not a memorized answer.

1. Define inventoryValue(products) with an accumulator or other calculation over price times stock.
2. Use a fresh fixture with Pen stock 10, Book stock 3 and Bag stock 0; do not reuse the modified Book stock from Exercise 6.
3. Return the numeric sum and test an empty array.
4. Add a different one-item fixture to prove the calculation generalizes.

**Check:** original fixture returns 3500; [] returns 0; one Pen at 200/2 returns 400. The input array and object fields should remain unchanged.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Find a product - 10 points

**Where:** `practice.js`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Implement findProduct(products,id) and document missing-result behaviour. Test first, last and absent IDs without changing the array.

Find by the printed ID, not by array position.

1. Define findProduct(products,id), comparing each object's id with the supplied value using the intended strict numeric-ID contract.
2. Return the matching object; document missing results as undefined if using Array.find, or choose null consistently.
3. Test first, last, missing ID 99 and empty array.
4. Snapshot input before/after to verify no changes.

**Check:** IDs 1 and 3 return Pen and Bag; absent cases return the documented missing value. An ID 42 can exist in a one-item array and should still be found.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Connect a basic page - 10 points

**Where:** `index.html and practice.js`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Create index.html with a labelled quantity input, button and output element. Load practice.js and display a calculated total on click; show an invalid-input message.

Connect calculation to a real browser action.

1. Create index.html with a label-linked quantity input, Calculate button and output/status element.
2. Load practice.js and attach a click listener after the elements exist.
3. Read quantity text, validate/convert it, and calculate at fixed unit price 200.
4. Display either a total or an input error using textContent.

**Check:** quantity 3 displays 600; empty and nonnumeric values show a message rather than NaN. For direct-text invalid tests, use an input that permits typing them or dispatch a test value; document what the actual browser allowed.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new accepted JavaScript calculation and an invalid input/type case. Record returned values separately from console output and object mutation. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 31
python grade.py rubric --lesson 31
```

The first checks the JSON prediction and writes `grading/reports/lesson-31.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-31/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

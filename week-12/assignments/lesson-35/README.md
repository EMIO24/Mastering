# Lesson 35 assignment: React state and controlled forms

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

State is a component’s remembered notebook. Each render sees a snapshot. Asking React to update it schedules a new snapshot; it does not rewrite the variable in the currently running handler.

Copy the previous React source/manifests into frontend/. Start with products in App.jsx. This lesson uses local state/callbacks, not backend requests. Keep text while typing, then convert/validate numeric fields on submit.

## Where to work and how to run it

Work in `week-12/assignments/lesson-35/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside frontend/ use the prepared dependencies and run `npm run dev`; open its printed URL. If starting fresh, while online run `npm create vite@latest frontend -- --template react` from the assignment folder, then `npm install` inside frontend/. Check its Node requirement and keep package-lock.json. JSX goes in src components, not a Python file or plain browser console. Offline work requires dependencies prepared in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `frontend/src/Counter.jsx` |
| 4 | `frontend/src/QuantityInput.jsx` |
| 5 | `frontend/src/ProductForm.jsx` |
| 6 | `frontend/src/App.jsx` |
| 7 | `frontend/src/App.jsx` |
| 8 | `frontend/src/InventorySummary.jsx` |
| 9 | `frontend/src/ProductForm.jsx` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **State** | Data React retains between renders. | the component’s notebook. |
| **Hook** | A React function connecting components to features such as state. | a standard notebook service. |
| **State setter** | A function scheduling a state update. | a request for the next notebook page. |
| **Controlled input** | An input whose displayed value comes from state. | a form box synchronized with the notebook. |
| **Lifting state** | Moving shared state to a common ancestor. | one shared notebook for two counters. |

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
import {useState} from "react";

export function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => {
    setCount(c => c + 1);
    setCount(c => c + 1);
  }}>{count}</button>;
}
```

**Question:** Starting at 0, what count is displayed after one click?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Functional updates receive the queued previous value, so one click adds 2. Two setCount(count + 1) calls in this handler would each use the same render snapshot. Keep Hooks at the top level of components or custom Hooks.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Add a counter - 10 points

**Where:** `frontend/src/Counter.jsx`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Implement Counter and demonstrate the initial 0 and one-click 2 result. Compare functional setters with two snapshot-based setters in a separate demonstration.

Functional state updates receive the queued previous value.

1. Implement Counter with useState(0) and a click handler calling setCount(c=>c+1) twice.
2. Render count in the button and click once, then twice.
3. In a separate comparison version use two setCount(count+1) calls and repeat from zero.
4. Explain each handler's render snapshot and queued updates.

**Check:** functional version goes 0→2→4; the two snapshot-based updates in one handler add only 1 per click. Do not interpret the setter as immediately rewriting the local count variable.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Control a quantity field - 10 points

**Where:** `frontend/src/QuantityInput.jsx`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Use state for an input value and onChange. Keep the raw text while editing; convert and validate on submit. Demonstrate empty, 3 and invalid text.

Keep an input editable before interpreting its contents as a number.

1. Use string state for the quantity field's value and update it in onChange.
2. On submit reject blank text, non-finite conversions and nonpositive/non-integer quantities.
3. Display accepted integer quantity or a useful error without losing the typed value.
4. Try empty text, 3, 0 and 2.5.

**Check:** 3 is accepted; other listed values reject. Clearing the input must leave it empty while editing, not force zero back into the field on every keystroke.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Build an add-product form - 10 points

**Where:** `frontend/src/ProductForm.jsx`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Control name, price and stock inputs. Reject blank name or negative/non-integer numbers with visible messages; successful submission calls a parent callback.

A controlled product form owns its draft until the parent accepts submission.

1. Create ProductForm with name, price and stock string state plus labelled inputs.
2. On submit prevent default browser navigation, strip/check name and convert nonnegative integer price/stock.
3. If valid, call onAdd with a normalized product draft; let the parent allocate an ID.
4. Try Pen/200/4, blank name, negative price and fractional stock.

**Check:** only the valid draft reaches the callback. Invalid fields show readable errors and retain their entered values. Browser restrictions supplement these checks rather than replacing them.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Update arrays immutably - 10 points

**Where:** `frontend/src/App.jsx`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Add a new product using a new array and update one product with map plus object spread. Show existing product data is preserved.

Update state through new containers so React can track the change.

1. In App hold the products array in state.
2. Add a draft using a new array and a stable new ID, with a functional setter if the update depends on prior state.
3. Update one product's stock using map and a copied object for that product.
4. Save before/after snapshots and display the list after both actions.

**Check:** adding increases length by one; editing changes only the targeted stock. Do not push into the existing state array or modify a referenced product and then reuse the same array.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Lift shared state - 10 points

**Where:** `frontend/src/App.jsx`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Put products in the common parent of list and summary. Add a product and show both components update from the same data source.

Two displays of the same inventory should read one owned state value.

1. Move products state into the nearest parent shared by ProductList and InventorySummary.
2. Pass the records down and supply the form with the parent's add callback.
3. Add a product through the form and inspect both list and summary.
4. Draw the data-down/events-up flow in answers.md.

**Check:** both displays update together without maintaining separate product arrays. Lifting state means moving ownership, not copying the current state into another component once.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Derive a total - 10 points

**Where:** `frontend/src/InventorySummary.jsx`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Calculate inventory value from products during rendering instead of storing a separate synchronized total. Show updating price or stock updates the summary.

A summary derived from products does not need a second synchronized notebook.

1. In InventorySummary calculate the sum of price*stock from props during rendering.
2. Use Pen 200/10 and Book 500/3 to expect 3500.
3. Update Book stock to 4 through the parent's state update and observe the summary.
4. Compare with an empty array and explain why a separate total state/effect is unnecessary here.

**Check:** totals are 3500, then 4000, and 0 for empty input. Derive from the current props instead of storing an old total that must be kept in sync manually.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Reset deliberately - 10 points

**Where:** `frontend/src/ProductForm.jsx`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** After a successful local submission clear the form; after a failed validation keep entered values. Demonstrate both flows with keyboard-accessible labels and buttons.

Reset a completed draft, but keep a rejected draft available to repair.

1. After a valid local onAdd completion, clear the form's input/error state.
2. After validation failure, preserve all draft fields and display the relevant error.
3. Submit valid Pen, then an invalid Book with negative stock, correct only its stock and resubmit.
4. Use keyboard tab/submit actions and confirm labels identify inputs.

**Check:** successful additions reset once; failed attempts retain data; correction adds only the intended record. Network-success handling is a later concern; this exercise's callback is a local operation.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new valid state/form update and a rejected draft or queued-update case. Record input retention and the list/summary values. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 35
python grade.py rubric --lesson 35
```

The first checks the JSON prediction and writes `grading/reports/lesson-35.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-35/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

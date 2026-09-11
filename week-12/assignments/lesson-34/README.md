# Lesson 34 assignment: React components and props

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A component is a reusable display recipe; props are the ingredients handed to it. Rendering describes the screen from those ingredients. A component should not quietly rewrite the parent’s ingredients.

Create/use a prepared React project in frontend/, with components in src/. No API is needed. Define fixture products in App.jsx: Pen 200/4, Book 500/8 and Bag 4000/0, with IDs 1/2/3.

## Where to work and how to run it

Work in `week-12/assignments/lesson-34/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside frontend/ use the prepared dependencies and run `npm run dev`; open its printed URL. If starting fresh, while online run `npm create vite@latest frontend -- --template react` from the assignment folder, then `npm install` inside frontend/. Check its Node requirement and keep package-lock.json. JSX goes in src components, not a Python file or plain browser console. Offline work requires dependencies prepared in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `frontend/` |
| 4 | `frontend/src/ProductCard.jsx` |
| 5 | `frontend/src/ProductList.jsx` |
| 6 | `frontend/src/ProductList.jsx` |
| 7 | `frontend/src/App.jsx` |
| 8 | `frontend/src/ProductCard.jsx` |
| 9 | `frontend/src/ProductCard.jsx and App.jsx` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Component** | A reusable unit describing UI. | the display recipe. |
| **JSX** | Syntax for describing elements inside JavaScript. | a structured display sketch. |
| **Props** | Inputs supplied to a component. | ingredients from the parent. |
| **Render** | Computing a UI description. | drawing the display from current ingredients. |
| **Key** | A stable identity hint for siblings in a list. | the permanent card number on repeated displays. |

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
export function ProductCard({product}) {
  return <article>
    <h2>{product.name}</h2>
    <p>{product.stock} units</p>
  </article>;
}
```

**Question:** With product={name:"Pen",stock:4}, enter the paragraph text.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Use this in a React project with JSX tooling already installed. The component receives product through props and returns a description. Render lists with stable product IDs as keys; array indexes can misidentify items after insertions or reordering.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Prepare React locally - 10 points

**Where:** `frontend/`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Use your installed React project/toolchain and record package versions plus the local start command. Confirm the starting page renders before adding features.

Establish a running React page before adding product components.

1. Use the prepared frontend/ project, or scaffold the React template while online and install its dependencies.
2. Record node --version and the React/build-tool versions from the installed dependency tree.
3. Run npm run dev inside frontend/ and open the exact printed URL.
4. Replace the starting heading with EMIO24 and verify the browser updates.

**Check:** the page is served by your local project and compilation succeeds. JSX needs the React build pipeline; pasting it into a plain browser console is not a component setup test.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Build ProductCard - 10 points

**Where:** `frontend/src/ProductCard.jsx`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Implement the example in a separate file. Display name, whole-naira price and stock with semantic HTML; render Pen and Book with different props.

A card receives its information through props rather than hard-coded product text.

1. Create ProductCard.jsx exporting ProductCard({product}).
2. Return semantic article content with a heading for name and text for whole-naira price and stock.
3. Import it in App.jsx and render Pen 200/4 and Book 500/8 from different product props.
4. Change only Book's fixture stock to 9 and observe the cards.

**Check:** the cards differ according to props, and only Book's displayed stock changes. Do not mutate the supplied product inside rendering.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Render a list - 10 points

**Where:** `frontend/src/ProductList.jsx`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Create ProductList mapping products to cards with key={product.id}. Reorder the fixture and verify each card still represents the correct product.

Map product records to repeated components with stable identity.

1. Create ProductList receiving a products prop.
2. Use map to return ProductCard for each object, placing key={product.id} on the repeated element.
3. Render IDs 1/2/3, then reorder them and add a new unique ID.
4. Inspect the browser console and displayed order.

**Check:** one correct card per record, correct order and no missing-key warning. Array position is not a stable product identity when records can be reordered or inserted.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Handle no data - 10 points

**Where:** `frontend/src/ProductList.jsx`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Render a clear empty-inventory message when products.length is 0. Demonstrate both empty and populated inputs.

An empty shelf needs a deliberate message instead of a confusing blank area.

1. In ProductList check whether products.length is zero.
2. Render a clear message such as No products yet for empty input; otherwise render the cards.
3. In App test [] and then a one-product array by changing the supplied fixture.
4. Ensure the page heading remains available in both states.

**Check:** empty state contains no fake product card; populated state has no stale empty message. Undefined data is a separate loading/interface issue; this component's input contract is an array.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Compose the page - 10 points

**Where:** `frontend/src/App.jsx`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Create App with Header, ProductList and Footer. Show the component tree and identify which component owns the fixture data.

Compose the screen from parts with clear responsibilities.

1. Create Header and Footer components and import them into App alongside ProductList.
2. Keep fixture product ownership in App and pass products down.
3. Draw App → Header/ProductList/Footer, with ProductList → ProductCard, in answers.md.
4. Change the shop heading through the chosen Header prop and show all products still render.

**Check:** components are used as components, not pasted duplicate markup. The tree identifies who owns data and who displays it; no network request is required in this lesson.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Use conditional content - 10 points

**Where:** `frontend/src/ProductCard.jsx`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Show Out of stock at 0 and Low stock for 1 through 5. Demonstrate 0,1,5,6 and avoid rendering an accidental numeric 0 from an && expression.

Render stock messages at the exact decision boundaries.

1. Add conditional text in ProductCard: Out of stock at 0, Low stock from 1 through 5, and your ordinary availability presentation above 5.
2. Render four cards with stocks 0,1,5,6.
3. Inspect visible text and DOM for accidental numeric zero output from an expression such as stock && something.
4. Use explicit Boolean comparisons or conditional branches where needed.

**Check:** each boundary gets the intended message and no stray 0 appears as a condition's rendered result. Keep the actual stock count visible too if it is part of your card design.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Keep props read-only - 10 points

**Where:** `frontend/src/ProductCard.jsx and App.jsx`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Add an onSelect callback prop and invoke it from a labelled button. Show the parent receives the selected ID; do not mutate product inside the card.

A child reports an event; the parent decides what it means.

1. Add an onSelect callback prop and a labelled button to ProductCard.
2. When clicked, call onSelect with that product's ID.
3. In App provide a handler that logs or displays the selected ID without modifying the product object in the child.
4. Click Pen then Book.

**Check:** callbacks receive 1 then 2 with the fixture IDs, and product fields remain unchanged. Passing a function to onClick is different from calling it while the component renders.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new product-prop combination and an empty/reordered/boundary display case. Inspect rendered text, keys and callback arguments. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 34
python grade.py rubric --lesson 34
```

The first checks the JSON prediction and writes `grading/reports/lesson-34.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-34/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

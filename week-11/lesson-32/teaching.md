# Lesson 32: Modern JavaScript transformations

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 31; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

map sends every product card through a rewriting station; filter keeps selected cards; reduce combines cards into one summary. A spread copy duplicates the outer box, not every nested object.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Arrow function | A compact function expression with lexical this. | a short task instruction using its surrounding context. |
| Destructuring | Extracting values through a matching pattern. | unpacking labelled compartments. |
| Spread | Expanding iterable values or object properties. | emptying one outer box into another. |
| map | Creating an array from one result per input item. | rewriting every card. |
| reduce | Accumulating values into a result. | combining receipt lines into a total. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```javascript
const products = [{name:"Pen",stock:4},{name:"Book",stock:8}];
const names = products.filter(p => p.stock <= 4).map(p => p.name);
console.log(names);
```

filter selects the Pen object, then map extracts its name. Neither call changes the original array in this example, but the selected object references are shared. Copy the changed nested object too when making an immutable update.

**Prediction:** Enter the resulting names array.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Extract fields

Use object destructuring to read name and stock from a product, with a default category. Demonstrate missing category versus a present category.

### Step 2: Transform without mutation

Use map to add a displayLabel to copied products. Show original objects have no new displayLabel property.

### Step 3: Filter low stock

Implement lowStockNames(products,threshold) with filter/map. Check equality at 4, above threshold, and an empty array.

### Step 4: Reduce totals

Use reduce with initial value 0 to total price*stock. Test the 3500 fixture and empty input.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: filter selects the Pen object, then map extracts its name.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-32/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

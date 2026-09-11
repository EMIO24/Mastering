# Lesson 34: React components and props

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 33; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A component is a reusable display recipe; props are the ingredients handed to it. Rendering describes the screen from those ingredients. A component should not quietly rewrite the parent’s ingredients.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Component | A reusable unit describing UI. | the display recipe. |
| JSX | Syntax for describing elements inside JavaScript. | a structured display sketch. |
| Props | Inputs supplied to a component. | ingredients from the parent. |
| Render | Computing a UI description. | drawing the display from current ingredients. |
| Key | A stable identity hint for siblings in a list. | the permanent card number on repeated displays. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```javascript
export function ProductCard({product}) {
  return <article>
    <h2>{product.name}</h2>
    <p>{product.stock} units</p>
  </article>;
}
```

Use this in a React project with JSX tooling already installed. The component receives product through props and returns a description. Render lists with stable product IDs as keys; array indexes can misidentify items after insertions or reordering.

**Prediction:** With product={name:"Pen",stock:4}, enter the paragraph text.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Prepare React locally

Use your installed React project/toolchain and record package versions plus the local start command. Confirm the starting page renders before adding features.

### Step 2: Build ProductCard

Implement the example in a separate file. Display name, whole-naira price and stock with semantic HTML; render Pen and Book with different props.

### Step 3: Render a list

Create ProductList mapping products to cards with key={product.id}. Reorder the fixture and verify each card still represents the correct product.

### Step 4: Handle no data

Render a clear empty-inventory message when products.length is 0. Demonstrate both empty and populated inputs.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Use this in a React project with JSX tooling already installed.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-34/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

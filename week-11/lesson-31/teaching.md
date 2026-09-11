# Lesson 31: JavaScript fundamentals

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 30; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

JavaScript values and control flow resemble Python’s stockroom tools, but the labels and rules differ. const locks a name’s binding; it does not freeze the contents of the box.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Binding | An association between a name and a value. | a label pointing to a box. |
| const | A declaration whose binding cannot be reassigned. | a fixed label attachment. |
| let | A block-scoped reassignable declaration. | a label you may move within one room. |
| Object | A collection of properties. | a named product card. |
| Strict equality | Equality comparison without type coercion. | comparing labels without automatic conversion. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```javascript
const product = {name: "Pen", stock: 4};
product.stock += 2;
console.log(product.stock);
console.log("6" === 6);
```

The const binding still points to the same object, whose stock property changes to 6. Strict equality compares the string and number as different types. Run plain JavaScript in Node or a browser console; JSX comes later.

**Prediction:** Enter the two logged values as a JSON list.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Use declarations

In practice.js declare shopName with const and stock with let. Update stock, then demonstrate a caught reassignment error for a const binding in a separate example.

### Step 2: Convert input

Convert "200" and "3" to numbers and calculate 600. Check Number.isFinite after conversion and reject a nonnumeric value; explain why empty text needs an explicit rule.

### Step 3: Classify stock

Implement stockLabel(stock) returning out for 0, low for 1 through 5 and available above 5. Demonstrate 0,1,5,6.

### Step 4: Represent products

Create an array of three product objects with id, name, price and stock. Update only the second product and show all records before/after.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: The const binding still points to the same object, whose stock property changes to 6.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-31/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

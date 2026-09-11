# Lesson 5: Class behaviour

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 4; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

Instance data is a note on one product card; class data is a notice on the stockroom wall. A mutable shared notice can accidentally collect changes from every card.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Class attribute | A value stored on a class and found through attribute lookup. | a shared wall notice. |
| Instance attribute | A value stored on one instance. | a note on one card. |
| Property | Managed attribute access through methods. | a service window guarding a field. |
| classmethod | A method receiving the class as its first argument. | a factory that knows which card design to use. |
| __str__ | The method producing a human-readable string. | the label printed for a customer. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
class Product:
    currency = "NGN"
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name} ({self.currency})"

p = Product("Pen")
print(str(p))
```

currency is looked up on the class because p has no currency attribute of its own. __str__ returns text; print then displays that text. Use properties when assignments need validation, rather than adding getters for every field.

**Prediction:** Enter the exact text printed, without a newline.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Shared and separate data

Extend Product with class currency = "NGN" and per-instance stock. Change stock on one of two products; show the other is unchanged and both initially use NGN.

### Step 2: Display a product

Implement __str__ returning "Pen: 4 units" for name Pen and stock 4. Check zero stock and a different name. Keep printing outside the method.

### Step 3: Useful debugging text

Implement __repr__ including class name, name, price and stock. Show repr(product) and str(product), and explain which reader each helps.

### Step 4: Guard stock assignment

Use a stock property backed by _stock. Reject negatives, text, fractions and bool; allow 0. Attempt an invalid assignment and show the previous value remains intact.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: currency is looked up on the class because p has no currency attribute of its own.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-05/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

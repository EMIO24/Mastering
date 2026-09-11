# Lesson 4: Classes, objects and instances

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 3; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A product class is a blank stock card design; each object is a separately filled card. Changing one card does not change the others. Unlike paper, objects also expose behaviour through methods.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Class | A definition used to create objects. | the blank stock card design. |
| Instance | One object created from a class. | one filled card. |
| Attribute | A value associated with an object. | the stock field on a card. |
| Method | A function accessed through an object or class. | a stock-card operation. |
| self | The instance passed to an instance method. | the particular card being handled. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

pen = Product("Pen", 4)
book = Product("Book", 7)
pen.stock -= 1
print(pen.stock, book.stock)
```

`__init__` initializes a newly created instance. Each assignment to self stores data on that instance. The two calls to Product create different objects, so changing pen leaves book at 7. A second name assigned to pen would refer to the same object.

### Constructor: make a card, then fill it in

A **constructor** is the mechanism used to create and initialize an object. Think of ordering a new stock card: first obtain a blank card, then fill in its name and starting stock. In the example, `Product("Pen", 4)` starts that process.

For this ordinary Python class, the steps are:

1. **`__new__` creates the instance**: like making the blank card. Product inherits this behaviour; you do not need to write it for this lesson.
2. **`__init__` initializes that instance**: like filling the card. Python supplies the new object as `self`, while `"Pen"` and `4` become `name` and `stock`.
3. **The class call returns the object**, which is assigned to `pen`. The initializer itself must return `None`; normally you leave out a return statement.

People often call `__init__` the constructor. More precisely, it is the **initializer**: the object already exists when it runs. Do not call `pen.__init__(...)` to create a separate product; call `Product(...)` again.

**Try it:** add `print("Initializing", name)` inside `__init__`. Predict what prints when you create Pen and Book. Then set `alias = pen`: does that initialize another object? It does not; alias refers to the existing object.

**Prediction:** After the example runs, enter the two stocks as a JSON list, in pen/book order.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Create stock cards

In product.py implement Product(name, price, stock). Store all three attributes. Create Pen at 200/4 and Book at 500/7; show each attribute and prove the instances differ.

### Step 2: Calculate value

Add inventory_value(self) returning price * stock. Pen initially returns 800; a zero-stock product returns 0. Return a number rather than only printing.

### Step 3: Protect construction

Reject blank names and negative prices or stock with ValueError. Accept zero price and stock. Demonstrate a valid object and each rejected field.

### Step 4: Restock

Add restock(quantity), requiring a positive integer and rejecting bool. Starting at 4, adding 3 leaves 7; adding 0 or -1 raises ValueError and leaves 7.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: `__init__` initializes a newly created instance.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-04/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

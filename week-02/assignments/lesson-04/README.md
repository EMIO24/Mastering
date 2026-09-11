# Lesson 4 assignment: Classes, objects and instances

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A product class is a blank stock card design; each object is a separately filled card. Changing one card does not change the others. Unlike paper, objects also expose behaviour through methods.

Start a new product.py; you do not need the previous CLI. Create a Product class and use Pen (price 200, stock 4) and Book (price 500, stock 7). Price is whole naira per unit; stock is a count. Keep demonstration calls under a main guard.

## Where to work and how to run it

Work in `week-02/assignments/lesson-04/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

From this assignment folder run `python checks.py`. Create checks.py with imports and test calls for the files you build. Put demonstrations in modules under `if __name__ == "__main__":` so imports do not launch them.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `product.py` |
| 4 | `product.py` |
| 5 | `product.py` |
| 6 | `product.py` |
| 7 | `product.py` |
| 8 | `product.py` |
| 9 | `product.py` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Class** | A definition used to create objects. | the blank stock card design. |
| **Instance** | One object created from a class. | one filled card. |
| **Attribute** | A value associated with an object. | the stock field on a card. |
| **Method** | A function accessed through an object or class. | a stock-card operation. |
| **self** | The instance passed to an instance method. | the particular card being handled. |

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

**Question:** After the example runs, enter the two stocks as a JSON list, in pen/book order.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

`__init__` initializes a newly created instance. Each assignment to self stores data on that instance. The two calls to Product create different objects, so changing pen leaves book at 7. A second name assigned to pen would refer to the same object.

### Constructor: make a card, then fill it in

A **constructor** is the mechanism used to create and initialize an object. Think of ordering a new stock card: first obtain a blank card, then fill in its name and starting stock. In the example, `Product("Pen", 4)` starts that process.

For this ordinary Python class, the steps are:

1. **`__new__` creates the instance**: like making the blank card. Product inherits this behaviour; you do not need to write it for this lesson.
2. **`__init__` initializes that instance**: like filling the card. Python supplies the new object as `self`, while `"Pen"` and `4` become `name` and `stock`.
3. **The class call returns the object**, which is assigned to `pen`. The initializer itself must return `None`; normally you leave out a return statement.

People often call `__init__` the constructor. More precisely, it is the **initializer**: the object already exists when it runs. Do not call `pen.__init__(...)` to create a separate product; call `Product(...)` again.

**Try it:** add `print("Initializing", name)` inside `__init__`. Predict what prints when you create Pen and Book. Then set `alias = pen`: does that initialize another object? It does not; alias refers to the existing object.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Create stock cards - 10 points

**Where:** `product.py`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** In product.py implement Product(name, price, stock). Store all three attributes. Create Pen at 200/4 and Book at 500/7; show each attribute and prove the instances differ.

A class is a stock-card design. Calling it makes a particular card.

1. In product.py define `class Product` with `__init__(self, name, price, stock)`. Keep the supplied values on `self.name`, `self.price` and `self.stock`.
2. In checks.py import Product. Create `pen = Product("Pen", 200, 4)` and `book = Product("Book", 500, 7)`.
3. Print each object's three attributes, then print `pen is book`. `is` checks identity, not matching field values.

**Check:** Pen prints Pen/200/4; Book prints Book/500/7; identity prints `False`. `__init__` initializes the object and should not return the object. Python normally inherits `__new__`, which creates it.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Calculate value - 10 points

**Where:** `product.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Add inventory_value(self) returning price * stock. Pen initially returns 800; a zero-stock product returns 0. Return a number rather than only printing.

Inventory value means the selling value of all units still on one card.

1. Add `inventory_value(self)` inside Product, at the same indentation level as `__init__`.
2. Read this object's price and stock and return their product. Do not add a print inside the method.
3. Call it with parentheses: `print(pen.inventory_value())`.

| Fresh object | Required result |
| --- | --- |
| Pen, price 200, stock 4 | 800 |
| Book, price 500, stock 7 | 3500 |
| Bag, price 4000, stock 0 | 0 |

**Check:** changing a price in a new object changes its result. Forgetting parentheses gives you a method reference, not the computed total.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Protect construction - 10 points

**Where:** `product.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Reject blank names and negative prices or stock with ValueError. Accept zero price and stock. Demonstrate a valid object and each rejected field.

A stock card should not be issued with unusable starting values.

1. At the start of `__init__`, check the name is a string with non-whitespace content. Use `name.strip()` for this check.
2. Require numeric price and integer stock to be nonnegative. For this course use whole-naira integers for both and exclude bool.
3. Raise `ValueError` before assigning attributes when a rule fails. Normal successful initialization needs no return statement.
4. Wrap each invalid construction in `try/except ValueError` in checks.py so all cases can run.

**Check:** blank name, name containing only spaces, price -1 and stock -1 each reject. `Product("Gift", 0, 0)` succeeds. Record which input failed; do not turn a failed construction into a partially usable product.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Restock - 10 points

**Where:** `product.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Add restock(quantity), requiring a positive integer and rejecting bool. Starting at 4, adding 3 leaves 7; adding 0 or -1 raises ValueError and leaves 7.

Restocking adds a delivery to the existing card.

1. Add `restock(self, quantity)`. Its input is a positive integer count, not a new total stock.
2. Reject non-integers, Booleans and values at or below zero before changing the object.
3. Add an accepted quantity to `self.stock`. No specific return value is required; inspect the stock afterward.
4. Start Pen at stock 4, call `pen.restock(3)`, then try invalid calls on that same object.

| Action | Stock afterward |
| --- | --- |
| Restock 3 | 7 |
| Attempt 0, -1, 2.5 or True | Remains 7; each raises ValueError |

**Check:** you incremented stock rather than overwriting it with the delivery quantity.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Sell - 10 points

**Where:** `product.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Add sell(quantity). Require a positive integer no greater than stock; return the sale total. Selling 2 at 200 leaves stock 5 after the restock and returns 400. Overselling leaves stock unchanged.

Selling both changes stock and hands a numeric total back to the caller.

1. Add `sell(self, quantity)` with the same positive-integer rules as restock.
2. Also reject quantity greater than available stock. Check all rules before subtraction.
3. Subtract quantity and return price multiplied by quantity.
4. For the sequential check, create Pen stock 4, restock 3, then sell 2. For boundary checks, create fresh objects.

**Check:** the sequential sale returns 400 and leaves stock 5. Selling all 4 units of a fresh Pen returns 800 and leaves 0. Selling 5 from fresh stock 4 raises ValueError and leaves 4. Printing a receipt without returning the number does not meet the contract.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Show identity - 10 points

**Where:** `product.py`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Set alias = pen and change alias.stock. Record why pen changes too while book does not. Then create a separate Product with matching values and explain identity versus equal field values.

An alias is a second name pointing at the same card.

1. Create `pen = Product("Pen", 200, 4)`, then assign `alias = pen`.
2. Change `alias.stock` to 9 and print `pen.stock` and `alias is pen`.
3. Create `other = Product("Pen", 200, 9)` and print `other is pen`.
4. Explain why equal-looking field values do not imply the same object. Keep Book from Exercise 3 separate and inspect its stock too.

**Check:** pen stock is 9, alias identity is True, other identity is False, and Book stays 7. You did not call the constructor when creating the alias; assignment only added a name.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Build an object inventory - 10 points

**Where:** `product.py`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Store three Product objects in a list and total their values using the method. Include one zero-stock item. Print item names and total; calculate the same result by hand.

Build a shelf containing object cards rather than dictionaries.

1. Create a fresh list with Pen 200/4, Book 500/7 and Bag 4000/0.
2. Loop over the objects, print each name and its `inventory_value()` result, and add those results to an accumulator starting at zero.
3. Print the final total outside the loop. Repeat using an empty list.
4. In answers.md show the hand calculation and explain why calling the method lets each object provide its own value.

**Check:** rows have values 800, 3500, 0; total 4300. Empty inventory totals 0. Use `product.name`, not `product["name"]`, because these entries are objects.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose one object calculation and one rejected stock change. Use a new product/price/quantity, and inspect stock before and after rejection. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 4
python grade.py rubric --lesson 4
```

The first checks the JSON prediction and writes `grading/reports/lesson-04.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-04/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

# Lesson 2 assignment: make checkout recover from mistakes

**10 exercises · 100 points.** Build a terminal checkout that keeps running after ordinary input mistakes. All inventory is kept in memory in this lesson; restarting resets it. File storage comes in Lesson 3.

## Before you begin

Work in `week-01/assignments/lesson-02/`.

| File | What you write |
| --- | --- |
| `starter.py` | Complete its existing input, lookup, sale and main functions. Keep their names and signatures. |
| `checks.py` | Create this file for direct function checks. Start it with `from starter import find_product, sell_product, read_positive_integer`. |
| `debug-notes.md` | Create this text file for Exercises 8–10 and copied menu results. Use numbered exercise headings. |

An **exception** is a signal that interrupts normal execution, like a blocked route. `except ValueError` is a recovery route for a particular kind of problem. **Validation** checks the rules before accepting data, like inspecting an order form. **Mutation** changes an existing object; for this assignment, decreasing stock is a mutation.

The caller supplies inputs to a function. `return` hands back a result; `print` shows something in the terminal. `raise ValueError("message")` reports that an input violates a rule. A test can catch that exception without ending the whole program.

Use these records for direct tests. Recreate them before an independent sale test so earlier sales do not change its starting point:

```python
products = [
    {"id": 1, "name": "Pen", "price": 200, "stock": 20},
    {"id": 2, "name": "Notebook", "price": 500, "stock": 10},
]
```

Prices are whole naira per unit. Stock counts available units. IDs identify products; they are not list positions.

Run from the course root, the folder containing `grade.py`:

```powershell
python week-01/assignments/lesson-02/checks.py
python week-01/assignments/lesson-02/starter.py
```

The first runs your direct checks; the second runs the menu once you implement `main()`. Use `py` if that is your Windows launcher. Put interactive startup under the existing main guard so importing functions does not launch the menu.

## Exercise 1: Ask again when text cannot become an integer

**Where:** `read_positive_integer(prompt)` in `starter.py`. Exercises 1 and 2 together earn the automatic `input_retry` score, out of 15.

**Scenario:** a customer types `three` when the cashier asks for a quantity. The program should explain the problem and ask again, instead of crashing.

1. Use the supplied `prompt` string as the message passed to `input(...)`.
2. Inside a loop, read a response and attempt to convert it with `int(...)`.
3. Catch `ValueError` from failed conversion. Print a message such as `Enter a whole number.` and repeat the loop.
4. If conversion succeeds, continue to the positive-number check in Exercise 2. This helper should eventually return an integer, not text.
5. In `checks.py`, call `print(read_positive_integer("Quantity: "))`. At the terminal, enter `three`, then `2.5`, then ` 3 `.

**Expected:** the first two entries cause messages and another prompt. The last is accepted as integer `3`, even with surrounding spaces. A whole number has no fractional part; this task intentionally rejects the text `2.5`.

**Finished when:** the sequence reaches 3 without a traceback or program exit. Do not catch every exception with a bare `except`; this task handles conversion failures specifically.

## Exercise 2: Reject zero and negative quantities

**Where:** extend the same helper. This is the second half of the `input_retry` behaviour; helpful distinct messages additionally earn `input_messages`, out of 5. Exercises 1 and 2 therefore total 20 points together.

Converting text is only the first check. `int("0")` succeeds, but a checkout quantity of zero is not allowed.

1. After successful conversion, check whether the number is greater than zero.
2. If it is zero or negative, print a different message, such as `Quantity must be greater than zero.`, and ask again.
3. Return the integer only when it passes both conversion and range checks.
4. Run one call with this complete input sequence:

| Entry typed | Expected behaviour |
| --- | --- |
| `three` | Whole-number message; prompt again |
| `2.5` | Whole-number message; prompt again |
| `0` | Positive-number message; prompt again |
| `-2` | Positive-number message; prompt again |
| `3` | Return integer 3 and stop asking |

**Finished when:** the one call has four retries and returns 3. Copy the interaction to `debug-notes.md`. The conversion and range messages need to be distinguishable; their exact wording is your choice.

## Exercise 3: Find a product without changing it — 15 points

**Where:** `find_product(products, product_id)` in `starter.py`; calls in `checks.py`.

Think of looking for a stock card by its printed ID.

1. Visit records in the supplied list and compare each `"id"` with `product_id`.
2. Return the matching dictionary as soon as you find it.
3. If none matches, return `None`, not the string `"None"`.
4. Do not change the list or its records.

| Call using the fixture above | Expected result |
| --- | --- |
| `find_product(products, 1)` | Pen dictionary |
| `find_product(products, 2)` | Notebook dictionary |
| `find_product(products, 99)` | `None` |
| `find_product([], 1)` | `None` |

Wrap each call in `print(...)`, and print the fixture before and after checking it. **Finished when:** matching, missing and empty cases work and the records remain unchanged. Automatic criterion: `lookup`.

## Exercise 4: Complete an allowed sale — 10 points

**Where:** `sell_product(product, quantity)` in `starter.py`.

Here `product` is **one dictionary**, not the full inventory. `quantity` is how many units to sell. The function must return the sale total and reduce that dictionary's stock.

1. Start with a fresh Notebook record: `{"id": 2, "name": "Notebook", "price": 500, "stock": 10}`.
2. Implement the successful case: calculate unit price multiplied by quantity and reduce stock by quantity.
3. Return the numeric total; do not print a receipt inside this function.
4. In `checks.py`, run:

```python
product = {"id": 2, "name": "Notebook", "price": 500, "stock": 10}
print(sell_product(product, 3))  # Expected: 1500
print(product["stock"])        # Expected: 7
```

Then recreate the starting record and sell exactly 10 units. Expect total `5000` and stock `0`. Complete Exercise 5 before treating this function as finished: its failure rules must protect the successful logic. Automatic criterion: `sale_success`.

## Exercise 5: Reject bad sales before changing stock — 25 points

**Where:** add validation at the beginning of `sell_product`.

A cashier should check an order before crossing stock out of the ledger. Your function must do the same.

1. Require `quantity` to be an actual Python `int`, excluding `bool`. Python treats Booleans as a subtype of integers, so `isinstance(True, int)` alone does not enforce this rule. Use an explicit Boolean rejection or `type(quantity) is int`.
2. Require quantity greater than zero.
3. Require quantity no greater than the available stock.
4. On any violation, raise `ValueError` with a useful explanation. Perform all checks **before** decreasing stock.
5. Test each input below against a **fresh** product with stock 10.

| Quantity passed directly to the function | Expected result | Stock afterward |
| --- | --- | --- |
| `0` | `ValueError` | `10` |
| `-1` | `ValueError` | `10` |
| `11` | `ValueError` | `10` |
| `2.5` | `ValueError` | `10` |
| `"3"` | `ValueError` | `10` |
| `True` | `ValueError` | `10` |

These are Python values, not all typed responses to `input()`. The input helper converts valid user text; the sale function also needs to defend itself when called directly.

Use this checking pattern in `checks.py`, changing the quantity and recreating the product for each test:

```python
product = {"id": 2, "name": "Notebook", "price": 500, "stock": 10}
try:
    sell_product(product, 11)
except ValueError as error:
    print("Rejected:", error)
print(product["stock"])  # Must still be 10
```

**Finished when:** every bad value is rejected without mutation, and Exercise 4 still works. Automatic criterion: `sale_invalid`. Successful and rejected sales are required mastery checks; a high overall score cannot compensate for corrupted stock.

## Exercise 6: Build a repeating list/sell/quit menu

**Where:** `main()` in `starter.py`. Exercises 6 and 7 share `menu`, worth 15 points.

1. Keep the two-product fixture inside `main()` as the live inventory.
2. Repeatedly display:

```text
1. List products
2. Sell a product
3. Quit
```

3. Read the option with `input(...)` and compare the resulting string.
4. For `1`, display each product's ID, name, unit price and stock. For `3`, leave the loop and finish normally. Exercise 7 implements `2`.
5. For any other option, display a useful message and show the menu again.

**Check:** run `starter.py`; choose `1`, then `9`, then `1`, then `3`. Expect a product list, an invalid-option message, the same list and a clean exit. Use a loop, not calls to `main()` from inside itself.

## Exercise 7: Connect the sale functions to the menu

**Where:** the option `2` branch inside `main()`.

1. Ask for a positive product ID using your input helper.
2. Use `find_product` to locate the record. If it returns `None`, show `Product not found` and return to the menu without asking for quantity.
3. For a found record, ask for quantity with your input helper.
4. Call `sell_product` inside a `try` block. Catch its `ValueError`, display the message, and return to the menu. Do not report success after rejection.
5. After success, print a receipt showing product name, sold quantity, total and remaining stock.

**Check this journey from a fresh run:** list products; try ID 99; try to buy 11 Notebooks; buy 3 Notebooks; list again; quit. Expect the unknown-ID message, an oversale rejection with stock still 10, then total 1500 and Notebook stock 7. Pen stock stays 20.

**Finished when:** the program remains usable after each error. Copy the journey's actual terminal text to `debug-notes.md`. Exercises 6 and 7 together earn `menu`, out of 15; this is also a required mastery check.

## Exercise 8: Explain and fix a missing-key error — 5 points

**Where:** put this experiment in `checks.py`; write the cause and correction in `debug-notes.md`.

```python
record = {"name": "Pen"}
try:
    print(record["price"])
except KeyError as error:
    print(type(error).__name__, str(error))
```

1. Run it and record the exception name and missing key.
2. Explain that the card has no `price` field; this differs from a field whose value is zero.
3. Correct the example by supplying a price, or intentionally use `.get(...)` with a documented default if missing prices are allowed in your experiment.
4. Explain why your correction fits the rule you chose. Do not use a blanket exception handler to pretend all records are valid.

Marks: cause 2, appropriate correction 2, explanation 1. This contributes to `debug` with Exercises 9 and 10.

## Exercise 9: Trace try, except, else and finally — 5 points

**Where:** experiment in `checks.py`; trace in `debug-notes.md`.

1. Write a small conversion experiment using `int(raw)` inside `try`.
2. In `except ValueError`, print `conversion failed`.
3. In `else`, print `conversion succeeded`.
4. In `finally`, print `attempt finished`.
5. Run once with `raw = "3"` and once with `raw = "three"`. Use labels to separate the two runs.

| Input | Expected branch messages in order |
| --- | --- |
| `"3"` | `conversion succeeded`, `attempt finished` |
| `"three"` | `conversion failed`, `attempt finished` |

Explain that `else` runs after the try block completes without an exception; `finally` runs when leaving this try statement during ordinary execution or exception unwinding. It is like putting borrowed equipment away after either a successful job or a handled problem.

**Finished when:** both traces and explanations are saved. Marks: traces 2, else explanation 1, finally explanation 2. You do not need to force `else` and `finally` into the checkout if they have no purpose there.

## Exercise 10: Explain why validation comes first — 5 points

**Where:** `debug-notes.md`; use your sale function for evidence.

1. Make two independent tests, each starting with Notebook stock 10.
2. Reject quantity 11 in the first; sell quantity 3 in the second.
3. Record the actual stock before and after each operation. Expect `10 -> 10` for rejection and `10 -> 7` for success.
4. Explain what would go wrong if a function subtracted stock and only afterward noticed the order was invalid.
5. Point to the part of your implementation that validates before mutation. Compare it to inspecting an order before changing the stock ledger.

Marks: corruption risk explained 2, correct ordering shown 2, mapped analogy 1. Exercises 8–10 are combined once into the manual `debug` score, out of 15.

## Save, check and review

From the course root:

```powershell
python grade.py check --lesson 2
python grade.py rubric --lesson 2
```

The checker automatically tests helper functions: 65 points. Messages, menu behaviour and explanations need review: 35 points. **REVIEW PENDING** means those marks still need evidence-based review; it is not a program crash. See the [checker guide](../../../grading/README.md) to record manual scores. Exact message wording is flexible where not explicitly specified; the distinction and recovery behaviour matter.

- [ ] All ten exercises attempted and the actual menu journey saved.
- [ ] Direct helper checks cover good, bad and missing inputs.
- [ ] At least 80/100 after review, with valid sales, rejected-sale protection and menu behaviour all passing the required gates.

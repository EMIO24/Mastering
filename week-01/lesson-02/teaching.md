# Lesson 2 — Exceptions and defensive programming

**Goal:** Make the inventory program respond sensibly to mistakes without damaging its stock records.

**Time:** 35 minutes teaching, 25 minutes examples, 70–110 minutes assignment, 20 minutes explanation and review.

## 1. A shop assistant needs rules for unusual situations

You ask a customer how many notebooks they want. They answer "three", then -2, then 500 when you have only 10.

Those are different problems:

- `"three"` cannot be converted with `int()`.
- `-2` is an integer but violates the sale rule.
- `500` is a positive integer but exceeds stock.

Defensive programming means checking assumptions where information enters the program and before changing important data. It does not mean hiding every error.

## 2. Exceptions interrupt the normal route

```python
raw_quantity = "three"
try:
    quantity = int(raw_quantity)  # This raises ValueError
except ValueError:
    print("Enter a whole number, such as 3.")
else:
    # Only runs if the try block finished without an exception.
    print(f"You requested {quantity} items.")
finally:
    # Runs when leaving this try statement in ordinary execution,
    # whether the conversion succeeded or failed.
    print("Quantity check finished.")
```

Think of `try` as the normal checkout lane, `except` as the desk for a specific problem, `else` as the next step after successful checkout, and `finally` as tidying the counter afterward.

`finally` is mainly useful for cleanup, not for announcing success. It is not a guarantee against power loss or forced process termination. For files, `with` usually handles cleanup more clearly.

## 3. Catch only the problem you understand

| Exception | Example cause | Sensible next step |
| --- | --- | --- |
| `ValueError` | `int("two")` | Ask for a whole number |
| `TypeError` | `"200" + 3` | Fix incompatible types |
| `KeyError` | Missing dictionary key | Check the data contract or use deliberate optional lookup |
| `IndexError` | Access beyond a list's end | Check bounds or iterate directly |
| `ZeroDivisionError` | Dividing by zero | Define what a zero denominator means |
| `FileNotFoundError` | Opening a missing file for reading | Handle first-run behaviour if expected |

Avoid `except: pass` and broad `except Exception:` around your entire program. A mistyped variable is a programming bug; it should not turn into a misleading "bad quantity" message.

Keep `try` blocks small. You should know which operation is expected to raise the exception you catch.

## 4. Raise your own error when a business rule fails

```python
def sell_product(product, quantity):
    if type(quantity) is not int:
        # Exact type rejects True and False, which are int subclasses.
        raise ValueError("Quantity must be a whole number.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    if quantity > product["stock"]:
        raise ValueError("Not enough stock.")

    # All checks passed. Only now change the product.
    product["stock"] -= quantity
    return product["price"] * quantity
```

The function enforces the rule; the caller decides how to show the message. Later, a command-line message can become an HTTP error response without changing the basic rule.

Here we assume the product dictionary already has valid `price` and `stock` values. Lesson 3 validates that assumption when loading files.

**Check:** Why not subtract first and check later? The failure would already have changed stock. Validating first keeps rejected operations from leaving partial changes.

## 5. Retrying input is a loop, not recursion

```python
def read_positive_integer(prompt):
    while True:
        raw_value = input(prompt)
        try:
            value = int(raw_value)
        except ValueError:
            print("Enter a whole number.")
            continue  # Ask again; do not use an unassigned value

        if value <= 0:
            print("Enter a number greater than zero.")
            continue
        return value  # A valid value ends both the function and loop
```

`int("2.5")` fails; `int(" 3 ")` succeeds. Do not use `int(float(raw_value))` to silently turn a fractional sale into a different quantity.

## 6. Debugging is following a receipt trail

A traceback tells you how execution reached the failure. Read the final line first for the exception type and message, then locate the relevant file and line immediately above it. Earlier frames show the calls that led there.

```python
product = {"name": "Pen", "stock": 4}
print(product["stocks"])  # KeyError: 'stocks' — the key is singular
```

A useful debugging routine:

1. Reproduce the failure using the smallest input.
2. Read the exception and failing line.
3. Inspect relevant values and types with `print(repr(value), type(value))`.
4. State the wrong assumption: "I assumed this dictionary had a `stocks` key."
5. Fix the cause and rerun both the failing case and a successful case.

Do not catch this typo just to make the traceback disappear. Correct the key.

## Walkthrough and assignment

Run [examples.py](examples.py). It demonstrates successful conversion, failed conversion, a rejected sale, and a successful sale. Predict the stock after each attempt first.

Then complete [Assignment 2](../assignments/lesson-02/README.md).

Before moving on, explain aloud: "An exception signals a failure; a handler responds to a failure it understands; validation protects the program's assumptions."

## References and offline checking

- [Week 1 references](../references.md)
- [Offline assignment checker](../../grading/README.md)

## Terminology through everyday analogies

| Term | Precise meaning | Everyday analogy |
| --- | --- | --- |
| Exception | A signal interrupting normal execution. | an obstacle changing a planned route. |
| Handler | Code responding to a selected exception. | the recovery route for that obstacle. |
| Validation | Checking input against required rules. | a clerk inspecting a form before accepting it. |
| Traceback | The call chain leading to an exception. | a route map locating the obstacle. |
| State | The system information at a moment. | the current stock ledger. |

Read the [foundation glossary](../../glossary.md) for further terms and analogy limits. Then complete the [ten-exercise assignment](../assignments/lesson-02/README.md).

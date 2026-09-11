# Week 1 self-review guide

Open this after attempting the assignments. Use it to diagnose mistakes rather than replace your own implementation.

## Lesson 1 answer checks

### A. Expressions

| Expression | Result | Type |
| --- | --- | --- |
| `"250" * 2` | `"250250"` | `str` |
| `int("250") * 2` | `500` | `int` |
| `17 // 5` | `3` | `int` |
| `17 % 5` | `2` | `int` |
| `bool("")` | `False` | `bool` |

### B. Control flow

```python
def stock_label(stock):
    if stock == 0:
        return "out"
    if stock <= 5:
        return "low"
    return "available"

total = 0
for quantity in [3, -1, 0, 5, -2]:
    if quantity > 0:
        total += quantity
# total is 8
```

This function relies on the diagnostic's nonnegative-input assumption. Lesson 2 teaches rejecting invalid input explicitly.

### C. Collections

Your inventory should be a list containing separate dictionaries. Access the second product with `products[1]`. Update `products[1]["stock"]`; gather categories with a set and `add()`. A coordinate tuple might be `(6.45, 3.39)`.

A dictionary gives each field a meaningful name. A list holds multiple records in order. A set represents unique category values without promising their iteration order.

### D. Functions

See the commented [Lesson 1 examples](lesson-01/examples.py) for accumulation and filtering.

```python
def find_product(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None  # Only decide 'not found' after checking every record
```

If you put `return None` inside the loop, you may stop at the first nonmatching product. Try finding the second item to expose that bug.

### E. Debugging

Replace `print(price * quantity)` with `return price * quantity` when the caller needs the result. Print it at the call site.

Use `names.append("Notebook")` on its own. `append()` changes the existing list and returns `None`; assigning that return value back to `names` loses the list reference held by that name.

### After marking

Use the assignment's point breakdown, record scores, and target the weak sections. On a retry, use new product values and calculate expected results by hand before running your code.

## Lesson 2 review prompts

- Is the conversion the only operation inside its `try` block?
- Does a rejected sale leave stock exactly as it was?
- Does a direct call with zero, negative, excessive, fractional, or Boolean quantity fail before mutation?
- Can you explain why a typo should be fixed instead of hidden in a broad exception handler?
- Does the menu keep working after two bad inputs in a row?

`else` runs when the `try` block completes without an exception. `finally` runs on leaving the statement in ordinary execution, including after handled or unhandled exceptions and returns. It is not a success branch.

## Lesson 3 review prompts

- Is the file path anchored to the script rather than the terminal location?
- Does your loader return an empty list only for the defined missing-file case?
- Are list shape, field types, ranges, and ID uniqueness checked after parsing?
- Are all changes made on copied product dictionaries before saving?
- Does an exception from saving prevent both success output and the in-memory commit?
- Is the main JSON file replaced only after writing the temporary file finishes?
- Does the CSV export select the four required fields if a loaded product has extra keys?

Frequent bug: `candidate = products.copy()` only copies the outer list. The dictionaries are still shared. For this week's flat product records, use `[product.copy() for product in products]`. Nested mutable fields would require additional copying or a different update design.

The final project intentionally remains an assignment. A working demonstration and your explanation are the evidence of mastery.

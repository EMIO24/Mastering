# Lesson 1 — Python fundamentals graduation test

**Goal:** Find the parts of Python you can use independently and repair specific gaps. This is a diagnostic, not a reason to repeat every beginner topic.

**Time:** 15 minutes preparation, 75 minutes diagnostic, 30 minutes marking, then 30–90 minutes targeted repair.

Start with the [diagnostic assignment](../assignments/lesson-01/README.md). Read the explanations below after your first attempt.

## 1. Variables and types: labels on stockroom shelves

A variable name is like a shelf label: it helps you refer to something. More precisely, Python names refer to objects; assigning a name does not necessarily copy an object.

```python
product_name = "Notebook"  # str: text, even if text contains digits
stock = 12                 # int: a whole number
weight_kg = 0.25           # float: a fractional measurement
is_available = stock > 0   # bool: True or False
supplier = None            # No supplier has been recorded yet

price = "500"              # Text received from a form or input()
total = int(price) * 3     # Convert before doing arithmetic
print(total)               # 1500
```

`"500" * 3` repeats text. `500 * 3` multiplies numbers. A value's type determines which operations make sense. `input()` always returns a string; conversion can fail, which Lesson 2 handles.

**Check:** Why is `bool("False")` true? A nonempty string is truthy; its spelling is not interpreted as a Boolean value.

## 2. Operators and conditions: the shop's decision rules

```python
items = 17
box_size = 5
print(items / box_size)   # 3.4: ordinary division
print(items // box_size)  # 3: whole boxes for these positive integers
print(items % box_size)   # 2: items left over

stock = 3
requested = 4
if requested <= 0:
    print("Quantity must be positive")
elif requested > stock:
    print("Not enough stock")
else:
    print("Sale allowed")
```

`=` assigns; `==` compares. `and` requires both conditions to hold; `or` requires at least one; `not` reverses truth. Python's `//` floors toward negative infinity, so do not generalize the positive-box analogy to negative numbers.

Conditions are checked in order. Put invalid cases before the successful action so that a bad request never reaches a stock update.

**Check:** What changes when `requested` equals `stock`? The sale is allowed and leaves zero stock.

## 3. Collections: choose the right shop record

| Python structure | Shop analogy | Useful property |
| --- | --- | --- |
| List | A shopping list | Ordered, mutable, allows duplicates |
| Tuple | A fixed coordinate pair | Ordered, immutable sequence |
| Dictionary | A product card with named fields | Access values using unique keys |
| Set | A collection of unique categories | Removes duplicates; no dependable display order |

```python
shopping_list = ["pen", "book", "pen"]
shop_location = (6.45, 3.39)
product = {"id": 1, "name": "Pen", "price": 200, "stock": 10}
categories = {"stationery", "stationery", "food"}

print(product["name"])           # Pen; missing keys raise KeyError
print(product.get("supplier"))  # None; the key is absent
product["stock"] -= 2           # Update the dictionary's stock value
shopping_list.append("eraser")  # Append mutates a list; it returns None
```

A tuple cannot have its elements reassigned, but a mutable object inside a tuple may still change. A dictionary is not automatically a database: its contents disappear when the process ends unless you save them.

## 4. Loops and nested data: visit each product card

```python
products = [
    {"id": 1, "name": "Pen", "price": 200, "stock": 10},
    {"id": 2, "name": "Notebook", "price": 500, "stock": 3},
]

inventory_value = 0
for product in products:
    # Multiply each unit price by its stock, then accumulate.
    inventory_value += product["price"] * product["stock"]

print(inventory_value)  # 3500
print(products[1]["name"])  # Notebook: second list item, then its name
```

The loop variable refers to each dictionary in turn. Updating `product["stock"]` inside this loop changes that dictionary in `products` too.

A `for` loop visits a collection. A `while` loop repeats while a condition stays true, which suits a menu waiting for the user to quit. `break` exits the nearest loop; `continue` skips to its next iteration. `range(3)` produces 0, 1, 2, excluding 3.

**Check:** What should an inventory total return for an empty list? Zero. Initializing the accumulator before the loop makes that case work naturally.

## 5. Functions: a reusable service counter

Imagine a counter where you hand over product records and receive a total. The inputs are parameters; the returned result can be used elsewhere.

```python
def calculate_inventory_value(products):
    total = 0
    for product in products:
        total += product["price"] * product["stock"]
    return total  # Give the caller a value; do not just display it

amount = calculate_inventory_value(products)
print(f"Inventory value: NGN {amount}")
```

`print()` shows a value to a person. `return` sends a value to the caller and ends the function. A function that reaches its end without `return` returns `None`.

Keep calculations separate from prompts. A function that accepts data and returns an answer is easier to reuse later in a Django view or API.

## 6. Problem solving: rehearse with three product cards

Before coding, write down:

1. **Input:** What do I receive? A list of product dictionaries.
2. **Output:** What should I produce? Perhaps a list of low-stock names.
3. **Rule:** Does low stock mean `< 5` or `<= 5`? Define the boundary.
4. **Examples:** Try zero products, one at the boundary, and one above it.
5. **Steps:** Visit each product, check its stock, append matching names, return the list.

This is useful programming work even before you type Python.

## Targeted repair

| Weakness | Practice before retrying |
| --- | --- |
| Types/operators | Predict five mixed string/integer expressions, then explain the results |
| Conditions/loops | Trace stocks 0, 4, 5, 6 against a threshold of 5 |
| Collections | Model three products and list their unique categories |
| Functions | Rewrite a print-only calculation to return a value |
| Nested data/problem solving | Calculate total value by hand, then implement it for an empty list too |

Run [examples.py](examples.py) after attempting the diagnostic. Change the data and predict the new outputs before running again.

## References and offline checking

- [Week 1 references](../references.md)
- [Offline assignment checker](../../grading/README.md)

## Terminology through everyday analogies

| Term | Precise meaning | Everyday analogy |
| --- | --- | --- |
| Variable | A named reference to an object. | a shelf label, not a box containing a copied object. |
| Type | A classification determining valid operations. | handling rules for a container. |
| Loop | Repeated execution over data or a condition. | visiting each stock card. |
| Function | A callable operation that can return a result. | a service counter handing back an answer. |
| Mutation | Changing an existing object. | editing the same card. |

Read the [foundation glossary](../../glossary.md) for further terms and analogy limits. Then complete the [ten-exercise assignment](../assignments/lesson-01/README.md).

# Lesson 1 assignment: practise Python with a small shop inventory

**10 exercises · 100 points.** Work through the exercises in order. You are helping a shopkeeper keep track of products, stock and prices. You do not need to build a menu, accept keyboard input or save files in this lesson.

## Before you begin

Keep these files in `week-01/assignments/lesson-01/`:

| File | What to put there |
| --- | --- |
| `starter.py` | Complete the four existing functions for Exercises 2, 6, 7 and 8. Add test calls at the bottom, inside the existing `if __name__ == "__main__":` block. |
| `practice.py` | Create this file for Exercises 1, 3, 4, 5, 9 and 10. Separate your work with comments such as `# Exercise 3`. |
| `answers.md` | Create this text file for predictions, explanations and copied results. Use headings `## Exercise 1` through `## Exercise 10`. You can write ordinary sentences below each heading. |

A **function** is a reusable operation, like a shop counter offering a service. Its **parameter** is an input name, such as `stock`. Calling `stock_label(5)` supplies the **argument** `5`. A **return value** is the answer handed back to the caller. `print(...)` displays that answer in the terminal.

`pass` is a placeholder that does nothing. Replace it with your code, keeping the existing function names. Indent the function body by four spaces. Put test calls under the existing main block so importing the file for grading does not run your experiments.

Open a terminal in the **course root**: the `My-path` folder containing `grade.py`. Run a saved file with:

```powershell
python week-01/assignments/lesson-01/practice.py
python week-01/assignments/lesson-01/starter.py
```

On Windows, replace `python` with `py` if that is your installed launcher. If a function still contains `pass`, a test may print `None`; that means it has not returned a useful answer yet.

Try each task before looking up a solution. The [lesson notes](../../lesson-01/teaching.md) are available if you need a refresher; the requirements for these exercises are all written below.

## Exercise 1: Predict values and types — 20 points

**Where:** predictions in `answers.md`; experiments in `practice.py`.

**What this means:** a value is the actual information, such as `12`. Its **type** tells Python how to treat it. Think of a number and a written price label: they may look similar, but you calculate with the number. `str` means text, `int` means a whole number, and `bool` means `True` or `False`.

1. Copy this table into your Exercise 1 answer section.
2. Before running code, fill in the result you think each expression produces and its type. Include quotes when showing a text result.
3. In `practice.py`, use `print(expression)` and `print(type(expression))` to check each prediction. Replace the word `expression` with the actual expression from the table.
4. Record what actually happened beside your prediction. If you were wrong, keep the original prediction and explain the correction.

| Expression | My predicted result | My predicted type | Actual result and type |
| --- | --- | --- | --- |
| `"250" * 2` | Fill in | Fill in | Fill in after running |
| `int("250") * 2` | Fill in | Fill in | Fill in after running |
| `17 // 5` | Fill in | Fill in | Fill in after running |
| `17 % 5` | Fill in | Fill in | Fill in after running |
| `bool("")` | Fill in | Fill in | Fill in after running |

Here is how to check a **different** expression:

```python
print(9 + 2)        # Displays 11
print(type(9 + 2))  # Displays <class 'int'>
```

`int(...)` attempts to convert a value to a whole number. With positive integers, `//` counts whole groups and `%` gives the remainder. `bool(...)` asks whether the value is truthy. Add a sentence comparing types to different kinds of shop labels or containers; explain that a Python variable is a name referring to an object.

**Finished when:** all five rows contain predictions and checked results. For diagnostic scoring, mark the original predictions: 2 points for each correct value and 2 for each correct type. Record corrected understanding separately. Manual criterion: `types`.

## Exercise 2: Return a label for a stock quantity — 10 points

**Where:** the existing `stock_label(stock)` function in `starter.py`.

**Scenario:** the shop wants a short label showing whether an item is unavailable, running low or well stocked. `stock` means how many units of one product are left. For this exercise it is always a whole number of zero or more.

1. Find `def stock_label(stock):`.
2. Replace its `pass` with decision logic using `if`, `elif` and/or `else`.
3. Return one of the exact strings below. The quotes matter in your Python code: `"out"` is text, while an unquoted `out` would be treated as a variable name.
4. Do not use `input()` here. The caller already supplies the stock number.
5. Add the test calls below inside the main block and run `starter.py`.

| Input | Required return value | Reason |
| --- | --- | --- |
| `0` | `"out"` | Nothing is left. |
| `1` | `"low"` | Between 1 and 5 units remain. |
| `5` | `"low"` | 5 is included in the low range. |
| `6` | `"available"` | More than 5 units remain. |

```python
# Place these under the existing main block, indented four spaces.
print(stock_label(0))
print(stock_label(1))
print(stock_label(5))
print(stock_label(6))
```

Expected terminal lines, in order:

```text
out
low
low
available
```

Use `return` inside the function; use `print` around the calls to see the result. This is like a counter handing back a label, then someone showing it to the shopkeeper.

**Finished when:** all four calls match and the function works for other nonnegative integers. Automatic marks: zero case 3, low range 4, above-five case 3 (`stock_zero`, `stock_low`, `stock_available`).

## Exercise 3: Add only the positive quantities — 10 points

**Where:** `practice.py`; explanation in `answers.md`.

**Scenario:** a rough quantity list includes positive numbers, zero and negative corrections. For this exercise, add **only values greater than zero**. Ignore both zero and negative values.

Start with:

```python
quantities = [3, -1, 0, 5, -2]
positive_total = 0
# Write your loop here, then print positive_total.
```

1. Use a `for` loop to visit each number in `quantities`.
2. Inside the loop, check whether the current number is greater than zero.
3. Add it to `positive_total` only if it passes that check.
4. Print the total **after** the loop has finished.
5. Change only the input list and rerun for every row below.

| Input list | Expected total |
| --- | --- |
| `[3, -1, 0, 5, -2]` | `8`, because only 3 and 5 count |
| `[]` | `0`, because there are no numbers |
| `[0, -2]` | `0`, because neither number is positive |
| `[2, 4, 1]` | `7` |

An **accumulator** is a variable holding a running total, like a cashier adding accepted amounts to a receipt. Do not write `positive_total = 8` as your solution: the same loop must handle all the lists.

**Finished when:** the loop gives the four totals, and you explain why the accumulator starts at zero. Manual marks: loop 3, positive check 3, accumulation/result 4 (`positive_loop`).

## Exercise 4: Create product records and update one — 10 points

**Where:** `practice.py`. Keep this data for Exercise 5.

A **dictionary** stores named fields, like a product card with boxes labelled name, price and stock. A **list** keeps several cards together. Create a list named `catalogue` containing these two product dictionaries:

| Field | First product | Second product |
| --- | --- | --- |
| `id` | `1` | `2` |
| `name` | `"Pen"` | `"Notebook"` |
| `price` | `200` | `500` |
| `stock` | `10` | `3` |
| `category` | `"Stationery"` | `"Stationery"` |

`price` is the price of **one unit**, in whole naira. `stock` is the number of units. `id` is a unique product number; it is not the list position.

1. Write both dictionaries yourself using the exact field names above, and put them inside one list.
2. Print the list before changing it.
3. Update the second product's `stock` from `3` to `8` by accessing it through the list. Python list positions start at zero, so the second product is at index `1`.
4. Print the list again. Check the first product still has stock `10` and the second now has `8`.

A different record illustrates field access: if `record = {"colour": "blue"}`, then `record["colour"]` reads that field. Use the same idea on the selected product dictionary.

**Finished when:** the list contains both complete records, and only the second stock field changes. Manual marks: outer list 2, two dictionaries 2, required fields 2, targeted update 4. These 10 points are combined with Exercise 5 under `collections`.

## Exercise 5: Use a set and a tuple — 10 points

**Where:** continue in `practice.py`; explanations in `answers.md`.

A **set** keeps unique values, like a guest register listing each guest once. A **tuple** is a sequence whose entries cannot be reassigned, like a fixed pair of coordinates.

1. Use the `catalogue` from Exercise 4. Read each product's category and collect the categories into a set named `unique_categories`. You may use a loop and `.add(...)` or a set comprehension.
2. Print the set. Both products have the same category, so it must contain only `"Stationery"`. Do not simply hard-code a set containing that word; derive it from the records.
3. Create `shop_location` as a tuple containing latitude `6.5` followed by longitude `3.4`. These are practice coordinates. Print it; expect `(6.5, 3.4)`.
4. In `answers.md`, write two sentences: why named dictionary fields suit one product, and why a list suits a collection of products.

**Finished when:** categories are derived from the records without duplicates, the coordinates are a tuple, and both explanations are present. Set display order is not graded. Marks: set 4, tuple 2, explanations 4. Exercises 4 and 5 together are recorded once as `collections`, out of 20.

## Exercise 6: Calculate the value of all remaining stock — 10 points

**Where:** the existing `inventory_value(products)` function in `starter.py`.

**Scenario:** the shopkeeper asks how much the remaining inventory is worth at the recorded prices. For each product, multiply its unit price by its stock, then add those values.

Use this **separate fixture** for Exercises 6–8. A fixture is a known set of practice data, like arranging a sample shelf before testing. It already appears in the main block of `starter.py`; do not use the modified `catalogue` from Exercise 4.

```python
products = [
    {"id": 1, "name": "Pen", "price": 200, "stock": 10},
    {"id": 2, "name": "Notebook", "price": 500, "stock": 3},
    {"id": 3, "name": "Bag", "price": 4000, "stock": 0},
]
```

1. The `products` parameter receives a list of dictionaries in this shape.
2. Visit each product and calculate `price × stock` using its fields.
3. Add the product values and return the numeric total. Do not modify any records.
4. If the list is empty, return `0`.
5. Under the main block add `print(inventory_value(products))` and `print(inventory_value([]))`.

| Check | Expected value |
| --- | --- |
| Pen | `200 × 10 = 2000` |
| Notebook | `500 × 3 = 1500` |
| Bag | `4000 × 0 = 0` |
| Complete fixture | `3500` |
| Empty list | `0` |

**Finished when:** the two calls print `3500` and `0`, and changing an input price changes the calculation appropriately. Automatic marks: nonempty calculations 8, empty case 2 (`inventory_total`, `inventory_empty`).

## Exercise 7: Return the names of low-stock products — 10 points

**Where:** `low_stock_names(products, threshold)` in `starter.py`. Use the Exercise 6 fixture.

A **threshold** is a chosen cutoff. Think of a shop rule: “Tell me which products have at most 3 units left.” Here `threshold` is the `3`; “at most” means less than **or equal to** it.

1. Start with an empty result list inside the function.
2. Visit the product dictionaries in their original order.
3. For each product whose stock is less than or equal to `threshold`, add its **name** to the result.
4. Return the list of names, not the full product dictionaries. Keep zero-stock products if they meet the cutoff.
5. Run all the calls below from the main block.

| Call | Required return value |
| --- | --- |
| `low_stock_names(products, 3)` | `["Notebook", "Bag"]` |
| `low_stock_names(products, 0)` | `["Bag"]` |
| `low_stock_names(products, 10)` | `["Pen", "Notebook", "Bag"]` |
| `low_stock_names([], 3)` | `[]` |

Wrap a call in `print(...)` to see it. Python may display strings with single quotes; that is fine. What matters is the same names in the same order.

**Finished when:** all four results match, including stock exactly equal to the threshold. Automatic marks: selection/order 8, empty case 2 (`low_stock`, `low_empty`).

## Exercise 8: Find a product by its ID — 10 points

**Where:** `find_product(products, product_id)` in `starter.py`. Use the Exercise 6 fixture.

An **ID** is a product's identifying number, like the number printed on its stock card. It is not a list index. `product_id` is the number the caller wants to find.

1. Visit each product in the supplied list.
2. Compare its `"id"` field with `product_id`.
3. If they match, return that whole product dictionary.
4. If the search finishes without a match, return `None`, Python's explicit “no result” value. Do not return the string `"None"`.
5. Do not remove records or change any field while searching.

| Call | Required return value |
| --- | --- |
| `find_product(products, 1)` | The Pen dictionary |
| `find_product(products, 2)` | `{"id": 2, "name": "Notebook", "price": 500, "stock": 3}` |
| `find_product(products, 3)` | The Bag dictionary |
| `find_product(products, 99)` | `None` |
| `find_product([], 1)` | `None` |

Print the products before and after these calls; they should be unchanged. Also try a one-record list whose product has ID `42`; a search for `42` should work even though the list has only one position.

**Finished when:** found, missing and empty cases behave as specified, without changing the inventory. Automatic marks: matches 5, missing/empty 3, unchanged data 2 (`find_match`, `find_missing`, `find_unchanged`).

## Exercise 9: Repair a function that only prints — 5 points

**Where:** copy this deliberately faulty example into `practice.py`; write your explanation in `answers.md`.

```python
def total(price, quantity):
    print(price * quantity)

answer = total(200, 3)
print(answer)
```

1. Run the example unchanged. You should see `600`, followed by `None`.
2. Explain why the function can display `600` while `answer` receives `None`. Think of a cashier announcing a total but handing back no receipt.
3. Change the function so it **returns** the calculation to the caller. Keep `answer = total(200, 3)` and `print(answer)`.
4. Run again. Now this example should print just `600` once.
5. Change the call to `total(50, 4)` and check it produces `200`; do not hard-code 600 in the function.

**Finished when:** both inputs work, and your explanation distinguishes printing from returning. Marks: cause 2, correction 2, explanation 1. Combine with Exercise 10 under `debug`.

## Exercise 10: Repair an incorrectly assigned list update — 5 points

**Where:** `practice.py`; explanation in `answers.md`.

Copy and run this deliberately faulty example:

```python
names = ["Pen"]
names = names.append("Notebook")
print(names)
```

1. Record the output: `None`.
2. Explain what `.append(...)` does. It changes the existing list, like writing an extra item onto the same shopping list, and returns `None`.
3. Correct the code so `names` still refers to the list after Notebook is added.
4. Run the corrected example. The list must contain Pen followed by Notebook: `["Pen", "Notebook"]`.
5. Explain why assigning the result of `.append(...)` back to `names` loses the list reference held by that name.

**Finished when:** both names remain in the list and the cause is explained. Marks: cause 2, correction 2, explanation 1. Exercises 9 and 10 together are reviewed once as `debug`, out of 10.

## Save and check your work

Save all three files, then run from the course root:

```powershell
python grade.py check --lesson 1
python grade.py rubric --lesson 1
```

The first command runs the supported function checks and creates [your local report](../../../grading/reports/lesson-01.md). The second lists the marking criteria. A **criterion** is one part of the marking scheme; names such as `stock_low` identify those parts, not extra tasks for you to implement.

Exercises 2, 6, 7 and 8 are automatically checked: 40 points. Exercises 1, 3, 4, 5, 9 and 10 need review: 60 points. **REVIEW PENDING** means a person must review those parts; it does not mean every exercise failed. See the [checker guide](../../../grading/README.md) for recording evidence-based manual scores.

For every written answer, distinguish what you predicted from what you actually observed. You do not need screenshots: copied terminal output and a short explanation are enough.

- [ ] All ten exercises attempted; code and written answers saved.
- [ ] All specified test cases run and actual results recorded.
- [ ] Automatic failures corrected and manual work reviewed.
- [ ] At least 80/100 overall and at least half of each diagnostic section: types 10/20, conditions/loop 10/20, collections 10/20, functions 15/30, debugging 5/10.

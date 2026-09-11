# Assignment 1 — Fundamentals diagnostic

**Time:** 75 minutes. **Total:** 100 points.

Use [starter.py](starter.py) for code and create `answers.md` here for written answers. Do the first attempt without the teaching notes, example solutions, or AI-generated answers. Running your own code is allowed after you write your output predictions. Record any help you use; this is a diagnostic, not a competition.

## A. Types and operators — 20 points

Predict the exact result and its type for each expression. Award 2 points for the value and 2 for the type.

```python
"250" * 2
int("250") * 2
17 // 5
17 % 5
bool("")
```

## B. Conditions and loops — 20 points

1. Write `stock_label(stock)` returning `"out"` for 0, `"low"` for 1–5, and `"available"` above 5. Assume nonnegative integer input. **10 points:** correct 0 case (3), 1–5 including 5 (4), above 5 (3).
2. Use a loop to sum only positive quantities in `[3, -1, 0, 5, -2]`. Expected total: **8**. Do not hard-code the result. **10 points:** iteration (3), positive check (3), accumulator and correct total (4).

## C. Collections — 20 points

1. Create a list of two product dictionaries with `id`, `name`, `price`, `stock`, and `category`. **6 points:** outer list (2), two dictionaries (2), required keys (2).
2. Update the second product's stock through the list. **4 points.**
3. Collect unique categories in a set. **4 points.**
4. Represent a shop's latitude/longitude as a tuple. **2 points.**
5. Explain one reason to use a dictionary for a product and a list for an inventory. **4 points.**

## D. Functions and nested data — 30 points

Use this exact dataset for your first check:

```python
products = [
    {"id": 1, "name": "Pen", "price": 200, "stock": 10},
    {"id": 2, "name": "Notebook", "price": 500, "stock": 3},
    {"id": 3, "name": "Bag", "price": 4000, "stock": 0},
]
```

Implement:

- `inventory_value(products)` → **3500**; returns **0** for `[]`. **10 points:** calculation (6), return (2), empty case (2).
- `low_stock_names(products, threshold)` → **["Notebook", "Bag"]** for threshold 3; returns `[]` for empty input. Use `<=`. **10 points:** filtering including equality (5), names in original order (3), empty case (2).
- `find_product(products, product_id)` → matching dictionary for ID 2; `None` for ID 99 or an empty list. **10 points:** matching record (5), missing/empty cases (3), does not change data (2).

## E. Explain and debug — 10 points

Explain and fix both problems. Each is worth 5 points: cause (2), correction (2), clear explanation (1).

```python
def total(price, quantity):
    print(price * quantity)

answer = total(200, 3)
print(answer)  # Why does this print None after 600?
```

```python
names = ["Pen"]
names = names.append("Notebook")
print(names)  # Why is this no longer a list?
```

## Completion checklist

- [ ] Saved code and written answers.
- [ ] Tried each function with the supplied examples and empty input.
- [ ] Opened the [review guide](../../review-guide.md) only after attempting the work.
- [ ] Recorded scores by section in `../progress.md`.
- [ ] Reached 80/100 and at least half the marks in every section.
- [ ] If below the threshold, practised weak areas and repeated them with changed product data.

The score guides review. Passing does not mean you must memorize every Python feature before Lesson 2.

## Offline grading

Run from the course root:

```powershell
python grade.py check --lesson 1
python grade.py rubric --lesson 1
```

See the [checker guide](../../../grading/README.md). Scores and evidence are stored locally. Automated checks cover functions; written work and demonstrations require manual review.

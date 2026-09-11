# Assignment 2 — A checkout that handles mistakes

**Deliverables:** completed `starter.py`, a short `debug-notes.md`, and evidence in `../progress.md`.

Use the starter's in-memory products. Persistence belongs to Lesson 3.

## Part A — Validate input

Implement `read_positive_integer(prompt)`. Repeatedly ask until the user enters an integer greater than zero. Show distinct messages for a failed integer conversion and a value of zero or less.

## Part B — Protect stock

Implement `find_product(products, product_id)` and `sell_product(product, quantity)`.

- A missing product returns `None` from the lookup.
- Selling requires an actual positive integer quantity; reject Boolean values too.
- Reject quantities greater than available stock using `raise ValueError(...)`.
- A rejected sale must not change stock.
- A successful sale reduces stock and returns its total price in whole naira.
- The sale function must also reject invalid direct calls, even when the input helper normally prevents them.

## Part C — Build the interaction

Repeat a menu: `1. List products`, `2. Sell`, `3. Quit`.

For a sale, ask for a product ID, look it up, then ask for quantity. Report an unknown product and return to the menu. Catch sale validation errors where the menu calls the sale function. Print a receipt only after success.

No bare `except`, swallowed errors, or recursive calls to restart the menu.

## Part D — Debug and explain

In `debug-notes.md`:

1. Show a small `KeyError` you encountered or deliberately reproduced, its cause, and the corrected code.
2. Explain when `else` and `finally` run. You need not force them into the menu if they serve no purpose there.
3. Explain why validation happens before the stock update.

## Acceptance cases

Start each independent sale case with Notebook stock 10 and price 500.

| Input/action | Expected behaviour |
| --- | --- |
| Quantity `three` or `2.5` | Ask again; whole-number message |
| Quantity `0` or `-2` | Ask again; positive-number message |
| Quantity ` 3 ` | Accepted; total 1500; stock 7 |
| Quantity `11` | Rejected; stock remains 10 |
| Quantity `10` | Accepted; stock becomes 0 |
| Sell 1 after stock reaches 0 | Rejected; stock stays 0 |
| Product ID 99 | Product not found; menu continues |
| Call sale function with `True` | Raises ValueError; stock unchanged |
| Unknown menu option | Helpful message; menu continues |

## Checklist and rubric — 100 points

- [ ] Input retries and useful messages — 20
- [ ] Lookup and unknown-product handling — 15
- [ ] Sale rules, correct total, and unchanged stock on failure — 35
- [ ] Working menu and quit option — 15
- [ ] Debug notes and specific exception handling — 15

Aim for 80/100, with every stock-protection case passing before proceeding.

## Offline grading

Run from the course root:

```powershell
python grade.py check --lesson 2
python grade.py rubric --lesson 2
```

See the [checker guide](../../../grading/README.md). Scores and evidence are stored locally. Automated checks cover functions; written work and demonstrations require manual review.

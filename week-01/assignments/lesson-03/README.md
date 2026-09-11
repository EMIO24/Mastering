# Lesson 3 assignment: keep inventory after the program closes

**10 exercises · 100 points.** Extend the shop into a terminal program that loads its inventory, accepts changes and saves them. A restart must not erase successful additions or sales.

## Before you begin

Work in `week-01/assignments/lesson-03/`:

| File | Purpose |
| --- | --- |
| `starter.py` | Complete the existing validation, loading, saving, input, lookup, export and main functions. Preserve their signatures. |
| `file_drills.py` | Create this for Exercises 1–3. Use a separate `drill-data/` directory for these experiments. |
| `checks.py` | Create this for direct function calls. Import the functions you are checking from `starter`. |
| `demo.md` | Create this text file for copied results, restart steps and explanations. Label each exercise. |

**Persistence** means keeping data after the program exits, like filing a stock ledger instead of leaving temporary notes on the desk. **Serialization** packs data into a storage format; **parsing** reads that format back. **Validation** checks that the unpacked records follow the shop rules. Valid JSON can still contain invalid inventory.

Your starter defines inventory storage at `data/inventory.json` and export output at `exports/inventory.csv`, relative to the starter file's folder. A **path** is the location of a file. A parent directory is the folder containing it. The `with` statement closes an opened file when ordinary execution leaves its block, including when an exception is raised.

Run from the course root, the folder containing `grade.py`:

```powershell
python week-01/assignments/lesson-03/file_drills.py
python week-01/assignments/lesson-03/checks.py
python week-01/assignments/lesson-03/starter.py
```

Use `py` instead if needed on Windows. Keep interactive startup under the main guard. Do not complete file exercises by changing your real coursework files; use the practice paths described below.

## Exercise 1: Write, append and read a text notebook — 5 points

**Where:** `file_drills.py`, writing only `drill-data/notes.txt`.

1. Use `Path(__file__).resolve().parent / "drill-data"` to locate the drill folder. Create it with `mkdir(parents=True, exist_ok=True)`.
2. Open `notes.txt` in mode `"w"` with UTF-8 encoding and a `with` block. Write `Shop opened` followed by a newline, then `Counted stock` followed by a newline.
3. Close that block. Open the same file in mode `"a"` and add `Shop closed` followed by a newline.
4. Open in mode `"r"`, read and print the content.
5. Explain why starting the script again with `"w"` replaces the earlier contents rather than adding another copy.

Expected saved lines:

```text
Shop opened
Counted stock
Shop closed
```

`w` starts a new page, `a` adds at the end of the existing page, and `r` reads without rewriting it. **Finished when:** the file has exactly these three lines after a complete run. Marks: write/append/read result 3, overwrite explanation 2. This contributes to the shared `drills` criterion.

## Exercise 2: Pack and unpack a dictionary as JSON — 5 points

**Where:** `file_drills.py`; explanation in `demo.md`.

Start with this dictionary:

```python
product = {"id": 1, "name": "Pen", "price": 200, "stock": 5}
```

1. Import `json`.
2. Use `json.dumps(product)` to create a JSON **string** and give that string a variable name.
3. Pass the string to `json.loads(...)` and store the restored value in a different variable.
4. Print the original type, packed type and restored type. Expect `dict`, `str`, `dict`.
5. Compare the restored dictionary with the original using `==`; expect `True`.
6. Explain serialization and parsing using the packing/unpacking analogy. Explain why `json.loads("[]")` succeeds but does not prove a shop has a particular product.

**Finished when:** the fields survive the round trip and the type changes are recorded. Marks: round trip/types 3, explanation 2. This contributes to `drills`.

## Exercise 3: Write and read a CSV ledger — 5 points

**Where:** `file_drills.py`, using `drill-data/products.csv`.

Use these rows:

| id | name | price | stock |
| --- | --- | --- | --- |
| 1 | Notebook, A5 | 500 | 2 |
| 2 | Pen | 200 | 3 |

1. Import `csv`. Write a header and these records using `csv.DictWriter` with fields `id`, `name`, `price`, `stock`, in that order.
2. Open CSV files with `newline=""` and `encoding="utf-8"`. Let the CSV writer handle commas inside names; do not build rows with manual string joining.
3. Read the file with `csv.DictReader`.
4. Check that the first name comes back as the single value `Notebook, A5`, not two columns.
5. Reader field values are text. Convert price and stock to integers before calculating each price times stock.
6. Sum the row values: expect `500*2 + 200*3 = 1600`.

**Finished when:** the name survives quoting and the numeric total is 1600. Marks: CSV handling 2, conversion 1, total 2. Review Exercises 1–3 together as `drills`, out of 15.

## Exercise 4: Validate records before trusting them — 10 points

**Where:** `validate_inventory(records)` in `starter.py`.

`records` should be a list of product dictionaries. Enforce this exact contract:

| Part | Required rule |
| --- | --- |
| Outer value | A list; `[]` is allowed |
| Every item | A dictionary containing `id`, `name`, `price` and `stock` |
| `id` | Positive integer, unique within this inventory |
| `name` | String containing at least one non-whitespace character |
| `price` | Integer greater than or equal to zero, in whole naira |
| `stock` | Integer greater than or equal to zero |
| Integer fields | `True` and `False` are rejected even though bool is an int subtype |

1. Check the outer type before iterating and each record's type before reading fields.
2. Check the required keys, value types, ranges and duplicate IDs.
3. Raise `ValueError` when a rule fails. Include enough detail to identify the problem.
4. On valid data, finish without raising; no particular successful return value is required. Do not silently repair or discard invalid records.

In `checks.py`, try a valid one-product list, `[]`, a dictionary instead of a list, a missing name, a blank name, a duplicate ID, a negative stock and Boolean stock. The first two must succeed; the others must raise `ValueError`. Catch expected errors in your check script so you can run all cases.

**Finished when:** the rules are enforced before data is accepted. Automatic criterion: `validation`.

## Exercise 5: Load missing and damaged files differently — 10 points

**Where:** `load_inventory(path)` in `starter.py`.

A missing ledger can mean the shop has not started recording stock. A damaged ledger needs attention; replacing it with a blank one would hide the problem.

1. Open the supplied path as UTF-8 and parse its JSON.
2. Validate parsed records with Exercise 4's function, then return the list.
3. Catch only `FileNotFoundError` as the “no saved inventory yet” case and return `[]`.
4. Let malformed JSON, invalid inventory, invalid UTF-8 and other read errors remain errors. Never write to the path from this loading function.

Test these in a temporary directory, using different paths:

| File situation | Expected outcome |
| --- | --- |
| Path does not exist | Return `[]` |
| Contents `[]` | Return `[]` |
| Valid product-list JSON | Return matching records |
| Contents `{broken` | Parsing error; contents unchanged |
| Contents `{}` | Validation error; contents unchanged |
| Directory supplied instead of a file | Read error; do not treat it as empty inventory |

**Finished when:** valid files load and every existing bad input remains intact. Automatic criterion: `loading`; this is a required mastery check.

## Exercise 6: Save through a temporary file — 10 points

**Where:** `save_inventory(path, records)` in `starter.py`.

Think of writing a replacement ledger completely before swapping it for the original.

1. Validate `records` before touching the destination.
2. Create missing parent directories.
3. Use a temporary file beside the destination, named with an added `.tmp`: `inventory.json` uses `inventory.json.tmp`.
4. Write complete UTF-8 JSON to that temporary file and close it.
5. Replace the destination with the temporary file only after writing succeeds, using `Path.replace(...)` or equivalent. Let write/replace errors reach the caller.
6. Test save followed by load in a temporary directory; the restored records must equal the input.

To check a failed write safely, first create a valid destination in a **disposable directory**, then create a directory named `inventory.json.tmp` beside it. Attempt another save. Opening the temporary path as a file must fail, and the original `inventory.json` must still contain the first data. Also try saving invalid records: validation must reject them before altering the destination.

**Finished when:** round trip works and both failed saves preserve the previous file. Automatic criterion: `saving`, a required mastery check. This pattern does not solve two programs editing the same inventory concurrently.

## Exercise 7: Load, list and add products — 20 points

**Where:** `main()`, `read_integer(prompt, minimum)` and `find_product(...)` in `starter.py`.

1. At startup call `load_inventory(DATA_FILE)`. If an existing file cannot be read/validated, explain the error and stop before showing a menu. Do not overwrite it.
2. Implement this repeating menu:

```text
1. List products
2. Add product
3. Record sale
4. Export CSV
5. Quit
```

3. List IDs, names, prices and stocks; for an empty list show `No products yet`. Unknown menu choices produce a message and show the menu again.
4. Implement `read_integer(prompt, minimum)` to keep asking after failed conversion or a value below `minimum`. Return the first acceptable integer. Use minimum 0 for stock/price and 1 for IDs/quantities.
5. For Add, ask for a name and strip surrounding whitespace; keep asking if it becomes blank. Ask for nonnegative price and stock.
6. Allocate ID `1` if empty; otherwise use one greater than the largest existing ID. Do not use the number of records as the ID.
7. Build a **candidate** list containing the proposed new record. Save it first. Only on success make it the live inventory and print success. On failure retain the old live list and show an error.

**Check from empty inventory:** add Notebook at price 500/stock 10, then Pen at 200/5. Expect IDs 1 and 2. Quit/restart, add Bag at 4000/0 and expect ID 3 with earlier records preserved. Try a blank name, text price and negative stock to prove the prompts retry.

**Finished when:** list/add/restart and invalid menu/input behaviour work. Record the journey in `demo.md`. Manual criterion: `menu_add`.

## Exercise 8: Record a sale that survives restart — 20 points

**Where:** option 3 of `main()` and any helper you choose to add.

1. Ask for product ID and use `find_product` to locate it. Return to the menu with a helpful message if missing.
2. Ask for a positive integer quantity. Enforce the sale rules: no zero, negative, fractional, Boolean or excessive quantity. Direct helpers must reject wrong types even if the menu already converts input.
3. Make a candidate inventory with independent copied product dictionaries. Copying only the outer list still shares its inner dictionaries; editing those could change live stock before saving succeeds.
4. Decrease stock in the candidate, calculate unit price times quantity, and save the candidate.
5. Only after a successful save replace the live inventory and print a receipt. After failure, both the live stock and original disk file must be unchanged.

| Independent check starting with Notebook stock 10, price 500 | Expected result |
| --- | --- |
| Sell 3 | Receipt total 1500; stock 7 after restart |
| Sell 10 | Total 5000; stock 0 |
| Sell 11 | Rejection; stock 10 |
| Unknown ID | Rejection; all records unchanged |
| Save fails after a valid sale request | No success receipt; memory and file retain stock 10 |

Use separate disposable starting data for these checks. **Finished when:** successful sales persist, failed sales do not change stock and the evidence is in `demo.md`. Manual criterion: `sales`, a required mastery check.

## Exercise 9: Export the current inventory as CSV — 5 points

**Where:** `export_csv(path, products)` and option 4 in the menu.

1. Create missing parent folders of the supplied export path.
2. Write UTF-8 CSV using `DictWriter`, `newline=""`, and exactly `id,name,price,stock` columns in that order.
3. Always write the header, including when `products` is empty.
4. Write the selected fields for every current product. Ignore any extra dictionary fields; do not add extra CSV columns.
5. Preserve names containing commas through CSV quoting.
6. In the menu call the function with `EXPORT_FILE` and the live inventory. Print success only if it finishes without an error.

**Check:** export a record named `Notebook, A5`, read it back with DictReader and verify the exact name. Export `[]` to another path and confirm there is a header with no product rows. After a sale, an export must show the updated stock, not the old fixture.

**Finished when:** all three cases work without changing the inventory. Automatic criterion: `csv_export`.

## Exercise 10: Demonstrate restart and failure recovery — 10 points

**Where:** `demo.md`. Use a disposable copy of the application for destructive failure experiments.

1. Copy `starter.py` into a fresh practice folder named `failure-demo/`. Its file-relative paths keep this run's `data/` and `exports/` separate from your real submission data. Run the copy, add a product, sell, quit and restart; record the actual retained stock.
2. In this copy only, replace `data/inventory.json` with `{broken`, then run again. Expect a clear startup refusal, no menu and unchanged damaged contents. Repeat independently with `{}`.
3. Restore valid starting data. Create a **directory** named `data/inventory.json.tmp` in the disposable copy. Attempt an add or sale. The save should fail. Use the menu to confirm the original live stock remains; inspect the saved inventory to confirm it remains too.
4. In a fresh disposable copy with valid inventory, create an `exports/` directory containing a directory named `inventory.csv`. Attempt export. Expect an error message with no success message; the inventory is unaffected.
5. In `demo.md`, answer: what is in memory versus on disk; why missing and damaged files differ; why parsing differs from validation; why candidate-save-commit protects a failed save; and why two simultaneous editors need more coordination.

Use fresh folders to repeat these cases instead of overwriting your useful inventory. **Expected evidence:** numbered action, input, expected outcome, actual outcome, and copied message for each test. No screenshots are required.

Marks: restart, startup refusal and failed-save consistency 5 (`persistence_demo`, required mastery check); explanations and failed-export reporting 5 (`demo`).

## Save, check and review

From the course root:

```powershell
python grade.py check --lesson 3
python grade.py rubric --lesson 3
```

Automatic validation, load, save and CSV checks cover 35 points. Drills and integrated program demonstrations require review for 65 points. **REVIEW PENDING** identifies unreviewed work. Use the [checker guide](../../../grading/README.md) to record manual scores after inspecting actual evidence.

- [ ] All ten exercises completed; drill files kept separate from inventory.
- [ ] Direct checks and complete menu demonstrations recorded.
- [ ] At least 80/100 after review, with loading, safe saving, sales and persistence gates passing.

# Assignment 3 — Persistent EMIO24 inventory CLI

**Deliverables:** completed `starter.py`, a sample `exports/inventory.csv`, `demo.md`, and the completed Week 1 checklist. Use functions and ordinary dictionaries; classes, databases, and external packages are not needed.

## Part A — Short file drills

Create `file_drills.py` in this folder:

1. Write two shop notes to a text file using `w`, then add a third using `a`. Read and display the contents. Explain what running the `w` step again does.
2. Convert a product dictionary into a JSON string and back. Print the types before and after parsing.
3. Create a CSV with a header and two products, including a product named `Notebook, A5`. Read it using `DictReader`, convert stock and price to integers, and calculate total inventory value.

Keep drill files separate from the CLI's inventory file.

## Part B — Build the CLI in stages

### Stage 1: Load and list

Use the paths in `starter.py`. Load `data/inventory.json` at startup and validate the contract in the teaching notes. A missing file means an empty inventory. Malformed JSON, invalid UTF-8, invalid record structure, or other read errors must produce a useful message and stop startup without overwriting the file.

List ID, name, price, and stock. Display a clear message for an empty inventory.

### Stage 2: Add products

Prompt for a nonblank name, nonnegative integer price, and nonnegative integer starting stock. Assign an ID one larger than the highest existing ID, or 1 for an empty inventory. Strip surrounding whitespace from the name.

For each add: create candidate data, save it, then replace in-memory inventory and report success. Duplicate names are allowed this week; IDs must remain unique. Boolean values are not valid integer fields in loaded data.

### Stage 3: Record sales

Reuse your Lesson 2 rules. Find the product by ID and require a positive integer quantity no greater than stock. Make the change on candidate data, save, commit in memory, and show quantity and total price only after success.

A missing product, invalid quantity, or failed save must leave in-memory stock unchanged.

### Stage 4: Export and quit

Export the current inventory to `exports/inventory.csv` with exactly these columns:

```text
id,name,price,stock
```

Use the CSV module. An empty export must still contain the header. Catch file-write errors and do not report a successful export if writing fails. Saving inventory after each successful change means quitting needs no extra save.

### Required menu

```text
EMIO24 Inventory
1. List products
2. Add product
3. Record sale
4. Export CSV
5. Quit
```

Invalid choices show a message and return to the menu. A save failure should also show a message and return to the menu with the previous data intact.

## Suggested functions

`validate_inventory`, `load_inventory`, `save_inventory`, `read_integer`, `find_product`, `add_product`, `record_sale`, `export_csv`, and `main`.

The provided function signatures are suggestions, not a required architecture. You may reuse the teaching notes' persistence helpers, but explain every line and implement the menu yourself.

## Acceptance checklist

- [ ] First run without a data file starts with an empty inventory.
- [ ] Add Notebook at 500 with stock 10: ID 1.
- [ ] Add Pen at 200 with stock 5: ID 2.
- [ ] Sell 3 notebooks: total 1500; notebook stock 7.
- [ ] Restart: both products and the updated quantities are restored.
- [ ] Add a third product after restart: ID 3.
- [ ] Reject blank names, fractional quantities, negative values, and overselling.
- [ ] Unknown product ID returns to the menu without a crash.
- [ ] CSV matches current data and handles a comma in a product name.
- [ ] Empty inventory export contains the header.
- [ ] JSON containing `{broken` stops startup and remains unchanged.
- [ ] Valid JSON containing `{}` stops startup and remains unchanged.
- [ ] A list with duplicate IDs, missing fields, negative stock, or Boolean stock is rejected.
- [ ] A failed inventory save does not report success or change in-memory data.
- [ ] A failed export does not report success.

Use a **disposable copy of your assignment folder** for damaged-file and failure experiments. For a predictable save failure, create a directory named `inventory.json.tmp` next to a valid inventory file: opening that directory as a file should raise `OSError`. Start with the valid file, try a sale, then list stock to confirm it is unchanged. For an export failure, create a directory at the expected `exports/inventory.csv` file path in a disposable copy. These checks do not require changing system permissions.

## Marking — 100 points

| Area | Points |
| --- | --- |
| Text, JSON-string, and CSV drills | 15 |
| Menu, listing, adding, unique IDs | 20 |
| Sale validation and correct totals | 20 |
| Loading, record validation, preservation of invalid files | 20 |
| Saving, restart behaviour, failed-save consistency | 15 |
| CSV export and clear demonstration notes | 10 |

Aim for 80/100. Regardless of score, persistence across restart, unchanged stock after rejected operations, and preservation of invalid files must work before checking off the week.

## Your five-minute demonstration

In `demo.md`, record the steps and results for adding, selling, restarting, and exporting. Explain:

1. What lives in memory, and what lives on disk?
2. Why is a missing file treated differently from a damaged file?
3. Why is parsing different from validation?
4. Why save candidate data before changing the live inventory?
5. What would happen if two copies of the program changed the same file?

**Optional extension after the core works:** add a low-stock report or total inventory value. Leave authentication, receipts, and sales history for later lessons.

## Offline grading

Run from the course root:

```powershell
python grade.py check --lesson 3
python grade.py rubric --lesson 3
```

See the [checker guide](../../../grading/README.md). Scores and evidence are stored locally. Automated checks cover functions; written work and demonstrations require manual review.

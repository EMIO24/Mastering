# Lesson 3 — Files, CSV, JSON and persistence

**Goal:** Keep inventory between runs and handle missing or damaged files deliberately.

**Time:** 45 minutes teaching, 30 minutes examples, 75–120 minutes building. Use the practice day to finish and demonstrate the CLI.

## 1. Memory is the counter; a file is the stock book

During the day, a shop assistant may calculate stock on a scrap of paper. If that paper disappears, the next assistant cannot reconstruct the count. Recording the count in a stock book makes it available tomorrow.

Python variables live in the running process. A file stores data beyond that process. **Persistence** means keeping information so it can be retrieved later. A file is one way to do this; a database is another, introduced later.

Saving is a separate operation that can fail. Changing a dictionary does not automatically change a file.

## 2. Open, read, write, close

```python
with open("shop-note.txt", "w", encoding="utf-8") as file:
    file.write("Stock checked today.\n")  # write() does not add a newline

with open("shop-note.txt", "r", encoding="utf-8") as file:
    note = file.read()  # Reads the entire file as a string

print(note)
```

`open()` returns a file object, which provides methods such as `read()` and `write()`. `with` closes it when you leave the block, including when an exception occurs.

| Mode | Meaning | If the file already exists |
| --- | --- | --- |
| `r` | Read | Leaves contents unchanged; missing file raises an error |
| `w` | Write | Truncates existing contents as soon as it opens |
| `a` | Append | Writes at the end |

Write and append modes create a missing file when its parent directory exists and permissions allow it. Use `encoding="utf-8"` consistently for text.

For large text files, iterate over lines instead of calling `read()` on the entire file:

```python
with open("shop-note.txt", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip("\n"))
```

## 3. Paths: the address of the stock book

A relative filename such as `"inventory.json"` is resolved against the terminal's current working directory. Running a script from a different directory can therefore appear to lose its data.

For this project, anchor data beside the script:

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "inventory.json"
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
```

`__file__` is the script's path; `parent` gets its folder. The `/` operator joins path components. This is a small use of a standard-library module; modules and project organization receive a full lesson in Week 3. Run these examples as files, since `__file__` is not normally defined in an interactive Python prompt.

## 4. JSON: a stock book with labelled fields

JSON represents structured data as text. It fits a list of product dictionaries better than an informal paragraph.

```json
[
  {"id": 1, "name": "Notebook", "price": 500, "stock": 10}
]
```

JSON uses double-quoted property names and strings, `true`, `false`, and `null`. Python uses `True`, `False`, and `None`. JSON does not allow comments or trailing commas.

| Operation | Direction | Example |
| --- | --- | --- |
| `json.dump(data, file)` | Python → JSON file | Save inventory |
| `json.load(file)` | JSON file → Python | Restore inventory |
| `json.dumps(data)` | Python → JSON string | Prepare text for transmission |
| `json.loads(text)` | JSON string → Python | Parse received text |

Remember: the **s** means **string**, not plural. `dump()` writes to a file object; it does not return the JSON text.

```python
import json

product = {"name": "Notebook", "stock": 10}
text = json.dumps(product)  # A str containing JSON
restored = json.loads(text)  # A dict again

with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product, file, indent=2)  # indent makes it readable

with open("product.json", "r", encoding="utf-8") as file:
    restored = json.load(file)
```

Do not use append mode for an inventory JSON document. Appending a second list after the first creates invalid JSON rather than extending the stored list.

JSON arrays become Python lists; tuples also serialize as arrays and return as lists. Sets are not directly JSON serializable. JSON object keys are strings, so do not rely on integer dictionary keys surviving a round trip unchanged.

## 5. Valid JSON is not necessarily valid inventory

`{"message": "hello"}` is valid JSON but not the inventory list our application expects. Parsing checks syntax; validation checks meaning.

Our inventory contract is a list of dictionaries. Every record must have:

- `id`: unique positive integer;
- `name`: string containing at least one non-whitespace character;
- `price`: nonnegative integer in whole naira;
- `stock`: nonnegative integer.

Reject Boolean values in integer fields. Python treats `bool` as an `int` subclass, so use `type(value) is int` for this exercise's strict contract.

```python
def validate_inventory(records):
    if not isinstance(records, list):
        raise ValueError("Inventory must be a list.")

    seen_ids = set()
    for product in records:
        if not isinstance(product, dict):
            raise ValueError("Each product must be a dictionary.")
        required = {"id", "name", "price", "stock"}
        if not required.issubset(product):
            raise ValueError("A product is missing required fields.")
        if type(product["id"]) is not int or product["id"] <= 0:
            raise ValueError("Product ID must be a positive integer.")
        if product["id"] in seen_ids:
            raise ValueError("Product IDs must be unique.")
        seen_ids.add(product["id"])
        if not isinstance(product["name"], str) or not product["name"].strip():
            raise ValueError("Product name cannot be blank.")
        for field in ("price", "stock"):
            if type(product[field]) is not int or product[field] < 0:
                raise ValueError(f"{field} must be a nonnegative integer.")
```

Extra fields are allowed by this validator. It checks the required fields without changing the records.

## 6. Missing, corrupt, and unreadable files are different

```python
def load_inventory(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            records = json.load(file)
    except FileNotFoundError:
        return []  # A normal first run: nothing has been saved yet

    validate_inventory(records)
    return records
```

Let other failures reach the startup code, where you can show a useful message and stop:

```python
try:
    products = load_inventory(DATA_FILE)
except json.JSONDecodeError as error:
    print(f"Inventory JSON is damaged: {error}")
    # Stop startup; preserve the file for inspection.
except (OSError, UnicodeError, ValueError) as error:
    print(f"Cannot load inventory: {error}")
    # Stop startup for unreadable files, encoding errors, or bad structure.
else:
    print(f"Loaded {len(products)} products.")
    # Enter your menu only here, after successful loading.
```

`JSONDecodeError` is a subclass of `ValueError`; put the more specific handler first. Do not replace damaged inventory with `[]` and then save over it. Missing data on first run and damaged existing data require different responses.

## 7. Save a replacement before replacing the stock book

Writing directly to the main file in `w` mode erases its old contents before writing finishes. A better pattern for this exercise is to write a temporary file beside it, close that file, and then replace the destination.

```python
def save_inventory(path, records):
    validate_inventory(records)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with open(temporary, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)
    temporary.replace(path)  # Replacement happens after writing and closing
```

Let save errors reach the caller. Report success only after this function returns. This reduces the risk of leaving a partially written main file; it is not a backup system or a guarantee against every disk failure. It assumes one running application; simultaneous writers need a different design.

Keep in-memory state consistent too:

```python
# Each product here contains only scalar fields, so dictionary copies suffice.
candidate = [product.copy() for product in products]
# Apply the requested stock change to candidate, not products.
# Validate and save candidate first.
save_inventory(DATA_FILE, candidate)
products = candidate  # Commit in memory only after the save succeeds
```

When saving raises an error, keep the original `products` and show a failure message. A list copy alone would still share its product dictionaries; that would not protect the original stock.

## 8. CSV: a spreadsheet-shaped stock book

CSV suits flat rows and columns, such as an inventory export. JSON is more convenient for nested data.

```python
import csv

fields = ["id", "name", "price", "stock"]
with open("inventory.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerow({"id": 1, "name": "Notebook, A5", "price": 500, "stock": 10})

with open("inventory.csv", "r", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        # CSV fields arrive as strings; convert numbers deliberately.
        stock = int(row["stock"])
        print(row["name"], stock)
```

`newline=""` lets the CSV module handle line endings correctly, including on Windows. Do not build rows by joining strings with commas: names can contain commas, quotes, or line breaks, and the CSV module handles quoting for you.

Run [examples.py](examples.py), inspect its `demo-data` files, and then complete [Assignment 3](../assignments/lesson-03/README.md).

## References and offline checking

- [Week 1 references](../references.md)
- [Offline assignment checker](../../grading/README.md)

## Terminology through everyday analogies

| Term | Precise meaning | Everyday analogy |
| --- | --- | --- |
| Persistence | Keeping data after a process exits. | filing the ledger instead of leaving it on the desk. |
| Serialization | Converting data to a storage/transport format. | packing cards in an agreed envelope. |
| Parsing | Interpreting text according to a format. | unpacking the envelope; contents still need validation. |
| Path | A filesystem location. | directions to a filing cabinet. |
| Context manager | Setup/cleanup around a with block. | a tool borrowing procedure that returns the tool on ordinary exit. |

Read the [foundation glossary](../../glossary.md) for further terms and analogy limits. Then complete the [ten-exercise assignment](../assignments/lesson-03/README.md).

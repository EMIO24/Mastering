"""Build your persistent inventory CLI here. TODO functions are incomplete."""

import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "inventory.json"
EXPORT_FILE = BASE_DIR / "exports" / "inventory.csv"

records = [
    {
        "id": 101,
        "name": "Wireless Mechanical Keyboard",
        "price": 129,
        "stock": 45
    },
    {
        "id": 102,
        "name": "Ergonomic Optical Mouse",
        "price": 49,
        "stock": 120
    },
    {
        "id": 103,
        "name": "USB-C Docking Station",
        "price": 89,
        "stock": 0
    }
]

def validate_inventory(records):
    # TODO: Check the list, every record, all required fields, and unique IDs.
    ID = set()
    required = {"id", "name", "price", "stock"}
    for products in records:
        if not required.issubset(products):
            raise ValueError("Required key missing")

        if products["id"] in ID:
            raise ValueError("Id number must be unique")
        ID.add(products["id"])


    for products in records:
        if not isinstance(products["id"], int) or products["id"] <= 0:
            raise ValueError("Id must be Positive integer only")
        if not isinstance(products["name"], str) or products["name"].strip() == "":
            raise ValueError("The product name should be a strind and contain at least one non-whitespace character")
        if not isinstance(products["price"], int) or products["price"] <= 0:
            raise ValueError("Integer must be greater than or equal to zero, in whole naira")
        if not isinstance(products["stock"], int) or products["stock"] <= 0:
            raise ValueError("Integer must be greater than or equal to zero, in whole naira")

    return records


def load_inventory(path):
    # TODO: Return [] only for a missing file; validate successfully parsed data.
    raise NotImplementedError("Implement loading.")


def save_inventory(path, records):
    # TODO: Validate, write a temporary file beside the destination, then replace.
    raise NotImplementedError("Implement saving.")


def read_integer(prompt, minimum):
    # TODO: Retry conversion failures and values below the supplied minimum.
    raise NotImplementedError("Implement integer input.")


def find_product(products, product_id):
    raise NotImplementedError("Implement lookup.")


def export_csv(path, products):
    # TODO: Create the parent folder and write the header and selected fields.
    raise NotImplementedError("Implement CSV export.")


def main():
    # TODO: Load first; do not start the menu if an existing file is invalid.
    # TODO: Make candidate copies for changes; commit only after a successful save.
    print("Implement the five-option inventory menu here.")


if __name__ == "__main__":
    main()

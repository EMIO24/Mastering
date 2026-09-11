"""Build your persistent inventory CLI here. TODO functions are incomplete."""

import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "inventory.json"
EXPORT_FILE = BASE_DIR / "exports" / "inventory.csv"


def validate_inventory(records):
    # TODO: Check the list, every record, all required fields, and unique IDs.
    raise NotImplementedError("Implement inventory validation.")


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

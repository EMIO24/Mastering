"""Demonstrate text, JSON and CSV in an isolated demo-data directory."""

import csv
import json
from pathlib import Path


def main():
    demo_dir = Path(__file__).resolve().parent / "demo-data"
    demo_dir.mkdir(exist_ok=True)

    note_path = demo_dir / "note.txt"
    with open(note_path, "w", encoding="utf-8") as file:
        file.write("Opening stock checked.\n")  # Reset this demo each run
    with open(note_path, "a", encoding="utf-8") as file:
        file.write("Closing stock checked.\n")
    with open(note_path, "r", encoding="utf-8") as file:
        print(file.read(), end="")

    products = [{"id": 1, "name": "Notebook, A5", "price": 500, "stock": 10}]
    json_path = demo_dir / "products.json"
    temporary = json_path.with_suffix(".json.tmp")
    with open(temporary, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=2)
    temporary.replace(json_path)
    with open(json_path, "r", encoding="utf-8") as file:
        restored = json.load(file)
    print("JSON file restored:", restored)

    text = json.dumps(products)
    print("JSON string type:", type(text).__name__)  # str
    print("Parsed string type:", type(json.loads(text)).__name__)  # list

    csv_path = demo_dir / "products.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "price", "stock"])
        writer.writeheader()
        writer.writerows(products)
    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            print("CSV stock before conversion:", type(row["stock"]).__name__)
            print("CSV inventory value:", int(row["price"]) * int(row["stock"]))
    print("Demo files:", demo_dir)


if __name__ == "__main__":
    main()

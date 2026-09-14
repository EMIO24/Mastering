from pathlib import Path
import json
import csv

DIR = Path(__file__).resolve().parent
file_path =DIR /"drill-data"/ "notes.txt"
file_path.parent.mkdir(parents=True, exist_ok=True)

with open(file_path, 'w', encoding='utf-8') as file:
    file.write("Shop opened\n")
    file.write("Counted stock\n")

with open(file_path, 'a', encoding="UTF-8") as file:
    file.write("Shop closed\n")

with open(file_path, 'r', encoding='UTF-8') as file:
    shop = file.read()
    print(shop)


product = {"id": 1, "name": "Pen", "price": 200, "stock": 5}

prod_as_a_str = json.dumps(product)
convert_to_actual_dict = json.loads(prod_as_a_str)


print(type(product))
print(type(prod_as_a_str))
print(type(convert_to_actual_dict))

check = product == convert_to_actual_dict
print(check)


csv_ = DIR /"drill-data"/ "products.csv"
csv_.parent.mkdir(parents=True, exist_ok=True)

fields = ["id", "name", "price", "stock"]
with open(csv_, 'w', newline = "", encoding='utf-8') as file:
    records = csv.DictWriter(file, fieldnames=fields)
    records.writeheader()
    records.writerow({"id": 1, "name": "Notebook, A5", "price": 500,"stock": 2})
    records.writerow({"id":2, "name": "Pen", "price":200, "stock":3})

with open(csv_, 'r', newline="", encoding="utf-8") as file:
    record = csv.DictReader(file)
    for line in record:
        print(line)

with open(csv_, 'r', newline="", encoding="utf-8") as file:
    record = csv.DictReader(file)
    total = None
    Total = 0
    for line in record:
        price = int(line["price"])
        stock = int(line["stock"])
        total = price * stock
        Total += total
    print(Total)


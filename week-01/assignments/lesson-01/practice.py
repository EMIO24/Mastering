# number three
quantities = [3, -1, 0, 5, -2]
positive_total = 0
_list = len(quantities)

for i in range(_list):
    if quantities[i] <= 0:
        positive_total += 0
    else:
        positive_total += quantities[i]

print(positive_total)

# number four 

products = [
    {"id" : 1, "name": "Pen", "price" : 200, "stock": 10, "category": "Stationary"},
    {"id" : 2, "name": "Notebook", "price" : 500, "stock": 3, "category": "Stationary"}
]

for product in products:
    if product == products[1]:
        product["stock"] = 8
    print(products)

## Exercise 5: Use a set and a tuple — 10 points
unique_categories = set()
shop_location = (6.5, 3.4)
for product in products:
    unique_categories.add(product["category"])
print(unique_categories)
print(shop_location)


# Number 10
names = ["Pen"]
names = names.append("Notebook")
print(names)

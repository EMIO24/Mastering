"""Complete the diagnostic. Replace each pass with your own implementation."""

'''
Complete stock_label(stock): return out for 0, low for 1 through 5, 
available above 5. Assume nonnegative integer inputs. 
Show 0,1,5,6. Marks: zero 3, low boundary 4, available 3. 
Explain conditions as shop decision rules.
'''
def stock_label(stock):
    label = ''
    if stock <= 0:
        label = "out"
    elif stock == 1 or stock < 6:
        label = "low"
    else:
        label = "available"
    return label

products = [
    {"id": 1, "name": "Pen", "price": 200, "stock": 10},
    {"id": 2, "name": "Notebook", "price": 500, "stock": 3},
    {"id": 3, "name": "Bag", "price": 4000, "stock": 0},
]

def inventory_value(products):
    total = 0
    for product in products:
        total += product["price"] * product["stock"]
    return total

def low_stock_names(products, threshold):
    threshold_list = []
    for product in products:
        if product["stock"] <= threshold:
            threshold_list.append(product["name"])
    print(threshold_list)
    return threshold_list


def find_product(products, product_id):
    prod = None
    for product in products:
        if product_id == int(product["id"]):
            prod = product
        elif product_id > len(products):
            prod = None
    print(prod)

## Exercise 9: Repair a function that only prints — 5 points
def total(price, quantity):
    return price * quantity

answer = total(200, 3)
print(answer)



if __name__ == "__main__":
    products = [
        {"id": 1, "name": "Pen", "price": 200, "stock": 10},
        {"id": 2, "name": "Notebook", "price": 500, "stock": 3},
        {"id": 3, "name": "Bag", "price": 4000, "stock": 0},
    ]
    # Add your own calls and compare actual results with the assignment.

    print(stock_label(0))
    print(stock_label(1))
    print(stock_label(5))
    print(stock_label(6))

    low_stock_names(products, 3)
    low_stock_names(products, 0)
    low_stock_names(products, 10)
    low_stock_names([], 3)

    find_product(products, 1)
    find_product(products, 2)
    find_product(products, 3)
    find_product(products, 99)
    find_product([], 1)

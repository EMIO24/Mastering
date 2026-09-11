"""Run after the diagnostic; no external packages are required."""


def inventory_value(products):
    """Return the value of all stock in whole naira."""
    total = 0
    for product in products:
        total += product["price"] * product["stock"]
    return total


def low_stock_names(products, threshold):
    names = []
    for product in products:
        if product["stock"] <= threshold:
            names.append(product["name"])
    return names


def main():
    products = [
        {"id": 1, "name": "Pen", "price": 200, "stock": 10},
        {"id": 2, "name": "Notebook", "price": 500, "stock": 3},
    ]
    print("Inventory value:", inventory_value(products))  # 3500
    print("Low stock:", low_stock_names(products, 3))  # ['Notebook']
    print("Empty inventory:", inventory_value([]))  # 0

    # Assignment creates a second reference, not a separate dictionary.
    product = products[0]
    product["stock"] -= 1
    print("Stock after update:", products[0]["stock"])  # 9


# Run the demonstration only when this file is executed directly.
if __name__ == "__main__":
    main()

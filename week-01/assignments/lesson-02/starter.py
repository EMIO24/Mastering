"""Implement this week's in-memory checkout."""
'''
| Exception | Example cause | Sensible next step |
| --- | --- | --- |
| `ValueError` | `int("two")` | Ask for a whole number |
| `TypeError` | `"200" + 3` | Fix incompatible types |
| `KeyError` | Missing dictionary key | Check the data contract or use deliberate optional lookup |
| `IndexError` | Access beyond a list's end | Check bounds or iterate directly |
| `ZeroDivisionError` | Dividing by zero | Define what a zero denominator means |
| `FileNotFoundError` | Opening a missing file for reading | Handle first-run behaviour if expected |

Avoid `except: pass` and broad `except Exception:` around your entire program. A mistyped variable is a programming bug; it should not turn into a misleading "bad quantity" message.

Keep `try` blocks small. You should know which operation is expected to raise the exception you catch.

'''

def read_positive_integer(prompt):
    # TODO: Retry conversion failures and reject nonpositive values.
    while True:
        try:
            quantity = int(input(prompt))
        except ValueError:
            print("Enter a whole number")
        else:
            if quantity <= 0:
                print("Quantity must be greater than zero")
            else:
                return quantity

def find_product(products, product_id):
    print(products)
    found = None
    for product in products:
        if product["id"] == product_id:
            found = product
            break
        else:
            found = None
    print(found)
    return found


def sell_product(product, quantity):
    # TODO: Validate every rule before changing stock; return the total.
    total = 0
    if type(quantity) != int:
        raise ValueError("Quantity must be a whole number")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    if quantity > product["stock"]:
        raise ValueError("Quantity is more than available stock")
    else:
        product["stock"] -= quantity

    total = product["price"] * quantity
    return total


def main():
    products = [
        {"id": 1, "name": "Pen", "price": 200, "stock": 20},
        {"id": 2, "name": "Notebook", "price": 500, "stock": 10},
    ]

    while True:
        print('''
1. List products
2. Sell a product
3. Quit''')
        option = int(input("choose an option: "))
        if option == 1:
            for product in products:
                print(product["id"], product["name"], product["price"], product["stock"])

        elif option == 2:
            product_id = int(input("Input a positive product ID: "))
            product = find_product(products, product_id)
            if product is not None:
                quantity = int(input("Enter quantity: "))
            try:
                sell = sell_product(product, quantity)
            except ValueError:
                print("Sorry!, try again")
            else:
                print(f"""Reciept
Product Name: {product["name"]}
Sold Quantity: {quantity}
Price: {sell}
Remaining stock: {product["stock"]}""")

        elif option == 3:
            break
        else:
            print("Invalid option")
    # TODO: Add a loop with list, sell, and quit options.


if __name__ == "__main__":
    main()

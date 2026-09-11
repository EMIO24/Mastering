"""Small exception demonstrations, separate from the assignment solution."""


def convert_quantity(raw_value):
    try:
        quantity = int(raw_value)
    except ValueError:
        print(f"{raw_value!r}: enter a whole number.")
    else:
        print("Converted quantity:", quantity)
    finally:
        print("Conversion attempt finished.")


def sell_product(product, quantity):
    if type(quantity) is not int:
        raise ValueError("Quantity must be a whole number.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    if quantity > product["stock"]:
        raise ValueError("Not enough stock.")
    product["stock"] -= quantity  # Change state only after validation
    return product["price"] * quantity


def main():
    convert_quantity("3")
    convert_quantity("three")
    product = {"name": "Notebook", "price": 500, "stock": 10}
    for quantity in (12, 3):
        try:
            total = sell_product(product, quantity)
        except ValueError as error:
            print("Sale rejected:", error)
        else:
            print("Sale total: NGN", total)
        print("Remaining stock:", product["stock"])  # 10, then 7


if __name__ == "__main__":
    main()

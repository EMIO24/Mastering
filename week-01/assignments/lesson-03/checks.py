records = [
    {
        "id": 101,
        "name": "Wireless Mechanical Keyboard",
        "price": 129.99,
        "stock": 45
    },
    {
        "id": 102,
        "name": "Ergonomic Optical Mouse",
        "price": 49.50,
        "stock": 120
    },
    {
        "id": 103,
        "name": "USB-C Docking Station",
        "price": 89.00,
        "stock": 0
    }
]

def validate_inventory(records):
    # TODO: Check the list, every record, all required fields, and unique IDs.
    ID = set()
    required = {"id", "name", "price", "stock"}
    for products in records:
        ID.add(products["id"])
        if not required.issubset(products):
            raise ValueError("Required key missing")


    for products in records:
        if not isinstance(products["id"], int) and products["id"] <= 0:
            raise ValueError("Id must be Positive integer only")
        if products["id"] not in ID:
            raise ValueError("Id must be Unique")
        if not isinstance(products["name"], str) or products["name"].strip() == "":
            raise ValueError("The product name should be a strind and contain at least one non-whitespace character")
        if not isinstance(products["price"], int) and products["price"] <= 0:
            raise ValueError("Integer must be greater than or equal to zero, in whole naira")
        if not isinstance(products["stock"], int) and products["stock"] >= 0:
            raise ValueError("Integer must be greater than or equal to zero, in whole naira")

    return records

confirm = validate_inventory(records)
print(confirm)
from starter import find_product, sell_product, read_positive_integer

record = {"name": "Pen", "price": 2000}
try:
    print(record["price"])
except KeyError as error:
    print(type(error).__name__, str(error))


'''
'''

def experiment(raw):
    try:
        con = int(raw)
    except ValueError:
        print("conversion failed")
    else:
        print("conversion succeeded")
    finally:
        print("attempt finished")

experiment("three")
experiment("3")
# Lesson 4: Classes, objects and instances

**Goal:** Understand why classes exist, then explain and use classes, objects/instances, attributes, methods, `self`, and `__init__` without memorising syntax.

**Prerequisite:** Lesson 3 concepts such as functions, validation, exceptions, and state are useful here. This lesson deliberately connects OOP to those ideas.

## 1. Start with what you already know

Before classes, you can represent a product with a dictionary:

```python
pen = {"name": "Pen", "price": 200, "stock": 4}
```

And write functions that operate on it:

```python
def inventory_value(product):
    return product["price"] * product["stock"]

def restock(product, quantity):
    product["stock"] += quantity
```

This is valid Python. Classes do not exist because dictionaries or functions are bad. A class gives us another way to organise **related data and related behaviour**.

## 2. Function versus class

A function mainly describes an action:

```python
def calculate_value(price, stock):
    return price * stock
```

Think: **inputs -> action -> result**.

A class describes a kind of thing from which objects can be created:

```python
class Product:
    pass
```

Think: **definition -> create individual objects -> each object can hold its own data and use related behaviour**.

A class can contain functions. A function associated with a class is called a **method**.

## 3. Class versus object versus instance

```python
class Product:
    pass

pen = Product()
book = Product()
```

- `Product` is the **class**: the definition.
- `pen` is an **object** created from Product.
- `book` is another object.
- Saying “pen is an **instance of Product**” means pen is an object created from that class.

Mental model:

```text
             Product
              class
             /     \
            /       \
          pen       book
        instance   instance
```

The class is not Pen or Book. It defines the kind of object they are.

## 4. Giving each object its own data

Empty objects are not useful enough. We want:

```text
pen:  name="Pen",  price=200, stock=4
book: name="Book", price=500, stock=7
```

Python commonly initializes this data with `__init__`:

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
```

Now:

```python
pen = Product("Pen", 200, 4)
book = Product("Book", 500, 7)
```

Each call creates a different Product object.

## 5. Understand self before memorising it

`self` means **the particular instance this method is currently working with**.

When this runs:

```python
pen = Product("Pen", 200, 4)
```

inside `__init__`, conceptually:

```text
self  -> the new pen object
name  -> "Pen"
price -> 200
stock -> 4
```

So:

```python
self.name = name
```

means: take the incoming `name` value and store it as an attribute on this particular object.

The two sides are different:

- right side `name`: parameter received by the method;
- left side `self.name`: attribute stored on the object.

Likewise `self.stock = stock` stores the incoming stock on that object.

## 6. Attributes

An **attribute** is a value associated with an object.

```python
print(pen.name)   # Pen
print(pen.price)  # 200
print(pen.stock)  # 4
```

Changing one object's attribute does not automatically change another object's attribute:

```python
pen.stock = 10
print(pen.stock)   # 10
print(book.stock)  # 7
```

Why? Pen and Book are different instances with separate instance state.

## 7. Methods: functions connected to objects

Start with an ordinary function:

```python
def inventory_value(price, stock):
    return price * stock
```

Now place the behaviour on Product:

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def inventory_value(self):
        return self.price * self.stock
```

Then:

```python
pen = Product("Pen", 200, 4)
print(pen.inventory_value())  # 800
```

When `pen.inventory_value()` runs, `self` refers to `pen`. Therefore `self.price` is 200 and `self.stock` is 4.

The same method works for Book using Book's state:

```python
book = Product("Book", 500, 7)
print(book.inventory_value())  # 3500
```

## 8. Methods can change object state

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def restock(self, quantity):
        self.stock += quantity
```

Trace:

```python
pen = Product("Pen", 200, 4)
pen.restock(3)
print(pen.stock)  # 7
```

Inside `restock`:

```text
self -> pen
quantity -> 3
self.stock += quantity
4 + 3 -> 7
```

**State** is the current data an object holds. Pen's stock state changed from 4 to 7.

## 9. __init__ precisely

People often call `__init__` the constructor. For this course, understand the more precise sequence:

1. Calling `Product(...)` starts object creation.
2. `__new__` creates the instance (normally inherited; you do not need to write it here).
3. Python passes that new instance to `__init__` as `self`.
4. `__init__` initializes its attributes.
5. The created object is returned by the class call and assigned to a variable.

Do not manually call `pen.__init__(...)` to create another product. Create another object with `Product(...)`.

## 10. References and aliases

This creates a new object:

```python
book = Product("Book", 500, 7)
```

This does **not**:

```python
alias = pen
```

Now `alias` and `pen` refer to the same object:

```python
alias.stock = 99
print(pen.stock)  # 99
```

This distinction matters when debugging mutation.

## 11. Bring Week 1 validation forward

Objects still need valid data:

```python
class Product:
    def __init__(self, name, price, stock):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be blank.")
        if type(price) is not int or price < 0:
            raise ValueError("Price must be a nonnegative integer.")
        if type(stock) is not int or stock < 0:
            raise ValueError("Stock must be a nonnegative integer.")

        self.name = name
        self.price = price
        self.stock = stock
```

Notice the connection:

```text
Week 1: validation + exceptions + state + functions
                         |
                         v
Week 2: objects with validated state + methods
```

Zero price and zero stock are valid because **nonnegative** means greater than or equal to zero. `bool` is deliberately rejected by exact type checks.

## 12. Protect a state-changing method

The assignment asks for positive integer restocking:

```python
def restock(self, quantity):
    if type(quantity) is not int or quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")
    self.stock += quantity
```

Validation happens before mutation. If quantity is invalid, stock remains unchanged. This is the same validation-first principle from Week 1.

## 13. Worked example: predict before running

```python
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

pen = Product("Pen", 4)
book = Product("Book", 7)
pen.stock -= 1
print(pen.stock, book.stock)
```

Before running it, answer:
1. How many objects are created?
2. What does `self` refer to during each initialization?
3. Which object's state changes?
4. What exactly will print, and why?

Then run it and compare prediction with reality.

## 14. Vocabulary you must be able to explain

- **Class:** definition used to create objects.
- **Object:** an individual runtime object.
- **Instance:** an object considered as belonging to a particular class.
- **Attribute:** data associated with an object/class.
- **Method:** function associated with a class/object.
- **self:** the current instance supplied to an instance method.
- **State:** current data held by an object.
- **Initialization:** setting up a newly created object's starting state.

Do not merely memorise these sentences. Explain each using Product/Pen.

## 15. Guided build

Build in this order:

1. `Product(name, price, stock)`; create Pen 200/4 and Book 500/7.
2. Print attributes and prove the objects are separate.
3. Add `inventory_value(self)`; Pen should return 800.
4. Validate construction; reject blank names and negative price/stock while allowing zero.
5. Add `restock(quantity)`; require a positive integer and reject bool.
6. Test success and failure. Confirm failed validation does not change state.
7. Try `alias = pen` and explain why changing alias changes pen.

## Understanding checkpoint

Before the assignment, you should be able to answer without notes:

1. Why might we use a class when dictionaries and functions already work?
2. What is the difference between `Product` and `pen`?
3. Explain `self.name = name` from both sides of the equals sign.
4. Why does changing `pen.stock` not change `book.stock`?
5. Why does changing `alias.stock` change `pen.stock` after `alias = pen`?
6. What makes `inventory_value` a method rather than an ordinary standalone function?
7. Why validate before changing stock?

Continue with the [ten-exercise assignment](../assignments/lesson-04/README.md). Use the [week references](../references.md), [setup guide](../../SETUP.md), and [offline checker guide](../../grading/README.md) when needed.

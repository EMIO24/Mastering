# Lesson 5: Class behaviour

**Goal:** Build on Lesson 4 and understand how classes control shared data, object display, validated attributes, and alternative constructors.

Do not start by memorising `classmethod`, `property`, or dunder methods. Start from the problems they solve.

## 1. What Lesson 4 gave us

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def inventory_value(self):
        return self.price * self.stock
```

Each Product has separate instance data. Now we ask: what information should be shared? How should an object display itself? How can we control assignments such as `product.stock = -5`?

## 2. Instance attributes versus class attributes

These belong to each individual object:

```python
self.name = name
self.price = price
self.stock = stock
```

They are **instance attributes**.

But suppose every Product uses Nigerian naira. Repeating this on every object is unnecessary. We can put shared/default information on the class:

```python
class Product:
    currency = "NGN"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
```

`currency` is a **class attribute**.

```python
pen = Product("Pen", 200, 4)
book = Product("Book", 500, 7)

print(pen.currency)   # NGN
print(book.currency)  # NGN
```

Mental model:

```text
Product class
└── currency = "NGN"   shared/default lookup

pen instance
├── name = "Pen"
├── price = 200
└── stock = 4

book instance
├── name = "Book"
├── price = 500
└── stock = 7
```

Python can find `pen.currency` through the class when the instance does not have its own `currency`.

## 3. Shadowing: an instance can have its own value

```python
pen.currency = "USD"

print(pen.currency)   # USD
print(book.currency)  # NGN
print(Product.currency)  # NGN
```

You did not change the class attribute. You created/found an instance-level value on Pen that shadows the class value during lookup.

This is why you must know **where authoritative state lives**.

## 4. The mutable class attribute trap

This is dangerous:

```python
class Product:
    tags = []
```

That one list is shared through the class. Mutating it through one instance can appear through others.

For per-object mutable data, create it in `__init__`:

```python
class Product:
    def __init__(self):
        self.tags = []
```

Now each instance receives its own list.

Rule of thumb for this lesson: immutable shared configuration may fit a class attribute; mutable per-object state normally belongs on each instance.

## 5. Why print(product) is not automatically useful

Without a useful string representation:

```python
print(pen)
```

may show something like an object type and memory-oriented representation, not the business information a human wants.

We can define `__str__`:

```python
class Product:
    def __str__(self):
        return f"{self.name}: {self.stock} units"
```

Then:

```python
print(pen)
```

can display:

```text
Pen: 4 units
```

`__str__` should **return a string**. It should not merely print.

Think: `__str__` answers, “How should this object be represented for a human reader?”

## 6. __repr__: useful developer representation

`__repr__` is generally aimed at an unambiguous/useful developer representation:

```python
def __repr__(self):
    return (
        f"Product(name={self.name!r}, "
        f"price={self.price!r}, stock={self.stock!r})"
    )
```

Then compare:

```python
print(str(pen))
print(repr(pen))
```

A practical mental model:
- `str`: friendly human-facing description;
- `repr`: developer/debugging-oriented description.

They are methods, and `self` still means the particular object being represented.

## 7. The problem with direct assignment

Lesson 4 validation can ensure construction starts valid:

```python
pen = Product("Pen", 200, 4)
```

But later somebody might do:

```python
pen.stock = -100
```

If stock is just a public attribute with no control, the object can become invalid after construction.

A **property** lets normal-looking attribute access run controlled logic.

## 8. Property from the ground up

We store the actual value in `_stock` and expose `stock` through a property:

```python
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if type(value) is not int or value < 0:
            raise ValueError("Stock must be a nonnegative integer.")
        self._stock = value
```

Now:

```python
pen.stock = 5
```

looks like ordinary assignment, but Python routes it through the setter.

If:

```python
pen.stock = -5
```

the setter raises before changing `_stock`.

Important: `_stock` is a naming convention meaning “internal implementation detail”; the underscore is not a security barrier.

## 9. Why __init__ can use self.stock

Notice:

```python
def __init__(self, name, stock):
    self.name = name
    self.stock = stock
```

Because `stock` is a property, `self.stock = stock` uses the setter during initialization too. That lets one validation rule protect both initial and later assignments.

## 10. classmethod: behaviour about the class

Instance methods receive `self`:

```python
def inventory_value(self):
    ...
```

A **class method** receives the class, conventionally called `cls`:

```python
@classmethod
def from_dict(cls, data):
    return cls(data["name"], data["price"], data["stock"])
```

Use:

```python
data = {"name": "Pen", "price": 200, "stock": 4}
pen = Product.from_dict(data)
```

Why `cls(...)` rather than hard-coding `Product(...)`? The method is written in terms of the class it was called on, which becomes useful with subclasses later.

A common use of class methods is an **alternative constructor**: another convenient route for creating an object from a different input format.

## 11. Instance method versus class method

```text
instance method
    receives self
    works with a particular object

class method
    receives cls
    works with the class / often creates objects
```

Do not choose based on syntax. Ask: “Does this behaviour need one particular Product, or does it concern the Product class/construction?”

## 12. Worked example

```python
class Product:
    currency = "NGN"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.currency})"

p = Product("Pen")
print(str(p))
```

Before running:
1. Which attribute is stored on `p`?
2. Where is `currency` stored?
3. Why can `self.currency` still find it?
4. What exact text does `__str__` return?

## 13. Putting the ideas together

```python
class Product:
    currency = "NGN"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if type(value) is not int or value < 0:
            raise ValueError("Stock must be a nonnegative integer.")
        self._stock = value

    def __str__(self):
        return f"{self.name}: {self.stock} units"

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r}, stock={self.stock!r})"

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"], data["stock"])
```

Do not read this as one giant block. Identify each responsibility:
- shared/default class data;
- instance initialization;
- controlled stock access;
- human display;
- debugging display;
- alternate construction.

## 14. Vocabulary

- **Instance attribute:** value stored on one object.
- **Class attribute:** value stored on the class and available through attribute lookup.
- **Property:** managed attribute access implemented through methods/descriptors.
- **Getter:** logic used when reading a managed value.
- **Setter:** logic used when assigning a managed value.
- **classmethod:** method receiving the class as `cls`.
- **__str__:** human-readable string representation.
- **__repr__:** developer-oriented representation.

## 15. Understanding checkpoint

Explain without copying definitions:

1. Why should Pen's stock usually be an instance attribute rather than a class attribute?
2. What happens if Pen shadows `currency` with its own value?
3. Why can a mutable list on a class create surprising behaviour?
4. Why must `__str__` return text rather than only print it?
5. What problem does a stock property solve?
6. Why does validation happen before `_stock` changes?
7. Difference between `self` and `cls`?
8. Why might `from_dict` be a classmethod?

Continue with the [ten-exercise assignment](../assignments/lesson-05/README.md). Use the [week references](../references.md), [setup guide](../../SETUP.md), and [offline checker guide](../../grading/README.md).

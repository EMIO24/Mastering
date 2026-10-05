# Lesson 6: OOP pillars and composition

**Goal:** Understand encapsulation, abstraction, inheritance, polymorphism, and composition as design ideas—not vocabulary to memorise—and use them deliberately in the checkout/payment exercises.

## 1. Why this lesson exists

By now you can create objects with data and methods. The next problem is design:

- Which object should be responsible for what?
- How do we stop callers from depending on every internal detail?
- How can different objects provide the same service?
- When should one class inherit from another?
- When should one object simply contain/use another?

These questions lead to the OOP ideas in this lesson.

## 2. Begin with a checkout without OOP jargon

Suppose checkout supports cash:

```python
def pay_cash(amount):
    return f"cash:{amount}"
```

Then transfer:

```python
def pay_transfer(amount):
    return f"transfer:{amount}"
```

Both perform the same kind of service: **pay an amount**.

We can model each payment strategy as an object:

```python
class CashPayment:
    def pay(self, amount):
        return f"cash:{amount}"

class TransferPayment:
    def pay(self, amount):
        return f"transfer:{amount}"
```

Different objects, same operation: `pay(amount)`.

That simple idea is the foundation for several concepts below.

## 3. Encapsulation

**Encapsulation** means grouping related state and behaviour and controlling interaction through an interface.

Example:

```python
class Product:
    def __init__(self, stock):
        self.stock = stock

    def sell(self, quantity):
        if quantity > self.stock:
            raise ValueError("Not enough stock.")
        self.stock -= quantity
```

Instead of every part of the program inventing its own stock-changing rules, Product can provide a controlled operation.

Think less “hide everything” and more:

> Keep responsibility together and provide controlled ways to use it.

Python does not make underscore-prefixed attributes truly private. Encapsulation is primarily a design boundary here.

## 4. Abstraction

Imagine paying by bank transfer. A checkout should not need to know every banking/network step.

It wants a simple operation:

```python
receipt = payment.pay(600)
```

**Abstraction** means exposing the operation the caller needs while hiding/isolating unnecessary implementation detail.

The caller knows **what service to request**. It does not need every detail of **how the service is performed**.

Real-world analogy: you drive a car using steering wheel and pedals without directly controlling fuel injection timing. The controls are an abstraction over more complicated mechanisms.

The analogy has limits: software abstractions are explicit contracts, not human judgement.

## 5. Contracts and interfaces

For this lesson, define what callers can rely on:

```text
pay(amount)

Input:
- positive whole-naira integer
- bool rejected

Success:
- returns receipt text

Invalid input:
- raises ValueError

Simulated refusal:
- raises RuntimeError
```

This is a **contract**. It tells callers what behaviour to expect.

Python does not require CashPayment and TransferPayment to share a parent class for this simple example. If both satisfy the operation the caller needs, the caller can use them similarly.

## 6. Polymorphism

```python
class CashPayment:
    def pay(self, amount):
        return f"cash:{amount}"

class TransferPayment:
    def pay(self, amount):
        return f"transfer:{amount}"

payments = [CashPayment(), TransferPayment()]

for payment in payments:
    print(payment.pay(600))
```

The loop does not ask:

```python
if type(payment) is CashPayment:
    ...
elif type(payment) is TransferPayment:
    ...
```

It simply asks each object to perform `pay(600)`.

**Polymorphism** means different objects can be used through a compatible/common operation.

Same request:

```text
pay(600)
```

Different behaviour:

```text
CashPayment     -> cash:600
TransferPayment -> transfer:600
```

The important idea is substitutability through behaviour, not merely “many forms” as a memorised phrase.

## 7. Composition

Now checkout needs a payment strategy.

One bad mental model would be:

> Checkout *is a* CashPayment.

That is not true. Checkout is not a kind of payment method.

Instead:

> Checkout *has/uses a* payment object.

```python
class Checkout:
    def __init__(self, payment):
        self.payment = payment

    def charge(self, amount):
        return self.payment.pay(amount)
```

Use:

```python
cash_checkout = Checkout(CashPayment())
transfer_checkout = Checkout(TransferPayment())

print(cash_checkout.charge(600))
print(transfer_checkout.charge(600))
```

This is **composition**: building an object using other objects.

Mental shortcut:
- inheritance often models **is-a**;
- composition often models **has-a / uses-a**.

It is a guide, not a law.

## 8. Dependency injection without scary terminology

Look again:

```python
Checkout(CashPayment())
```

Checkout does not create CashPayment internally. We give the dependency to Checkout from outside.

That is a simple form of **dependency injection**.

Why useful? We can replace the worker:

```python
Checkout(TransferPayment())
```

or during tests:

```python
Checkout(FakePayment())
```

without rewriting Checkout.

This is one reason composition improves testability.

## 9. Inheritance

Inheritance describes a class deriving behaviour/state from another class.

```python
class Product:
    def inventory_value(self):
        return self.price * self.stock

class DiscountedProduct(Product):
    pass
```

`DiscountedProduct` is a subclass of Product.

But inheritance should not be used merely because two classes share some code.

Ask:

> Is the child genuinely a kind of the parent, and can it honour the behaviour callers expect from the parent?

If callers expect `inventory_value()` to return a number, a subtype should not unexpectedly return unrelated receipt text.

## 10. Overriding

A subclass can provide its own implementation of an inherited method:

```python
class DiscountedProduct(Product):
    def __init__(self, name, price, stock, discount):
        super().__init__(name, price, stock)
        self.discount = discount

    def inventory_value(self):
        original = super().inventory_value()
        return original * (100 - self.discount) / 100
```

This is **method overriding**.

`super()` lets us call behaviour from the parent according to Python's method-resolution rules.

For Pen at 200 × 4:
- regular value = 800;
- 50% discount value = 400.

The operation remains conceptually compatible: both return an inventory value.

## 11. Inheritance and polymorphism together

```python
products = [
    Product("Pen", 200, 4),
    DiscountedProduct("Pen", 200, 4, 50),
]

for product in products:
    print(product.inventory_value())
```

The caller uses the same operation on both. The subtype can provide specialised behaviour while preserving the expected contract.

But remember: Python polymorphism does not always require inheritance. The Cash/Transfer example already demonstrated compatible behaviour without a common custom parent.

## 12. Composition versus inheritance

Suppose discounts vary frequently.

Inheritance approach:

```text
Product
└── DiscountedProduct
```

Composition approach:

```text
Product/Service
└── has PricingPolicy
       ├── RegularPricing
       └── PercentageDiscount
```

Composition can let you swap policies at runtime without creating a new Product subtype for every pricing rule.

Neither is automatically “better.” Choose based on the relationship and change you need to model.

Ask:
- Is this genuinely an **is-a** relationship?
- Or does this object merely **use/contain** another behaviour?
- Do I need to swap that behaviour independently?
- What contract must remain stable?

## 13. Protect state across multiple operations

Checkout introduces a sequencing problem.

Suppose stock is 4 and a customer wants 2.

Correct conceptual order:

```text
1. Validate quantity.
2. Validate available stock.
3. Calculate total.
4. Attempt payment.
5. Only if payment succeeds, reduce stock.
```

Why not reduce stock first?

Because payment may fail. Then your inventory would claim items were sold when payment never succeeded.

This connects directly to Week 1's **validation before mutation** principle.

```python
def sell(self, product, quantity):
    # validate first
    total = product.price * quantity
    receipt = self.payment.pay(total)  # may raise
    product.stock -= quantity          # only after success
    return receipt
```

The exact assignment adds the required validation rules.

## 14. Fakes and testability

Because Checkout receives a payment object, we can test it without a bank:

```python
class FakePayment:
    def __init__(self, should_fail=False):
        self.should_fail = should_fail
        self.amounts = []

    def pay(self, amount):
        self.amounts.append(amount)
        if self.should_fail:
            raise RuntimeError("Payment refused.")
        return f"fake:{amount}"
```

Now tests can verify:
- what amount Checkout attempted to charge;
- whether stock changed;
- whether a failed payment left stock unchanged;
- whether invalid stock/quantity prevented payment from being called.

This is composition producing a practical engineering benefit, not just OOP vocabulary.

## 15. The five core terms together

### Encapsulation
Keep related data/behaviour together and control how callers interact with it.

### Abstraction
Expose the useful operation while keeping unnecessary implementation detail behind it.

### Inheritance
Create a class based on another class's behaviour/state when a genuine subtype relationship exists.

### Polymorphism
Use different objects through a compatible operation/contract.

### Composition
Build an object by giving it/containing other objects that provide needed behaviour.

One checkout example can involve several at once. These are not mutually exclusive boxes.

## 16. Worked example: predict before running

```python
class Cash:
    def pay(self, amount):
        return f"cash:{amount}"

class Transfer:
    def pay(self, amount):
        return f"transfer:{amount}"

for payment in [Cash(), Transfer()]:
    print(payment.pay(600))
```

Before running:
1. How many payment objects are created?
2. Does the loop inspect their class names?
3. What operation does it rely on?
4. What exact two lines print?
5. Why is this polymorphism even without a custom shared parent?

## 17. Guided build mapped to the assignment

1. Write the `pay(amount)` contract first.
2. Implement CashPayment and TransferPayment to satisfy it.
3. Use both through the same call to demonstrate polymorphism.
4. Create Checkout and inject a payment object: composition.
5. Validate sale before payment; mutate stock only after success.
6. Build DiscountedProduct deliberately: inheritance + overriding.
7. Compare that with a composed pricing-policy design.
8. Inject FakePayment to test Checkout without network/bank dependencies.

Do these in order. Each stage exists to make one design idea observable.

## 18. Understanding checkpoint

Explain in your own words:

1. Difference between encapsulation and abstraction.
2. Why CashPayment and TransferPayment demonstrate polymorphism.
3. Why Checkout should contain/use a payment strategy rather than inherit from CashPayment.
4. What “is-a” and “has-a” are trying to help you decide.
5. What method overriding means.
6. Why inheritance is not simply a code-reuse trick.
7. Why payment must succeed before stock is reduced.
8. Why FakePayment becomes easy to use when Checkout receives its dependency from outside.
9. Give one example where composition is more flexible than inheritance.

Continue with the [ten-exercise assignment](../assignments/lesson-06/README.md). Use the [week references](../references.md), [setup guide](../../SETUP.md), and [offline checker guide](../../grading/README.md) when needed.

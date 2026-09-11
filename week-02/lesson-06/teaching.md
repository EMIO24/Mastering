# Lesson 6: OOP pillars and composition

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 5; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A checkout is a shop counter with a stable service contract. Cash and transfer staff can both accept payment. The counter can use a payment worker without becoming that worker; that is composition.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Encapsulation | Grouping data and behaviour behind an interface. | a counter controlling stock changes. |
| Abstraction | Exposing needed operations while hiding detail. | asking to pay without operating the bank. |
| Inheritance | Deriving behaviour from a base class. | a specialized version of a staff role. |
| Polymorphism | Using different objects through a common operation. | cash and transfer workers both accept pay. |
| Composition | Building an object using other objects. | a checkout has a payment worker. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

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

The loop only relies on pay(amount). Python does not require a shared parent class for this example. Inheritance is appropriate when a subtype can honour its parent contract; sharing a few lines is not sufficient reason.

**Prediction:** Enter the printed lines as a JSON list of strings.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Define a payment contract

In design.md specify pay(amount), positive whole-naira input, returned receipt text and failure behaviour. Give valid 600 and invalid -1 cases.

### Step 2: Implement two strategies

Write CashPayment and TransferPayment implementing the contract. Both reject nonpositive amounts before producing a receipt. Demonstrate both with 600.

### Step 3: Compose checkout

Implement Checkout(payment) that calls the injected payment object. Run the same checkout operation with each payment class without conditionals on class names.

### Step 4: Protect stock

Have checkout validate the sale before calling payment and decrease stock only after simulated payment success. A failing payment raises an exception; show unchanged stock.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: The loop only relies on pay(amount).

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-06/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

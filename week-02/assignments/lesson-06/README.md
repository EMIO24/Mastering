# Lesson 6 assignment: OOP pillars and composition

> **How to use this assignment:** Do one exercise at a time. Do not try to understand all ten at once. For every exercise, first read **What you are learning**, then **What to do**, then run the listed checks. Only after the code behaves correctly should you record the evidence. If a technical word is unfamiliar, return to this lesson's teaching notes before coding.

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A checkout is a shop counter with a stable service contract. Cash and transfer staff can both accept payment. The counter can use a payment worker without becoming that worker; that is composition.

Create Python modules for payments, checkout and products. Use Product(name, price, stock) from Lesson 4. Payments here are simulated: they return receipt text or raise an error and never contact a bank. Recreate stock before each independent sale test.

## Where to work and how to run it

Work in `week-02/assignments/lesson-06/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

From this assignment folder run `python checks.py`. Create checks.py with imports and test calls for the files you build. Put demonstrations in modules under `if __name__ == "__main__":` so imports do not launch them.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `design.md` |
| 4 | `payments.py` |
| 5 | `checkout.py` |
| 6 | `checkout.py` |
| 7 | `products.py` |
| 8 | `pricing.py` |
| 9 | `checks.py` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Encapsulation** | Grouping data and behaviour behind an interface. | a counter controlling stock changes. |
| **Abstraction** | Exposing needed operations while hiding detail. | asking to pay without operating the bank. |
| **Inheritance** | Deriving behaviour from a base class. | a specialized version of a staff role. |
| **Polymorphism** | Using different objects through a common operation. | cash and transfer workers both accept pay. |
| **Composition** | Building an object using other objects. | a checkout has a payment worker. |

### Assignment words in simpler English

- **Fixture:** the known starting data you use for a test. Example: Pen starts with stock 4.
- **Boundary case:** a value exactly at the edge of a rule. Example: selling all 4 items when stock is 4.
- **Expected result:** what you predict should happen before you run the code.
- **Actual result:** what really happened when you ran it.
- **Criterion:** one thing the marker is checking.
- **Artefact:** a real file or output you created.
- **Demonstrate:** actually run the code and show the result. Writing “it works” is not evidence.

## Exercise 1: Explain the five terms — 10 points

**Where to work:** under `## Exercise 1` in `answers.md`.

### What you are learning

This exercise checks whether you understand the lesson's five main terms. You are **not** being tested on memorising the definition word-for-word.

### What to do

For each of the five terms listed above:

1. Explain it in your own words, as if you were explaining it to another beginner.
2. Give one everyday example or analogy.
3. Explain how the analogy connects to the programming idea.

After all five, choose **one** analogy and explain one way the real Python concept is more precise than the analogy.

### Example of the style expected

Do not copy this as one of your answers:

> A function is like a service counter. You give the counter an order (arguments), work happens, and you may receive something back (return value). The analogy is imperfect because a Python function follows exact programmed instructions rather than human judgement.

### You are done when

You have five explanations in your own words, five connected examples/analogies, and one limitation of an analogy.

**Points:** 10 total — 2 points per term (1 for the meaning, 1 for showing that you understand it through the example). Manual criterion: `exercise_01`.

## Exercise 2: Predict and check the worked example — 10 points

**Where:** `exercise_02` in `submission.json`; reasoning in `answers.md`.

### What you are learning

This checks whether you can read code and predict what it will do **before** Python tells you the answer.

### What to do

Read the code below, but do not run it yet.

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

**Question:** Enter the printed lines as a JSON list of strings.

1. Predict the answer on your own first.
2. Write **why** you expect that answer under Exercise 2 in `answers.md`.
3. Run the code and compare the real result with your prediction.
4. In `submission.json`, replace only the `null` beside `"exercise_02"` with the required answer. Keep the file valid JSON.
5. If your prediction was wrong, keep a short note in `answers.md` explaining what you misunderstood and what rule corrected your thinking.

**Important:** do not put explanations inside `submission.json`. That file holds only the machine-checkable answer. Your reasoning belongs in `answers.md`.

<details>
<summary>Worked-example explanation — read after predicting</summary>

The loop only relies on pay(amount). Python does not require a shared parent class for this example. Inheritance is appropriate when a subtype can honour its parent contract; sharing a few lines is not sufficient reason.

</details>

**You are done when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Define a payment contract - 10 points

**Where:** `design.md`. Record results under Exercise 3 in `answers.md`.

**In simple terms — what you need to achieve:** In design.md specify pay(amount), positive whole-naira input, returned receipt text and failure behaviour. Give valid 600 and invalid -1 cases.

A contract tells callers what service they may request without knowing its internal details.

1. In design.md specify `pay(amount)` for this exercise: amount is a positive whole-naira integer, excluding bool; success returns receipt text and failure raises ValueError for invalid amounts.
2. Give a valid call with 600 and an invalid call with -1, including expected return/error behaviour.
3. State that a simulated payment refusal raises RuntimeError and must not pretend payment succeeded.
4. Define how checkout recognizes success: pay returns normally before stock changes.

**Test these cases before you call it finished:** the contract covers input, output and both failure categories. Map pay to a counter operation and receipt text to its returned evidence; no real transaction takes place.

**What to write in `answers.md`:** record: (1) what you ran, (2) the starting values, (3) what you expected, (4) what actually happened, and (5) one sentence explaining why. When a case is meant to be independent, create fresh objects so an earlier test cannot affect it.

**How this exercise is graded:** 6 points for the required implementation, 3 points for actually running and recording the required checks, and 1 point for your explanation. Manual criterion: `exercise_03`. Creating the file alone is not enough; the behaviour must work.

## Exercise 4: Implement two strategies - 10 points

**Where:** `payments.py`. Record results under Exercise 4 in `answers.md`.

**In simple terms — what you need to achieve:** Write CashPayment and TransferPayment implementing the contract. Both reject nonpositive amounts before producing a receipt. Demonstrate both with 600.

Different workers can perform the same named service.

1. In payments.py implement CashPayment and TransferPayment with `pay(self, amount)` following your contract.
2. Return distinguishable receipts, for example `cash:600` and `transfer:600`, using the actual amount.
3. Put both objects in a list and call pay(600) in one loop without checking their class names.
4. Try 0 and -1 on each; add text and Boolean values to verify the whole-number rule.

**Test these cases before you call it finished:** both implementations succeed for 600 and reject invalid amounts before producing a receipt. Explain polymorphism as one request understood by different workers, rather than an if/else chain naming every worker type.

**What to write in `answers.md`:** record: (1) what you ran, (2) the starting values, (3) what you expected, (4) what actually happened, and (5) one sentence explaining why. When a case is meant to be independent, create fresh objects so an earlier test cannot affect it.

**How this exercise is graded:** 6 points for the required implementation, 3 points for actually running and recording the required checks, and 1 point for your explanation. Manual criterion: `exercise_04`. Creating the file alone is not enough; the behaviour must work.

## Exercise 5: Compose checkout - 10 points

**Where:** `checkout.py`. Record results under Exercise 5 in `answers.md`.

**In simple terms — what you need to achieve:** Implement Checkout(payment) that calls the injected payment object. Run the same checkout operation with each payment class without conditionals on class names.

Composition means the checkout has a payment worker; it is not itself a payment subtype.

1. Define `Checkout(payment)` in checkout.py and retain the supplied object on the instance.
2. Add `charge(amount)` that delegates to `self.payment.pay(amount)` and returns its result.
3. Create one checkout with CashPayment and another with TransferPayment; charge 600 through both.
4. Check that checkout never asks which concrete payment class it has.

**Test these cases before you call it finished:** results distinguish cash and transfer while the Checkout code is identical. Replacing the worker only changes construction. Passing a worker missing pay should expose the interface problem rather than silently reporting success.

**What to write in `answers.md`:** record: (1) what you ran, (2) the starting values, (3) what you expected, (4) what actually happened, and (5) one sentence explaining why. When a case is meant to be independent, create fresh objects so an earlier test cannot affect it.

**How this exercise is graded:** 6 points for the required implementation, 3 points for actually running and recording the required checks, and 1 point for your explanation. Manual criterion: `exercise_05`. Creating the file alone is not enough; the behaviour must work.

## Exercise 6: Protect stock - 10 points

**Where:** `checkout.py`. Record results under Exercise 6 in `answers.md`.

**In simple terms — what you need to achieve:** Have checkout validate the sale before calling payment and decrease stock only after simulated payment success. A failing payment raises an exception; show unchanged stock.

A refused payment must leave the stock ledger untouched.

1. Extend Checkout with a sale operation accepting a product and quantity.
2. Validate positive whole-number quantity and available stock before calling payment. Calculate the total from product price.
3. Call pay(total). Deduct stock only after it returns successfully; let simulated RuntimeError propagate to the caller.
4. Use Pen price 200, stock 4 with quantity 2. Repeat from fresh stock with a worker whose pay raises RuntimeError.

**Test these cases before you call it finished:** success charges 400 and leaves stock 2; refusal leaves 4. Quantity 5 leaves 4 and makes no payment call. This is local sequencing, not a real bank/database distributed transaction.

**What to write in `answers.md`:** record: (1) what you ran, (2) the starting values, (3) what you expected, (4) what actually happened, and (5) one sentence explaining why. When a case is meant to be independent, create fresh objects so an earlier test cannot affect it.

**How this exercise is graded:** 6 points for the required implementation, 3 points for actually running and recording the required checks, and 1 point for your explanation. Manual criterion: `exercise_06`. Creating the file alone is not enough; the behaviour must work.

## Exercise 7: Use inheritance deliberately - 10 points

**Where:** `products.py`. Record results under Exercise 7 in `answers.md`.

**In simple terms — what you need to achieve:** Create a DiscountedProduct subtype with a value calculation that honours the base return type. Show base and subtype in one inventory list. Document discount bounds 0 through 100.

Inheritance should preserve the operation that callers rely on.

1. Define DiscountedProduct as a Product subtype with an additional discount percentage bounded from 0 to 100.
2. Override its value calculation to account for the discount, while returning a numeric amount as the base method does. Choose a rounding policy and document it; use exact whole-naira examples first.
3. Put base Pen 200/4 and a 50%-discounted Pen 200/4 in one list and call inventory_value on both.

**Test these cases before you call it finished:** values are 800 and 400; 0% gives 800, 100% gives 0, invalid discounts reject. Explain why a subtype returning receipt text would violate the shared numeric contract.

**What to write in `answers.md`:** record: (1) what you ran, (2) the starting values, (3) what you expected, (4) what actually happened, and (5) one sentence explaining why. When a case is meant to be independent, create fresh objects so an earlier test cannot affect it.

**How this exercise is graded:** 6 points for the required implementation, 3 points for actually running and recording the required checks, and 1 point for your explanation. Manual criterion: `exercise_07`. Creating the file alone is not enough; the behaviour must work.

## Exercise 8: Explain the alternative - 10 points

**Where:** `pricing.py`. Record results under Exercise 8 in `answers.md`.

**In simple terms — what you need to achieve:** Replace the discount subtype with a composed pricing policy in a separate example. Compare changing policies at runtime and the number of classes needed.

Composition offers another way to choose pricing without a new product subtype per policy.

1. In pricing.py define regular and percentage-discount policy objects with one common price/value operation.
2. Have a product or pricing service receive its policy as an input rather than inherit from it.
3. Calculate value for Pen 200/4 with a regular policy, then replace the policy with 50% off and calculate again.
4. Compare this design with Exercise 7 in answers.md: where is discount validation, and what changes when a new policy is added?

**Test these cases before you call it finished:** values are 800 then 400, without creating a discount subtype for the second calculation. Document policy replacement explicitly; do not change stored stock to simulate a discount.

**What to write in `answers.md`:** record: (1) what you ran, (2) the starting values, (3) what you expected, (4) what actually happened, and (5) one sentence explaining why. When a case is meant to be independent, create fresh objects so an earlier test cannot affect it.

**How this exercise is graded:** 6 points for the required implementation, 3 points for actually running and recording the required checks, and 1 point for your explanation. Manual criterion: `exercise_08`. Creating the file alone is not enough; the behaviour must work.

## Exercise 9: Substitute a fake - 10 points

**Where:** `checks.py`. Record results under Exercise 9 in `answers.md`.

**In simple terms — what you need to achieve:** Create a FakePayment recording amounts and optionally failing. Demonstrate one successful and one rejected checkout without a bank or network. Include the recorded call list.

A fake payment worker makes checkout checks repeatable without a network.

1. In checks.py implement FakePayment with an `amounts` list and a configurable failure flag.
2. Have pay append the requested amount, then return a receipt or raise RuntimeError according to the flag.
3. Inject it into Checkout. Sell two Pens from stock 4 at price 200, then repeat with a fresh failing fake and product.
4. Make an oversale attempt with another fresh fake to test validation order.

**Test these cases before you call it finished:** successful and refused payment attempts each record [400]; stock becomes 2 only after success. An oversale records [] because no payment was attempted. Explain why recording a call alone does not prove successful payment.

**What to write in `answers.md`:** record: (1) what you ran, (2) the starting values, (3) what you expected, (4) what actually happened, and (5) one sentence explaining why. When a case is meant to be independent, create fresh objects so an earlier test cannot affect it.

**How this exercise is graded:** 6 points for the required implementation, 3 points for actually running and recording the required checks, and 1 point for your explanation. Manual criterion: `exercise_09`. Creating the file alone is not enough; the behaviour must work.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose one payment implementation and one checkout failure. Inspect both the fake call list and product stock, not just receipt text. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**You are done when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Before grading

Stop and ask yourself: **Can I explain the code I wrote, change one input without help, and predict the result?** If not, revisit the relevant teaching section before treating the assignment as complete.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 6
python grade.py rubric --lesson 6
```

The first checks the JSON prediction and writes `grading/reports/lesson-06.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-06/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

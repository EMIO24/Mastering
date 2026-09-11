# Lesson 6 assignment: OOP pillars and composition

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

A **fixture** is known starting data, like a prepared sample shelf. A **boundary case** lies at the edge of a rule, such as requesting exactly the available stock. **Expected** is what the rule says should happen; **actual** is what you observed. A **criterion** is one part of the marking scheme. An **artefact** is a file or concrete result you created. **Demonstrate** means carry out the action and record its actual result, not merely say that it works.

## Exercise 1: Explain the five terms — 10 points

**Where:** Exercise 1 in `answers.md`.

1. Read the five topic terms above, then explain each in your own words.
2. Give an everyday analogy for each and map its parts explicitly. For example: “A function is like a service counter: arguments are the order and the returned value is the item handed back.” Use this form with this lesson's terms.
3. Explain one point where one of your analogies stops fitting the precise rule. Software cannot infer missing instructions through human judgement.

**Finished when:** all five terms have an accurate meaning and mapped analogy. Each earns 1 point for meaning and 1 for mapping. Manual criterion: `exercise_01`.

## Exercise 2: Predict and check the worked example — 10 points

**Where:** `exercise_02` in `submission.json`; reasoning in `answers.md`.

Use this exact example and the input/conditions in the question. This may be a code fragment or a message/query to trace. Use the setup above and the explanation below to place it correctly.

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

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

The loop only relies on pay(amount). Python does not require a shared parent class for this example. Inheritance is appropriate when a subtype can honour its parent contract; sharing a few lines is not sufficient reason.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Define a payment contract - 10 points

**Where:** `design.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** In design.md specify pay(amount), positive whole-naira input, returned receipt text and failure behaviour. Give valid 600 and invalid -1 cases.

A contract tells callers what service they may request without knowing its internal details.

1. In design.md specify `pay(amount)` for this exercise: amount is a positive whole-naira integer, excluding bool; success returns receipt text and failure raises ValueError for invalid amounts.
2. Give a valid call with 600 and an invalid call with -1, including expected return/error behaviour.
3. State that a simulated payment refusal raises RuntimeError and must not pretend payment succeeded.
4. Define how checkout recognizes success: pay returns normally before stock changes.

**Check:** the contract covers input, output and both failure categories. Map pay to a counter operation and receipt text to its returned evidence; no real transaction takes place.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Implement two strategies - 10 points

**Where:** `payments.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Write CashPayment and TransferPayment implementing the contract. Both reject nonpositive amounts before producing a receipt. Demonstrate both with 600.

Different workers can perform the same named service.

1. In payments.py implement CashPayment and TransferPayment with `pay(self, amount)` following your contract.
2. Return distinguishable receipts, for example `cash:600` and `transfer:600`, using the actual amount.
3. Put both objects in a list and call pay(600) in one loop without checking their class names.
4. Try 0 and -1 on each; add text and Boolean values to verify the whole-number rule.

**Check:** both implementations succeed for 600 and reject invalid amounts before producing a receipt. Explain polymorphism as one request understood by different workers, rather than an if/else chain naming every worker type.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Compose checkout - 10 points

**Where:** `checkout.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Implement Checkout(payment) that calls the injected payment object. Run the same checkout operation with each payment class without conditionals on class names.

Composition means the checkout has a payment worker; it is not itself a payment subtype.

1. Define `Checkout(payment)` in checkout.py and retain the supplied object on the instance.
2. Add `charge(amount)` that delegates to `self.payment.pay(amount)` and returns its result.
3. Create one checkout with CashPayment and another with TransferPayment; charge 600 through both.
4. Check that checkout never asks which concrete payment class it has.

**Check:** results distinguish cash and transfer while the Checkout code is identical. Replacing the worker only changes construction. Passing a worker missing pay should expose the interface problem rather than silently reporting success.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Protect stock - 10 points

**Where:** `checkout.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Have checkout validate the sale before calling payment and decrease stock only after simulated payment success. A failing payment raises an exception; show unchanged stock.

A refused payment must leave the stock ledger untouched.

1. Extend Checkout with a sale operation accepting a product and quantity.
2. Validate positive whole-number quantity and available stock before calling payment. Calculate the total from product price.
3. Call pay(total). Deduct stock only after it returns successfully; let simulated RuntimeError propagate to the caller.
4. Use Pen price 200, stock 4 with quantity 2. Repeat from fresh stock with a worker whose pay raises RuntimeError.

**Check:** success charges 400 and leaves stock 2; refusal leaves 4. Quantity 5 leaves 4 and makes no payment call. This is local sequencing, not a real bank/database distributed transaction.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Use inheritance deliberately - 10 points

**Where:** `products.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Create a DiscountedProduct subtype with a value calculation that honours the base return type. Show base and subtype in one inventory list. Document discount bounds 0 through 100.

Inheritance should preserve the operation that callers rely on.

1. Define DiscountedProduct as a Product subtype with an additional discount percentage bounded from 0 to 100.
2. Override its value calculation to account for the discount, while returning a numeric amount as the base method does. Choose a rounding policy and document it; use exact whole-naira examples first.
3. Put base Pen 200/4 and a 50%-discounted Pen 200/4 in one list and call inventory_value on both.

**Check:** values are 800 and 400; 0% gives 800, 100% gives 0, invalid discounts reject. Explain why a subtype returning receipt text would violate the shared numeric contract.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Explain the alternative - 10 points

**Where:** `pricing.py`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Replace the discount subtype with a composed pricing policy in a separate example. Compare changing policies at runtime and the number of classes needed.

Composition offers another way to choose pricing without a new product subtype per policy.

1. In pricing.py define regular and percentage-discount policy objects with one common price/value operation.
2. Have a product or pricing service receive its policy as an input rather than inherit from it.
3. Calculate value for Pen 200/4 with a regular policy, then replace the policy with 50% off and calculate again.
4. Compare this design with Exercise 7 in answers.md: where is discount validation, and what changes when a new policy is added?

**Check:** values are 800 then 400, without creating a discount subtype for the second calculation. Document policy replacement explicitly; do not change stored stock to simulate a discount.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Substitute a fake - 10 points

**Where:** `checks.py`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Create a FakePayment recording amounts and optionally failing. Demonstrate one successful and one rejected checkout without a bank or network. Include the recorded call list.

A fake payment worker makes checkout checks repeatable without a network.

1. In checks.py implement FakePayment with an `amounts` list and a configurable failure flag.
2. Have pay append the requested amount, then return a receipt or raise RuntimeError according to the flag.
3. Inject it into Checkout. Sell two Pens from stock 4 at price 200, then repeat with a fresh failing fake and product.
4. Make an oversale attempt with another fresh fake to test validation order.

**Check:** successful and refused payment attempts each record [400]; stock becomes 2 only after success. An oversale records [] because no payment was attempted. Explain why recording a call alone does not prove successful payment.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose one payment implementation and one checkout failure. Inspect both the fake call list and product stock, not just receipt text. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

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

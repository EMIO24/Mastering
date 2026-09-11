# Lesson 5 assignment: Class behaviour

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

Instance data is a note on one product card; class data is a notice on the stockroom wall. A mutable shared notice can accidentally collect changes from every card.

Copy your Product class from Lesson 4 into product.py. It accepts name, price and stock and validates its fields. Use separate Pen 200/4 and Book 500/7 objects. Keep the shared-list bug in a separate file so it does not contaminate the working class.

## Where to work and how to run it

Work in `week-02/assignments/lesson-05/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

From this assignment folder run `python checks.py`. Create checks.py with imports and test calls for the files you build. Put demonstrations in modules under `if __name__ == "__main__":` so imports do not launch them.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `product.py` |
| 4 | `product.py` |
| 5 | `product.py` |
| 6 | `product.py` |
| 7 | `product.py` |
| 8 | `shared_tags.py` |
| 9 | `identity_demo.py` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Class attribute** | A value stored on a class and found through attribute lookup. | a shared wall notice. |
| **Instance attribute** | A value stored on one instance. | a note on one card. |
| **Property** | Managed attribute access through methods. | a service window guarding a field. |
| **classmethod** | A method receiving the class as its first argument. | a factory that knows which card design to use. |
| **__str__** | The method producing a human-readable string. | the label printed for a customer. |

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
class Product:
    currency = "NGN"
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"{self.name} ({self.currency})"

p = Product("Pen")
print(str(p))
```

**Question:** Enter the exact text printed, without a newline.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

currency is looked up on the class because p has no currency attribute of its own. __str__ returns text; print then displays that text. Use properties when assignments need validation, rather than adding getters for every field.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Shared and separate data - 10 points

**Where:** `product.py`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Extend Product with class currency = "NGN" and per-instance stock. Change stock on one of two products; show the other is unchanged and both initially use NGN.

A class attribute is a notice shared through attribute lookup; instance attributes belong to individual cards.

1. Add `currency = "NGN"` directly inside Product, outside its methods. Keep stock assigned to self inside initialization.
2. Make Pen stock 4 and Book stock 7. Print each currency and stock.
3. Set only `pen.stock = 9`; inspect both objects. Then set `Product.currency = "USD"` and inspect currency again.

**Check:** stocks become 9 and 7; both currencies become USD if neither instance shadows currency. Restore NGN for later tasks. Explain why `pen.currency = "USD"` would instead create an instance-level override.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Display a product - 10 points

**Where:** `product.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Implement __str__ returning "Pen: 4 units" for name Pen and stock 4. Check zero stock and a different name. Keep printing outside the method.

`__str__` supplies friendly display text when print needs to show an object.

1. Add `__str__(self)` and return a string containing name, a colon, stock and the word units.
2. Use an f-string to insert actual attributes. Do not print from inside the method.
3. Run `print(str(Product("Pen", 200, 4)))` and `print(Product("Bag", 4000, 0))`.

**Check:** exact results are `Pen: 4 units` and `Bag: 0 units`. A different name must appear without modifying the method. Returning a number from __str__ is invalid; the method's result must be text.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Useful debugging text - 10 points

**Where:** `product.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Implement __repr__ including class name, name, price and stock. Show repr(product) and str(product), and explain which reader each helps.

`__repr__` is debugging text intended to help a programmer inspect the card.

1. Add `__repr__(self)` including the class name and all three constructor values.
2. Choose a readable form such as `Product(name='Pen', price=200, stock=4)`. Using `!r` in an f-string keeps quotes visible around a name.
3. Print `repr(pen)`, `str(pen)`, and a one-item list containing pen.
4. Explain which representation the list uses and why the debug version includes more fields.

**Check:** repr includes Product, Pen, 200 and 4; str still matches Exercise 4. A name containing an apostrophe remains understandable. The checker does not require one exact repr spelling.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Guard stock assignment - 10 points

**Where:** `product.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Use a stock property backed by _stock. Reject negatives, text, fractions and bool; allow 0. Attempt an invalid assignment and show the previous value remains intact.

A property is a service window that can inspect an assignment before accepting it.

1. Back the public stock attribute with `_stock`.
2. Add a `@property` getter returning `_stock` and a `@stock.setter` method that validates the incoming value before storing it.
3. Route initialization through `self.stock = stock` so construction and later assignment use the same rule.
4. Start at 4; assign 0 successfully, then separately attempt -1, "3", 2.5 and True.

**Check:** zero is accepted. Every invalid assignment raises ValueError and retains the previous stock. Inside the setter assign `_stock`, not `stock`, or the setter would repeatedly call itself.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Alternative constructor - 10 points

**Where:** `product.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Implement Product.from_dict(record) as a classmethod using cls. Accept name/price/stock and reuse validation. Demonstrate valid input and a missing required field with a clear error.

An alternative constructor translates another input format into the normal creation call.

1. Add `@classmethod` above `from_dict(cls, record)`.
2. Require keys name, price and stock. Report missing fields with a clear ValueError rather than silently inventing values.
3. Return `cls(...)` using those three values. Reuse constructor validation instead of copying it.
4. Call `Product.from_dict({"name":"Pen","price":200,"stock":4})` and inspect the returned object's fields.

**Check:** valid data creates a Product; missing stock and negative stock reject. Explain why using cls rather than the literal Product name supports subclasses inheriting this factory.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Fix a shared-list bug - 10 points

**Where:** `shared_tags.py`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Reproduce class tags = [] with two products. Append on one and show leakage. Move list creation into __init__, rerun, and show independent tags.

A mutable class-level list can behave like one shared notice that every product edits.

1. In shared_tags.py create a small demonstration class with `tags = []` in its class body.
2. Make two instances, append "sale" through the first and inspect both lists. Record the unexpected sharing.
3. In a separate corrected class create `self.tags = []` inside __init__.
4. Repeat the same two-instance experiment, then add a different tag to the second object.

**Check:** the broken pair both show sale. The corrected first has only sale and the corrected second has only its own tag. Keep both demonstrations; do not alter Product's working fields just to reproduce this bug.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Compare value and identity - 10 points

**Where:** `identity_demo.py`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Construct two separate products with identical fields. Document whether your class defines __eq__; demonstrate is and == and explain their observed results without claiming they mean the same thing.

Equality and identity answer different questions: matching card contents versus the same card.

1. In identity_demo.py make two separate Products with identical name/price/stock.
2. Print `a is b` and `a == b`. Inspect whether Product defines __eq__ or inherits default behaviour.
3. If no custom equality exists, document the observed default result. You may optionally define field equality, but explain the choice rather than claiming all classes compare by fields automatically.
4. Set `alias = a` and repeat both comparisons with alias.

**Check:** separate objects have identity False; alias identity is True. Your equality explanation must match the implementation actually used, including whether modifying a field changes the equality result.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose one property/factory operation and one identity or shared-state case. Use new objects so prior edits cannot influence your conclusion. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 5
python grade.py rubric --lesson 5
```

The first checks the JSON prediction and writes `grading/reports/lesson-05.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-05/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

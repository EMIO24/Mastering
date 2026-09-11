# Lesson 7 assignment: Modules and packages

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

Modules are labelled drawers in a workshop; packages group related drawers. Importing should make tools available, not unexpectedly start the whole shop.

Create inventory/ in this assignment folder with an empty inventory/__init__.py. Use plain Python calculation functions and a small CLI. Run package commands from this assignment folder, the parent of inventory/.

## Where to work and how to run it

Work in `week-03/assignments/lesson-07/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

From this assignment folder use `python main.py` initially and `python -m inventory` after adding inventory/__main__.py. `python -c "import inventory.calculations"` checks an import; it should not open a menu.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `inventory/calculations.py` |
| 4 | `inventory/cli.py` |
| 5 | `inventory/__main__.py` |
| 6 | `namespace_demo.py` |
| 7 | `imports.md` |
| 8 | `inventory/storage.py` |
| 9 | `project-notes.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Module** | A unit of Python code with its own namespace. | one tool drawer. |
| **Package** | A way to organize related modules. | a cabinet of drawers. |
| **Import** | Loading or accessing another module. | bringing a named tool to the bench. |
| **Namespace** | A mapping of names to objects. | labels within one drawer. |
| **Entry point** | Where an application begins running. | the shop opening switch. |

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
# Put this in totals.py
def line_total(price, quantity):
    return price * quantity

if __name__ == "__main__":
    print(line_total(200, 3))
```

**Question:** What number is printed when totals.py is run directly?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

When run as a script, __name__ is __main__ and the example prints 600. When imported as totals, the function becomes available but the guarded print is skipped. Imports can still execute any unguarded top-level statements.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Extract calculations - 10 points

**Where:** `inventory/calculations.py`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Move line_total and inventory_value into inventory/calculations.py; add __init__.py. Import them from main.py. Check 200*3 and empty inventory.

Separate reusable calculations from the program that talks to a person.

1. Create inventory/calculations.py and define `line_total(price, quantity)` and `inventory_value(products)` there. Products are dictionaries with price and stock.
2. Create main.py beside inventory/ and import the functions using `from inventory.calculations import line_total, inventory_value`.
3. Print line_total(200,3), an inventory with Pen 200/10 and Book 500/3, and an empty inventory's value.

**Check:** `python main.py` prints 600, 3500 and 0. There should be one implementation of each calculation; importing it should not require copy-pasting its body into main.py.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Separate interaction - 10 points

**Where:** `inventory/cli.py`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Move prompts into inventory/cli.py. Import calculations without any prompt or menu appearing. Record the command and observed silence.

An import should make a tool available without unexpectedly opening the shop.

1. Create inventory/cli.py with a main function containing a small repeatable menu and input prompts. Import calculations into this module.
2. Make root main.py call cli.main only inside its `if __name__ == "__main__":` block.
3. Run `python -c "import inventory.calculations; import inventory.cli"` from the assignment folder.
4. Then run `python main.py` and choose Quit.

**Check:** the import command finishes without prompts; direct execution displays the menu and quits normally. Moving a prompt to the top level would run it during import, even if other code has a main guard.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Create a package entry point - 10 points

**Where:** `inventory/__main__.py`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Add inventory/__main__.py calling the menu. Run python -m inventory from its parent folder and show that quitting returns to the shell.

A package entry point lets Python start a folder as an application.

1. Add inventory/__main__.py; import the CLI main function there and call it under a main guard.
2. Keep __init__.py present. Its job is not to start the interactive menu.
3. From the parent of inventory/, run `python -m inventory`, choose a calculation/list option, then quit.
4. Compare its behaviour with `python main.py` from Exercise 4.

**Check:** both start the same menu; importing inventory alone does not start it. The `-m` option asks Python to find and run a module/package through its module search path, not a file named -m.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Resolve names - 10 points

**Where:** `namespace_demo.py`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Create two modules each defining describe(). Import using module names and call both. Explain how qualification avoids overwriting a local name.

Module qualification distinguishes identical tool names in different drawers.

1. Create inventory/products.py and inventory/suppliers.py, each defining describe(). Make them return different text identifying the module's subject.
2. In namespace_demo.py import the modules, then call `products.describe()` and `suppliers.describe()` using your chosen import bindings.
3. Run the file and record both outputs.
4. Explain what would happen if you imported both functions into the same local name using two `from ... import describe` statements.

**Check:** both descriptions are callable and distinct. A later same-name import replaces the earlier local binding; the original module's function is not deleted.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Repair a circular import - 10 points

**Where:** `imports.md`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Draw a dependency cycle between cli and storage, then extract shared validation into a third module. Submit the before/after import graph and a working import.

A circular import is like two drawers each refusing to open until the other is open.

1. In imports.md draw a bad dependency: cli imports storage and storage imports cli for validation.
2. Identify validation as shared logic rather than user interaction. Create inventory/validation.py with a small record checker.
3. Make both CLI and storage import that checker; remove storage's dependency on cli.
4. Run `python -c "import inventory.cli; import inventory.storage"` and exercise one valid/invalid record.

**Check:** imports complete, validation remains available to both callers, and the new graph has no return arrow from storage to cli. You need not leave a crashing circular version in the working package.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Use stable file paths - 10 points

**Where:** `inventory/storage.py`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Resolve a sample data path relative to the relevant module with pathlib. Run from two working directories and show the same intended file is read.

A relative filesystem path starts from the process's working directory, which may change.

1. Put a sample notes.txt inside inventory/data/ containing `Pen stock: 4`.
2. In inventory/storage.py derive its path from `Path(__file__).resolve().parent`, then read it as UTF-8.
3. Expose that read through a small callable or script entry point; print the resolved path and text.
4. Run once from the assignment folder, then from another working directory using the full path to your script.

**Check:** both runs identify the same notes.txt and read `Pen stock: 4`. Explain why simply opening `data/notes.txt` without an anchored path can target the wrong folder.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Document the package - 10 points

**Where:** `project-notes.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Write a folder tree and one sentence per file explaining responsibility. Give exact run commands and show calculations can be reused without launching the UI.

Write instructions another learner can follow without knowing your folder layout.

1. In project-notes.md draw the actual file tree, including __init__.py, __main__.py, calculations, CLI, validation and storage.
2. Give one responsibility per file and show the import direction between them.
3. State the required working directory and exact commands for running the app and checking an import.
4. Add a short example reusing line_total from another script without opening the menu.

**Check:** a reader can reproduce a 600 total and quit the menu using only these instructions. Mark directories as directories; do not list generated __pycache__ files as source that someone must write.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose one reusable calculation and one import/path case. Run from a different working directory and explain which path or namespace is being resolved. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 7
python grade.py rubric --lesson 7
```

The first checks the JSON prediction and writes `grading/reports/lesson-07.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-07/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

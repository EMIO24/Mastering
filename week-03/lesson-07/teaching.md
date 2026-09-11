# Lesson 7: Modules and packages

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 6; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

Modules are labelled drawers in a workshop; packages group related drawers. Importing should make tools available, not unexpectedly start the whole shop.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Module | A unit of Python code with its own namespace. | one tool drawer. |
| Package | A way to organize related modules. | a cabinet of drawers. |
| Import | Loading or accessing another module. | bringing a named tool to the bench. |
| Namespace | A mapping of names to objects. | labels within one drawer. |
| Entry point | Where an application begins running. | the shop opening switch. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
# Put this in totals.py
def line_total(price, quantity):
    return price * quantity

if __name__ == "__main__":
    print(line_total(200, 3))
```

When run as a script, __name__ is __main__ and the example prints 600. When imported as totals, the function becomes available but the guarded print is skipped. Imports can still execute any unguarded top-level statements.

**Prediction:** What number is printed when totals.py is run directly?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Extract calculations

Move line_total and inventory_value into inventory/calculations.py; add __init__.py. Import them from main.py. Check 200*3 and empty inventory.

### Step 2: Separate interaction

Move prompts into inventory/cli.py. Import calculations without any prompt or menu appearing. Record the command and observed silence.

### Step 3: Create a package entry point

Add inventory/__main__.py calling the menu. Run python -m inventory from its parent folder and show that quitting returns to the shell.

### Step 4: Resolve names

Create two modules each defining describe(). Import using module names and call both. Explain how qualification avoids overwriting a local name.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: When run as a script, __name__ is __main__ and the example prints 600.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-07/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

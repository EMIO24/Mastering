# Lesson 28: Testing the backend

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 27; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

Tests are repeatable quality checks at the shop. A fixture sets up known stock; an assertion compares what happened with what should happen. A passing check proves only the cases it actually examines.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Test case | A repeatable check with setup, action and expected result. | one quality inspection. |
| Assertion | A condition that must hold for a test to pass. | the inspector’s comparison. |
| Fixture | Known data or environment used by a test. | the prepared sample shelf. |
| Unit test | A focused check of a small piece of behaviour. | testing one counter tool. |
| Integration test | A check of collaborating components. | rehearsing the whole checkout handoff. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
import unittest

def total(price, quantity):
    return price * quantity

class TotalTests(unittest.TestCase):
    def test_sale(self):
        self.assertEqual(total(200, 3), 600)

if __name__ == "__main__":
    unittest.main()
```

The assertion uses an independently known expected value. A test that calculates its expectation using the same broken logic can miss defects. Django TestCase adds database isolation; APIClient supports API request checks. Test both returned responses and persistent side effects.

**Prediction:** What expected numeric value does the assertion use?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Test a calculation

Write a standard-library unittest for sale totals with 200*3=600, zero stock value and another price. Show the exact discovery command and results.

### Step 2: Test validation

Add tests rejecting zero, negative, fractional and excessive sale quantities. Assert unchanged stock for every rejected case.

### Step 3: Test persistence

Use a temporary database/file fixture and verify a saved product can be reloaded. Keep tests independent from your working inventory.

### Step 4: Test the API contract

Use DRF APIClient for valid creation 201, invalid creation 400 and missing detail 404. Check response fields and row counts.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: The assertion uses an independently known expected value.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-28/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

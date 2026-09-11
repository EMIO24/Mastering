> Lesson 2 has been regraded: **79/85 (92.9%)**. See [the current regrade](lesson-02-exercises-01-07-regrade.md). The Lesson 2 scores below are historical; the Lesson 1 review is unchanged.

# Week 1 marking: Lesson 1 and Lesson 2 exercises 1–7

Reviewed 2026-09-10 against the assignment briefs, rubric files, submitted code and written answers. Scope confirmed by the learner: all of Lesson 1; only exercises 1–7 of Lesson 2. Submission code was left unchanged.

| Scope | Mark | Result |
| --- | --- | --- |
| Lesson 1, exercises 1–10 | **68/100** | Needs practice; types and debugging diagnostic minimums are unmet. |
| Lesson 2, exercises 1–7 | **62/85 (72.9%)** | Partial lesson assessment; menu mastery is not yet met. Exercises 8–10 excluded. |

## Lesson 1

| Exercise | Mark | Evidence and feedback |
| --- | --- | --- |
| 1: Values and types | 0/20 | The Number 1 answer section is empty. No predictions or value/type experiments submitted. |
| 2: Stock labels | 10/10 | All automatic checks pass, including 0, 1–5 and values above 5. |
| 3: Positive total | 10/10 | Loop, positive filtering and accumulation work. Running the submitted loop with the four prescribed input lists produced 8, 0, 0 and 7. Add the requested explanation of why the accumulator starts at zero. |
| 4: Product records | 9/10 | List 2/2, dictionaries 2/2, required data 1/2, targeted update 4/4. Category is spelled `Stationary` rather than the specified `Stationery`. Pen stays at 10 and Notebook changes from 3 to 8. Also use the requested name `catalogue`. |
| 5: Set and tuple | 10/10 | Categories are derived and deduplicated; coordinates are a tuple. Written dictionary/list explanations demonstrate the intended understanding. |
| 6: Inventory value | 10/10 | Fixture, changed price/stock and empty-list checks pass. |
| 7: Low-stock names | 10/10 | Selection, order, inclusive cutoff and empty-list checks pass. |
| 8: Product lookup | 5/10 | Match checks fail because the function prints `prod` without returning it. Missing/empty cases earn 3 and non-mutation earns 2. Remove the assumption that an ID can be compared with list length: IDs need not be consecutive. |
| 9: Print versus return | 4/5 | Cause 2/2 and corrected `total` function in starter.py 2/2. Explanation 0/1: Python permits assigning a call to `print`, but its return value is `None`; assignment itself is not forbidden. |
| 10: Append correction | 0/5 | The faulty assignment remains in practice.py and prints `None`. No correction or explanation was submitted. |

The official Lesson 1 marks, report and gradebook have been updated. Section scores: types 0/20, conditions/loops 20/20, collections 19/20, functions 25/30, debugging 4/10. Passing requires at least 80/100 and half the marks in each section.

## Lesson 2: exercises 1–7 only

| Exercises / criterion | Mark | Evidence and feedback |
| --- | --- | --- |
| 1–2: Input retries | 0/15 | `int(prompt)` converts the prompt text itself. `read_positive_integer('Quantity: ')` repeatedly prints the conversion error without ever calling `input`. The bounded check stopped the repeated output. |
| 1–2: Distinct messages | 3/5 | Partial credit for appropriate, distinct conversion and nonpositive messages in the source. The remaining 2 points require a working input/retry demonstration; the submitted helper cannot complete the required sequence. |
| 3: Lookup | 15/15 | Matching, missing, empty and unchanged-data checks all pass. Extra debugging prints can be removed for cleaner menu output. |
| 4: Successful sale | 10/10 | Selling 3 Notebooks returns 1500 and leaves 7; selling the remaining 7 leaves 0 with the correct total. |
| 5: Rejected sales | 25/25 | Invalid quantities, including Boolean, text, fractional, nonpositive and excessive values, raise ValueError without changing stock. Selling from zero stock is also rejected. |
| 6–7: Menu | 9/15 | Reviewer partial-credit breakdown: repeating menu/list/quit 4; numeric invalid-option recovery 1; successful sale/receipt 3; catching oversale and continuing 1. Missing: unknown-ID recovery 2, safe input-helper integration 2, displaying the specific sale error 1, saved journey evidence 1. |
| 8–10 | Excluded | Outside the requested scope: no deductions and no full-lesson pass/fail assigned. |

Observed menu cases:

- `1, 9, 1, 3`: lists products, rejects option 9, lists again and exits normally.
- `2, 99`: crashes with `UnboundLocalError` because `quantity` has not been assigned. An unknown product must return to the menu before attempting a sale.
- Oversell 11 Notebooks, then sell 3: rejection leaves stock 10; the successful sale prints total 1500 and remaining stock 7. Pen stock remains 20.
- Text menu option `hello`: unhandled `ValueError`.
- Quantity text `three`: unhandled `ValueError` in the menu's direct conversion.

`checks.py` contains only imports, and `debug-notes.md` is empty. The menu evidence above comes from reviewer-run checks, not submitted transcripts.

Lesson 2's score is recorded in this scoped report. Its official full-lesson report was not regenerated: the current input helper loops indefinitely, and the bundled checker runs all criteria in one worker, so a timeout would mask the independently passing lookup and sale checks. The existing behavior checks were instead run independently with a bounded output capture. No grader or submission code was modified.

## What to work on next

1. Finish Lesson 1's five original value/type predictions and the append correction and explanation. Keep predictions separate from observed results.
2. Return the matching dictionary from Lesson 1's lookup; compare IDs to record IDs rather than list length.
3. In Lesson 2, read a new response with `input(prompt)` inside each input-helper loop iteration, then convert that response.
4. Keep menu choices as strings; use the positive-integer helper for product IDs and quantities. For a missing product, display `Product not found` and continue the menu loop immediately.
5. Display the caught sale error so the user knows why the sale was rejected. Add direct checks and save the required menu journey.

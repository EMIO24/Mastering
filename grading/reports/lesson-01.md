# Lesson 1 feedback

**NEEDS PRACTICE**

Earned: **68/100**. Awaiting manual review: **0 points**.

Pending points are not failed points. A final grade requires all manual criteria to be reviewed.

Checked at: 2026-09-10T17:14:26+00:00

## types: 0/20 (reviewed)

Mark five predicted values and types using the assignment breakdown.

Exercise 1: answers.md has an empty Number 1 section; no original value/type predictions or experiments submitted. 0/20.

## stock_zero: 3/3 (passed)

Zero stock returns out.

Passed the automated behaviour cases.

## stock_low: 4/4 (passed)

Stocks 1 through 5 return low.

Passed the automated behaviour cases.

## stock_available: 3/3 (passed)

Stocks above 5 return available.

Passed the automated behaviour cases.

## positive_loop: 10/10 (reviewed)

Review iteration (3), positive check (3), and accumulation/result (4).

Exercise 3: iteration 3/3, positive filtering 3/3, accumulation 4/4. Executed the submitted loop with only the input fixture changed: mixed=8, empty=0, nonpositive=0, positive=7. Add the requested explanation of starting at zero.

## collections: 19/20 (reviewed)

Review the list/dictionaries (6), update (4), set (4), tuple (2), and explanation (4).

Exercise 4: outer list 2/2, dictionaries 2/2, required data 1/2 (Stationary instead of specified Stationery), targeted update 4/4. Execution preserves Pen stock 10 and changes Notebook 3 to 8. Exercise 5: derived set 4/4, tuple 2/2, dictionary/list explanations in answers.md 4/4. Use the requested catalogue variable name.

## inventory_total: 8/8 (passed)

Return correct inventory totals for multiple datasets.

Passed the automated behaviour cases.

## inventory_empty: 2/2 (passed)

Empty inventory has value zero.

Passed the automated behaviour cases.

## low_stock: 8/8 (passed)

Return matching names in order including the threshold.

Passed the automated behaviour cases.

## low_empty: 2/2 (passed)

Empty input returns an empty list.

Passed the automated behaviour cases.

## find_match: 0/5 (failed)

Find first and later records by ID.

AssertionError: Expected {'id': 1, 'name': 'Pen', 'price': 200, 'stock': 10}; received None

## find_missing: 3/3 (passed)

Missing IDs and empty input return None.

Passed the automated behaviour cases.

## find_unchanged: 2/2 (passed)

Lookup does not mutate records.

Passed the automated behaviour cases.

## debug: 4/10 (reviewed)

Review cause, correction, and explanation for both bugs.

Exercise 9: identifies print versus return 2/2; corrected total in starter.py 2/2; explanation 0/1 because assigning a print result is legal, but gives None. Exercise 10: 0/5; practice.py retains names = names.append(...), prints None, and has no correction or explanation.

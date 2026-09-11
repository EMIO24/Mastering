# Lesson 2 regrade: exercises 1?7

Reviewed 2026-09-10. **79/85 (92.9%)**, up from 62/85.

| Criterion | Mark |
| --- | --- |
| Input retries (exercises 1?2) | 15/15 |
| Distinct input messages (exercises 1?2) | 5/5 |
| Lookup (exercise 3) | 15/15 |
| Successful sales (exercise 4) | 10/10 |
| Rejected-sale stock protection (exercise 5) | 25/25 |
| Menu (exercises 6?7) | 9/15 |

The corrected `int(input(prompt))` accepts new input on each iteration. Testing `three`, `2.5`, `0`, `-2`, and ` 3 ` produced four appropriate error messages, five prompts, and integer 3. All four automatic criteria pass in the bundled checker.

Menu partial credit remains unchanged: repeating/list/quit 4, numeric invalid-option recovery 1, successful sale/receipt 3, oversale recovery 1. The list/invalid-option/list/quit journey exits normally. Overselling then buying 3 Notebooks produces total 1500 and stock 7.

The remaining six marks require:

- Unknown-ID recovery (2): ID 99 currently raises UnboundLocalError. Display Product not found and continue before attempting a sale.
- Safe input-helper integration (2): text menu options and quantities currently raise unhandled ValueError. Compare menu choices as strings and use the helper for IDs and quantities.
- Specific sale error (1): display the caught ValueError message instead of only Sorry!, try again.
- Saved journey evidence (1): checks.py contains only imports and debug-notes.md is empty.

The official Lesson 2 report and gradebook are updated: 79/100 with 15 points pending. Exercises 8?10 remain outside the requested scope, so this review uses 85 as its denominator. A full-lesson pass is not awarded, and the required menu mastery gate remains unmet. Submission code was unchanged.

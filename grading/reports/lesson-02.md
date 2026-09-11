# Lesson 2 feedback

**REVIEW PENDING**

Earned: **79/100**. Awaiting manual review: **15 points**.

Pending points are not failed points. A final grade requires all manual criteria to be reviewed.

Checked at: 2026-09-10T17:23:27+00:00

## input_retry: 15/15 (passed)

Retry invalid/fractional/nonpositive input and accept a whitespace-padded positive integer.

Passed the automated behaviour cases.

## input_messages: 5/5 (reviewed)

Demonstrate distinct conversion and nonpositive messages.

Regrade of exercises 1-7: supplied three, 2.5, 0, -2, and whitespace-padded 3. Helper prompts five times, returns actual int 3, and prints distinct whole-number and greater-than-zero messages. Full 5/5.

## lookup: 15/15 (passed)

Find records and handle missing/empty input without mutation.

Passed the automated behaviour cases.

## sale_success: 10/10 (passed)

A valid sale returns the total and reduces stock correctly.

Passed the automated behaviour cases.

## sale_invalid: 25/25 (passed)

Reject zero, negative, excessive, fractional, text, and Boolean quantities without mutation.

Passed the automated behaviour cases.

## menu: 9/15 (reviewed)

Demonstrate list/sell/quit, unknown IDs/options, and continued use after errors.

Regrade exercises 6-7: repeating/list/quit 4, numeric invalid-option recovery 1, successful sale and receipt 3, oversale caught and continued use 1. Still missing: unknown-ID recovery 2 (ID 99 causes UnboundLocalError), input-helper integration 2 (text option/quantity raises uncaught ValueError), displaying specific sale error 1, saved journey evidence 1. checks.py only imports; debug-notes.md empty. Exercises 8-10 excluded from requested review.

## debug: pending/15 (pending)

Review debug-notes.md, specific exceptions, and explanations of else/finally and validate-before-mutate.

Manual review and evidence required.

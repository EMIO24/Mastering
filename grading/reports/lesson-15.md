# Lesson 15 feedback

**REVIEW PENDING**

Earned: **0/100**. Awaiting manual review: **90 points**.

Pending points are not failed points. A final grade requires all manual criteria to be reviewed.

Checked at: 2026-09-08T11:22:37+00:00

## exercise_01: pending/10 (pending)

Terminology: five accurate definitions/analogies worth 2 each (1 meaning, 1 analogy with mapping).

Manual review and evidence required.

## exercise_02: 0/10 (failed)

Exact worked-example prediction in submission.json.

Missing or incorrect prediction. Trace the example and check JSON types, then retry.

## exercise_03: pending/10 (pending)

Draw products, suppliers, sales and sale_lines with keys and cardinalities. State which columns may be NULL and which are required. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_04: pending/10 (pending)

Show a duplicated supplier phone in three product rows. Move supplier details to a suppliers table and demonstrate one update changes the authoritative value. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_05: pending/10 (pending)

Write schema.sql with nonnegative stock/price checks, nonblank name validation at the application boundary, and unique product SKU. Demonstrate a duplicate SKU rejection. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_06: pending/10 (pending)

Implement a transaction that decreases stock and inserts a sale line. Starting stock 5, selling 2 commits stock 3 and one line. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_07: pending/10 (pending)

Cause line insertion to fail after the stock update in a disposable database. Show stock remains 5 and no sale line persists when starting from the original fixture. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_08: pending/10 (pending)

Populate at least 1000 products and use EXPLAIN QUERY PLAN on SKU lookup before/after an appropriate index. Save plans; explain extra write/storage cost. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_09: pending/10 (pending)

Trace two buyers attempting the last unit. Explain why reading then blindly writing loses correctness; propose an atomic conditional UPDATE and check its affected-row count. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_10: pending/10 (pending)

Independent verification: new normal case (3), boundary/failure case (3), reproducible commands and observed outputs (2), limitation and repair plan (2).

Manual review and evidence required.

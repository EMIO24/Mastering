# Lesson 26 feedback

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

Add an owner foreign key to Product and migrate. Plan how existing rows receive owners in a disposable fixture rather than silently assigning every real row. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_04: pending/10 (pending)

Filter the queryset to request.user. Seed A with two products and B with three; demonstrate their lists contain 2 and 3 records respectively. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_05: pending/10 (pending)

Have A request B’s detail, update and delete URLs directly. Verify no data exposure or mutation; document whether your scoped endpoint returns 404 or 403. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_06: pending/10 (pending)

Use perform_create(serializer.save(owner=request.user)) or equivalent. Submit B’s ID as A and show A cannot transfer ownership through writable input. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_07: pending/10 (pending)

Define staff read/write privileges explicitly and implement them. Demonstrate one allowed and one denied operation for an ordinary user and a staff user. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_08: pending/10 (pending)

Apply the same scope and permission rules to low-stock and sale actions. Show that a custom route cannot bypass another user’s inventory boundary. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_09: pending/10 (pending)

Write automated API tests covering anonymous/A/B/staff against list/detail/create/update/delete. Record expected status and database effect for each relevant case. Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).

Manual review and evidence required.

## exercise_10: pending/10 (pending)

Independent verification: new normal case (3), boundary/failure case (3), reproducible commands and observed outputs (2), limitation and repair plan (2).

Manual review and evidence required.

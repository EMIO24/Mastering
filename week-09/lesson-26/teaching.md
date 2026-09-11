# Lesson 26: Permissions and ownership

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 25; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

Signing in gets a visitor into reception; ownership checks decide which stockroom records that visitor may see or change. Hiding a door in the UI does not lock it.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Permission | A rule deciding whether an operation is allowed. | the room-access rule. |
| Object-level permission | Authorization concerning a particular record. | access to one specific cabinet. |
| Queryset scoping | Restricting queried records to those the user may access. | only bringing authorized cards to the desk. |
| Least privilege | Granting only access needed for a task. | issuing the fewest necessary keys. |
| Tenant | An isolated customer or organization sharing an application. | one business renting space in the building. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
# Inside an authenticated ProductViewSet
def get_queryset(self):
    return Product.objects.filter(owner=self.request.user)
```

Add an owner relation to Product first. Filtering prevents other users’ records appearing in list results and ordinary detail lookup. Object permissions do not automatically filter every list item; creation also needs explicit ownership assignment from request.user.

**Prediction:** User A owns 2 products and user B owns 3. How many should A see in this queryset?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Add ownership

Add an owner foreign key to Product and migrate. Plan how existing rows receive owners in a disposable fixture rather than silently assigning every real row.

### Step 2: Scope list results

Filter the queryset to request.user. Seed A with two products and B with three; demonstrate their lists contain 2 and 3 records respectively.

### Step 3: Block guessed IDs

Have A request B’s detail, update and delete URLs directly. Verify no data exposure or mutation; document whether your scoped endpoint returns 404 or 403.

### Step 4: Assign owner server-side

Use perform_create(serializer.save(owner=request.user)) or equivalent. Submit B’s ID as A and show A cannot transfer ownership through writable input.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Add an owner relation to Product first.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-26/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

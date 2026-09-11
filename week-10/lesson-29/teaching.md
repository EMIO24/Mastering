# Lesson 29: Query performance and caching

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 28; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

Performance work is timing the queue before changing the shop layout. Fetching one supplier per product is many trips to the same cabinet; a joined fetch can reduce those trips.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Latency | Elapsed time for an operation. | one customer’s waiting time. |
| Throughput | Operations completed per unit time. | customers served per minute. |
| N+1 queries | One initial query followed by a query per result. | one catalogue trip plus a supplier trip per card. |
| Cache | Stored reusable results. | a temporary copy at the counter. |
| Invalidation | Removing or updating cached results after changes. | replacing an outdated counter copy. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
# Product has a supplier ForeignKey.
products = Product.objects.select_related("supplier").order_by("id")
for product in products:
    print(product.name, product.supplier.name)
```

select_related joins single-valued relationships such as foreign keys. prefetch_related uses separate queries and joins results in Python, fitting collections. Fewer queries do not guarantee faster execution for every workload; measure representative data and response correctness.

**Prediction:** A naive list does 1 product query plus 1 supplier query for each of 5 products. How many queries is that?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Create a baseline

Seed at least 100 products with suppliers. Measure query count and elapsed time for a list endpoint with repeated trials; record fixture size and environment.

### Step 2: Expose N+1

Render each product’s supplier name without eager loading. Capture query count and explain the repeated pattern.

### Step 3: Join a foreign key

Apply select_related for supplier and measure again. Verify returned names and ordering are unchanged; report query counts before/after.

### Step 4: Prefetch a collection

For a many-to-many category relation or reverse sale lines, compare naive access with prefetch_related. Explain why select_related alone cannot serve that collection.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: select_related joins single-valued relationships such as foreign keys.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-29/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

# Lesson 11: HTTP requests and responses

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 10; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

HTTP is the order-and-receipt format at the counter. The method says the kind of action; the path names the resource; the status reports what happened. A receipt alone does not explain every business outcome.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| HTTP method | A request token expressing intended semantics. | the action on an order form. |
| Header | Metadata sent with a request or response. | delivery instructions. |
| Body | The message content. | the order details. |
| Status code | A numeric response classification. | the result stamp. |
| Idempotent | Having the same intended effect when repeated. | setting a shelf label to the same value twice. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```text
HTTP/1.1 201 Created
Content-Type: application/json
Location: /products/4

{"id":4,"name":"Pen","stock":10}
```

The blank line separates headers from the body. 201 means creation succeeded; Location can identify the created resource. GET should be safe; PUT is intended to be idempotent; POST is not generally idempotent. An identical status on repeated requests is not the definition of idempotency.

**Prediction:** Enter the response status code as a number.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Write a read request

Write a complete GET /products/4 HTTP/1.1 request with Host in requests.http. Include the blank line and explain why the path is not the method.

### Step 2: Write a create request

Add a POST /products request with Content-Type application/json and name/price/stock body. Include a matching 201 response with Location.

### Step 3: Classify failures

Write response examples for malformed input (400), missing authentication (401), forbidden access (403), missing resource (404), and server error (500). Explain a scenario for each.

### Step 4: Compare updates

Describe replacing a complete product with PUT versus changing stock with PATCH. Give request bodies and explicitly state your API’s required fields.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: The blank line separates headers from the body.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-11/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

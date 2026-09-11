# Lesson 10: How the web works

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 9; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A browser requesting a page resembles a customer sending an order to a shop address. DNS finds an address; the server handles the request. The analogy leaves out caches, proxies and repeated network connections.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Client | Software requesting a service. | the customer. |
| Server | Software handling requests. | the shop counter. |
| DNS | A system resolving domain names to records such as IP addresses. | an address directory. |
| URL | An address identifying a resource and access scheme. | a shop address plus department. |
| Port | A numbered network endpoint on a host. | a numbered service door. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
from urllib.parse import urlparse

u = urlparse("http://localhost:8000/products?low=1")
print(u.hostname, u.port, u.path)
```

localhost refers to the local machine; port 8000 selects the listening service. /products is a path handled by that service. The query carries extra request information. Parsing a URL does not contact a server.

**Prediction:** Enter the host, port and path from the example as a JSON list.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Draw one request

Draw browser -> name resolution -> connection -> server -> response -> browser rendering. Explain each arrow and distinguish transferred HTML from displayed pixels.

### Step 2: Dissect addresses

Break http://localhost:8000/products?low=1 into scheme, host, port, path and query in answers.md. Explain why localhost on a friend’s laptop is not your machine.

### Step 3: Serve a page locally

Create public/index.html with an inventory heading and two products. From public run python -m http.server 8000 --bind 127.0.0.1; open http://127.0.0.1:8000/ and record the response.

### Step 4: Inspect the request

Use browser Network tools to record request URL, method, status and content type for index.html. Explain each field using the shop analogy.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: localhost refers to the local machine; port 8000 selects the listening service.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-10/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

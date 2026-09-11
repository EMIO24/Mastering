# Lesson 25: JWT authentication

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 24; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A signed access token resembles a tamper-evident visitor pass. A verifier checks its signature and expiry. The printed claims are usually readable; a signature is not encryption.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| JWT | A compact token format carrying claims. | the visitor pass format. |
| Claim | A statement stored in a token payload. | a printed field on the pass. |
| Signature | Cryptographic integrity/authenticity protection. | the tamper-evident seal. |
| Access token | A credential used to access a protected resource. | the short-lived entry pass. |
| Refresh token | A credential used to obtain new access tokens. | the renewal voucher. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
{"sub":"user-7","exp":2000,"iss":"emio24"}

# Illustrative claims only; this is not a signed token.
# A verifier rejects it when current time is >= exp.
```

A complete verification policy checks signature, allowed algorithm, expiry and applicable issuer/audience rules. Decoding a payload alone does not authenticate anyone. Use a maintained authentication library; never build cryptography from this teaching sketch.

**Prediction:** At time 2001, is a token expiring at 2000 expired? Enter a Boolean.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Define the token flow

Draw login -> access/refresh tokens -> authenticated API request -> expiry -> refresh. Identify which steps require credentials and which can fail.

### Step 2: Configure library authentication

Use a maintained JWT integration compatible with your installed Django/DRF versions. Record its exact version and configure access-token authentication without implementing signatures yourself.

### Step 3: Obtain disposable tokens

Create token endpoints and request tokens for a local test user. Record statuses and claim names with credential/token values redacted.

### Step 4: Call a protected endpoint

Send an access token using Authorization: Bearer. Demonstrate a valid request and a missing/invalid credential rejection; record the configured status semantics.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: A complete verification policy checks signature, allowed algorithm, expiry and applicable issuer/audience rules.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-25/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

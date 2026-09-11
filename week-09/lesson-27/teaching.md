# Lesson 27: Application security foundations

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 26; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

Security resembles protecting a shop through several controls: checked inputs, locked cabinets and limited keys. One locked door does not protect an open back entrance.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Threat model | A description of assets, actors, trust boundaries and possible abuse. | the shop’s break-in map. |
| Injection | Untrusted data being interpreted as executable instructions. | an order form rewriting the clerk’s rules. |
| XSS | Untrusted script executing in a user’s browser context. | a forged notice running commands at reception. |
| CORS | Browser rules controlling cross-origin response access. | rules for which outside desks may read replies. |
| Secret | Sensitive material used to authenticate or protect systems. | a key rather than a public sign. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
# Bind values as data, never concatenate them into SQL.
cursor.execute("SELECT id FROM products WHERE name = %s", [user_input])
# This is Django cursor syntax; sqlite3 directly uses ? placeholders.
```

Parameterized SQL separates instruction structure from input values. CORS is enforced by browsers and does not authenticate clients. Keep Django template escaping and CSRF protection enabled for relevant browser flows, and store deployment secrets outside committed code.

**Prediction:** Does CORS replace API authentication? Enter a Boolean.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Map trust boundaries

Draw browser, API, database and deployment configuration. List stock records, credentials and customer information as assets with one realistic abuse case each.

### Step 2: Demonstrate safe query input

In a local fixture search for a name containing quotes using bound parameters. Show it is treated as a name and cannot change query structure.

### Step 3: Verify escaping

Render the literal product name <script>alert(1)</script> in a local template. Confirm it displays as text rather than executing. Document why marking user text safe changes this.

### Step 4: Check CSRF

With Django test client CSRF enforcement enabled, submit a session-authenticated write without a CSRF token and then with a valid token. Record expected rejection and success.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Parameterized SQL separates instruction structure from input values.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-27/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

# Lesson 40: Deployment, architecture and mock interview

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 39; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

Deployment moves the rehearsed shop into its operating premises. A release includes the building, configuration, ledger changes and a way to recover if opening goes wrong.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Deployment | Installing and configuring a runnable release in an environment. | opening the shop premises. |
| Reverse proxy | A server forwarding incoming requests to backend services. | the public reception desk. |
| Health check | A probe reporting a service’s operational condition. | a quick opening inspection. |
| Rollback plan | A documented way to recover from a failed release. | the plan for reopening the previous setup. |
| Observability | Understanding system behaviour from outputs such as logs and metrics. | the shop’s operational records and gauges. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
# Local release rehearsal, using the project environment
python manage.py check --deploy
python manage.py showmigrations
python manage.py test
# Inspect check output; do not assume zero warnings means all deployment work is complete.
```

Rehearse on a local production-like environment before choosing a host. Separate configuration and secrets, build frontend assets, use an appropriate production application server, plan migrations and backups, and test deep links and API routes. A health endpoint alone does not prove every dependency is healthy.

**Prediction:** Should a backup be restored in a rehearsal to verify recoverability? Enter a Boolean.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Draw the final architecture

Diagram browser, static assets, proxy, Django service, database and persistent storage. Label protocols, trust boundaries and which component owns stock.

### Step 2: Prepare release configuration

Document environment variable names, DEBUG=False, allowed hosts, HTTPS/cookie assumptions and dependency versions. Run check --deploy and explain each unresolved finding.

### Step 3: Build a release locally

Build frontend assets and run the backend with an appropriate production server in a local rehearsal. Record exact versions/commands and verify static assets plus an API request.

### Step 4: Rehearse migration and backup

Back up a disposable populated database, apply pending migrations, then restore into another disposable database. Verify product/sale counts and explain compatible rollback limits.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Rehearse on a local production-like environment before choosing a host.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-40/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

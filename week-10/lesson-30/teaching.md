# Lesson 30: Docker and reproducible services

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 29; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

An image is a packaged workshop template; a container is a running workshop made from it. A volume is storage kept outside that workshop’s replaceable walls.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Image | A layered template for container files and configuration. | the packaged workshop template. |
| Container | An isolated process environment created from an image. | one running workshop. |
| Dockerfile | Instructions for building an image. | the packaging recipe. |
| Volume | Storage managed independently of a container’s writable layer. | the external storeroom. |
| Port mapping | Connecting a host port to a container port. | linking an outside door to an inside counter. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```text
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

This is a development Dockerfile, not a production server configuration. requirements.txt must contain compatible dependencies. The process listens on all container interfaces so a published port can reach it. Building requires the base image and packages to be available locally or downloaded beforehand.

**Prediction:** With -p 8080:8000, which port does the browser use on the host?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Package development

Write a Dockerfile based on the example for your Django project. Include explicit dependency versions and describe every instruction.

### Step 2: Exclude unnecessary files

Write .dockerignore excluding .git, .venv, node_modules, .env and private local database files. Inspect build context contents for accidental data inclusion.

### Step 3: Build and identify

Build an emio24-dev image and record its image ID plus build output. If offline artifacts are missing, record the missing prerequisite rather than a fabricated build.

### Step 4: Run the service

Run a disposable container mapping host 8080 to 8000. Request the health endpoint, record 200, then stop the container.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: This is a development Dockerfile, not a production server configuration.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-30/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

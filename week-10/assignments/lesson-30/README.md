# Lesson 30 assignment: Docker and reproducible services

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

An image is a packaged workshop template; a container is a running workshop made from it. A volume is storage kept outside that workshop’s replaceable walls.

Copy the working Django source to project/ with requirements.txt. Dockerfile paths are relative to project/; run docker build there. Exclude private/generated files with .dockerignore. The example deliberately runs a development server; production rehearsal comes in Lesson 40.

## Where to work and how to run it

Work in `week-10/assignments/lesson-30/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside project/ run `docker build -t emio24-dev .`, then `docker run --rm -p 8080:8000 emio24-dev`. Request health locally on port 8080. Docker and compatible image/package artifacts must be available for offline builds. The later persistence exercise adds an explicit data mount.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `project/Dockerfile` |
| 4 | `project/.dockerignore` |
| 5 | `container-notes.md` |
| 6 | `container-notes.md` |
| 7 | `project/config/settings.py` |
| 8 | `container-notes.md` |
| 9 | `offline-runbook.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Image** | A layered template for container files and configuration. | the packaged workshop template. |
| **Container** | An isolated process environment created from an image. | one running workshop. |
| **Dockerfile** | Instructions for building an image. | the packaging recipe. |
| **Volume** | Storage managed independently of a container’s writable layer. | the external storeroom. |
| **Port mapping** | Connecting a host port to a container port. | linking an outside door to an inside counter. |

A **fixture** is known starting data, like a prepared sample shelf. A **boundary case** lies at the edge of a rule, such as requesting exactly the available stock. **Expected** is what the rule says should happen; **actual** is what you observed. A **criterion** is one part of the marking scheme. An **artefact** is a file or concrete result you created. **Demonstrate** means carry out the action and record its actual result, not merely say that it works.

## Exercise 1: Explain the five terms — 10 points

**Where:** Exercise 1 in `answers.md`.

1. Read the five topic terms above, then explain each in your own words.
2. Give an everyday analogy for each and map its parts explicitly. For example: “A function is like a service counter: arguments are the order and the returned value is the item handed back.” Use this form with this lesson's terms.
3. Explain one point where one of your analogies stops fitting the precise rule. Software cannot infer missing instructions through human judgement.

**Finished when:** all five terms have an accurate meaning and mapped analogy. Each earns 1 point for meaning and 1 for mapping. Manual criterion: `exercise_01`.

## Exercise 2: Predict and check the worked example — 10 points

**Where:** `exercise_02` in `submission.json`; reasoning in `answers.md`.

Use this exact example and the input/conditions in the question. This may be a code fragment or a message/query to trace. Use the setup above and the explanation below to place it correctly.

```text
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

**Question:** With -p 8080:8000, which port does the browser use on the host?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

This is a development Dockerfile, not a production server configuration. requirements.txt must contain compatible dependencies. The process listens on all container interfaces so a published port can reach it. Building requires the base image and packages to be available locally or downloaded beforehand.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Package development - 10 points

**Where:** `project/Dockerfile`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Write a Dockerfile based on the example for your Django project. Include explicit dependency versions and describe every instruction.

Package the development app with a repeatable recipe.

1. In project/Dockerfile choose the course Python base, set WORKDIR, copy requirements first, install them, then copy source.
2. Use a JSON-array CMD that runs the development server on 0.0.0.0:8000.
3. Explain each instruction and why copying requirements separately can reuse a dependency layer.
4. Check requirements reflect your working environment.

**Check:** the recipe contains the app's required files and an explicit startup command. This exercise packages development; runserver is not the production application server used in the release lesson.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Exclude unnecessary files - 10 points

**Where:** `project/.dockerignore`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Write .dockerignore excluding .git, .venv, node_modules, .env and private local database files. Inspect build context contents for accidental data inclusion.

Keep generated and private material outside the image's source bundle.

1. Create project/.dockerignore excluding .git, .venv, node_modules, .env, caches and private local database files.
2. Keep a harmless .env.example if useful, ensuring the ignore patterns do not unintentionally exclude required source.
3. Review Dockerfile COPY instructions against these patterns.
4. Inspect a disposable build image's /app listing after Exercise 5.

**Check:** source/configuration templates are present while the actual .env and private database are absent. A file inside the build context may be copied into image layers even if you remove it in a later instruction.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Build and identify - 10 points

**Where:** `container-notes.md`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Build an emio24-dev image and record its image ID plus build output. If offline artifacts are missing, record the missing prerequisite rather than a fabricated build.

A build result is an image, not yet a running service.

1. From project/ run `docker build -t emio24-dev .`.
2. Record relevant successful build output and the image ID from `docker image inspect emio24-dev`.
3. Run a disposable inspection such as `docker run --rm emio24-dev python --version`.
4. If offline resources are missing, identify the missing base image/package rather than recording an imagined build.

**Check:** the image exists and its interpreter runs. Installing Docker alone does not cache the selected base image or Python dependencies.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Run the service - 10 points

**Where:** `container-notes.md`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Run a disposable container mapping host 8080 to 8000. Request the health endpoint, record 200, then stop the container.

Map an outside door to the container's listening service.

1. Run `docker run --rm -p 8080:8000 emio24-dev` with the needed local configuration.
2. Open the app's health path at http://127.0.0.1:8080/health/.
3. Record status/body and the container's request log; then stop this disposable run.
4. Explain host port 8080 versus container port 8000.

**Check:** health returns the configured 200 response. The process must listen on 0.0.0.0 inside the container for the mapping; binding only its internal loopback can make it unreachable from the host mapping.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Pass configuration - 10 points

**Where:** `project/config/settings.py`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Provide a dummy environment variable at runtime and read it through settings. Show it is not baked into the Dockerfile or image source.

Runtime configuration should not require rebuilding the source image.

1. Make settings read a harmless DEMO_SHOP_NAME environment value with a documented fallback.
2. Run a disposable container with `-e DEMO_SHOP_NAME=PracticeShop` and print the setting through a shell command or harmless view.
3. Run again with a different value using the same image ID.
4. Inspect Dockerfile to ensure the runtime value was not hard-coded there.

**Check:** observed configuration changes without an image rebuild. Use fake settings here; do not print secrets as evidence or bake them into an image layer.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Persist outside the container - 10 points

**Where:** `container-notes.md`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Mount a dedicated practice volume for database/data storage. Create a product, replace the container using the same volume, and show the product persists.

Store the ledger outside the container's replaceable writable layer.

1. Configure SQLite/data storage at /data/inventory.sqlite3 and create a dedicated named volume, for example emio24-practice-data.
2. Run migrations in a disposable container with `--mount type=volume,src=emio24-practice-data,dst=/data`, using that database setting.
3. Run the app with the same mount, create a product, stop it, then start a replacement container with the same volume.
4. Query the product again and record its fields.

**Check:** the product survives container replacement. A volume mounted at a path the app never uses proves no persistence. Keep the practice volume distinct from useful data. [Volume reference](https://docs.docker.com/engine/storage/volumes/).

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Document offline readiness - 10 points

**Where:** `offline-runbook.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** List required Docker engine, base image and dependency artifacts. Write reproducible build/run/stop instructions and explain the production changes still needed before deployment.

Write a runbook that distinguishes prepared resources from downloadable names.

1. List required Docker engine, image/base artifacts, dependency files, environment variables and volume path.
2. Give exact build, migration, run, health-check and stop commands for your implementation.
3. Rehearse them from the documented starting state without relying on an unmentioned running container.
4. Explain what production still needs: proper application server, configuration, HTTPS/proxy and durable backup plan.

**Check:** another person can reproduce the local service and retained data. A command that needs an unavailable download is an offline prerequisite gap, not an offline success.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a successful container/configuration operation and a missing-resource or replacement-container case. Identify the actual data mount and image used. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 30
python grade.py rubric --lesson 30
```

The first checks the JSON prediction and writes `grading/reports/lesson-30.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-30/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

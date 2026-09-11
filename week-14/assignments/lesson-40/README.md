# Lesson 40 assignment: Deployment, architecture and mock interview

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

Deployment moves the rehearsed shop into its operating premises. A release includes the building, configuration, ledger changes and a way to recover if opening goes wrong.

Use Lesson 39 in a local release rehearsal; buying hosting or publishing is not required. Use a disposable populated database for backup/restore. Record application server, frontend build, configuration and actual runtime versions.

## Where to work and how to run it

Work in `week-14/assignments/lesson-40/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Run backend and frontend from their own project/ and frontend/ directories. For Lesson 39 use the project interpreter with `python manage.py runserver` and use `npm run dev` in a second terminal. In Lesson 40 use `npm run build` and your selected production application server; document its exact command and configuration. The assignment checker does not start these services.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `architecture.md` |
| 4 | `release-settings.md` |
| 5 | `release-notes.md` |
| 6 | `backup-rehearsal.md` |
| 7 | `release-checks.md` |
| 8 | `operations.md` |
| 9 | `interview.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Deployment** | Installing and configuring a runnable release in an environment. | opening the shop premises. |
| **Reverse proxy** | A server forwarding incoming requests to backend services. | the public reception desk. |
| **Health check** | A probe reporting a service’s operational condition. | a quick opening inspection. |
| **Rollback plan** | A documented way to recover from a failed release. | the plan for reopening the previous setup. |
| **Observability** | Understanding system behaviour from outputs such as logs and metrics. | the shop’s operational records and gauges. |

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
# Local release rehearsal, using the project environment
python manage.py check --deploy
python manage.py showmigrations
python manage.py test
# Inspect check output; do not assume zero warnings means all deployment work is complete.
```

**Question:** Should a backup be restored in a rehearsal to verify recoverability? Enter a Boolean.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Rehearse on a local production-like environment before choosing a host. Separate configuration and secrets, build frontend assets, use an appropriate production application server, plan migrations and backups, and test deep links and API routes. A health endpoint alone does not prove every dependency is healthy.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Draw the final architecture - 10 points

**Where:** `architecture.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Diagram browser, static assets, proxy, Django service, database and persistent storage. Label protocols, trust boundaries and which component owns stock.

Describe the system someone would operate, including where durable state lives.

1. Draw browser, static assets, reverse proxy, Django application server, database and persistent storage.
2. Label protocols and routing for document requests, assets and /api/ calls.
3. Mark trust boundaries and where secrets/configuration enter.
4. Trace one sale and identify authoritative stock and backup scope.

**Check:** each box maps to a component used in your local rehearsal. Do not draw a managed database or HTTPS service you have not selected; label planned components separately from tested ones.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Prepare release configuration - 10 points

**Where:** `release-settings.md`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Document environment variable names, DEBUG=False, allowed hosts, HTTPS/cookie assumptions and dependency versions. Run check --deploy and explain each unresolved finding.

Release configuration must be explicit and reproducible without copying secret values into notes.

1. Document environment variable names, dependency versions, DEBUG=False, allowed hosts and HTTPS/cookie assumptions.
2. Run `python manage.py check --deploy` with the rehearsal settings, not accidentally the development settings.
3. Record every unresolved finding and the change needed, distinguishing local-HTTP constraints from production requirements.
4. Check that missing required configuration fails clearly.

**Check:** the notes name actual settings and unresolved risks. Zero command exit status alone is not proof that an app is fully production-ready, backed up or reachable through the intended proxy.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Build a release locally - 10 points

**Where:** `release-notes.md`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Build frontend assets and run the backend with an appropriate production server in a local rehearsal. Record exact versions/commands and verify static assets plus an API request.

Rehearse a built release rather than relying on development hot reload.

1. Build the frontend with npm run build and serve its generated assets through your chosen static/proxy arrangement.
2. Run Django with an appropriate production application server compatible with your environment, recording its exact command/version. For example use a Windows-compatible WSGI server or a Linux container setup rather than assuming every server runs natively on Windows.
3. Request a document, static asset and API health route.
4. Record routing and statuses.

**Check:** the built frontend and production-server process actually run. Vite's development server plus Django runserver does not satisfy this release rehearsal.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Rehearse migration and backup - 10 points

**Where:** `backup-rehearsal.md`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Back up a disposable populated database, apply pending migrations, then restore into another disposable database. Verify product/sale counts and explain compatible rollback limits.

A backup is only a recovery plan after restoration has been tested.

1. Use a disposable populated database and record product/sale counts.
2. Take a consistent backup using the database's supported method; stop writes or use its online-backup facility rather than blindly copying a live database file.
3. Apply pending migrations in the rehearsal, then restore the backup into a separate disposable database with compatible schema/code.
4. Query counts and sample receipt totals after restoration.

**Check:** restored data matches recorded facts. Explain which migrations are reversible and why rolling code back does not automatically reverse a destructive data migration.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Verify release behaviour - 10 points

**Where:** `release-checks.md`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Check health, login, product CRUD, sale validation, authorization and frontend deep-link refresh. Record expected/actual results and unresolved failures.

Check a release as a user and as an operator.

1. In release-checks.md make rows for health, login, list/create/edit/delete, valid sale, oversale rejection, cross-owner denial and frontend deep-link refresh.
2. For each row state starting data, action, expected status/screen/database effect and actual result.
3. Run the journey against the built rehearsal, not an unrelated development instance.
4. Record failures and repeat only after the relevant fix.

**Check:** sale stock persists across refresh/restart and unauthorized access remains denied. A working health endpoint alone does not certify the other rows.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Write an operations runbook - 10 points

**Where:** `operations.md`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Document startup, shutdown, logs, health checks, failed-release recovery and secret rotation responsibilities. Include a simulated failure and the recovery steps you actually tried.

Write recovery instructions another operator can follow under pressure.

1. In operations.md give exact startup/shutdown commands, configuration locations, log access and health checks.
2. Document migration/backup order, failed-release recovery and responsibility for rotating secrets.
3. Simulate one local failure, such as stopping the app service, and follow your own recovery instructions.
4. Record symptoms, commands, recovery verification and any runbook correction.

**Check:** the procedure restores the intended service and confirms data. A proposed rollback that has never been tried must be labelled untested rather than presented as a demonstrated recovery.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Conduct the mock interview - 10 points

**Where:** `interview.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Write and speak answers to: trace a sale end to end; prevent overselling; explain ORM queries; distinguish authentication/authorization; explain React state/effects; identify your hardest bug. Record evidence, tradeoffs and one improvement for each.

Explain your implementation using evidence rather than memorized definitions.

1. In interview.md answer six prompts: trace a sale end to end; prevent overselling; explain ORM query timing; distinguish authentication/authorization; explain React state/effects; describe your hardest reproduced bug.
2. For each answer cite your own file/function or observed test, then state one tradeoff and one improvement.
3. Speak the answers aloud or rehearse with a partner; record which explanation was unclear and revise it.
4. Keep credentials and private data out of examples.

**Check:** all six answers connect concepts to your actual app. An analogy helps explain the mechanism but must not replace the technical rule or claim unimplemented behaviour.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new release operation and a failure/recovery scenario. Verify the running version, restored data and actual request results instead of merely reviewing configuration. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 40
python grade.py rubric --lesson 40
```

The first checks the JSON prediction and writes `grading/reports/lesson-40.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-40/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

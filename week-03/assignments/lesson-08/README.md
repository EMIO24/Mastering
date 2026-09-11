# Lesson 8 assignment: Virtual environments and dependencies

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

A virtual environment is a project toolbox. It keeps this project’s installed Python tools separate from another project’s tools, but it does not isolate the computer like a locked machine.

Create practice-project/ here and run environment commands inside it. .venv and .venv-rebuild are separate generated interpreter/package folders. Record evidence in environment.md beside practice-project/. No third-party package is assumed installed at the start.

## Where to work and how to run it

Work in `week-03/assignments/lesson-08/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside practice-project/ run `python -m venv .venv`, then `.venv/Scripts/python.exe -c "import sys; print(sys.executable)"` on Windows. Use `.venv/bin/python` on macOS/Linux. Record the interpreter path printed.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `environment.md` |
| 4 | `environment.md` |
| 5 | `environment.md` |
| 6 | `requirements.txt` |
| 7 | `environment.md` |
| 8 | `environment.md` |
| 9 | `environment.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Interpreter** | The program executing Python code. | the worker using the toolbox. |
| **Virtual environment** | An isolated Python package installation context. | a dedicated project toolbox. |
| **Dependency** | Software your program relies on. | a tool required for a job. |
| **Version pin** | A requirement naming an exact release. | specifying the exact tool model. |
| **Reproducibility** | Being able to recreate an environment or result. | another worker assembling the same toolbox. |

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

```python
import sys
from pathlib import Path

print(Path(sys.executable).name)
print(sys.prefix != sys.base_prefix)
```

**Question:** Inside a standard active venv, what Boolean does the second print produce?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

The executable path identifies the interpreter actually running the program. The prefix comparison is normally true inside a venv. Use python -m pip so pip belongs to that interpreter. Activation changes command lookup; directly invoking the venv interpreter also works.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Create a toolbox - 10 points

**Where:** `environment.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Run python -m venv .venv inside a practice project. Record the command, Python version and environment path. Exclude .venv from source control.

A virtual environment is a project-specific Python toolbox, not a replacement for the operating system.

1. Inside practice-project/ run `python -m venv .venv`.
2. Record the base interpreter's `python --version` output in environment.md.
3. Check that .venv/ contains Scripts/python.exe on Windows, or bin/python on macOS/Linux.
4. Add `.venv/` and `.venv-rebuild/` to the practice project's .gitignore if it has source control.

**Check:** the environment interpreter exists and reports a Python version. Do not submit thousands of environment files as authored code. If venv creation fails, record the actual error and resolve it before claiming the toolbox exists.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Use its interpreter - 10 points

**Where:** `environment.md`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** On Windows run .venv/Scripts/python.exe -c "import sys; print(sys.executable)". Record the full output and identify the project environment segment.

Typing python can select a different worker than you intended. Inspect the worker directly.

1. In practice-project/ run `.venv/Scripts/python.exe -c "import sys; print(sys.executable)"` on Windows; substitute .venv/bin/python on other systems.
2. Copy the printed path into environment.md and identify the .venv segment.
3. Run that interpreter with `-c "import sys; print(sys.prefix != sys.base_prefix)"`.
4. Compare with the unqualified python command from the same terminal.

**Check:** the explicit environment command points inside practice-project/.venv and the prefix comparison is True. No activation script is required when you invoke the interpreter by its full path.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Inspect dependencies - 10 points

**Where:** `environment.md`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Run the environment interpreter with -m pip list. Save output in environment.md; distinguish the standard library from installed third-party distributions.

Installed distributions are toolbox contents; standard-library modules are supplied with Python itself.

1. Run the environment interpreter with `-m pip list`, then `-m pip --version`.
2. Record distribution names/versions and the pip installation path. Do not assume an exact initial package count across Python versions.
3. Run `-c "import json, pathlib; print('standard library imports work')"` using the same interpreter.
4. Explain why importing json does not imply a json distribution must appear in pip list.

**Check:** commands use the same environment, pip reports an environment path, and both standard-library imports succeed. A package name on a website is not evidence it is installed locally.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Record requirements - 10 points

**Where:** `requirements.txt`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** For an installed project dependency, record its exact installed version in requirements.txt. If no packages are installed yet, document that and use the bundled standard-library app.

A requirements file lists tools needed to recreate the project.

1. Choose one actual third-party dependency already installed for your practice program and identify its exact version with pip show. If there are none, keep requirements.txt empty and explicitly document a standard-library-only project.
2. Write a requirement in `distribution-name==installed.version` form for that dependency. Do not paste the illustrative name/version literally.
3. Record why it is needed and the command that imports its module successfully.
4. Compare `pip freeze` output with the explicit file and explain any development-only packages you excluded.

**Check:** every listed version matches an installed distribution. An empty requirements file is valid only with the documented dependency-free route.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Prepare offline installation - 10 points

**Where:** `environment.md`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** When online, use python -m pip download -r requirements.txt -d wheelhouse with the intended interpreter/platform. Document that compatible dependency artifacts are required; do not claim a package name is an offline copy.

Offline installation needs actual package artifacts, not just the shopping list of names.

1. While online and using the intended project interpreter, run `-m pip download -r requirements.txt -d wheelhouse`.
2. List the downloaded filenames in environment.md. Record the Python version and operating system used to prepare them.
3. Explain that transitive dependencies are tools required by your selected tool; the download must include them too.
4. For a standard-library-only project, record that no third-party artifacts are required instead of inventing downloads.

**Check:** the artifacts exist on disk. A source archive may need build tools, so offline readiness is not proven until the clean rebuild in Exercise 8 succeeds.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Rebuild locally - 10 points

**Where:** `environment.md`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Create .venv-rebuild and, if using dependencies, install with -m pip install --no-index --find-links wheelhouse -r requirements.txt. Show an import and version. Record a missing wheel as a blocker, not success.

Rebuilding is the practical proof that a second toolbox can run the project.

1. Create `.venv-rebuild` with `python -m venv .venv-rebuild`.
2. Use its interpreter for `-m pip install --no-index --find-links wheelhouse -r requirements.txt`. `--no-index` prevents fetching missing packages from an online index.
3. Run the same import/small program used in Exercise 6 and record its output plus interpreter path.
4. If requirements is empty, run the standard-library import check instead.

**Check:** the fresh environment succeeds using local resources and points to .venv-rebuild. Missing artifacts are an actionable failure, not a passing offline test; record the missing package and prepare it before retrying.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Diagnose a mismatch - 10 points

**Where:** `environment.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Compare sys.executable and -m pip --version for two interpreters. Explain how a package can be installed for one while an import fails in the other; provide the corrected command.

A package installed for one interpreter is not automatically installed for every interpreter.

1. For your base Python and .venv Python, collect sys.executable and `-m pip --version`.
2. Compare their paths, then query one dependency with `-m pip show` under both.
3. If availability differs, demonstrate the differing import result. If both have it, explain the hypothetical mismatch using the actual paths; do not fabricate an error.
4. Write the corrected installation and execution commands that explicitly select the intended environment.

**Check:** your diagnosis names the mismatched interpreter, not merely “Python is broken.” Using python -m pip binds package management to the selected interpreter.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose one successful environment recreation/import and one missing-dependency or interpreter-selection scenario. Preserve actual interpreter paths in your evidence. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 8
python grade.py rubric --lesson 8
```

The first checks the JSON prediction and writes `grading/reports/lesson-08.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-08/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

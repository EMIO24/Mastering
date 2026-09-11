# Lesson 8: Virtual environments and dependencies

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 7; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A virtual environment is a project toolbox. It keeps this project’s installed Python tools separate from another project’s tools, but it does not isolate the computer like a locked machine.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Interpreter | The program executing Python code. | the worker using the toolbox. |
| Virtual environment | An isolated Python package installation context. | a dedicated project toolbox. |
| Dependency | Software your program relies on. | a tool required for a job. |
| Version pin | A requirement naming an exact release. | specifying the exact tool model. |
| Reproducibility | Being able to recreate an environment or result. | another worker assembling the same toolbox. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
import sys
from pathlib import Path

print(Path(sys.executable).name)
print(sys.prefix != sys.base_prefix)
```

The executable path identifies the interpreter actually running the program. The prefix comparison is normally true inside a venv. Use python -m pip so pip belongs to that interpreter. Activation changes command lookup; directly invoking the venv interpreter also works.

**Prediction:** Inside a standard active venv, what Boolean does the second print produce?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Create a toolbox

Run python -m venv .venv inside a practice project. Record the command, Python version and environment path. Exclude .venv from source control.

### Step 2: Use its interpreter

On Windows run .venv/Scripts/python.exe -c "import sys; print(sys.executable)". Record the full output and identify the project environment segment.

### Step 3: Inspect dependencies

Run the environment interpreter with -m pip list. Save output in environment.md; distinguish the standard library from installed third-party distributions.

### Step 4: Record requirements

For an installed project dependency, record its exact installed version in requirements.txt. If no packages are installed yet, document that and use the bundled standard-library app.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: The executable path identifies the interpreter actually running the program.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-08/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

# Lesson 9: Git and version control

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 8; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

Git is a project history album. The working tree is today’s desk, the staging area selects the next photograph, and a commit records that selection. A branch is a movable bookmark, not a duplicate folder.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Repository | Stored project history and metadata. | the history album. |
| Commit | A recorded project snapshot with metadata. | a labelled photograph. |
| Staging area | The proposed contents of the next commit. | the photo selection tray. |
| Branch | A movable reference to a commit. | a bookmark. |
| Merge conflict | Changes Git cannot combine automatically. | two incompatible edits to one caption. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```text
# Run in a new practice folder after git init
git status
git add notes.txt
git diff --cached
git commit -m "Add inventory notes"
```

Create notes.txt before these commands. git add stages its current contents; editing it afterward does not automatically change the staged version. git diff --cached shows what a commit would record. Set local user.name and user.email if Git requires an identity.

**Prediction:** Stage a file containing A, then edit it to B without staging again. Which text will the next commit record?
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Start local history

Create a separate practice folder, git init, and a notes.txt describing EMIO24. Record git status before and after adding the file. Avoid changing a parent repository.

### Step 2: Inspect the staging area

Stage notes.txt, edit it again, and save git diff and git diff --cached. Identify which version would be committed and then commit intentionally.

### Step 3: Ignore generated files

Add .venv/, __pycache__/, .env and local data outputs to .gitignore. Create a dummy .env containing only fake values; show git status excludes it.

### Step 4: Make a feature branch

Create feature/low-stock with git switch -c. Change a practice function and commit. Save git log --oneline --all --graph.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Create notes.txt before these commands.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-09/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

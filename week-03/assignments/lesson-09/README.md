# Lesson 9 assignment: Git and version control

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

Git is a project history album. The working tree is today’s desk, the staging area selects the next photograph, and a commit records that selection. A branch is a movable bookmark, not a duplicate folder.

Create git-practice/ here and run Git commands inside it. Initialize the repository there, not in a parent. Create notes.txt before staging. If Git requests an identity, set user.name and user.email for this practice repository. Record the original branch name with git branch --show-current. No remote repository or push is required.

## Where to work and how to run it

Work in `week-03/assignments/lesson-09/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside git-practice/ start with `git init` and `git status`. Read command output before proceeding. Save evidence in history.md outside the practice repository. All required operations are local.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `history.md` |
| 4 | `history.md` |
| 5 | `history.md` |
| 6 | `history.md` |
| 7 | `history.md` |
| 8 | `history.md` |
| 9 | `history.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Repository** | Stored project history and metadata. | the history album. |
| **Commit** | A recorded project snapshot with metadata. | a labelled photograph. |
| **Staging area** | The proposed contents of the next commit. | the photo selection tray. |
| **Branch** | A movable reference to a commit. | a bookmark. |
| **Merge conflict** | Changes Git cannot combine automatically. | two incompatible edits to one caption. |

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
# Run in a new practice folder after git init
git status
git add notes.txt
git diff --cached
git commit -m "Add inventory notes"
```

**Question:** Stage a file containing A, then edit it to B without staging again. Which text will the next commit record?

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Create notes.txt before these commands. git add stages its current contents; editing it afterward does not automatically change the staged version. git diff --cached shows what a commit would record. Set local user.name and user.email if Git requires an identity.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Start local history - 10 points

**Where:** `history.md`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Create a separate practice folder, git init, and a notes.txt describing EMIO24. Record git status before and after adding the file. Avoid changing a parent repository.

A repository records snapshots inside a chosen project boundary.

1. In a fresh git-practice/ folder run `git init`. Create notes.txt containing a short description of EMIO24.
2. Run `git status`, then `git add notes.txt`, then status again.
3. If a commit later asks for identity, configure local user.name/user.email in this repository, using your intended author identity.
4. Record the repository path and both status outputs in history.md outside git-practice/.

**Check:** notes.txt starts untracked and becomes staged. Do not initialize or alter a parent repository to complete this exercise. No network or remote is required.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Inspect the staging area - 10 points

**Where:** `history.md`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Stage notes.txt, edit it again, and save git diff and git diff --cached. Identify which version would be committed and then commit intentionally.

The staging area selects the next snapshot, not every edit currently on your desk.

1. Stage notes.txt containing a line `Inventory draft A`.
2. Change that line to `Inventory draft B` without staging again.
3. Run `git diff` and `git diff --cached`; explain which comparison shows B and which shows the staged A.
4. Commit the staged version with `git commit -m "Record inventory draft A"`, then inspect `git show HEAD:notes.txt` and status.

**Check:** the commit contains A while the working file contains B. Stage and commit B afterward so subsequent branch work starts clean. Record both commit messages and hashes rather than assuming staging happens automatically.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Ignore generated files - 10 points

**Where:** `history.md`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Add .venv/, __pycache__/, .env and local data outputs to .gitignore. Create a dummy .env containing only fake values; show git status excludes it.

An ignore rule prevents new generated/private files from being offered for tracking.

1. Create .gitignore containing `.venv/`, `__pycache__/`, `.env` and your practice generated-data folder.
2. Make a dummy .env with only `DEMO_SETTING=fake`; do not use a real secret.
3. Run `git status --short` and `git check-ignore -v .env`.
4. Stage/commit .gitignore, then explain what would happen if .env had already been tracked before the rule existed.

**Check:** .env is excluded and check-ignore identifies the rule. Ignore rules do not erase tracked history; this exercise should start with an untracked dummy file.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Make a feature branch - 10 points

**Where:** `history.md`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Create feature/low-stock with git switch -c. Change a practice function and commit. Save git log --oneline --all --graph.

A branch is a movable history bookmark, not a new folder on disk.

1. Record the current branch using `git branch --show-current`; call it your original branch in notes.
2. Run `git switch -c feature/low-stock`.
3. Add a small Python low-stock function or improve an existing practice one. Run its boundary checks, then stage and commit the change.
4. Capture `git log --oneline --all --graph` and `git status`.

**Check:** feature/low-stock points at the new commit and the working tree is clean. The original branch has not moved just because you committed while another branch was selected.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Merge a change - 10 points

**Where:** `history.md`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Switch to your original branch and merge the feature branch. Demonstrate the added function and document whether the merge fast-forwarded.

A merge brings the feature's history into the branch currently checked out.

1. Switch back to the exact original branch name you recorded.
2. Run `git merge feature/low-stock` and read the output before continuing.
3. Execute the low-stock function checks again and inspect the combined graph.
4. Explain whether this merge fast-forwarded: that means the branch pointer could move ahead without a separate merge commit.

**Check:** the original branch now contains the tested feature. Do not claim a merge commit was created if the actual operation fast-forwarded. Save the command output as evidence.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Resolve a practice conflict - 10 points

**Where:** `history.md`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** In two local branches edit the same line differently and merge. Record conflict markers, choose a coherent final line, stage and finish the merge. Run the affected program.

A conflict means Git needs a person to decide how competing edits fit together.

1. From a clean common commit create two practice branches, conflict-a and conflict-b, each changing the same notes.txt line differently and committing it.
2. On conflict-a run `git merge conflict-b`. Record the conflict output and the marked section of the file.
3. Edit that section into one coherent final line, removing `<<<<<<<`, `=======` and `>>>>>>>` markers.
4. Stage the resolved file, finish the merge with a commit, and inspect status/log.

**Check:** Git reports no unresolved paths, the file contains your intended line, and the history includes both branches. If your chosen changes merge automatically, retry on the same original line rather than fabricating a conflict.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Undo with history - 10 points

**Where:** `history.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Create a disposable incorrect commit then use git revert on it. Show that both the mistake and reversal remain in the log. Explain why this differs from deleting shared history.

Revert records an undo as another snapshot, preserving the historical explanation.

1. On your disposable practice branch make an intentionally wrong change and commit it. Record that commit's hash.
2. Run `git revert --no-edit HASH`, replacing HASH with the recorded identifier.
3. Show the file's corrected contents and `git log --oneline -3`.
4. Explain how this differs from deleting commits or rewriting shared history.

**Check:** both the erroneous commit and its reversal remain visible; the working content matches the pre-error version. Use this exercise's disposable mistake, not an unrelated commit in another repository.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose one local history operation and one conflicting/unstaged-change case. Compare file contents, staged contents and commits rather than relying only on a clean-status message. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 9
python grade.py rubric --lesson 9
```

The first checks the JSON prediction and writes `grading/reports/lesson-09.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-09/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

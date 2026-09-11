# Python / Django / React Full-Stack Developer Accelerator

Build **EMIO24 Business OS**, beginning with a small Python inventory program and gradually growing it into a full-stack product.

## Start here

Open [Week 1](week-01/README.md). All 40 lessons now include analogy-based teaching and terminology explanations, with exactly 10 detailed exercises per lesson: **400 exercises total**. Each assignment has a 100-point rubric. Read the [terminology glossary](glossary.md), [setup guide](SETUP.md), and [offline checker guide](grading/README.md).

The original plan has 40 lessons at three lessons per week: 13 weeks cover Lessons 1–39, with a final Week 14 session for Lesson 40. Allow more time for the final project if needed.

| Week | Lessons | Focus |
| --- | --- | --- |
| [01](week-01/README.md) | 1–3 | Python diagnostic, exceptions, files and persistence |
| [02](week-02/README.md) | 4–6 | Classes, class behaviour, OOP pillars |
| [03](week-03/README.md) | 7–9 | Modules, environments, Git |
| [04](week-04/README.md) | 10–12 | Web, HTTP, REST APIs |
| [05](week-05/README.md) | 13–15 | SQL, relationships, database design |
| [06](week-06/README.md) | 16–18 | Django architecture, migrations, ORM |
| [07](week-07/README.md) | 19–21 | CRUD, forms, authentication |
| [08](week-08/README.md) | 22–24 | DRF serializers, views, routers |
| [09](week-09/README.md) | 25–27 | JWT, permissions, security |
| [10](week-10/README.md) | 28–30 | Testing, performance, Docker |
| [11](week-11/README.md) | 31–33 | JavaScript, modern syntax, async APIs |
| [12](week-12/README.md) | 34–36 | React components, state, effects |
| [13](week-13/README.md) | 37–39 | React routing, architecture, integration |
| [14](week-14/README.md) | 40 | Deployment, architecture, mock interview |

## How to use a lesson

1. Read the objectives and analogy.
2. Predict each example's output before running it.
3. Change an input and explain what changes.
4. Complete the assignment in its own folder.
5. Record evidence against the checklist: an output, a short explanation, or a demonstrated behaviour.

Use Python 3 for Week 1; its examples need only the standard library. From this folder, check `python --version`. On Windows, use `py` instead of `python` if that is how your interpreter is installed. A text editor and terminal are enough. Git and virtual environments are taught later.

Checked boxes mean you can demonstrate a skill, not merely that you read about it.

## Grade your work offline

From this folder run:

```powershell
python grade.py check --lesson 1
python grade.py check --all
```

The checker runs Week 1 Python behaviour tests and later lessons' worked-example prediction checks. Written answers and practical projects have explicit local review rubrics; their scores stay pending until reviewed. No internet is needed for the checker. Framework practice requires the tools described in [setup](SETUP.md).

# Mastering

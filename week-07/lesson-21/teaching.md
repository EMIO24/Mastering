# Lesson 21: Authentication and sessions

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 20; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

Authentication checks who is at the door; authorization decides which room they may enter. A session cookie is a reference to signed-in state, not permission to do everything.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Authentication | Establishing an identity. | checking an identity card. |
| Authorization | Deciding whether an identity may perform an action. | checking the room-access list. |
| Session | Server-side interaction state associated with a client identifier. | the desk’s record for a visitor ticket. |
| Password hash | A one-way password verification representation with a work factor. | a verification imprint rather than a readable password. |
| Logout | Ending the client’s authenticated session. | invalidating the visitor ticket. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def dashboard(request):
    return JsonResponse({"username": request.user.username})
```

Django authentication middleware populates request.user. login_required normally redirects anonymous browser visitors to login. It does not enforce product ownership or staff privileges. Use Django password APIs rather than storing or comparing plaintext passwords.

**Prediction:** Is checking a signed-in user owns a product authentication or authorization? Enter the term.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Create local users

Create two disposable users through Django APIs or management commands. Use set_password/create_user; demonstrate check_password works without saving plaintext in notes.

### Step 2: Add login

Use Django’s LoginView and a login template. Configure redirect paths. Show correct credentials reach a dashboard and incorrect credentials produce a useful error.

### Step 3: Guard a view

Protect dashboard with login_required. Record the anonymous redirect and authenticated 200 response.

### Step 4: Implement logout

Use a CSRF-protected POST logout form. After logout, revisit dashboard and confirm authentication is required again.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Django authentication middleware populates request.user.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-21/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

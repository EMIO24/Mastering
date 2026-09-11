# Lesson 16: Django architecture and request flow

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 15; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

Django routes a visitor through a reception desk: the URL dispatcher selects a view, the view coordinates work, and a template formats the response. A model handles stored records.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Framework | Reusable structure that calls your application code. | a staffed building where you fill assigned roles. |
| Project | Django configuration for a site. | the building’s central plan. |
| App | A reusable unit of Django functionality. | one department. |
| View | A callable handling a request and returning a response. | the selected service desk. |
| Template | A document pattern rendered with data. | a reusable receipt layout. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
# inventory/views.py
from django.http import JsonResponse

def health(request):
    return JsonResponse({"status": "ok"})

# inventory/urls.py
from django.urls import path
from .views import health
urlpatterns = [path("health/", health)]
```

Create an inventory app inside a Django project and include its URLs at the root to expose /health/. A request reaches the view only after URL resolution. JsonResponse converts the dictionary to JSON and sets its content type. runserver is a development server.

**Prediction:** Enter the JSON response body for GET /health/ as an object.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Create the project

With Django 5.2 available in your environment, run python -m django startproject config . in a new project folder and python manage.py startapp inventory. Save version and folder tree.

### Step 2: Register the department

Add inventory to INSTALLED_APPS and create inventory/urls.py. Include it from config/urls.py. Explain project URLs versus app URLs.

### Step 3: Add health status

Implement the shown health view and route. Request /health/ locally; expect status 200, JSON content type and status ok.

### Step 4: Render HTML

Add a home view and inventory/home.html template with an EMIO24 heading. Pass shop_name as context and verify it appears in the response.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Create an inventory app inside a Django project and include its URLs at the root to expose /health/.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-16/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

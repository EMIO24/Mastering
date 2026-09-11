# Lesson 24: ViewSets, routers and pagination

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 23; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

A ViewSet groups related counter services; a router prints the directory mapping URLs and methods to those services. The directory does not decide who is allowed through the door.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| ViewSet | A class grouping resource actions. | one resource department. |
| Router | A generator of URL patterns for ViewSets. | the printed counter directory. |
| Action | A named operation on a ViewSet. | a service offered at the counter. |
| basename | The base used for generated route names. | the directory’s naming prefix. |
| Pagination | Bounding collection responses into pages. | handing out catalogue pages. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```python
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="product")
urlpatterns = router.urls
```

Define ProductViewSet with a queryset and serializer_class, then include these URLs beneath /api/. The list/create path is products/; detail actions include a lookup value. Route names such as product-list derive from basename, not necessarily the model class.

**Prediction:** Enter the generated list route name for basename product.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Create a ViewSet

Implement ProductViewSet using ModelViewSet, Product queryset and serializer. Preserve your existing validation rules.

### Step 2: Register routes

Register products with basename product under /api/. Use reverse for product-list and product-detail and record resolved URLs.

### Step 3: Verify CRUD routing

Record method/path/action mappings for list, create, retrieve, update, partial_update and destroy. Test one success and one missing detail.

### Step 4: Bound collection size

Configure page-number pagination with page size 2. Seed five products and verify page lengths 2, 2, 1 with stable ID ordering.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Define ProductViewSet with a queryset and serializer_class, then include these URLs beneath /api/.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-24/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

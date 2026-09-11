# Lesson 37: React routing

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson 36; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

Client routing is the shop directory inside the browser. It chooses the displayed page for a URL. A hidden route or redirect is a convenience for users; the API must still enforce its own locks.

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
| Client-side route | A mapping from browser location to UI. | the internal shop directory. |
| Route parameter | A variable segment of a matched route. | the card number on a directory entry. |
| Navigation | Moving to another location/page. | walking to a listed department. |
| History | The browser’s sequence of navigable locations. | the visitor’s route trail. |
| Fallback route | UI shown when no specific route matches. | the directory’s unknown-room desk. |

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```javascript
// React Router declarative mode; import from your installed package.
<Routes>
  <Route path="/products" element={<ProductListPage />} />
  <Route path="/products/:id" element={<ProductDetailPage />} />
  <Route path="*" element={<NotFoundPage />} />
</Routes>
```

Place Routes inside a BrowserRouter and import the components from your installed React Router package (record its version). The detail page reads id with useParams. A production server must serve the app entry for appropriate client routes on refresh, while preserving API/static routes.

**Prediction:** For /products/7 matched by /products/:id, enter the id parameter as a string.
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

### Step 1: Install and document routing

Use a compatible locally available React Router package, record version/import package, and wrap the app in BrowserRouter. Show the initial route renders.

### Step 2: Create list and detail routes

Implement /products and /products/:id pages. Read the ID parameter and display the matching local product; distinguish unknown ID from loading.

### Step 3: Navigate with links

Use router links from list cards to details. Demonstrate navigation and browser Back/Forward while preserving coherent page content.

### Step 4: Add a fallback

Show an accessible NotFound page for /unknown with a link back to products. Explain how unknown UI routes differ from API 404 responses.

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: Place Routes inside a BrowserRouter and import the components from your installed React Router package (record its version).

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-37/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).

# Lesson 37 assignment: React routing

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

Client routing is the shop directory inside the browser. It chooses the displayed page for a URL. A hidden route or redirect is a convenience for users; the API must still enforce its own locks.

Use the React app with working product pages. Add a compatible React Router package and record its import path/version. Wrap the app in BrowserRouter with Routes/Route inside. Use product IDs 1/2/3 for navigation checks.

## Where to work and how to run it

Work in `week-13/assignments/lesson-37/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

Inside frontend/ use the prepared dependencies and run `npm run dev`; open its printed URL. If starting fresh, while online run `npm create vite@latest frontend -- --template react` from the assignment folder, then `npm install` inside frontend/. Check its Node requirement and keep package-lock.json. JSX goes in src components, not a Python file or plain browser console. Offline work requires dependencies prepared in advance.

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
| 3 | `frontend/src/main.jsx` |
| 4 | `frontend/src/App.jsx and pages` |
| 5 | `frontend/src/ProductCard.jsx` |
| 6 | `frontend/src/NotFoundPage.jsx` |
| 7 | `frontend/src/ProductListPage.jsx` |
| 8 | `frontend/src/App.jsx` |
| 9 | `deep-link-notes.md` |

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
| **Client-side route** | A mapping from browser location to UI. | the internal shop directory. |
| **Route parameter** | A variable segment of a matched route. | the card number on a directory entry. |
| **Navigation** | Moving to another location/page. | walking to a listed department. |
| **History** | The browser’s sequence of navigable locations. | the visitor’s route trail. |
| **Fallback route** | UI shown when no specific route matches. | the directory’s unknown-room desk. |

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

```javascript
// React Router declarative mode; import from your installed package.
<Routes>
  <Route path="/products" element={<ProductListPage />} />
  <Route path="/products/:id" element={<ProductDetailPage />} />
  <Route path="*" element={<NotFoundPage />} />
</Routes>
```

**Question:** For /products/7 matched by /products/:id, enter the id parameter as a string.

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{"exercise_02": 12}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

Place Routes inside a BrowserRouter and import the components from your installed React Router package (record its version). The detail page reads id with useParams. A production server must serve the app entry for appropriate client routes on refresh, while preserving API/static routes.

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.

## Exercise 3: Install and document routing - 10 points

**Where:** `frontend/src/main.jsx`. Record results under Exercise 3 in `answers.md`.

**Required outcome:** Use a compatible locally available React Router package, record version/import package, and wrap the app in BrowserRouter. Show the initial route renders.

The router needs one browser-location provider around its route tree.

1. Install/use a compatible React Router package and record the version and import package you use.
2. In main.jsx wrap App with BrowserRouter; do not nest another BrowserRouter accidentally inside App.
3. Add a simple products route and verify it renders at /products.
4. Record start command and local URL.

**Check:** navigation components receive router context and the console has no missing-router error. Match imports to the installed version. [Declarative setup reference](https://reactrouter.com/start/declarative/installation).

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_03`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 4: Create list and detail routes - 10 points

**Where:** `frontend/src/App.jsx and pages`. Record results under Exercise 4 in `answers.md`.

**Required outcome:** Implement /products and /products/:id pages. Read the ID parameter and display the matching local product; distinguish unknown ID from loading.

A route parameter is URL text identifying the requested product.

1. Add routes for /products and /products/:id with separate list/detail page components.
2. In the detail page use useParams, then validate/convert the ID to match your numeric fixture/API convention.
3. Load/display Pen for its known ID and show a useful missing-product state for an absent ID.
4. Distinguish a request still loading from a completed lookup with no match.

**Check:** known detail shows the correct product; an unknown ID does not leave an endless spinner. The parameter is initially a string, so strict comparison with numeric IDs needs an intentional conversion.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_04`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 5: Navigate with links - 10 points

**Where:** `frontend/src/ProductCard.jsx`. Record results under Exercise 5 in `answers.md`.

**Required outcome:** Use router links from list cards to details. Demonstrate navigation and browser Back/Forward while preserving coherent page content.

Router links update browser location while keeping navigation history coherent.

1. Make product cards link to their detail URLs using Link or the installed router's equivalent.
2. Navigate list → Pen detail → list → Book detail.
3. Use browser Back and Forward and record location and displayed page at each step.
4. Inspect whether your chosen link caused an unnecessary full page reload.

**Check:** history restores the matching UI for each URL. A button that changes visible content without updating location does not satisfy route navigation in this task.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_05`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 6: Add a fallback - 10 points

**Where:** `frontend/src/NotFoundPage.jsx`. Record results under Exercise 6 in `answers.md`.

**Required outcome:** Show an accessible NotFound page for /unknown with a link back to products. Explain how unknown UI routes differ from API 404 responses.

Unknown UI paths need a clear destination of their own.

1. Add a wildcard route displaying NotFoundPage with a heading and a products link.
2. Visit /unknown directly through the local app and use its return link.
3. Compare this page with a known detail route whose product ID does not exist.
4. Explain browser-rendered fallback content versus an API's HTTP 404 response.

**Check:** both cases are understandable but represent different failures: unmatched UI route versus matched route with missing data. A client-side NotFound screen does not automatically change the document server's HTTP status.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_06`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 7: Reflect filters in the URL - 10 points

**Where:** `frontend/src/ProductListPage.jsx`. Record results under Exercise 7 in `answers.md`.

**Required outcome:** Store a search/filter value in query parameters. Copy the URL into a new tab and show the same filter is restored.

A URL can carry enough state to reproduce a filtered catalogue.

1. Store the name filter in a query parameter, such as q, using useSearchParams or equivalent.
2. Initialize the displayed filter from the URL and update it when the user searches.
3. Search for Pen, copy the complete URL and open it in another tab.
4. Use Back/Forward to check your chosen history policy.

**Check:** the second tab restores the same filter and matching products. Keep unrelated query parameters where appropriate and avoid an update loop between local state and URL state.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_07`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 8: Guard a page for UX - 10 points

**Where:** `frontend/src/App.jsx`. Record results under Exercise 8 in `answers.md`.

**Required outcome:** Redirect signed-out users away from a dashboard to login and return to the intended page after login. Demonstrate the API independently rejects unauthenticated access.

A client route guard helps navigation, while the API remains the access authority.

1. Guard the dashboard using the app's session state and redirect signed-out visitors to login.
2. Preserve a safe internal intended destination and navigate there after successful login.
3. Sign out and revisit the dashboard directly.
4. Separately call the protected API without credentials and record its rejection.

**Check:** the UI follows the login flow and the server denies unauthorized requests independently. Do not accept an arbitrary external redirect target from user input or treat hidden routes as security enforcement.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_08`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 9: Test deep links - 10 points

**Where:** `deep-link-notes.md`. Record results under Exercise 9 in `answers.md`.

**Required outcome:** Open and refresh a detail URL directly. Configure or document the development/production fallback needed, ensuring /api/ requests are not replaced by HTML.

Deep-link refresh asks the web server for the URL before React can route it.

1. Open a detail URL directly in a new tab and refresh it.
2. Test both the development server and your documented production-like static serving arrangement when available.
3. Configure app-entry fallback for client routes while preserving real static assets and /api/ handling.
4. Request an API URL and a missing static asset to inspect what they actually receive.

**Check:** detail refresh loads the app, API requests still receive API responses and missing assets are not silently returned as index.html. Record untested production configuration as a limitation rather than a verified deployment.

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_09`. The case-specific check above defines completion; a file merely existing earns no implementation points.

## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** Choose a new valid direct URL and an unknown/unauthenticated navigation case. Check browser location, displayed page and independent API authorization. Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson 37
python grade.py rubric --lesson 37
```

The first checks the JSON prediction and writes `grading/reports/lesson-37.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-37/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.

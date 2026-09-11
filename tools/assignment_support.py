"""Self-contained briefs. Writes instructions only, never learner code or marks."""
try:
    from .detailed_assignments import DETAILS, REVIEW_FOCUS
except ImportError:
    from detailed_assignments import DETAILS, REVIEW_FOCUS

# Concrete locations for Exercises 3 through 9, in order.
FILES = {
4: ['product.py']*7,
5: ['product.py']*5+['shared_tags.py','identity_demo.py'],
6: ['design.md','payments.py','checkout.py','checkout.py','products.py','pricing.py','checks.py'],
7: ['inventory/calculations.py','inventory/cli.py','inventory/__main__.py','namespace_demo.py','imports.md','inventory/storage.py','project-notes.md'],
8: ['environment.md']*3+['requirements.txt']+['environment.md']*3,
9: ['history.md']*7,
10: ['request-flow.md','answers.md','public/index.html','network-notes.md','network-notes.md','public/index.html','architecture.md'],
11: ['requests.http','requests.http','responses.http','update-contract.md','repetition.md','network-notes.md','errors.json'],
12: ['api-contract.md']*7,
13: ['practice.py']*7,
14: ['schema.sql and practice.py','seed.sql','queries.sql and practice.py','queries.sql and practice.py','queries.sql and practice.py','practice.py','schema.sql and practice.py'],
15: ['schema-design.md','schema.sql and practice.py','schema.sql and practice.py','practice.py','practice.py','performance.md and practice.py','concurrency.md'],
16: ['project/','project/config/settings.py and project/config/urls.py','project/inventory/views.py and project/inventory/urls.py','project/inventory/views.py and project/inventory/templates/inventory/home.html','project/inventory/urls.py','answers.md','request-flow.md'],
17: ['project/inventory/models.py','project/inventory/migrations/','answers.md','answers.md','project/inventory/models.py','migration-notes.md','rebuild-notes.md'],
18: ['query-notes.md']*7,
19: ['project/inventory/views.py and templates','project/inventory/urls.py and templates','project/inventory/views.py and templates','project/inventory/views.py and templates','project/inventory/views.py and templates','project/inventory/views.py','method-matrix.md'],
20: ['project/inventory/forms.py']*4+['project/inventory/views.py','project/inventory/templates/inventory/','project/inventory/tests.py'],
21: ['user-setup.md','project/config/urls.py and templates','project/inventory/views.py','project/config/urls.py and templates','project/inventory/views.py','session-notes.md','project/inventory/tests.py'],
22: ['project/config/settings.py','project/inventory/serializers.py','serializer-checks.md','project/inventory/serializers.py','project/inventory/serializers.py','serializer-checks.md','serializer-checks.md'],
23: ['project/inventory/views.py and project/inventory/urls.py']*6+['project/inventory/generic_views.py'],
24: ['project/inventory/views.py','project/inventory/urls.py','route-matrix.md','project/config/settings.py','project/inventory/views.py','project/inventory/views.py','api-contract.md'],
25: ['token-flow.md','project/config/settings.py and requirements.txt','project/config/urls.py','token-checks.md','token-checks.md','token-checks.md','token-storage.md'],
26: ['project/inventory/models.py','project/inventory/views.py','project/inventory/tests.py','project/inventory/views.py and serializers.py','project/inventory/permissions.py','project/inventory/views.py','project/inventory/tests.py'],
27: ['threat-model.md','project/inventory/tests.py','project/inventory/templates/inventory/','project/inventory/tests.py','project/config/settings.py and origins.md','project/config/settings.py and .env.example','project/config/settings.py and error-notes.md'],
28: ['project/inventory/tests.py']*7,
29: ['performance.md','performance.md']+['project/inventory/views.py']*4+['project/inventory/views.py and tests.py'],
30: ['project/Dockerfile','project/.dockerignore','container-notes.md','container-notes.md','project/config/settings.py','container-notes.md','offline-runbook.md'],
31: ['practice.js']*6+['index.html and practice.js'],
32: ['practice.js']*5+['calculations.js and main.js','practice.js'],
33: ['practice.js','api.js','index.html and main.js','api.js and main.js','mocks.js and main.js','main.js','mocks.js'],
34: ['frontend/','frontend/src/ProductCard.jsx','frontend/src/ProductList.jsx','frontend/src/ProductList.jsx','frontend/src/App.jsx','frontend/src/ProductCard.jsx','frontend/src/ProductCard.jsx and App.jsx'],
35: ['frontend/src/Counter.jsx','frontend/src/QuantityInput.jsx','frontend/src/ProductForm.jsx','frontend/src/App.jsx','frontend/src/App.jsx','frontend/src/InventorySummary.jsx','frontend/src/ProductForm.jsx'],
36: ['frontend/src/ProductPage.jsx']*7,
37: ['frontend/src/main.jsx','frontend/src/App.jsx and pages','frontend/src/ProductCard.jsx','frontend/src/NotFoundPage.jsx','frontend/src/ProductListPage.jsx','frontend/src/App.jsx','deep-link-notes.md'],
38: ['architecture.md','frontend/src/api/products.js','frontend/src/hooks/useProducts.js','frontend/src/ProductList.jsx','frontend/src/SessionContext.jsx','frontend/src/ErrorMessage.jsx','regression-notes.md'],
39: ['api-contract.md','frontend/src/api/ and auth UI','frontend/src/ProductListPage.jsx','frontend/src/ProductForm.jsx','project/inventory/views.py and frontend/src/SaleForm.jsx','failure-notes.md','demo.md'],
40: ['architecture.md','release-settings.md','release-notes.md','backup-rehearsal.md','release-checks.md','operations.md','interview.md']}

START = {
4: 'Start a new product.py; you do not need the previous CLI. Create a Product class and use Pen (price 200, stock 4) and Book (price 500, stock 7). Price is whole naira per unit; stock is a count. Keep demonstration calls under a main guard.',
5: 'Copy your Product class from Lesson 4 into product.py. It accepts name, price and stock and validates its fields. Use separate Pen 200/4 and Book 500/7 objects. Keep the shared-list bug in a separate file so it does not contaminate the working class.',
6: 'Create Python modules for payments, checkout and products. Use Product(name, price, stock) from Lesson 4. Payments here are simulated: they return receipt text or raise an error and never contact a bank. Recreate stock before each independent sale test.',
7: 'Create inventory/ in this assignment folder with an empty inventory/__init__.py. Use plain Python calculation functions and a small CLI. Run package commands from this assignment folder, the parent of inventory/.',
8: 'Create practice-project/ here and run environment commands inside it. .venv and .venv-rebuild are separate generated interpreter/package folders. Record evidence in environment.md beside practice-project/. No third-party package is assumed installed at the start.',
9: 'Create git-practice/ here and run Git commands inside it. Initialize the repository there, not in a parent. Create notes.txt before staging. If Git requests an identity, set user.name and user.email for this practice repository. Record the original branch name with git branch --show-current. No remote repository or push is required.',
10: 'Create public/index.html and work on your own machine. Start the local server from public/. localhost and 127.0.0.1 refer to the computer running the browser. Keep observations in text files beside public/. No public website is needed.',
11: 'This is an HTTP message-reading/design assignment. requests.http and responses.http are text documents; the worked response is not Python code. For the real browser observation, serve public/index.html locally. No working create/update API is required yet.',
12: 'Write api-contract.md as a specification another programmer could implement; you are not building the server yet. Use five products with IDs 1 through 5, names Pen/Notebook/Bag/Pencil/Eraser and stocks 4/8/0/2/6. Use page size 2 and ID order unless an exercise says otherwise.',
13: 'Use Python sqlite3 in practice.py and inventory.sqlite3 for persistent work. A :memory: database disappears when closed. Seed Pen 200/4, Book 500/8 and Bag 4000/0 with IDs 1/2/3. Avoid inserting duplicate fixtures when repeating a run.',
14: 'Use sqlite3 in practice.py and a disposable relationships.sqlite3. Define products(id,name,price), sales(id), sale_lines(id,sale_id,product_id,quantity,unit_price). References must point to existing rows. Start with Pen ID 1 price 200 and Book ID 2 price 500; add unsold Bag ID 3 later. Execute schema.sql/seed.sql through your script.',
15: 'Use sqlite3 in practice.py with disposable design.sqlite3. Model suppliers(id,name,phone), products(id,sku,name,price,stock,supplier_id), sales(id), sale_lines(id,sale_id,product_id,quantity,unit_price). Choose/document SQL types and constraints. Start independent sale/failure checks with stock 5.',
16: 'Create a new Django project in project/. Its configuration package is config and its app is inventory. No Product model is required yet. The health endpoint returns JSON and the home page renders HTML.',
17: 'Copy the working Lesson 16 project with config/, inventory/, manage.py and registered settings/routes. Add Product here. Saving models.py alone does not create database tables.',
18: 'Use the migrated Lesson 17 Product(name,price,stock) model. Seed Pen 200/4, Book 500/8 and Bag 4000/0 in a disposable database. Work in manage.py shell after importing Product from inventory.models. Save queries and actual output in query-notes.md.',
19: 'Use the Lesson 18 project. Put templates under inventory/templates/inventory/ and route URLs to inventory/views.py. Build ordinary HTML browser flows here; JSON APIs come later.',
20: 'Use the Lesson 19 browser CRUD project. A form receives raw submitted text; validation converts accepted fields before saving. Use a Product with stock 4 for the sale check. Browser input restrictions do not replace server validation.',
21: 'Use the Lesson 20 project with default authentication/session middleware and migrations. Create disposable ordinary and privileged users. Keep passwords and cookie values out of evidence files.',
22: 'Use the Lesson 21 project and add DRF. Run serializer experiments in manage.py shell; import Product and your serializer from their inventory modules. Use Pen name/price/stock values Pen/200/4.',
23: 'Use the Lesson 22 project with ProductSerializer working. Put API routes beneath /api/. Start with Pen 200/4 and Book 500/8. Check response status and database effects for every write test.',
24: 'Use the Lesson 23 API. Keep serializer validation and access rules when replacing views with a ViewSet. Use five products in stable ID order and page size 2.',
25: 'Use the authenticated-user model from the existing DRF project. Choose a maintained JWT integration compatible with your installed versions and follow its authentication-class and token-view setup. Record its package/version first. The illustrative claims below are not usable credentials.',
26: 'Use the Lesson 25 API. Make user A with two products and user B with three. Add/migrate ownership before running scoped queries. Refer to users by labels in evidence, not credentials.',
27: 'Use a disposable copy of the Lesson 26 app with fictional data. All security demonstrations target this local app. An origin includes scheme, host and port; record actual frontend/backend origins before configuring them.',
28: 'Use the existing backend. Put tests in inventory/tests.py or its established tests/ package. The first pure-function test can use a small standalone total function; use Django/DRF facilities for database/request tests. Keep test data separate from working stock.',
29: 'Use a disposable backend database. Add Supplier(name) and a Product supplier ForeignKey if missing, then migrate. Add a categories many-to-many or reverse sale-line relation for the collection task. Seed at least 100 products and several suppliers; record fixture size before measuring.',
30: 'Copy the working Django source to project/ with requirements.txt. Dockerfile paths are relative to project/; run docker build there. Exclude private/generated files with .dockerignore. The example deliberately runs a development server; production rehearsal comes in Lesson 40.',
31: 'Create practice.js for plain JavaScript and index.html for the input/button task. Load the script from the HTML page. For inventory totals use Pen 200/10, Book 500/3 and Bag 4000/0.',
32: 'Use objects with id/name/price/stock. For total 3500 use Pen 200/10, Book 500/3 and Bag 4000/0. The worked low-stock example has its own Pen stock 4 and Book stock 8 fixture; do not mix the two.',
33: 'Create a browser page with a labelled Load products button, status element and product-list element. main.js handles UI, api.js handles requests, mocks.js simulates local responses. Start your backend for real requests; otherwise label mocked evidence clearly.',
34: 'Create/use a prepared React project in frontend/, with components in src/. No API is needed. Define fixture products in App.jsx: Pen 200/4, Book 500/8 and Bag 4000/0, with IDs 1/2/3.',
35: 'Copy the previous React source/manifests into frontend/. Start with products in App.jsx. This lesson uses local state/callbacks, not backend requests. Keep text while typing, then convert/validate numeric fields on submit.',
36: 'Use the Lesson 35 React app and ProductPage.jsx. Use a real local API or labelled mocks with the same paginated contract: {count,next,previous,results}. A mocked success does not prove backend integration.',
37: 'Use the React app with working product pages. Add a compatible React Router package and record its import path/version. Wrap the app in BrowserRouter with Routes/Route inside. Use product IDs 1/2/3 for navigation checks.',
38: 'Use the working list/detail/form React app. Record current behaviour before extracting modules. The API client below expects the results field of a paginated response; reconcile it with your actual API contract.',
39: 'Keep backend in project/ and frontend in frontend/, with separate prepared dependencies. Run both locally and use your existing authentication approach consistently. Start each independent sale check with stock 10; the server owns authoritative stock.',
40: 'Use Lesson 39 in a local release rehearsal; buying hosting or publishing is not required. Use a disposable populated database for backup/restore. Record application server, frontend build, configuration and actual runtime versions.'}


def runtime(n):
    if n in (4,5,6):
        return 'From this assignment folder run `python checks.py`. Create checks.py with imports and test calls for the files you build. Put demonstrations in modules under `if __name__ == "__main__":` so imports do not launch them.'
    if n == 7:
        return 'From this assignment folder use `python main.py` initially and `python -m inventory` after adding inventory/__main__.py. `python -c "import inventory.calculations"` checks an import; it should not open a menu.'
    if n == 8:
        return 'Inside practice-project/ run `python -m venv .venv`, then `.venv/Scripts/python.exe -c "import sys; print(sys.executable)"` on Windows. Use `.venv/bin/python` on macOS/Linux. Record the interpreter path printed.'
    if n == 9:
        return 'Inside git-practice/ start with `git init` and `git status`. Read command output before proceeding. Save evidence in history.md outside the practice repository. All required operations are local.'
    if n in (10,11):
        return 'Inside public/ run `python -m http.server 8000 --bind 127.0.0.1`. Open `http://127.0.0.1:8000/`, open browser Developer Tools → Network, and reload. Stop the server with Ctrl+C. Write HTTP message examples in text files; they are not shell commands.'
    if n == 12:
        return 'No server command is needed. Walk each request/response through your contract, checking method, URL, fields, status and database effect. Save the scenario trace in answers.md.'
    if n in (13,14,15):
        return 'From this folder run `python practice.py`. Import sqlite3 in it. Read .sql text and use connection.executescript(...) for setup scripts; execute SELECT queries with connection.execute(...).fetchall() and print the rows. Commit successful persistent changes and close the connection.'
    if 16 <= n <= 29:
        return '''Inside project/, use its prepared Python environment. Create one with `python -m venv .venv` if needed. The Windows interpreter is `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

For the new Lesson 16 project, install Django 5.2 while online or from your prepared package cache, then run `python -m django startproject config .` and `python manage.py startapp inventory` with that interpreter. Add inventory to INSTALLED_APPS. For later lessons, copy the previous source and install its recorded requirements instead of creating a second project over it.

Run `python manage.py migrate`, then `python manage.py runserver` for browser/API checks. In another terminal use `python manage.py shell` or `python manage.py test inventory`. Here python means the project interpreter; substitute its full path if the environment is not active. Lesson 22 installs djangorestframework and registers rest_framework. Offline installation requires downloaded compatible artifacts in advance.'''
    if n == 30:
        return 'Inside project/ run `docker build -t emio24-dev .`, then `docker run --rm -p 8080:8000 emio24-dev`. Request health locally on port 8080. Docker and compatible image/package artifacts must be available for offline builds. The later persistence exercise adds an explicit data mount.'
    if n in (31,32,33):
        return 'Run plain scripts with `node practice.js` or load them in a browser page and use its Console. ES module files need `<script type="module" src="main.js"></script>`. Serve this folder with `python -m http.server 8080 --bind 127.0.0.1` and open `http://127.0.0.1:8080/`. Relative /api/ fetches need a backend/proxy at that origin; otherwise use an explicit local API URL with appropriate origin settings or a labelled mock.'
    if 34 <= n <= 38:
        return 'Inside frontend/ use the prepared dependencies and run `npm run dev`; open its printed URL. If starting fresh, while online run `npm create vite@latest frontend -- --template react` from the assignment folder, then `npm install` inside frontend/. Check its Node requirement and keep package-lock.json. JSX goes in src components, not a Python file or plain browser console. Offline work requires dependencies prepared in advance.'
    return 'Run backend and frontend from their own project/ and frontend/ directories. For Lesson 39 use the project interpreter with `python manage.py runserver` and use `npm run dev` in a second terminal. In Lesson 40 use `npm run build` and your selected production application server; document its exact command and configuration. The assignment checker does not start these services.'


def language(n):
    if n in (9,11,12,14,25,30,40):
        return 'text'
    return 'javascript' if 31 <= n <= 39 else 'python'


def render_assignment(item):
    n=item['number']; w=(n-1)//3+1
    terms='\n'.join(f'| **{term}** | {meaning}. | {analogy}. |' for term,meaning,analogy in item['terms'])
    files='\n'.join(f'| {i} | `{path}` |' for i,path in enumerate(FILES[n],3))
    result=f'''# Lesson {n} assignment: {item['title']}

**10 exercises · 10 points each · 100 points total.** Work through them in order. Each practical exercise has individually written steps and concrete checks, with its inputs, expected outcomes and common mistakes explained below.

## What you are building and why

{item['analogy']}

{START[n]}

## Where to work and how to run it

Work in `week-{w:02}/assignments/lesson-{n:02}/`. File paths below are relative to this folder. Create a named directory if it does not exist. For an existing framework project, edit the source inside your copy. A directory or “templates/pages” entry means related files live there; name them for the page or behaviour they implement.

{runtime(n)}

Keep `answers.md` for explanations and copied results, `submission.json` for Exercise 2's automatic answer, and `verification.md` for Exercise 10. Write ordinary text under headings such as `## Exercise 3`. Do not put prose in the JSON file.

| Practical exercise | File(s) to create or edit |
| --- | --- |
{files}

If a step explicitly names another file, create that too. If an exercise changes a Git branch or database, its notes file records commands/results; writing the note alone does not perform the action.

## Words used in this assignment

| Term | Meaning | Everyday analogy |
| --- | --- | --- |
{terms}

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

```{language(n)}
{item['code']}
```

**Question:** {item['prediction']}

1. Read the example and question before executing. Identify the supplied values.
2. Work out the requested result. Follow the question's answer shape: number, string, Boolean, list or object.
3. Keep the `"exercise_02"` key in submission.json and replace its `null` value. JSON strings need double quotes; Booleans are lowercase `true`/`false`. Do not add comments or a trailing comma.
4. Write your reasoning separately under Exercise 2 in answers.md.
5. Run in the required environment, or trace the message/query for a design example. Compare actual and predicted results; explain any correction.

For an unrelated question whose answer is 12, the file would be `{{"exercise_02": 12}}`. **12 illustrates the format; it is not this lesson's answer.**

<details>
<summary>Worked-example explanation — read after predicting</summary>

{item['explanation']}

</details>

**Finished when:** valid JSON contains the requested answer and reasoning is saved separately. The checker awards 10 automatic points for the exact final prediction (`exercise_02`). It does not verify reasoning or practical code through this answer.
'''
    for i,(title,detail) in enumerate(item['tasks'],3):
        result+=f"""
## Exercise {i}: {title} - 10 points

**Where:** `{FILES[n][i-3]}`. Record results under Exercise {i} in `answers.md`.

**Required outcome:** {detail}

{DETAILS[n][i-3]}

**Record:** the exact call, command or browser action; starting input; expected result above; actual output; and one sentence explaining the result. Use a fresh fixture whenever the instructions describe an independent case.

**Marks:** meeting the stated requirements 6, demonstrated cases with actual evidence 3, explanation 1. Manual criterion: `exercise_{i:02}`. The case-specific check above defines completion; a file merely existing earns no implementation points.
"""
    result+=f'''
## Exercise 10: Verify new cases and explain a limitation — 10 points

**Where:** create `verification.md` in this assignment folder.

**For this lesson:** {REVIEW_FOCUS[n]} Choose your own new values/scenario; do not simply copy an earlier supplied check.

1. Select two practical exercises from Exercises 3–9 and write their numbers.
2. For the first, choose a **new normal case** that should succeed and is different from the provided example. State its input and expected outcome before executing. For a calculation, for example, choose a different price/quantity pair. Run or trace it and record the actual result (3 points).
3. For the second, choose a **new boundary/failure case** appropriate to its rule: an empty collection, exact cutoff, missing record, failed request or invalid operation are possible case types. State the expectation, perform the check and record what happens (3 points).
4. Include exact commands/actions and observed outputs so someone else can repeat both cases (2 points).
5. Explain a specific remaining limitation and a concrete next change to address it (2 points). If the checks pass, discuss an unhandled scenario or scope limitation; do not invent a failure.

**Finished when:** a reader can repeat both checks and understand the limitation. Manual criterion: `exercise_10`. This is further verification, not two additional projects.

## Save and grade offline

Save your work. Return to the **course root**, the folder containing `grade.py`, and run:

```powershell
python grade.py check --lesson {n}
python grade.py rubric --lesson {n}
```

The first checks the JSON prediction and writes `grading/reports/lesson-{n:02}.md`. The second lists criterion IDs and maximum points. The checker needs only Python; it does not install dependencies, run framework projects, inspect browser actions or judge explanations. Practical work uses the acceptance checks above and requires evidence-based human review.

**10 earned / 90 pending** means the prediction is correct and the other work still needs review; it does not mean the project failed or passed. See the [checker guide](../../../grading/README.md) for recording reviewed scores locally.

- [ ] All ten exercises attempted and required files saved.
- [ ] Specified cases checked with actual outcomes recorded.
- [ ] JSON answer checked and manual work reviewed.
- [ ] At least 80/100 after review; limitations explained.

Use [lesson notes](../../lesson-{n:02}/teaching.md), the [glossary](../../../glossary.md) and [setup guide](../../../SETUP.md) for reference. The task requirements are written in this brief.
'''
    return result

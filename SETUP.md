# Setup and offline preparation

The **grader** needs only Python 3. The **practical lessons** progressively need Git, Django, DRF, Node/React and Docker. Install or download the tools before going offline. All lesson text is local; linked reference pages and third-party dependencies are not bundled.

## Python, Git and SQL

Run `python --version` or `py --version`. Python 3.12 is the checker verification baseline. Week 1, the checker and SQLite practice use Python's standard library.

Create a practice environment with `python -m venv .venv`. On Windows invoke `.venv/Scripts/python.exe` directly without changing shell execution policy; on macOS/Linux use `.venv/bin/python`. Use that interpreter for pip and project commands. Install Git before Lesson 9 and work in a separate practice repository. SQLite examples do not demonstrate PostgreSQL-specific row locking.

## Django and DRF

Django 5.2 is the documentation baseline, not a claim about the newest release. Use a compatible patch release and record the exact installed version. In a new `project/` folder inside the Lesson 16 assignment, while online:

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install "Django>=5.2,<5.3"
.venv/Scripts/python.exe -m django startproject config .
.venv/Scripts/python.exe manage.py startapp inventory
.venv/Scripts/python.exe manage.py migrate
.venv/Scripts/python.exe manage.py runserver
```

Add inventory to INSTALLED_APPS. Use the environment interpreter for subsequent manage.py commands. Lesson 22 adds djangorestframework in that same environment and rest_framework to INSTALLED_APPS. Record installed dependency versions. Copy project source forward for later assignments so prior submissions stay reviewable; omit generated environments and rebuild them from requirements.

Django snippets belong in the named modules. A Product shell query needs `from inventory.models import Product`; views need URL patterns and templates need real files. Use the guided steps to connect these pieces.

For offline rebuilding, prepare and test compatible artifacts ahead of time:

```powershell
.venv/Scripts/python.exe -m pip freeze > requirements.txt
.venv/Scripts/python.exe -m pip download -r requirements.txt -d wheelhouse
.venv/Scripts/python.exe -m pip install --no-index --find-links wheelhouse -r requirements.txt
```

Use the intended interpreter/platform. Some downloads are platform-specific; source distributions may need build tools. Rehearse in a fresh environment before relying on the cache. JWT practice needs an additional maintained compatible integration package; record its exact version and follow its official setup instructions. No bank or online account is required.

## JavaScript and React

Plain JavaScript runs in an installed Node runtime or browser console. Browser ES modules need `<script type="module" src="main.js"></script>` and a local HTTP server.

React JSX requires React and build tooling. If you have no project, while online use `npm create vite@latest frontend -- --template react`, enter frontend, run `npm install`, then `npm run dev`. Check the generated template's Node requirement, record actual versions and keep package-lock.json. Verify it starts while disconnected. The course does not bundle npm dependencies.

For later assignments copy relevant source and package manifests, not generated node_modules. Reuse a prepared local setup or a verified offline package cache. React Router requires a compatible installed package; record its version and use the corresponding import path. Lessons use declarative BrowserRouter/Routes/Route concepts.

## Docker and release practice

Before Lesson 30 prepare a working Docker engine, chosen base image and dependency artifacts. Offline builds need those already available. The Python checker does not simulate a Docker build or a deployment. Lesson 40 can be completed as a local release rehearsal; buying hosting or publishing is not required.

## Primary references

- [Python environments](https://docs.python.org/3/tutorial/venv.html): environment and package concepts.
- [Django 5.2 documentation](https://docs.djangoproject.com/en/5.2/): setup, models, views, forms and tests.
- [DRF serializers](https://www.django-rest-framework.org/api-guide/serializers/), [permissions](https://www.django-rest-framework.org/api-guide/permissions/) and [testing](https://www.django-rest-framework.org/api-guide/testing/): API validation and behaviour.
- [React state](https://react.dev/learn/managing-state) and [Effects](https://react.dev/learn/synchronizing-with-effects): UI state and external synchronization.
- [Vite getting started](https://vite.dev/guide/) and [React Router declarative installation](https://reactrouter.com/start/declarative/installation): frontend setup.

See each week's references for more. Save external pages beforehand if you want to read them offline.

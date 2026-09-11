"""Maintain the authored lesson packs. Never overwrite learner submission files."""
import json
from pathlib import Path
try:
    from .assignment_support import render_assignment
except ImportError:
    from assignment_support import render_assignment

ROOT = Path(__file__).resolve().parents[1]
LESSONS = []


def lesson(number, title, analogy, terms, code, explanation, prediction, expected, tasks):
    assert len(tasks) == 7, number
    LESSONS.append(dict(number=number, title=title, analogy=analogy, terms=terms,
                        code=code, explanation=explanation, prediction=prediction,
                        expected=expected, tasks=tasks))


lesson(4, 'Classes, objects and instances',
       'A product class is a blank stock card design; each object is a separately filled card. Changing one card does not change the others. Unlike paper, objects also expose behaviour through methods.',
       [('Class', 'A definition used to create objects', 'the blank stock card design'), ('Instance', 'One object created from a class', 'one filled card'), ('Attribute', 'A value associated with an object', 'the stock field on a card'), ('Method', 'A function accessed through an object or class', 'a stock-card operation'), ('self', 'The instance passed to an instance method', 'the particular card being handled')],
       'class Product:\n    def __init__(self, name, stock):\n        self.name = name\n        self.stock = stock\n\npen = Product("Pen", 4)\nbook = Product("Book", 7)\npen.stock -= 1\nprint(pen.stock, book.stock)',
       '`__init__` initializes a newly created instance. Each assignment to self stores data on that instance. The two calls to Product create different objects, so changing pen leaves book at 7. A second name assigned to pen would refer to the same object.\n\n### Constructor: make a card, then fill it in\n\nA **constructor** is the mechanism used to create and initialize an object. Think of ordering a new stock card: first obtain a blank card, then fill in its name and starting stock. In the example, `Product("Pen", 4)` starts that process.\n\nFor this ordinary Python class, the steps are:\n\n1. **`__new__` creates the instance**: like making the blank card. Product inherits this behaviour; you do not need to write it for this lesson.\n2. **`__init__` initializes that instance**: like filling the card. Python supplies the new object as `self`, while `"Pen"` and `4` become `name` and `stock`.\n3. **The class call returns the object**, which is assigned to `pen`. The initializer itself must return `None`; normally you leave out a return statement.\n\nPeople often call `__init__` the constructor. More precisely, it is the **initializer**: the object already exists when it runs. Do not call `pen.__init__(...)` to create a separate product; call `Product(...)` again.\n\n**Try it:** add `print("Initializing", name)` inside `__init__`. Predict what prints when you create Pen and Book. Then set `alias = pen`: does that initialize another object? It does not; alias refers to the existing object.',
       'After the example runs, enter the two stocks as a JSON list, in pen/book order.', [3, 7],
       [('Create stock cards', 'In product.py implement Product(name, price, stock). Store all three attributes. Create Pen at 200/4 and Book at 500/7; show each attribute and prove the instances differ.'),
        ('Calculate value', 'Add inventory_value(self) returning price * stock. Pen initially returns 800; a zero-stock product returns 0. Return a number rather than only printing.'),
        ('Protect construction', 'Reject blank names and negative prices or stock with ValueError. Accept zero price and stock. Demonstrate a valid object and each rejected field.'),
        ('Restock', 'Add restock(quantity), requiring a positive integer and rejecting bool. Starting at 4, adding 3 leaves 7; adding 0 or -1 raises ValueError and leaves 7.'),
        ('Sell', 'Add sell(quantity). Require a positive integer no greater than stock; return the sale total. Selling 2 at 200 leaves stock 5 after the restock and returns 400. Overselling leaves stock unchanged.'),
        ('Show identity', 'Set alias = pen and change alias.stock. Record why pen changes too while book does not. Then create a separate Product with matching values and explain identity versus equal field values.'),
        ('Build an object inventory', 'Store three Product objects in a list and total their values using the method. Include one zero-stock item. Print item names and total; calculate the same result by hand.')])

lesson(5, 'Class behaviour',
       'Instance data is a note on one product card; class data is a notice on the stockroom wall. A mutable shared notice can accidentally collect changes from every card.',
       [('Class attribute', 'A value stored on a class and found through attribute lookup', 'a shared wall notice'), ('Instance attribute', 'A value stored on one instance', 'a note on one card'), ('Property', 'Managed attribute access through methods', 'a service window guarding a field'), ('classmethod', 'A method receiving the class as its first argument', 'a factory that knows which card design to use'), ('__str__', 'The method producing a human-readable string', 'the label printed for a customer')],
       'class Product:\n    currency = "NGN"\n    def __init__(self, name):\n        self.name = name\n    def __str__(self):\n        return f"{self.name} ({self.currency})"\n\np = Product("Pen")\nprint(str(p))',
       'currency is looked up on the class because p has no currency attribute of its own. __str__ returns text; print then displays that text. Use properties when assignments need validation, rather than adding getters for every field.',
       'Enter the exact text printed, without a newline.', 'Pen (NGN)',
       [('Shared and separate data', 'Extend Product with class currency = "NGN" and per-instance stock. Change stock on one of two products; show the other is unchanged and both initially use NGN.'),
        ('Display a product', 'Implement __str__ returning "Pen: 4 units" for name Pen and stock 4. Check zero stock and a different name. Keep printing outside the method.'),
        ('Useful debugging text', 'Implement __repr__ including class name, name, price and stock. Show repr(product) and str(product), and explain which reader each helps.'),
        ('Guard stock assignment', 'Use a stock property backed by _stock. Reject negatives, text, fractions and bool; allow 0. Attempt an invalid assignment and show the previous value remains intact.'),
        ('Alternative constructor', 'Implement Product.from_dict(record) as a classmethod using cls. Accept name/price/stock and reuse validation. Demonstrate valid input and a missing required field with a clear error.'),
        ('Fix a shared-list bug', 'Reproduce class tags = [] with two products. Append on one and show leakage. Move list creation into __init__, rerun, and show independent tags.'),
        ('Compare value and identity', 'Construct two separate products with identical fields. Document whether your class defines __eq__; demonstrate is and == and explain their observed results without claiming they mean the same thing.')])

lesson(6, 'OOP pillars and composition',
       'A checkout is a shop counter with a stable service contract. Cash and transfer staff can both accept payment. The counter can use a payment worker without becoming that worker; that is composition.',
       [('Encapsulation', 'Grouping data and behaviour behind an interface', 'a counter controlling stock changes'), ('Abstraction', 'Exposing needed operations while hiding detail', 'asking to pay without operating the bank'), ('Inheritance', 'Deriving behaviour from a base class', 'a specialized version of a staff role'), ('Polymorphism', 'Using different objects through a common operation', 'cash and transfer workers both accept pay'), ('Composition', 'Building an object using other objects', 'a checkout has a payment worker')],
       'class Cash:\n    def pay(self, amount):\n        return f"cash:{amount}"\n\nclass Transfer:\n    def pay(self, amount):\n        return f"transfer:{amount}"\n\nfor payment in [Cash(), Transfer()]:\n    print(payment.pay(600))',
       'The loop only relies on pay(amount). Python does not require a shared parent class for this example. Inheritance is appropriate when a subtype can honour its parent contract; sharing a few lines is not sufficient reason.',
       'Enter the printed lines as a JSON list of strings.', ['cash:600', 'transfer:600'],
       [('Define a payment contract', 'In design.md specify pay(amount), positive whole-naira input, returned receipt text and failure behaviour. Give valid 600 and invalid -1 cases.'),
        ('Implement two strategies', 'Write CashPayment and TransferPayment implementing the contract. Both reject nonpositive amounts before producing a receipt. Demonstrate both with 600.'),
        ('Compose checkout', 'Implement Checkout(payment) that calls the injected payment object. Run the same checkout operation with each payment class without conditionals on class names.'),
        ('Protect stock', 'Have checkout validate the sale before calling payment and decrease stock only after simulated payment success. A failing payment raises an exception; show unchanged stock.'),
        ('Use inheritance deliberately', 'Create a DiscountedProduct subtype with a value calculation that honours the base return type. Show base and subtype in one inventory list. Document discount bounds 0 through 100.'),
        ('Explain the alternative', 'Replace the discount subtype with a composed pricing policy in a separate example. Compare changing policies at runtime and the number of classes needed.'),
        ('Substitute a fake', 'Create a FakePayment recording amounts and optionally failing. Demonstrate one successful and one rejected checkout without a bank or network. Include the recorded call list.')])

lesson(7, 'Modules and packages',
       'Modules are labelled drawers in a workshop; packages group related drawers. Importing should make tools available, not unexpectedly start the whole shop.',
       [('Module', 'A unit of Python code with its own namespace', 'one tool drawer'), ('Package', 'A way to organize related modules', 'a cabinet of drawers'), ('Import', 'Loading or accessing another module', 'bringing a named tool to the bench'), ('Namespace', 'A mapping of names to objects', 'labels within one drawer'), ('Entry point', 'Where an application begins running', 'the shop opening switch')],
       '# Put this in totals.py\ndef line_total(price, quantity):\n    return price * quantity\n\nif __name__ == "__main__":\n    print(line_total(200, 3))',
       'When run as a script, __name__ is __main__ and the example prints 600. When imported as totals, the function becomes available but the guarded print is skipped. Imports can still execute any unguarded top-level statements.',
       'What number is printed when totals.py is run directly?', 600,
       [('Extract calculations', 'Move line_total and inventory_value into inventory/calculations.py; add __init__.py. Import them from main.py. Check 200*3 and empty inventory.'),
        ('Separate interaction', 'Move prompts into inventory/cli.py. Import calculations without any prompt or menu appearing. Record the command and observed silence.'),
        ('Create a package entry point', 'Add inventory/__main__.py calling the menu. Run python -m inventory from its parent folder and show that quitting returns to the shell.'),
        ('Resolve names', 'Create two modules each defining describe(). Import using module names and call both. Explain how qualification avoids overwriting a local name.'),
        ('Repair a circular import', 'Draw a dependency cycle between cli and storage, then extract shared validation into a third module. Submit the before/after import graph and a working import.'),
        ('Use stable file paths', 'Resolve a sample data path relative to the relevant module with pathlib. Run from two working directories and show the same intended file is read.'),
        ('Document the package', 'Write a folder tree and one sentence per file explaining responsibility. Give exact run commands and show calculations can be reused without launching the UI.')])

lesson(8, 'Virtual environments and dependencies',
       'A virtual environment is a project toolbox. It keeps this project’s installed Python tools separate from another project’s tools, but it does not isolate the computer like a locked machine.',
       [('Interpreter', 'The program executing Python code', 'the worker using the toolbox'), ('Virtual environment', 'An isolated Python package installation context', 'a dedicated project toolbox'), ('Dependency', 'Software your program relies on', 'a tool required for a job'), ('Version pin', 'A requirement naming an exact release', 'specifying the exact tool model'), ('Reproducibility', 'Being able to recreate an environment or result', 'another worker assembling the same toolbox')],
       'import sys\nfrom pathlib import Path\n\nprint(Path(sys.executable).name)\nprint(sys.prefix != sys.base_prefix)',
       'The executable path identifies the interpreter actually running the program. The prefix comparison is normally true inside a venv. Use python -m pip so pip belongs to that interpreter. Activation changes command lookup; directly invoking the venv interpreter also works.',
       'Inside a standard active venv, what Boolean does the second print produce?', True,
       [('Create a toolbox', 'Run python -m venv .venv inside a practice project. Record the command, Python version and environment path. Exclude .venv from source control.'),
        ('Use its interpreter', 'On Windows run .venv/Scripts/python.exe -c "import sys; print(sys.executable)". Record the full output and identify the project environment segment.'),
        ('Inspect dependencies', 'Run the environment interpreter with -m pip list. Save output in environment.md; distinguish the standard library from installed third-party distributions.'),
        ('Record requirements', 'For an installed project dependency, record its exact installed version in requirements.txt. If no packages are installed yet, document that and use the bundled standard-library app.'),
        ('Prepare offline installation', 'When online, use python -m pip download -r requirements.txt -d wheelhouse with the intended interpreter/platform. Document that compatible dependency artifacts are required; do not claim a package name is an offline copy.'),
        ('Rebuild locally', 'Create .venv-rebuild and, if using dependencies, install with -m pip install --no-index --find-links wheelhouse -r requirements.txt. Show an import and version. Record a missing wheel as a blocker, not success.'),
        ('Diagnose a mismatch', 'Compare sys.executable and -m pip --version for two interpreters. Explain how a package can be installed for one while an import fails in the other; provide the corrected command.')])

lesson(9, 'Git and version control',
       'Git is a project history album. The working tree is today’s desk, the staging area selects the next photograph, and a commit records that selection. A branch is a movable bookmark, not a duplicate folder.',
       [('Repository', 'Stored project history and metadata', 'the history album'), ('Commit', 'A recorded project snapshot with metadata', 'a labelled photograph'), ('Staging area', 'The proposed contents of the next commit', 'the photo selection tray'), ('Branch', 'A movable reference to a commit', 'a bookmark'), ('Merge conflict', 'Changes Git cannot combine automatically', 'two incompatible edits to one caption')],
       '# Run in a new practice folder after git init\ngit status\ngit add notes.txt\ngit diff --cached\ngit commit -m "Add inventory notes"',
       'Create notes.txt before these commands. git add stages its current contents; editing it afterward does not automatically change the staged version. git diff --cached shows what a commit would record. Set local user.name and user.email if Git requires an identity.',
       'Stage a file containing A, then edit it to B without staging again. Which text will the next commit record?', 'A',
       [('Start local history', 'Create a separate practice folder, git init, and a notes.txt describing EMIO24. Record git status before and after adding the file. Avoid changing a parent repository.'),
        ('Inspect the staging area', 'Stage notes.txt, edit it again, and save git diff and git diff --cached. Identify which version would be committed and then commit intentionally.'),
        ('Ignore generated files', 'Add .venv/, __pycache__/, .env and local data outputs to .gitignore. Create a dummy .env containing only fake values; show git status excludes it.'),
        ('Make a feature branch', 'Create feature/low-stock with git switch -c. Change a practice function and commit. Save git log --oneline --all --graph.'),
        ('Merge a change', 'Switch to your original branch and merge the feature branch. Demonstrate the added function and document whether the merge fast-forwarded.'),
        ('Resolve a practice conflict', 'In two local branches edit the same line differently and merge. Record conflict markers, choose a coherent final line, stage and finish the merge. Run the affected program.'),
        ('Undo with history', 'Create a disposable incorrect commit then use git revert on it. Show that both the mistake and reversal remain in the log. Explain why this differs from deleting shared history.')])

lesson(10, 'How the web works',
       'A browser requesting a page resembles a customer sending an order to a shop address. DNS finds an address; the server handles the request. The analogy leaves out caches, proxies and repeated network connections.',
       [('Client', 'Software requesting a service', 'the customer'), ('Server', 'Software handling requests', 'the shop counter'), ('DNS', 'A system resolving domain names to records such as IP addresses', 'an address directory'), ('URL', 'An address identifying a resource and access scheme', 'a shop address plus department'), ('Port', 'A numbered network endpoint on a host', 'a numbered service door')],
       'from urllib.parse import urlparse\n\nu = urlparse("http://localhost:8000/products?low=1")\nprint(u.hostname, u.port, u.path)',
       'localhost refers to the local machine; port 8000 selects the listening service. /products is a path handled by that service. The query carries extra request information. Parsing a URL does not contact a server.',
       'Enter the host, port and path from the example as a JSON list.', ['localhost', 8000, '/products'],
       [('Draw one request', 'Draw browser -> name resolution -> connection -> server -> response -> browser rendering. Explain each arrow and distinguish transferred HTML from displayed pixels.'),
        ('Dissect addresses', 'Break http://localhost:8000/products?low=1 into scheme, host, port, path and query in answers.md. Explain why localhost on a friend’s laptop is not your machine.'),
        ('Serve a page locally', 'Create public/index.html with an inventory heading and two products. From public run python -m http.server 8000 --bind 127.0.0.1; open http://127.0.0.1:8000/ and record the response.'),
        ('Inspect the request', 'Use browser Network tools to record request URL, method, status and content type for index.html. Explain each field using the shop analogy.'),
        ('Request a missing page', 'Visit /missing.html and record the status. Compare a server returning an error response with stopping the server and getting a connection failure.'),
        ('Separate client and server', 'Add a local HTML button that changes visible text with JavaScript. Observe whether clicking creates a network request. Explain where that change executes.'),
        ('Map a full-stack product', 'Draw React client, Django service and database with request/data arrows. Identify where stock is authoritative and why browser-visible stock can become stale.')])

lesson(11, 'HTTP requests and responses',
       'HTTP is the order-and-receipt format at the counter. The method says the kind of action; the path names the resource; the status reports what happened. A receipt alone does not explain every business outcome.',
       [('HTTP method', 'A request token expressing intended semantics', 'the action on an order form'), ('Header', 'Metadata sent with a request or response', 'delivery instructions'), ('Body', 'The message content', 'the order details'), ('Status code', 'A numeric response classification', 'the result stamp'), ('Idempotent', 'Having the same intended effect when repeated', 'setting a shelf label to the same value twice')],
       'HTTP/1.1 201 Created\nContent-Type: application/json\nLocation: /products/4\n\n{"id":4,"name":"Pen","stock":10}',
       'The blank line separates headers from the body. 201 means creation succeeded; Location can identify the created resource. GET should be safe; PUT is intended to be idempotent; POST is not generally idempotent. An identical status on repeated requests is not the definition of idempotency.',
       'Enter the response status code as a number.', 201,
       [('Write a read request', 'Write a complete GET /products/4 HTTP/1.1 request with Host in requests.http. Include the blank line and explain why the path is not the method.'),
        ('Write a create request', 'Add a POST /products request with Content-Type application/json and name/price/stock body. Include a matching 201 response with Location.'),
        ('Classify failures', 'Write response examples for malformed input (400), missing authentication (401), forbidden access (403), missing resource (404), and server error (500). Explain a scenario for each.'),
        ('Compare updates', 'Describe replacing a complete product with PUT versus changing stock with PATCH. Give request bodies and explicitly state your API’s required fields.'),
        ('Trace repetition', 'Apply PUT stock=5 twice to stock 10, then compare two POST sale quantity=2 operations starting at 10. Record final stocks and explain idempotency.'),
        ('Inspect real local headers', 'Use the local server from Lesson 10 and browser tools to save one request/response pair. Identify header/body boundaries and explain Content-Type.'),
        ('Design error content', 'Define a JSON error body with code, message and field errors. Give an invalid-stock example, ensuring it provides no stack trace or secret values.')])

lesson(12, 'REST API design',
       'An API is a published service counter contract. Resource URLs are labelled counters such as products and sales. REST is an architectural style, not merely putting JSON on any URL.',
       [('API', 'An interface through which software interacts', 'the published counter contract'), ('Resource', 'A concept identified and manipulated through a representation', 'a product record at a named counter'), ('Representation', 'Data describing a resource', 'a copy of the product card'), ('Stateless request', 'A request understood without relying on stored client conversation context', 'an order carrying the needed credentials and details'), ('Pagination', 'Dividing a collection into bounded result pages', 'issuing a catalogue a few pages at a time')],
       'GET /api/products/?page=2\n\n{"count":3,"next":null,"previous":"?page=1",\n "results":[{"id":3,"name":"Bag"}]}',
       'A collection response wraps a page of records with navigation metadata. A client must read results rather than assuming the root is an array. Statelessness does not mean the server has no database; it concerns request context.',
       'How many product records are in this response page?', 1,
       [('Specify resources', 'List products, customers and sales with collection/detail URLs. Use stable IDs, and explain why a sale deserves its own resource.'),
        ('Write endpoint contracts', 'Create api-contract.md covering list, detail, create, update and delete products. Specify method, URL, request fields, success status and error status for each.'),
        ('Define validation', 'Require nonblank name, integer price >=0 and integer stock >=0. Give one accepted JSON body and four rejected bodies with field-specific errors.'),
        ('Paginate products', 'Design a page size of 2 for five sample products. Write all three response pages and correct next/previous values. Keep ordering explicit by ID.'),
        ('Filter and order', 'Specify low-stock and name-search query parameters and allowed ordering fields. Give an example matching two records and define unknown parameter behaviour.'),
        ('Model stock changes', 'Design POST /sales/ with product ID and quantity. Specify insufficient-stock handling, unchanged stock after failure, and how clients learn the updated stock.'),
        ('Review compatibility', 'Add a new optional product field without removing existing fields. Compare that with renaming id, explain which clients break, and write a migration/versioning note.')])

lesson(13, 'SQL foundations',
       'A relational table is a carefully structured ledger. SQL describes which rows you want instead of making you walk through each page yourself. A table has no guaranteed display order without ORDER BY.',
       [('Database', 'An organized persistent collection of data', 'the ledger cabinet'), ('Table', 'Rows sharing a defined set of columns', 'one structured ledger'), ('Row', 'One record in a table', 'one ledger entry'), ('SQL', 'A language for relational data definition and manipulation', 'instructions to the ledger clerk'), ('Parameter', 'A separately bound query value', 'a filled form value rather than a rewritten instruction')],
       'import sqlite3\n\ndb = sqlite3.connect(":memory:")\ndb.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, stock INTEGER)")\ndb.executemany("INSERT INTO products VALUES (?, ?, ?)", [(1,"Pen",4),(2,"Book",8)])\nrows = db.execute("SELECT name FROM products WHERE stock <= ? ORDER BY id", (4,)).fetchall()\nprint(rows)',
       'The connection creates a temporary database for this example. The question mark binds 4 as data. fetchall returns tuples; selecting one column still produces a one-element tuple per row. Use a file path and commit for persistent exercises.',
       'Enter the selected product names as a JSON list.', ['Pen'],
       [('Create a ledger', 'In practice.py use sqlite3 to create a products table with id primary key, name, price and stock. Insert Pen 200/4, Book 500/8 and Bag 4000/0 using parameters.'),
        ('Read precise columns', 'Select name and stock ordered by id. Save the SQL and returned rows; do not use SELECT * for this exercise.'),
        ('Filter stock', 'Select stock <=4 ordered by stock then id. Expect Bag then Pen. Repeat for threshold 0 using a bound parameter.'),
        ('Update one row', 'Change Pen stock to 7 with WHERE id=1. Show before/after rows and verify Book remains 8. Explain the effect of omitting WHERE.'),
        ('Delete deliberately', 'Delete only the zero-stock Bag by ID. Show remaining row count 2. Work only on your disposable practice database.'),
        ('Aggregate value', 'Use SUM(price * stock) after the update/delete. Expect 5400. Define and demonstrate a zero result for an empty table using COALESCE.'),
        ('Preserve data and queries', 'Commit to inventory.sqlite3, close and reopen it, then show rows remain. Insert a name containing an apostrophe using parameters and demonstrate it reads back unchanged.')])

lesson(14, 'Relationships and joins',
       'A sale line references a product card by its permanent number instead of copying all its current details. A join matches those references. Historical sale prices still need their own snapshot.',
       [('Primary key', 'A column or columns uniquely identifying a row', 'the permanent card number'), ('Foreign key', 'A constrained reference to another row key', 'a valid card number on a sale line'), ('One-to-many', 'One record associated with several records', 'one sale with several lines'), ('JOIN', 'Combining rows according to a condition', 'matching sale slips with cards'), ('NULL', 'A marker for missing or unknown data', 'a blank field whose value is unknown')],
       'SELECT p.name, SUM(l.quantity) AS units\nFROM products AS p\nJOIN sale_lines AS l ON l.product_id = p.id\nGROUP BY p.id, p.name\nORDER BY p.id;',
       'The ON condition connects each line to its product. GROUP BY collects matching lines before SUM. An inner join omits products with no sales; a left join can retain them. COUNT(*) after a left join counts the retained row, so count a non-null child key when counting children.',
       'Pen has sale quantities 2 and 3. What is its SUM(quantity)?', 5,
       [('Create related tables', 'Create products, sales and sale_lines with primary/foreign keys in SQLite. Enable PRAGMA foreign_keys = ON on the connection. Save schema.sql and a runnable loader.'),
        ('Insert a small history', 'Insert two products and two sales. Add Pen quantities 2 and 3 to separate sales, plus Book quantity 1. Save seed SQL and explain each relationship.'),
        ('Join readable receipts', 'Join lines to products and show sale ID, product name and quantity, ordered by sale ID then line ID. Verify names match the referenced IDs.'),
        ('Aggregate by product', 'Produce Pen=5 and Book=1 units sold using GROUP BY. Explain why grouping by a name alone is unsafe if names can repeat.'),
        ('Include unsold products', 'Add Bag without a sale. Use LEFT JOIN and COALESCE so its units sold is 0. Show the difference from the inner join.'),
        ('Reject orphan lines', 'Attempt a line with product_id 999 and show the foreign-key error. Roll back and verify no invalid row remains.'),
        ('Keep historical prices', 'Store unit_price on sale_lines. Change the current product price and demonstrate that old receipt totals stay unchanged. Explain the intentional duplication.')])

lesson(15, 'Database design and transactions',
       'A transaction bundles stock deduction and sale recording into one sealed ledger update. Either the whole bundle is accepted or none is. A sketch of the ledger structure is its schema.',
       [('Schema', 'The structure and constraints of a database', 'the ledger blueprint'), ('Normalization', 'Organizing data to reduce harmful redundancy and anomalies', 'keeping supplier details on one master card'), ('Constraint', 'A rule enforced by the database', 'a ledger rule the clerk cannot bypass'), ('Transaction', 'A unit of database work committed or rolled back together', 'one sealed update bundle'), ('Index', 'A structure that helps locate data efficiently', 'the ledger’s lookup tabs')],
       'import sqlite3\ndb = sqlite3.connect(":memory:")\ndb.execute("CREATE TABLE stock (id INTEGER PRIMARY KEY, quantity INTEGER CHECK(quantity >= 0))")\nwith db:\n    db.execute("INSERT INTO stock VALUES (1, 5)")\ntry:\n    with db:\n        db.execute("UPDATE stock SET quantity = quantity - 6 WHERE id = 1")\nexcept sqlite3.IntegrityError:\n    pass\nprint(db.execute("SELECT quantity FROM stock").fetchone()[0])',
       'The first with commits the initial row. The second update violates CHECK and its transaction rolls back. Catching the error outside the with block lets the context manager observe failure. SQLite behaviour is useful practice but does not demonstrate PostgreSQL row locks.',
       'What stock quantity is printed after the failed update?', 5,
       [('Design the schema', 'Draw products, suppliers, sales and sale_lines with keys and cardinalities. State which columns may be NULL and which are required.'),
        ('Remove an anomaly', 'Show a duplicated supplier phone in three product rows. Move supplier details to a suppliers table and demonstrate one update changes the authoritative value.'),
        ('Enforce business rules', 'Write schema.sql with nonnegative stock/price checks, nonblank name validation at the application boundary, and unique product SKU. Demonstrate a duplicate SKU rejection.'),
        ('Bundle a sale', 'Implement a transaction that decreases stock and inserts a sale line. Starting stock 5, selling 2 commits stock 3 and one line.'),
        ('Roll back a failure', 'Cause line insertion to fail after the stock update in a disposable database. Show stock remains 5 and no sale line persists when starting from the original fixture.'),
        ('Measure an index', 'Populate at least 1000 products and use EXPLAIN QUERY PLAN on SKU lookup before/after an appropriate index. Save plans; explain extra write/storage cost.'),
        ('Plan concurrent sales', 'Trace two buyers attempting the last unit. Explain why reading then blindly writing loses correctness; propose an atomic conditional UPDATE and check its affected-row count.')])

lesson(16, 'Django architecture and request flow',
       'Django routes a visitor through a reception desk: the URL dispatcher selects a view, the view coordinates work, and a template formats the response. A model handles stored records.',
       [('Framework', 'Reusable structure that calls your application code', 'a staffed building where you fill assigned roles'), ('Project', 'Django configuration for a site', 'the building’s central plan'), ('App', 'A reusable unit of Django functionality', 'one department'), ('View', 'A callable handling a request and returning a response', 'the selected service desk'), ('Template', 'A document pattern rendered with data', 'a reusable receipt layout')],
       '# inventory/views.py\nfrom django.http import JsonResponse\n\ndef health(request):\n    return JsonResponse({"status": "ok"})\n\n# inventory/urls.py\nfrom django.urls import path\nfrom .views import health\nurlpatterns = [path("health/", health)]',
       'Create an inventory app inside a Django project and include its URLs at the root to expose /health/. A request reaches the view only after URL resolution. JsonResponse converts the dictionary to JSON and sets its content type. runserver is a development server.',
       'Enter the JSON response body for GET /health/ as an object.', {'status': 'ok'},
       [('Create the project', 'With Django 5.2 available in your environment, run python -m django startproject config . in a new project folder and python manage.py startapp inventory. Save version and folder tree.'),
        ('Register the department', 'Add inventory to INSTALLED_APPS and create inventory/urls.py. Include it from config/urls.py. Explain project URLs versus app URLs.'),
        ('Add health status', 'Implement the shown health view and route. Request /health/ locally; expect status 200, JSON content type and status ok.'),
        ('Render HTML', 'Add a home view and inventory/home.html template with an EMIO24 heading. Pass shop_name as context and verify it appears in the response.'),
        ('Use route names', 'Name the home and health routes and use reverse() to resolve them. Show both resolved paths without hard-coding the URLs in the calling code.'),
        ('Handle a missing route', 'Request /does-not-exist/ and record 404. Trace why your health view is not called. Distinguish routing failure from a Python exception inside a view.'),
        ('Trace the architecture', 'Annotate browser -> URL configuration -> view -> template/JsonResponse -> response with actual filenames. Explain where models will enter the flow next lesson.')])

lesson(17, 'Models and migrations',
       'A model describes the product ledger; a migration is a numbered renovation instruction for changing its structure. Editing the drawing alone does not renovate the database.',
       [('Model', 'A Python class mapping stored entities to database fields', 'the product-ledger design'), ('Field', 'A typed model attribute mapped to stored data', 'a ruled ledger column'), ('Migration', 'A versioned operation changing schema or data', 'a numbered renovation instruction'), ('makemigrations', 'The command generating migration files from model changes', 'writing the renovation plan'), ('migrate', 'The command applying pending migrations', 'carrying out the plan')],
       'from django.db import models\n\nclass Product(models.Model):\n    name = models.CharField(max_length=120)\n    price = models.PositiveIntegerField()\n    stock = models.PositiveIntegerField(default=0)\n\n    def __str__(self):\n        return self.name',
       'This belongs in inventory/models.py in the previous project. Django supplies a primary key unless you define one. PositiveIntegerField allows zero. Generate and inspect a migration, then apply it; saving models.py by itself does not add database columns.',
       'What stock value is declared as the default?', 0,
       [('Define Product', 'Add name max_length=120, price and stock whole-naira/integer fields with stock default 0. Explain each field choice and add __str__.'),
        ('Generate a migration', 'Run python manage.py makemigrations inventory. Open the generated file and identify CreateModel, field types and dependencies in notes.'),
        ('Apply the schema', 'Run python manage.py migrate and showmigrations inventory. Save output showing the migration applied; explain the difference between generation and application.'),
        ('Create a record', 'In manage.py shell create Pen price 200 stock 4. Close/reopen the shell and fetch the saved primary key. Record the persistent values.'),
        ('Add a field safely', 'Add optional description using blank=True and a suitable default. Generate/apply a second migration and show the existing Pen record remains usable.'),
        ('Inspect SQL', 'Run sqlmigrate for your first migration and annotate table creation and primary-key SQL. Explain why generated SQL depends on the configured database backend.'),
        ('Rebuild from history', 'Use a disposable project/database copy and apply migrations from empty. Verify Product can be created. Keep committed migration files and record the rebuild commands.')])

lesson(18, 'Django ORM queries',
       'The ORM is a translator from Python requests to database queries. A QuerySet is often an order ticket waiting to be executed, not a bag of already loaded records.',
       [('ORM', 'Object-relational mapping between code objects and database rows', 'the Python-to-ledger translator'), ('QuerySet', 'A composable database query and its results when evaluated', 'an order ticket'), ('Lazy evaluation', 'Deferring work until results are needed', 'filling the order when collected'), ('Lookup', 'A field comparison used in a query', 'the clerk’s selection rule'), ('Aggregation', 'Combining rows into summary values', 'adding ledger totals')],
       '# Run in manage.py shell after creating the fixture\nlow = Product.objects.filter(stock__lte=4).order_by("id")\nprint(list(low.values_list("name", flat=True)))',
       'Import Product from inventory.models first. filter composes a query; list evaluates it. stock__lte means stock less than or equal to the supplied value. get expects exactly one row and raises exceptions for zero or multiple matches.',
       'With Pen stock 4 and Book stock 8, inserted in that order, enter the names returned.', ['Pen'],
       [('Seed a fixture', 'Create Pen 200/4, Book 500/8 and Bag 4000/0 in a disposable database. Record primary keys and clear only your practice rows when repeating.'),
        ('Filter and order', 'Query stock <=4 ordered by stock then id. Expect Bag and Pen. Save Python and output, then check threshold 0.'),
        ('Retrieve safely', 'Use get(pk=...) for Pen and catch Product.DoesNotExist for a missing ID. Explain why filter returns an empty QuerySet instead of raising for no match.'),
        ('Update stock', 'Use an F expression to increase Pen stock by 3, then refresh_from_db. Expect 7. Explain why an already loaded object can show an older value.'),
        ('Calculate a summary', 'Use ORM aggregation to calculate the total stock units after the update: 15. Define empty-queryset behaviour and demonstrate it.'),
        ('Observe query timing', 'Use Django query capture in a test or shell to compare building a QuerySet with evaluating it. Save query counts and explain evaluation triggers.'),
        ('Limit returned data', 'Fetch only names and stock with values() or values_list(), then compare output types with model instances. Show explicit ordering and explain when this projection helps.')])

lesson(19, 'Django CRUD views',
       'CRUD is the four basic actions at the ledger desk: create a card, read it, update it and delete it. Web views wrap these actions in requests, responses and access rules.',
       [('CRUD', 'Create, read, update and delete operations', 'the four ledger services'), ('URL parameter', 'A value extracted from a matched URL', 'the card number on a request'), ('404', 'A response indicating the resource was not found', 'no card at that address'), ('Redirect', 'A response telling the client to request another URL', 'a direction to the next desk'), ('CSRF', 'Cross-site request forgery using a browser’s ambient credentials', 'an outsider tricking a signed-in clerk into submitting a form')],
       'from django.shortcuts import get_object_or_404, render\nfrom .models import Product\n\ndef product_detail(request, pk):\n    product = get_object_or_404(Product, pk=pk)\n    return render(request, "inventory/detail.html", {"product": product})',
       'The URL pattern must capture pk and the template must exist. get_object_or_404 converts a missing row into a 404 response. Read-only GET views should not change data. State-changing browser forms use POST and Django CSRF protection.',
       'What HTTP status should a missing product detail return?', 404,
       [('List products', 'Implement a GET list view ordered by ID. Render name, price and stock; show a clear empty-state message for no rows.'),
        ('Show one product', 'Add /products/<int:pk>/ and a detail template. Demonstrate a valid product and a missing ID returning 404.'),
        ('Create safely', 'Add a POST creation view that validates nonblank name and nonnegative integer price/stock. Use a CSRF-protected HTML form; invalid input must create no row.'),
        ('Update an existing record', 'Add edit GET/POST flows. Change stock 4 to 7 and redirect after success. A missing ID returns 404; invalid input preserves the stored row.'),
        ('Confirm deletion', 'GET displays a confirmation only; POST performs deletion with CSRF protection. Show that simply opening the confirmation URL leaves the record present.'),
        ('Handle browser refresh', 'Use POST-redirect-GET after successful creation. Refresh the resulting page and demonstrate that it does not create a duplicate record.'),
        ('Audit method behaviour', 'Record a matrix of routes and supported methods. Demonstrate that GET requests never add, edit or delete products and unsupported methods get an appropriate response.')])

lesson(20, 'Forms and validation',
       'A Django form is a receiving clerk who checks raw paperwork before handing trusted fields to the ledger. Browser checks help the visitor, but the server clerk must still check everything.',
       [('Bound form', 'A form associated with submitted data', 'paperwork filled by a visitor'), ('Validation', 'Checking and converting data against rules', 'the receiving clerk’s inspection'), ('cleaned_data', 'Validated and converted form values', 'the accepted fields'), ('ModelForm', 'A form derived from selected model fields', 'a form designed from the ledger columns'), ('Field error', 'Feedback attached to a particular input', 'a note next to the incorrect box')],
       'from django import forms\n\nclass StockForm(forms.Form):\n    quantity = forms.IntegerField(min_value=1)\n\nform = StockForm({"quantity": "3"})\nprint(form.is_valid())\nprint(form.cleaned_data["quantity"])',
       'Run within the configured Django project. Raw HTTP form values are strings. IntegerField converts and validates them, so cleaned quantity is integer 3. Access cleaned_data after validation, and only use fields that passed validation.',
       'Enter the two printed values as a JSON list.', [True, 3],
       [('Build ProductForm', 'Create a ModelForm exposing only name, price and stock. Render field errors and preserve submitted input when validation fails.'),
        ('Reject blank names', 'Strip name whitespace in clean_name and reject an all-space value. Demonstrate " Pen " becomes Pen and "   " creates no product.'),
        ('Validate quantities', 'Create SaleForm with IntegerField(min_value=1). Demonstrate 3 accepted and 0, -1, "two" and "2.5" rejected with visible field errors.'),
        ('Check related rules', 'Validate requested quantity against the selected product’s available stock. Starting stock 4, quantity 5 is rejected without changing the database.'),
        ('Use cleaned values', 'Refactor the view to use cleaned_data or form.save only after is_valid. Explain why directly using request.POST bypasses your validated values.'),
        ('Protect the form flow', 'Include csrf_token and a labelled submit button. Show GET renders an unbound form and invalid POST re-renders a bound form with errors.'),
        ('Test bypassed browser rules', 'Submit invalid values directly with Django’s test client rather than relying on HTML input restrictions. Record status, form errors and unchanged row count.')])

lesson(21, 'Authentication and sessions',
       'Authentication checks who is at the door; authorization decides which room they may enter. A session cookie is a reference to signed-in state, not permission to do everything.',
       [('Authentication', 'Establishing an identity', 'checking an identity card'), ('Authorization', 'Deciding whether an identity may perform an action', 'checking the room-access list'), ('Session', 'Server-side interaction state associated with a client identifier', 'the desk’s record for a visitor ticket'), ('Password hash', 'A one-way password verification representation with a work factor', 'a verification imprint rather than a readable password'), ('Logout', 'Ending the client’s authenticated session', 'invalidating the visitor ticket')],
       'from django.contrib.auth.decorators import login_required\nfrom django.http import JsonResponse\n\n@login_required\ndef dashboard(request):\n    return JsonResponse({"username": request.user.username})',
       'Django authentication middleware populates request.user. login_required normally redirects anonymous browser visitors to login. It does not enforce product ownership or staff privileges. Use Django password APIs rather than storing or comparing plaintext passwords.',
       'Is checking a signed-in user owns a product authentication or authorization? Enter the term.', 'authorization',
       [('Create local users', 'Create two disposable users through Django APIs or management commands. Use set_password/create_user; demonstrate check_password works without saving plaintext in notes.'),
        ('Add login', 'Use Django’s LoginView and a login template. Configure redirect paths. Show correct credentials reach a dashboard and incorrect credentials produce a useful error.'),
        ('Guard a view', 'Protect dashboard with login_required. Record the anonymous redirect and authenticated 200 response.'),
        ('Implement logout', 'Use a CSRF-protected POST logout form. After logout, revisit dashboard and confirm authentication is required again.'),
        ('Separate privileges', 'Restrict product deletion to staff or an explicit permission. Show a signed-in ordinary user denied and a permitted user allowed.'),
        ('Inspect session behaviour', 'Use browser tools to identify the session cookie without copying its value into your submission. Explain the roles of HttpOnly, Secure and SameSite.'),
        ('Test identity boundaries', 'Write tests for anonymous, normal and privileged users. Check both visible links and direct requests, proving hidden buttons alone do not enforce access.')])

lesson(22, 'DRF serializers',
       'A serializer is a bilingual receiving clerk: it converts model data to simple response values and checks incoming values before creating or changing records. It is not itself the network connection.',
       [('Serializer', 'A component converting and validating representations', 'the bilingual receiving clerk'), ('Deserialization', 'Turning an external representation into internal values', 'translating an incoming form'), ('validated_data', 'Input values accepted by serializer validation', 'the approved fields'), ('read_only', 'A field excluded from writable input', 'an office-assigned box'), ('ModelSerializer', 'A serializer with model-derived fields and defaults', 'a clerk using the ledger blueprint')],
       'from rest_framework import serializers\n\nclass SaleSerializer(serializers.Serializer):\n    quantity = serializers.IntegerField(min_value=1)\n\ns = SaleSerializer(data={"quantity": "3"})\nprint(s.is_valid())\nprint(s.validated_data["quantity"])',
       'Run in a Django project with DRF installed. Passing data= means incoming values need validation; passing an instance means representing existing data. is_valid performs checks before validated_data is consumed. This example converts the text quantity to integer 3.',
       'Enter the validated quantity as a JSON number.', 3,
       [('Configure DRF', 'Add rest_framework to INSTALLED_APPS in your project and record the installed version. Keep dependency versions in requirements.txt.'),
        ('Represent Product', 'Create ProductSerializer with explicit id, name, price and stock fields. Serialize Pen and show a JSON-compatible dictionary; serialize a list using many=True.'),
        ('Validate incoming data', 'Instantiate with data= for valid Pen input and invalid negative stock. Call is_valid and record validated_data or field errors; invalid input must not save.'),
        ('Protect assigned fields', 'Make id read-only. Supply an arbitrary id in input and demonstrate the client cannot choose an existing row’s primary key on creation.'),
        ('Add a field rule', 'Strip and validate name with validate_name. Show blank input rejected and padded valid input normalized.'),
        ('Create and update', 'Call save after successful validation to create then update a Product. Record row count and values; explain instance= versus data=.'),
        ('Partial update', 'Use partial=True to change stock alone. Show name remains unchanged. Compare the same incomplete input under full validation and record which fields are required.')])

lesson(23, 'DRF API views',
       'An API view is the dispatcher joining request handling, validation and response formatting. The serializer inspects the paperwork; the view decides when to use it and which response to send.',
       [('APIView', 'DRF’s class-based request handling base', 'the API service desk'), ('Response', 'A DRF response rendered according to content negotiation', 'a receipt awaiting its final format'), ('request.data', 'Parsed request content exposed by DRF', 'the opened order envelope'), ('Content negotiation', 'Choosing a supported response representation', 'agreeing on the receipt format'), ('Generic view', 'A reusable implementation of common API operations', 'a standard desk procedure')],
       'from rest_framework.decorators import api_view\nfrom rest_framework.response import Response\n\n@api_view(["GET"])\ndef health(request):\n    return Response({"status": "ok"})',
       'Wire health into Django URLs. The decorator restricts methods and wraps the Django request with DRF behaviour. Returning a dictionary alone is insufficient; Response carries data for rendering. Use serializer errors with 400 and creation success with 201.',
       'Which status code should POST to this GET-only endpoint return?', 405,
       [('List through an API', 'Implement GET /api/products/ using ProductSerializer(many=True). Demonstrate populated and empty results, documenting whether pagination is enabled.'),
        ('Create through an API', 'Implement POST using request.data, serializer validation and save. A valid product returns 201; invalid stock returns 400 and no extra row.'),
        ('Read one product', 'Implement GET detail using a primary-key URL parameter. Return serialized data for an existing row and 404 for a missing one.'),
        ('Update one product', 'Implement PUT or PATCH with the documented completeness rules. Demonstrate changing stock, preserving unrelated fields on PATCH, and rejecting a negative value.'),
        ('Delete through an API', 'Implement DELETE returning 204 with an empty body. Verify the row is gone and a subsequent detail request is 404.'),
        ('Exercise error paths', 'Send an unsupported method and malformed JSON using local API tests. Record 405 and 400 behaviour and prove the database remains unchanged.'),
        ('Compare implementations', 'Reimplement list/create with a DRF generic view in a separate module. Compare the serializer, queryset and permission configuration while retaining the same observable contract.')])

lesson(24, 'ViewSets, routers and pagination',
       'A ViewSet groups related counter services; a router prints the directory mapping URLs and methods to those services. The directory does not decide who is allowed through the door.',
       [('ViewSet', 'A class grouping resource actions', 'one resource department'), ('Router', 'A generator of URL patterns for ViewSets', 'the printed counter directory'), ('Action', 'A named operation on a ViewSet', 'a service offered at the counter'), ('basename', 'The base used for generated route names', 'the directory’s naming prefix'), ('Pagination', 'Bounding collection responses into pages', 'handing out catalogue pages')],
       'from rest_framework.routers import DefaultRouter\nfrom .views import ProductViewSet\n\nrouter = DefaultRouter()\nrouter.register("products", ProductViewSet, basename="product")\nurlpatterns = router.urls',
       'Define ProductViewSet with a queryset and serializer_class, then include these URLs beneath /api/. The list/create path is products/; detail actions include a lookup value. Route names such as product-list derive from basename, not necessarily the model class.',
       'Enter the generated list route name for basename product.', 'product-list',
       [('Create a ViewSet', 'Implement ProductViewSet using ModelViewSet, Product queryset and serializer. Preserve your existing validation rules.'),
        ('Register routes', 'Register products with basename product under /api/. Use reverse for product-list and product-detail and record resolved URLs.'),
        ('Verify CRUD routing', 'Record method/path/action mappings for list, create, retrieve, update, partial_update and destroy. Test one success and one missing detail.'),
        ('Bound collection size', 'Configure page-number pagination with page size 2. Seed five products and verify page lengths 2, 2, 1 with stable ID ordering.'),
        ('Add a read-only action', 'Add a low-stock collection action using stock <= supplied threshold. Validate threshold input and ensure its result is serialized and paginated consistently.'),
        ('Limit filtering', 'Support an explicit allowed set of ordering fields. Demonstrate stock ordering and document how an unsupported field is handled.'),
        ('Check the contract', 'Update api-contract.md to match generated routes, trailing slashes and page envelope. Test a client reads results rather than assuming the root is a list.')])

lesson(25, 'JWT authentication',
       'A signed access token resembles a tamper-evident visitor pass. A verifier checks its signature and expiry. The printed claims are usually readable; a signature is not encryption.',
       [('JWT', 'A compact token format carrying claims', 'the visitor pass format'), ('Claim', 'A statement stored in a token payload', 'a printed field on the pass'), ('Signature', 'Cryptographic integrity/authenticity protection', 'the tamper-evident seal'), ('Access token', 'A credential used to access a protected resource', 'the short-lived entry pass'), ('Refresh token', 'A credential used to obtain new access tokens', 'the renewal voucher')],
       '{"sub":"user-7","exp":2000,"iss":"emio24"}\n\n# Illustrative claims only; this is not a signed token.\n# A verifier rejects it when current time is >= exp.',
       'A complete verification policy checks signature, allowed algorithm, expiry and applicable issuer/audience rules. Decoding a payload alone does not authenticate anyone. Use a maintained authentication library; never build cryptography from this teaching sketch.',
       'At time 2001, is a token expiring at 2000 expired? Enter a Boolean.', True,
       [('Define the token flow', 'Draw login -> access/refresh tokens -> authenticated API request -> expiry -> refresh. Identify which steps require credentials and which can fail.'),
        ('Configure library authentication', 'Use a maintained JWT integration compatible with your installed Django/DRF versions. Record its exact version and configure access-token authentication without implementing signatures yourself.'),
        ('Obtain disposable tokens', 'Create token endpoints and request tokens for a local test user. Record statuses and claim names with credential/token values redacted.'),
        ('Call a protected endpoint', 'Send an access token using Authorization: Bearer. Demonstrate a valid request and a missing/invalid credential rejection; record the configured status semantics.'),
        ('Check expiry', 'Use a short lifetime in local test settings or the library’s time-testing support. Demonstrate an expired access token is rejected even though its payload can still be decoded.'),
        ('Refresh deliberately', 'Exchange a valid refresh token for a new access token, then try an invalid refresh token. Document rotation/revocation settings and their logout implications.'),
        ('Compare storage choices', 'Compare memory and HttpOnly-cookie approaches for a browser client, including XSS/CSRF implications. Choose one for your app and document reload, refresh and logout behaviour.')])

lesson(26, 'Permissions and ownership',
       'Signing in gets a visitor into reception; ownership checks decide which stockroom records that visitor may see or change. Hiding a door in the UI does not lock it.',
       [('Permission', 'A rule deciding whether an operation is allowed', 'the room-access rule'), ('Object-level permission', 'Authorization concerning a particular record', 'access to one specific cabinet'), ('Queryset scoping', 'Restricting queried records to those the user may access', 'only bringing authorized cards to the desk'), ('Least privilege', 'Granting only access needed for a task', 'issuing the fewest necessary keys'), ('Tenant', 'An isolated customer or organization sharing an application', 'one business renting space in the building')],
       '# Inside an authenticated ProductViewSet\ndef get_queryset(self):\n    return Product.objects.filter(owner=self.request.user)',
       'Add an owner relation to Product first. Filtering prevents other users’ records appearing in list results and ordinary detail lookup. Object permissions do not automatically filter every list item; creation also needs explicit ownership assignment from request.user.',
       'User A owns 2 products and user B owns 3. How many should A see in this queryset?', 2,
       [('Add ownership', 'Add an owner foreign key to Product and migrate. Plan how existing rows receive owners in a disposable fixture rather than silently assigning every real row.'),
        ('Scope list results', 'Filter the queryset to request.user. Seed A with two products and B with three; demonstrate their lists contain 2 and 3 records respectively.'),
        ('Block guessed IDs', 'Have A request B’s detail, update and delete URLs directly. Verify no data exposure or mutation; document whether your scoped endpoint returns 404 or 403.'),
        ('Assign owner server-side', 'Use perform_create(serializer.save(owner=request.user)) or equivalent. Submit B’s ID as A and show A cannot transfer ownership through writable input.'),
        ('Add a business role', 'Define staff read/write privileges explicitly and implement them. Demonstrate one allowed and one denied operation for an ordinary user and a staff user.'),
        ('Guard custom actions', 'Apply the same scope and permission rules to low-stock and sale actions. Show that a custom route cannot bypass another user’s inventory boundary.'),
        ('Build a permission matrix', 'Write automated API tests covering anonymous/A/B/staff against list/detail/create/update/delete. Record expected status and database effect for each relevant case.')])

lesson(27, 'Application security foundations',
       'Security resembles protecting a shop through several controls: checked inputs, locked cabinets and limited keys. One locked door does not protect an open back entrance.',
       [('Threat model', 'A description of assets, actors, trust boundaries and possible abuse', 'the shop’s break-in map'), ('Injection', 'Untrusted data being interpreted as executable instructions', 'an order form rewriting the clerk’s rules'), ('XSS', 'Untrusted script executing in a user’s browser context', 'a forged notice running commands at reception'), ('CORS', 'Browser rules controlling cross-origin response access', 'rules for which outside desks may read replies'), ('Secret', 'Sensitive material used to authenticate or protect systems', 'a key rather than a public sign')],
       '# Bind values as data, never concatenate them into SQL.\ncursor.execute("SELECT id FROM products WHERE name = %s", [user_input])\n# This is Django cursor syntax; sqlite3 directly uses ? placeholders.',
       'Parameterized SQL separates instruction structure from input values. CORS is enforced by browsers and does not authenticate clients. Keep Django template escaping and CSRF protection enabled for relevant browser flows, and store deployment secrets outside committed code.',
       'Does CORS replace API authentication? Enter a Boolean.', False,
       [('Map trust boundaries', 'Draw browser, API, database and deployment configuration. List stock records, credentials and customer information as assets with one realistic abuse case each.'),
        ('Demonstrate safe query input', 'In a local fixture search for a name containing quotes using bound parameters. Show it is treated as a name and cannot change query structure.'),
        ('Verify escaping', 'Render the literal product name <script>alert(1)</script> in a local template. Confirm it displays as text rather than executing. Document why marking user text safe changes this.'),
        ('Check CSRF', 'With Django test client CSRF enforcement enabled, submit a session-authenticated write without a CSRF token and then with a valid token. Record expected rejection and success.'),
        ('Configure origins', 'Document frontend/backend origins including ports. If separate origins are used, allow only the intended origins; demonstrate allowed and disallowed browser cases.'),
        ('Separate secrets', 'Read a dummy deployment secret from an environment variable; fail clearly if missing. Commit an example variable name with a placeholder and confirm actual .env is ignored.'),
        ('Review production errors', 'In local production-like settings disable debug output and test a controlled error. Show users receive a generic response while useful redacted detail is logged locally.')])

lesson(28, 'Testing the backend',
       'Tests are repeatable quality checks at the shop. A fixture sets up known stock; an assertion compares what happened with what should happen. A passing check proves only the cases it actually examines.',
       [('Test case', 'A repeatable check with setup, action and expected result', 'one quality inspection'), ('Assertion', 'A condition that must hold for a test to pass', 'the inspector’s comparison'), ('Fixture', 'Known data or environment used by a test', 'the prepared sample shelf'), ('Unit test', 'A focused check of a small piece of behaviour', 'testing one counter tool'), ('Integration test', 'A check of collaborating components', 'rehearsing the whole checkout handoff')],
       'import unittest\n\ndef total(price, quantity):\n    return price * quantity\n\nclass TotalTests(unittest.TestCase):\n    def test_sale(self):\n        self.assertEqual(total(200, 3), 600)\n\nif __name__ == "__main__":\n    unittest.main()',
       'The assertion uses an independently known expected value. A test that calculates its expectation using the same broken logic can miss defects. Django TestCase adds database isolation; APIClient supports API request checks. Test both returned responses and persistent side effects.',
       'What expected numeric value does the assertion use?', 600,
       [('Test a calculation', 'Write a standard-library unittest for sale totals with 200*3=600, zero stock value and another price. Show the exact discovery command and results.'),
        ('Test validation', 'Add tests rejecting zero, negative, fractional and excessive sale quantities. Assert unchanged stock for every rejected case.'),
        ('Test persistence', 'Use a temporary database/file fixture and verify a saved product can be reloaded. Keep tests independent from your working inventory.'),
        ('Test the API contract', 'Use DRF APIClient for valid creation 201, invalid creation 400 and missing detail 404. Check response fields and row counts.'),
        ('Test access boundaries', 'Create two users and prove one cannot read or change the other’s products. Include a direct request using a guessed valid ID.'),
        ('Use a fake service', 'Replace the external payment boundary with a fake returning success or failure. Check a failure does not deduct stock; no network calls should be needed.'),
        ('Prove a test detects a bug', 'Temporarily introduce an incorrect comparison at the stock boundary in a disposable copy. Show a relevant test fails, restore the correct implementation and show it passes.')])

lesson(29, 'Query performance and caching',
       'Performance work is timing the queue before changing the shop layout. Fetching one supplier per product is many trips to the same cabinet; a joined fetch can reduce those trips.',
       [('Latency', 'Elapsed time for an operation', 'one customer’s waiting time'), ('Throughput', 'Operations completed per unit time', 'customers served per minute'), ('N+1 queries', 'One initial query followed by a query per result', 'one catalogue trip plus a supplier trip per card'), ('Cache', 'Stored reusable results', 'a temporary copy at the counter'), ('Invalidation', 'Removing or updating cached results after changes', 'replacing an outdated counter copy')],
       '# Product has a supplier ForeignKey.\nproducts = Product.objects.select_related("supplier").order_by("id")\nfor product in products:\n    print(product.name, product.supplier.name)',
       'select_related joins single-valued relationships such as foreign keys. prefetch_related uses separate queries and joins results in Python, fitting collections. Fewer queries do not guarantee faster execution for every workload; measure representative data and response correctness.',
       'A naive list does 1 product query plus 1 supplier query for each of 5 products. How many queries is that?', 6,
       [('Create a baseline', 'Seed at least 100 products with suppliers. Measure query count and elapsed time for a list endpoint with repeated trials; record fixture size and environment.'),
        ('Expose N+1', 'Render each product’s supplier name without eager loading. Capture query count and explain the repeated pattern.'),
        ('Join a foreign key', 'Apply select_related for supplier and measure again. Verify returned names and ordering are unchanged; report query counts before/after.'),
        ('Prefetch a collection', 'For a many-to-many category relation or reverse sale lines, compare naive access with prefetch_related. Explain why select_related alone cannot serve that collection.'),
        ('Bound output', 'Paginate a list and select only needed fields where appropriate. Compare payload size and query behaviour without dropping required response fields.'),
        ('Cache a summary', 'Cache a stock summary with a documented key and expiry. Include owner/tenant in keys when relevant. Show users cannot receive each other’s cached totals.'),
        ('Invalidate after a sale', 'Sell an item and invalidate/update the relevant cache after a successful database commit. Demonstrate the next summary shows current stock and a failed sale does not publish a wrong total.')])

lesson(30, 'Docker and reproducible services',
       'An image is a packaged workshop template; a container is a running workshop made from it. A volume is storage kept outside that workshop’s replaceable walls.',
       [('Image', 'A layered template for container files and configuration', 'the packaged workshop template'), ('Container', 'An isolated process environment created from an image', 'one running workshop'), ('Dockerfile', 'Instructions for building an image', 'the packaging recipe'), ('Volume', 'Storage managed independently of a container’s writable layer', 'the external storeroom'), ('Port mapping', 'Connecting a host port to a container port', 'linking an outside door to an inside counter')],
       'FROM python:3.12-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN python -m pip install --no-cache-dir -r requirements.txt\nCOPY . .\nCMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]',
       'This is a development Dockerfile, not a production server configuration. requirements.txt must contain compatible dependencies. The process listens on all container interfaces so a published port can reach it. Building requires the base image and packages to be available locally or downloaded beforehand.',
       'With -p 8080:8000, which port does the browser use on the host?', 8080,
       [('Package development', 'Write a Dockerfile based on the example for your Django project. Include explicit dependency versions and describe every instruction.'),
        ('Exclude unnecessary files', 'Write .dockerignore excluding .git, .venv, node_modules, .env and private local database files. Inspect build context contents for accidental data inclusion.'),
        ('Build and identify', 'Build an emio24-dev image and record its image ID plus build output. If offline artifacts are missing, record the missing prerequisite rather than a fabricated build.'),
        ('Run the service', 'Run a disposable container mapping host 8080 to 8000. Request the health endpoint, record 200, then stop the container.'),
        ('Pass configuration', 'Provide a dummy environment variable at runtime and read it through settings. Show it is not baked into the Dockerfile or image source.'),
        ('Persist outside the container', 'Mount a dedicated practice volume for database/data storage. Create a product, replace the container using the same volume, and show the product persists.'),
        ('Document offline readiness', 'List required Docker engine, base image and dependency artifacts. Write reproducible build/run/stop instructions and explain the production changes still needed before deployment.')])

lesson(31, 'JavaScript fundamentals',
       'JavaScript values and control flow resemble Python’s stockroom tools, but the labels and rules differ. const locks a name’s binding; it does not freeze the contents of the box.',
       [('Binding', 'An association between a name and a value', 'a label pointing to a box'), ('const', 'A declaration whose binding cannot be reassigned', 'a fixed label attachment'), ('let', 'A block-scoped reassignable declaration', 'a label you may move within one room'), ('Object', 'A collection of properties', 'a named product card'), ('Strict equality', 'Equality comparison without type coercion', 'comparing labels without automatic conversion')],
       'const product = {name: "Pen", stock: 4};\nproduct.stock += 2;\nconsole.log(product.stock);\nconsole.log("6" === 6);',
       'The const binding still points to the same object, whose stock property changes to 6. Strict equality compares the string and number as different types. Run plain JavaScript in Node or a browser console; JSX comes later.',
       'Enter the two logged values as a JSON list.', [6, False],
       [('Use declarations', 'In practice.js declare shopName with const and stock with let. Update stock, then demonstrate a caught reassignment error for a const binding in a separate example.'),
        ('Convert input', 'Convert "200" and "3" to numbers and calculate 600. Check Number.isFinite after conversion and reject a nonnumeric value; explain why empty text needs an explicit rule.'),
        ('Classify stock', 'Implement stockLabel(stock) returning out for 0, low for 1 through 5 and available above 5. Demonstrate 0,1,5,6.'),
        ('Represent products', 'Create an array of three product objects with id, name, price and stock. Update only the second product and show all records before/after.'),
        ('Sum inventory', 'Implement inventoryValue(products) returning the sum of price*stock and 0 for empty input. Use Pen 200/10 and Book 500/3 to expect 3500.'),
        ('Find a product', 'Implement findProduct(products,id) and document missing-result behaviour. Test first, last and absent IDs without changing the array.'),
        ('Connect a basic page', 'Create index.html with a labelled quantity input, button and output element. Load practice.js and display a calculated total on click; show an invalid-input message.')])

lesson(32, 'Modern JavaScript transformations',
       'map sends every product card through a rewriting station; filter keeps selected cards; reduce combines cards into one summary. A spread copy duplicates the outer box, not every nested object.',
       [('Arrow function', 'A compact function expression with lexical this', 'a short task instruction using its surrounding context'), ('Destructuring', 'Extracting values through a matching pattern', 'unpacking labelled compartments'), ('Spread', 'Expanding iterable values or object properties', 'emptying one outer box into another'), ('map', 'Creating an array from one result per input item', 'rewriting every card'), ('reduce', 'Accumulating values into a result', 'combining receipt lines into a total')],
       'const products = [{name:"Pen",stock:4},{name:"Book",stock:8}];\nconst names = products.filter(p => p.stock <= 4).map(p => p.name);\nconsole.log(names);',
       'filter selects the Pen object, then map extracts its name. Neither call changes the original array in this example, but the selected object references are shared. Copy the changed nested object too when making an immutable update.',
       'Enter the resulting names array.', ['Pen'],
       [('Extract fields', 'Use object destructuring to read name and stock from a product, with a default category. Demonstrate missing category versus a present category.'),
        ('Transform without mutation', 'Use map to add a displayLabel to copied products. Show original objects have no new displayLabel property.'),
        ('Filter low stock', 'Implement lowStockNames(products,threshold) with filter/map. Check equality at 4, above threshold, and an empty array.'),
        ('Reduce totals', 'Use reduce with initial value 0 to total price*stock. Test the 3500 fixture and empty input.'),
        ('Update nested data', 'Create state={products:[...]}; replace one product stock using object spread and map. Demonstrate both original stock and unrelated product values remain unchanged.'),
        ('Export reusable functions', 'Move calculations to calculations.js with named exports and import from an ES module entry. Run with browser type=module or correctly configured Node modules and record the setup.'),
        ('Handle optional fields', 'Read an optional supplier name with optional chaining and ?? fallback. Show absent supplier and an intentionally empty string; explain why || may behave differently.')])

lesson(33, 'Async JavaScript and APIs',
       'A promise is a collection ticket for work that may finish later. await pauses that async function until the ticket settles; it does not freeze every activity in the browser.',
       [('Promise', 'An object representing eventual completion or failure', 'the collection ticket'), ('async', 'A function declaration/expression returning a promise', 'a counter that issues tickets'), ('await', 'Pausing an async function until a promise settles', 'waiting for your ticket at that counter'), ('fetch', 'A browser/JavaScript API for making requests', 'sending the order'), ('Race condition', 'A result depending on the timing of competing operations', 'older paperwork arriving after its replacement')],
       'async function loadProducts() {\n  const response = await fetch("/api/products/");\n  if (!response.ok) throw new Error(`HTTP ${response.status}`);\n  return response.json();\n}',
       'fetch commonly resolves even for HTTP 404 or 500, so inspect response.ok. Parsing JSON is another asynchronous operation. Surround calls with try/catch for request, status and parsing failures; distinguish loading, empty, success and error states.',
       'Does a fetch response with status 404 have ok equal to true? Enter a Boolean.', False,
       [('Trace scheduling', 'Log start, queue a resolved Promise callback, then log end. Predict and record the order in practice.js and explain why the callback follows synchronous code.'),
        ('Fetch local products', 'Implement loadProducts using the example and your local API. Document whether it returns an array or paginated envelope and extract the intended records.'),
        ('Show loading', 'Disable a load button while a request runs and display Loading. Restore the button in finally on both success and failure.'),
        ('Handle HTTP errors', 'Call a missing local endpoint and a mocked 500 response. Check response.ok and display a useful status-based message without treating the error body as product data.'),
        ('Handle parsing and network failures', 'Use local mocks returning invalid JSON and rejecting fetch. Demonstrate both reach the error UI and clear loading state.'),
        ('Cancel obsolete requests', 'Use AbortController for a replaced search request. Treat cancellation separately from a server failure; show an older response cannot replace newer search results.'),
        ('Use deterministic mocks', 'Create mock success, empty, delayed and rejected responses locally. Record observed UI states for each so practice and review need no internet.')])

lesson(34, 'React components and props',
       'A component is a reusable display recipe; props are the ingredients handed to it. Rendering describes the screen from those ingredients. A component should not quietly rewrite the parent’s ingredients.',
       [('Component', 'A reusable unit describing UI', 'the display recipe'), ('JSX', 'Syntax for describing elements inside JavaScript', 'a structured display sketch'), ('Props', 'Inputs supplied to a component', 'ingredients from the parent'), ('Render', 'Computing a UI description', 'drawing the display from current ingredients'), ('Key', 'A stable identity hint for siblings in a list', 'the permanent card number on repeated displays')],
       'export function ProductCard({product}) {\n  return <article>\n    <h2>{product.name}</h2>\n    <p>{product.stock} units</p>\n  </article>;\n}',
       'Use this in a React project with JSX tooling already installed. The component receives product through props and returns a description. Render lists with stable product IDs as keys; array indexes can misidentify items after insertions or reordering.',
       'With product={name:"Pen",stock:4}, enter the paragraph text.', '4 units',
       [('Prepare React locally', 'Use your installed React project/toolchain and record package versions plus the local start command. Confirm the starting page renders before adding features.'),
        ('Build ProductCard', 'Implement the example in a separate file. Display name, whole-naira price and stock with semantic HTML; render Pen and Book with different props.'),
        ('Render a list', 'Create ProductList mapping products to cards with key={product.id}. Reorder the fixture and verify each card still represents the correct product.'),
        ('Handle no data', 'Render a clear empty-inventory message when products.length is 0. Demonstrate both empty and populated inputs.'),
        ('Compose the page', 'Create App with Header, ProductList and Footer. Show the component tree and identify which component owns the fixture data.'),
        ('Use conditional content', 'Show Out of stock at 0 and Low stock for 1 through 5. Demonstrate 0,1,5,6 and avoid rendering an accidental numeric 0 from an && expression.'),
        ('Keep props read-only', 'Add an onSelect callback prop and invoke it from a labelled button. Show the parent receives the selected ID; do not mutate product inside the card.')])

lesson(35, 'React state and controlled forms',
       'State is a component’s remembered notebook. Each render sees a snapshot. Asking React to update it schedules a new snapshot; it does not rewrite the variable in the currently running handler.',
       [('State', 'Data React retains between renders', 'the component’s notebook'), ('Hook', 'A React function connecting components to features such as state', 'a standard notebook service'), ('State setter', 'A function scheduling a state update', 'a request for the next notebook page'), ('Controlled input', 'An input whose displayed value comes from state', 'a form box synchronized with the notebook'), ('Lifting state', 'Moving shared state to a common ancestor', 'one shared notebook for two counters')],
       'import {useState} from "react";\n\nexport function Counter() {\n  const [count, setCount] = useState(0);\n  return <button onClick={() => {\n    setCount(c => c + 1);\n    setCount(c => c + 1);\n  }}>{count}</button>;\n}',
       'Functional updates receive the queued previous value, so one click adds 2. Two setCount(count + 1) calls in this handler would each use the same render snapshot. Keep Hooks at the top level of components or custom Hooks.',
       'Starting at 0, what count is displayed after one click?', 2,
       [('Add a counter', 'Implement Counter and demonstrate the initial 0 and one-click 2 result. Compare functional setters with two snapshot-based setters in a separate demonstration.'),
        ('Control a quantity field', 'Use state for an input value and onChange. Keep the raw text while editing; convert and validate on submit. Demonstrate empty, 3 and invalid text.'),
        ('Build an add-product form', 'Control name, price and stock inputs. Reject blank name or negative/non-integer numbers with visible messages; successful submission calls a parent callback.'),
        ('Update arrays immutably', 'Add a new product using a new array and update one product with map plus object spread. Show existing product data is preserved.'),
        ('Lift shared state', 'Put products in the common parent of list and summary. Add a product and show both components update from the same data source.'),
        ('Derive a total', 'Calculate inventory value from products during rendering instead of storing a separate synchronized total. Show updating price or stock updates the summary.'),
        ('Reset deliberately', 'After a successful local submission clear the form; after a failed validation keep entered values. Demonstrate both flows with keyboard-accessible labels and buttons.')])

lesson(36, 'React effects and data fetching',
       'An Effect synchronizes the rendered application with an outside system, like arranging a delivery subscription after opening a counter. Cleanup cancels the old arrangement before a replacement or unmount.',
       [('Effect', 'Logic synchronizing a component with an external system', 'the delivery arrangement'), ('Dependency array', 'Reactive values that determine resynchronization', 'the details that require a new arrangement'), ('Cleanup', 'Logic stopping or undoing the previous synchronization', 'cancelling the old arrangement'), ('Unmount', 'Removing a component from the rendered tree', 'closing the counter'), ('Stale response', 'A completed request no longer matching current intent', 'a delivery for an old order')],
       'useEffect(() => {\n  const controller = new AbortController();\n  fetch(url, {signal: controller.signal})\n    .then(r => { if (!r.ok) throw new Error(`HTTP ${r.status}`); return r.json(); })\n    .then(setData)\n    .catch(e => { if (e.name !== "AbortError") setError(e.message); });\n  return () => controller.abort();\n}, [url]);',
       'Import useEffect and supply url, setData and setError within a component. This snippet illustrates synchronization/cleanup; the assignment adds complete loading and stale-result handling. Effects are not needed to calculate a total from existing state. Development Strict Mode may run an extra setup/cleanup cycle.',
       'If url changes from /a to /b, should this Effect resynchronize? Enter a Boolean.', True,
       [('Fetch on mount', 'Create a product page using an Effect and local API URL. Display products after a successful response and record the initial and loaded UI.'),
        ('Represent request states', 'Model loading, success, empty and error states explicitly. Provide a local mock for each and verify the right content is visible.'),
        ('Respond to dependencies', 'Add a search query or category input used in the request URL. Include reactive dependencies and demonstrate changed input fetches the corresponding data.'),
        ('Clean up requests', 'Use AbortController on cleanup and ignore cancellation errors. Navigate away during a delayed request and verify no obsolete update is applied.'),
        ('Prevent stale results', 'Delay query A longer than query B, request A then B, and prove B remains displayed when A finishes. Use cancellation or an active-request guard.'),
        ('Add retry', 'Provide a retry button after an error. Demonstrate failed -> loading -> success with a deterministic mock without forcing a full page reload.'),
        ('Remove unnecessary effects', 'Compute filtered visible products or inventory total directly from current data where appropriate. Explain why storing the derived value via another Effect risks unnecessary synchronization.')])

lesson(37, 'React routing',
       'Client routing is the shop directory inside the browser. It chooses the displayed page for a URL. A hidden route or redirect is a convenience for users; the API must still enforce its own locks.',
       [('Client-side route', 'A mapping from browser location to UI', 'the internal shop directory'), ('Route parameter', 'A variable segment of a matched route', 'the card number on a directory entry'), ('Navigation', 'Moving to another location/page', 'walking to a listed department'), ('History', 'The browser’s sequence of navigable locations', 'the visitor’s route trail'), ('Fallback route', 'UI shown when no specific route matches', 'the directory’s unknown-room desk')],
       '// React Router declarative mode; import from your installed package.\n<Routes>\n  <Route path="/products" element={<ProductListPage />} />\n  <Route path="/products/:id" element={<ProductDetailPage />} />\n  <Route path="*" element={<NotFoundPage />} />\n</Routes>',
       'Place Routes inside a BrowserRouter and import the components from your installed React Router package (record its version). The detail page reads id with useParams. A production server must serve the app entry for appropriate client routes on refresh, while preserving API/static routes.',
       'For /products/7 matched by /products/:id, enter the id parameter as a string.', '7',
       [('Install and document routing', 'Use a compatible locally available React Router package, record version/import package, and wrap the app in BrowserRouter. Show the initial route renders.'),
        ('Create list and detail routes', 'Implement /products and /products/:id pages. Read the ID parameter and display the matching local product; distinguish unknown ID from loading.'),
        ('Navigate with links', 'Use router links from list cards to details. Demonstrate navigation and browser Back/Forward while preserving coherent page content.'),
        ('Add a fallback', 'Show an accessible NotFound page for /unknown with a link back to products. Explain how unknown UI routes differ from API 404 responses.'),
        ('Reflect filters in the URL', 'Store a search/filter value in query parameters. Copy the URL into a new tab and show the same filter is restored.'),
        ('Guard a page for UX', 'Redirect signed-out users away from a dashboard to login and return to the intended page after login. Demonstrate the API independently rejects unauthenticated access.'),
        ('Test deep links', 'Open and refresh a detail URL directly. Configure or document the development/production fallback needed, ensuring /api/ requests are not replaced by HTML.')])

lesson(38, 'Frontend architecture',
       'A growing frontend is a shop with separate responsibilities: page counters coordinate tasks, reusable displays show information, and one delivery office handles API transport.',
       [('Separation of concerns', 'Assigning distinct responsibilities to code units', 'different staff roles'), ('Custom Hook', 'A reusable function composing React Hooks', 'a reusable stateful desk procedure'), ('API client', 'A module centralizing request behaviour', 'the delivery office'), ('Single source of truth', 'One authoritative owner for a piece of state', 'one official stock notebook'), ('Context', 'A React mechanism making a value available down a tree', 'a shared notice accessible to descendants')],
       '// api/products.js\nexport async function listProducts(signal) {\n  const response = await fetch("/api/products/", {signal});\n  if (!response.ok) throw new Error(`HTTP ${response.status}`);\n  const body = await response.json();\n  return body.results; // Contract: this endpoint is paginated.\n}',
       'Centralizing the transport contract means pages do not repeat envelope parsing and status handling. A custom Hook can own request state while a component owns display. Avoid putting every local input in global Context; scope state to its actual consumers.',
       'Which field contains the product array in the declared paginated contract?', 'results',
       [('Map the current app', 'Draw pages, reusable components, hooks and API modules. Identify duplicated request code and duplicated ownership of the same state.'),
        ('Extract the API client', 'Implement list/get/create/update product functions with consistent status and JSON handling. Document exact inputs/outputs and the pagination envelope.'),
        ('Create useProducts', 'Extract loading/data/error/retry behaviour into a custom Hook. Keep cancellation or stale-response protection and demonstrate two UI consumers using the same contract.'),
        ('Separate display', 'Make ProductList accept products and callbacks as props without fetching internally. Render it against local empty and populated fixtures.'),
        ('Scope shared state', 'Use Context for session information only where needed. Keep a single form’s draft state local and explain the boundary with a component tree.'),
        ('Centralize error presentation', 'Define a reusable error component with a message and optional retry action. Show network failure and field-validation feedback remain distinguishable.'),
        ('Check architectural change', 'Repeat list/detail/add/edit flows after refactoring. Record behaviour before/after and verify API calls, permissions and stale-response handling remain correct.')])

lesson(39, 'Full-stack integration',
       'Integration is a full rehearsal from shop display to ledger and back. The browser proposes a sale; the server authorizes and validates it; the database commits it; the browser shows the confirmed result.',
       [('End-to-end flow', 'A user operation spanning the system’s components', 'the complete checkout rehearsal'), ('Contract mismatch', 'Disagreement about request or response structure', 'two desks using different form versions'), ('Optimistic update', 'Showing an anticipated change before confirmation', 'writing a provisional receipt'), ('Rollback', 'Restoring a prior valid state after failure', 'cancelling the provisional entry'), ('Source of truth', 'The authoritative record used to resolve disagreement', 'the official ledger')],
       'async function createSale(productId, quantity) {\n  const response = await fetch("/api/sales/", {\n    method: "POST",\n    headers: {"Content-Type": "application/json"},\n    body: JSON.stringify({product_id: productId, quantity})\n  });\n  if (!response.ok) throw new Error(`HTTP ${response.status}`);\n  return response.json();\n}',
       'Add the authentication and CSRF handling required by your chosen session/token design; the snippet only shows the body contract. For the first implementation, show a sale as successful only after confirmation. A server transaction must protect stock regardless of client checks.',
       'Confirmed stock is 10 and a successful sale quantity is 3. What stock should the refreshed UI show?', 7,
       [('Agree on one contract', 'Compare frontend field names, routes, pagination and statuses with the running API. Write a corrected contract and resolve at least one demonstrated mismatch.'),
        ('Connect authentication', 'Implement the chosen login/logout flow and authenticated API transport. Demonstrate signed-out rejection, valid login and logout without recording credentials.'),
        ('Load owned inventory', 'Fetch and display only the signed-in user’s products. Use two users and demonstrate no cross-user records appear.'),
        ('Create and edit', 'Submit product forms to the API. Show successful changes appear after reload and server field errors remain visible without discarding the draft.'),
        ('Record a sale', 'Create the sale endpoint and frontend form with quantity validation and an atomic stock update. From stock 10 sell 3; show total and stock 7 after refresh.'),
        ('Recover from failures', 'Simulate a rejected oversale and interrupted request. Keep a coherent UI, do not display false success, and explain how retry avoids duplicate sales in your design.'),
        ('Rehearse the complete journey', 'Record register/create-user -> login -> add -> sell -> reload -> logout in demo.md. Include API/database evidence and a direct unauthorized access attempt.')])

lesson(40, 'Deployment, architecture and mock interview',
       'Deployment moves the rehearsed shop into its operating premises. A release includes the building, configuration, ledger changes and a way to recover if opening goes wrong.',
       [('Deployment', 'Installing and configuring a runnable release in an environment', 'opening the shop premises'), ('Reverse proxy', 'A server forwarding incoming requests to backend services', 'the public reception desk'), ('Health check', 'A probe reporting a service’s operational condition', 'a quick opening inspection'), ('Rollback plan', 'A documented way to recover from a failed release', 'the plan for reopening the previous setup'), ('Observability', 'Understanding system behaviour from outputs such as logs and metrics', 'the shop’s operational records and gauges')],
       '# Local release rehearsal, using the project environment\npython manage.py check --deploy\npython manage.py showmigrations\npython manage.py test\n# Inspect check output; do not assume zero warnings means all deployment work is complete.',
       'Rehearse on a local production-like environment before choosing a host. Separate configuration and secrets, build frontend assets, use an appropriate production application server, plan migrations and backups, and test deep links and API routes. A health endpoint alone does not prove every dependency is healthy.',
       'Should a backup be restored in a rehearsal to verify recoverability? Enter a Boolean.', True,
       [('Draw the final architecture', 'Diagram browser, static assets, proxy, Django service, database and persistent storage. Label protocols, trust boundaries and which component owns stock.'),
        ('Prepare release configuration', 'Document environment variable names, DEBUG=False, allowed hosts, HTTPS/cookie assumptions and dependency versions. Run check --deploy and explain each unresolved finding.'),
        ('Build a release locally', 'Build frontend assets and run the backend with an appropriate production server in a local rehearsal. Record exact versions/commands and verify static assets plus an API request.'),
        ('Rehearse migration and backup', 'Back up a disposable populated database, apply pending migrations, then restore into another disposable database. Verify product/sale counts and explain compatible rollback limits.'),
        ('Verify release behaviour', 'Check health, login, product CRUD, sale validation, authorization and frontend deep-link refresh. Record expected/actual results and unresolved failures.'),
        ('Write an operations runbook', 'Document startup, shutdown, logs, health checks, failed-release recovery and secret rotation responsibilities. Include a simulated failure and the recovery steps you actually tried.'),
        ('Conduct the mock interview', 'Write and speak answers to: trace a sale end to end; prevent overselling; explain ORM queries; distinguish authentication/authorization; explain React state/effects; identify your hardest bug. Record evidence, tradeoffs and one improvement for each.')])


def write(path, text, only_new=False):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    if not only_new or not path.exists():
        path.write_text(text.rstrip() + '\n', encoding='utf-8')


def build():
    for item in LESSONS:
        n = item['number']
        w = (n - 1) // 3 + 1
        base = f'week-{w:02}'
        teaching = f'{base}/lesson-{n:02}'
        assignment = f'{base}/assignments/lesson-{n:02}'
        language = ('python' if n <= 8 or n in (10, 13, 15) or 16 <= n <= 29 or n == 40
                    else 'javascript' if 31 <= n <= 39 else 'text')
        terms = '\n'.join(f'| {term} | {meaning}. | {analogy}. |' for term, meaning, analogy in item['terms'])
        steps = '\n\n'.join(f'### Step {i}: {title}\n\n{detail}' for i, (title, detail) in enumerate(item['tasks'][:4], 1))
        notes = f'''# Lesson {n}: {item['title']}

**Goal:** Explain the concepts below and implement the seven practical stages in the assignment.
**Prerequisite:** Complete Lesson {n-1}; bring its EMIO24 work forward as a copy so earlier submissions remain reviewable.
**Pace:** Allow 45–75 minutes for reading and experiments, then 2–4 hours for the ten exercises. Integration and deployment may need several sessions.

## Start with an analogy

{item['analogy']}

## Terminology in plain language

| Term | Technical meaning | Analogy |
| --- | --- | --- |
{terms}

These analogies explain one aspect of each concept. Use the technical definition when the analogy stops fitting; software still follows explicit rules rather than human judgement.
For foundational words such as algorithm, process and interface, see the [course glossary](../../glossary.md).

## Worked example: predict, trace, then run

```{language}
{item['code']}
```

{item['explanation']}

**Prediction:** {item['prediction']}
Write your answer before running the example. Then trace which statement or rule causes each part of the result.

## Guided build

{steps}

Work through these stages in order: start from the smallest successful case, inspect the result, then add rejected-input cases. The assignment completes the remaining stages and records evidence.

## Debugging practice

If the result differs from your prediction, record expected and actual values before changing code. Check the input type, the boundary condition and where the authoritative state lives. For this lesson, pay particular attention to this rule: {item['explanation'].split('. ')[0]}.

Change one value or condition in the example, predict the result again, and explain whether the analogy still fits. Do not change several things at once: you need to know which change caused the difference.

## Check your understanding

- Define every term above without copying the table, then give a new everyday analogy.
- Explain the worked example one line at a time, including its setup requirements.
- Demonstrate one successful operation and one failure or boundary case from the guided build.
- Explain where the analogy breaks and what the precise software rule says instead.

Continue with the [ten-exercise assignment](../assignments/lesson-{n:02}/README.md).
See [setup and offline preparation](../../SETUP.md), [week references](../references.md) and the [offline checker guide](../../grading/README.md).
'''
        write(f'{teaching}/teaching.md', notes)
        criteria = [dict(id='exercise_01', points=10, mode='manual', description='Terminology: five accurate definitions/analogies worth 2 each (1 meaning, 1 analogy with mapping).'),
                    dict(id='exercise_02', points=10, mode='auto', description='Exact worked-example prediction in submission.json.', expected=item['expected'])]
        for i, (title, detail) in enumerate(item['tasks'], 3):
            desc = f'{detail} Mark: implementation/artefact meets stated requirements (6); demonstrated stated cases with actual output (3); explanation of the result (1).'
            criteria.append(dict(id=f'exercise_{i:02}', points=10, mode='manual', description=desc))
        criteria.append(dict(id='exercise_10', points=10, mode='manual', description='Independent verification: new normal case (3), boundary/failure case (3), reproducible commands and observed outputs (2), limitation and repair plan (2).'))
        write(f'{assignment}/README.md', render_assignment(item))
        write(f'{assignment}/rubric.json', json.dumps(dict(lesson=n, week=w, status='ready', entrypoint='submission.json', engine='prediction', criteria=criteria), indent=2))
        write(f'{assignment}/submission.json', '{"exercise_02": null}', only_new=True)
        write(f'{assignment}/answers.md', f'# Lesson {n} evidence\n\n' + '\n\n'.join(f'## Exercise {i}\n\n<!-- Write your answer, file links, commands, expected and actual results here. -->' for i in range(1, 10)), only_new=True)
    for w in range(2, 15):
        group = [i for i in LESSONS if (i['number']-1)//3+1 == w]
        links = '\n'.join(f"- [Lesson {i['number']}: {i['title']}](lesson-{i['number']:02}/teaching.md) — [10 exercises](assignments/lesson-{i['number']:02}/README.md)" for i in group)
        write(f'week-{w:02}/README.md', f'# Week {w}: EMIO24 learning pack\n\nEach lesson includes an analogy, terminology definitions, a worked example and ten detailed exercises.\n\n{links}\n\nRead [setup](../SETUP.md), [references](references.md) and the [offline checker guide](../grading/README.md).\n\n[Course index](../README.md)')
        write(f'week-{w:02}/teaching.md', f'# Week {w} teaching\n\nRead these lessons in order.\n\n{links}')
        write(f'week-{w:02}/assignments/README.md', f'# Week {w} assignments\n\n' + '\n'.join(f"- [Lesson {i['number']}: ten exercises](lesson-{i['number']:02}/README.md)" for i in group) + f'\n\nRun `python grade.py check --week {w}` from the course root.')
        write(f'week-{w:02}/checklist.md', f'# Week {w} mastery checklist\n\n' + '\n'.join(f"- [ ] Lesson {i['number']}: explain terminology with analogies, complete all ten exercises, demonstrate practical cases, and review the offline report." for i in group))


if __name__ == '__main__':
    build()

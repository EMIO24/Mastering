"""Individually authored practical instructions, seven per lesson (Exercises 3–9)."""
DETAILS = {}

def pack(number, text):
    parts = text.strip().split('\n@@\n')
    if len(parts) != 7:
        raise ValueError(f'Lesson {number}: expected 7 practical briefs, got {len(parts)}')
    DETAILS[number] = parts

pack(4, r'''
A class is a stock-card design. Calling it makes a particular card.

1. In product.py define `class Product` with `__init__(self, name, price, stock)`. Keep the supplied values on `self.name`, `self.price` and `self.stock`.
2. In checks.py import Product. Create `pen = Product("Pen", 200, 4)` and `book = Product("Book", 500, 7)`.
3. Print each object's three attributes, then print `pen is book`. `is` checks identity, not matching field values.

**Check:** Pen prints Pen/200/4; Book prints Book/500/7; identity prints `False`. `__init__` initializes the object and should not return the object. Python normally inherits `__new__`, which creates it.
@@
Inventory value means the selling value of all units still on one card.

1. Add `inventory_value(self)` inside Product, at the same indentation level as `__init__`.
2. Read this object's price and stock and return their product. Do not add a print inside the method.
3. Call it with parentheses: `print(pen.inventory_value())`.

| Fresh object | Required result |
| --- | --- |
| Pen, price 200, stock 4 | 800 |
| Book, price 500, stock 7 | 3500 |
| Bag, price 4000, stock 0 | 0 |

**Check:** changing a price in a new object changes its result. Forgetting parentheses gives you a method reference, not the computed total.
@@
A stock card should not be issued with unusable starting values.

1. At the start of `__init__`, check the name is a string with non-whitespace content. Use `name.strip()` for this check.
2. Require numeric price and integer stock to be nonnegative. For this course use whole-naira integers for both and exclude bool.
3. Raise `ValueError` before assigning attributes when a rule fails. Normal successful initialization needs no return statement.
4. Wrap each invalid construction in `try/except ValueError` in checks.py so all cases can run.

**Check:** blank name, name containing only spaces, price -1 and stock -1 each reject. `Product("Gift", 0, 0)` succeeds. Record which input failed; do not turn a failed construction into a partially usable product.
@@
Restocking adds a delivery to the existing card.

1. Add `restock(self, quantity)`. Its input is a positive integer count, not a new total stock.
2. Reject non-integers, Booleans and values at or below zero before changing the object.
3. Add an accepted quantity to `self.stock`. No specific return value is required; inspect the stock afterward.
4. Start Pen at stock 4, call `pen.restock(3)`, then try invalid calls on that same object.

| Action | Stock afterward |
| --- | --- |
| Restock 3 | 7 |
| Attempt 0, -1, 2.5 or True | Remains 7; each raises ValueError |

**Check:** you incremented stock rather than overwriting it with the delivery quantity.
@@
Selling both changes stock and hands a numeric total back to the caller.

1. Add `sell(self, quantity)` with the same positive-integer rules as restock.
2. Also reject quantity greater than available stock. Check all rules before subtraction.
3. Subtract quantity and return price multiplied by quantity.
4. For the sequential check, create Pen stock 4, restock 3, then sell 2. For boundary checks, create fresh objects.

**Check:** the sequential sale returns 400 and leaves stock 5. Selling all 4 units of a fresh Pen returns 800 and leaves 0. Selling 5 from fresh stock 4 raises ValueError and leaves 4. Printing a receipt without returning the number does not meet the contract.
@@
An alias is a second name pointing at the same card.

1. Create `pen = Product("Pen", 200, 4)`, then assign `alias = pen`.
2. Change `alias.stock` to 9 and print `pen.stock` and `alias is pen`.
3. Create `other = Product("Pen", 200, 9)` and print `other is pen`.
4. Explain why equal-looking field values do not imply the same object. Keep Book from Exercise 3 separate and inspect its stock too.

**Check:** pen stock is 9, alias identity is True, other identity is False, and Book stays 7. You did not call the constructor when creating the alias; assignment only added a name.
@@
Build a shelf containing object cards rather than dictionaries.

1. Create a fresh list with Pen 200/4, Book 500/7 and Bag 4000/0.
2. Loop over the objects, print each name and its `inventory_value()` result, and add those results to an accumulator starting at zero.
3. Print the final total outside the loop. Repeat using an empty list.
4. In answers.md show the hand calculation and explain why calling the method lets each object provide its own value.

**Check:** rows have values 800, 3500, 0; total 4300. Empty inventory totals 0. Use `product.name`, not `product["name"]`, because these entries are objects.
''')

pack(5, r'''
A class attribute is a notice shared through attribute lookup; instance attributes belong to individual cards.

1. Add `currency = "NGN"` directly inside Product, outside its methods. Keep stock assigned to self inside initialization.
2. Make Pen stock 4 and Book stock 7. Print each currency and stock.
3. Set only `pen.stock = 9`; inspect both objects. Then set `Product.currency = "USD"` and inspect currency again.

**Check:** stocks become 9 and 7; both currencies become USD if neither instance shadows currency. Restore NGN for later tasks. Explain why `pen.currency = "USD"` would instead create an instance-level override.
@@
`__str__` supplies friendly display text when print needs to show an object.

1. Add `__str__(self)` and return a string containing name, a colon, stock and the word units.
2. Use an f-string to insert actual attributes. Do not print from inside the method.
3. Run `print(str(Product("Pen", 200, 4)))` and `print(Product("Bag", 4000, 0))`.

**Check:** exact results are `Pen: 4 units` and `Bag: 0 units`. A different name must appear without modifying the method. Returning a number from __str__ is invalid; the method's result must be text.
@@
`__repr__` is debugging text intended to help a programmer inspect the card.

1. Add `__repr__(self)` including the class name and all three constructor values.
2. Choose a readable form such as `Product(name='Pen', price=200, stock=4)`. Using `!r` in an f-string keeps quotes visible around a name.
3. Print `repr(pen)`, `str(pen)`, and a one-item list containing pen.
4. Explain which representation the list uses and why the debug version includes more fields.

**Check:** repr includes Product, Pen, 200 and 4; str still matches Exercise 4. A name containing an apostrophe remains understandable. The checker does not require one exact repr spelling.
@@
A property is a service window that can inspect an assignment before accepting it.

1. Back the public stock attribute with `_stock`.
2. Add a `@property` getter returning `_stock` and a `@stock.setter` method that validates the incoming value before storing it.
3. Route initialization through `self.stock = stock` so construction and later assignment use the same rule.
4. Start at 4; assign 0 successfully, then separately attempt -1, "3", 2.5 and True.

**Check:** zero is accepted. Every invalid assignment raises ValueError and retains the previous stock. Inside the setter assign `_stock`, not `stock`, or the setter would repeatedly call itself.
@@
An alternative constructor translates another input format into the normal creation call.

1. Add `@classmethod` above `from_dict(cls, record)`.
2. Require keys name, price and stock. Report missing fields with a clear ValueError rather than silently inventing values.
3. Return `cls(...)` using those three values. Reuse constructor validation instead of copying it.
4. Call `Product.from_dict({"name":"Pen","price":200,"stock":4})` and inspect the returned object's fields.

**Check:** valid data creates a Product; missing stock and negative stock reject. Explain why using cls rather than the literal Product name supports subclasses inheriting this factory.
@@
A mutable class-level list can behave like one shared notice that every product edits.

1. In shared_tags.py create a small demonstration class with `tags = []` in its class body.
2. Make two instances, append "sale" through the first and inspect both lists. Record the unexpected sharing.
3. In a separate corrected class create `self.tags = []` inside __init__.
4. Repeat the same two-instance experiment, then add a different tag to the second object.

**Check:** the broken pair both show sale. The corrected first has only sale and the corrected second has only its own tag. Keep both demonstrations; do not alter Product's working fields just to reproduce this bug.
@@
Equality and identity answer different questions: matching card contents versus the same card.

1. In identity_demo.py make two separate Products with identical name/price/stock.
2. Print `a is b` and `a == b`. Inspect whether Product defines __eq__ or inherits default behaviour.
3. If no custom equality exists, document the observed default result. You may optionally define field equality, but explain the choice rather than claiming all classes compare by fields automatically.
4. Set `alias = a` and repeat both comparisons with alias.

**Check:** separate objects have identity False; alias identity is True. Your equality explanation must match the implementation actually used, including whether modifying a field changes the equality result.
''')

pack(6, r'''
A contract tells callers what service they may request without knowing its internal details.

1. In design.md specify `pay(amount)` for this exercise: amount is a positive whole-naira integer, excluding bool; success returns receipt text and failure raises ValueError for invalid amounts.
2. Give a valid call with 600 and an invalid call with -1, including expected return/error behaviour.
3. State that a simulated payment refusal raises RuntimeError and must not pretend payment succeeded.
4. Define how checkout recognizes success: pay returns normally before stock changes.

**Check:** the contract covers input, output and both failure categories. Map pay to a counter operation and receipt text to its returned evidence; no real transaction takes place.
@@
Different workers can perform the same named service.

1. In payments.py implement CashPayment and TransferPayment with `pay(self, amount)` following your contract.
2. Return distinguishable receipts, for example `cash:600` and `transfer:600`, using the actual amount.
3. Put both objects in a list and call pay(600) in one loop without checking their class names.
4. Try 0 and -1 on each; add text and Boolean values to verify the whole-number rule.

**Check:** both implementations succeed for 600 and reject invalid amounts before producing a receipt. Explain polymorphism as one request understood by different workers, rather than an if/else chain naming every worker type.
@@
Composition means the checkout has a payment worker; it is not itself a payment subtype.

1. Define `Checkout(payment)` in checkout.py and retain the supplied object on the instance.
2. Add `charge(amount)` that delegates to `self.payment.pay(amount)` and returns its result.
3. Create one checkout with CashPayment and another with TransferPayment; charge 600 through both.
4. Check that checkout never asks which concrete payment class it has.

**Check:** results distinguish cash and transfer while the Checkout code is identical. Replacing the worker only changes construction. Passing a worker missing pay should expose the interface problem rather than silently reporting success.
@@
A refused payment must leave the stock ledger untouched.

1. Extend Checkout with a sale operation accepting a product and quantity.
2. Validate positive whole-number quantity and available stock before calling payment. Calculate the total from product price.
3. Call pay(total). Deduct stock only after it returns successfully; let simulated RuntimeError propagate to the caller.
4. Use Pen price 200, stock 4 with quantity 2. Repeat from fresh stock with a worker whose pay raises RuntimeError.

**Check:** success charges 400 and leaves stock 2; refusal leaves 4. Quantity 5 leaves 4 and makes no payment call. This is local sequencing, not a real bank/database distributed transaction.
@@
Inheritance should preserve the operation that callers rely on.

1. Define DiscountedProduct as a Product subtype with an additional discount percentage bounded from 0 to 100.
2. Override its value calculation to account for the discount, while returning a numeric amount as the base method does. Choose a rounding policy and document it; use exact whole-naira examples first.
3. Put base Pen 200/4 and a 50%-discounted Pen 200/4 in one list and call inventory_value on both.

**Check:** values are 800 and 400; 0% gives 800, 100% gives 0, invalid discounts reject. Explain why a subtype returning receipt text would violate the shared numeric contract.
@@
Composition offers another way to choose pricing without a new product subtype per policy.

1. In pricing.py define regular and percentage-discount policy objects with one common price/value operation.
2. Have a product or pricing service receive its policy as an input rather than inherit from it.
3. Calculate value for Pen 200/4 with a regular policy, then replace the policy with 50% off and calculate again.
4. Compare this design with Exercise 7 in answers.md: where is discount validation, and what changes when a new policy is added?

**Check:** values are 800 then 400, without creating a discount subtype for the second calculation. Document policy replacement explicitly; do not change stored stock to simulate a discount.
@@
A fake payment worker makes checkout checks repeatable without a network.

1. In checks.py implement FakePayment with an `amounts` list and a configurable failure flag.
2. Have pay append the requested amount, then return a receipt or raise RuntimeError according to the flag.
3. Inject it into Checkout. Sell two Pens from stock 4 at price 200, then repeat with a fresh failing fake and product.
4. Make an oversale attempt with another fresh fake to test validation order.

**Check:** successful and refused payment attempts each record [400]; stock becomes 2 only after success. An oversale records [] because no payment was attempted. Explain why recording a call alone does not prove successful payment.
''')

pack(7, r'''
Separate reusable calculations from the program that talks to a person.

1. Create inventory/calculations.py and define `line_total(price, quantity)` and `inventory_value(products)` there. Products are dictionaries with price and stock.
2. Create main.py beside inventory/ and import the functions using `from inventory.calculations import line_total, inventory_value`.
3. Print line_total(200,3), an inventory with Pen 200/10 and Book 500/3, and an empty inventory's value.

**Check:** `python main.py` prints 600, 3500 and 0. There should be one implementation of each calculation; importing it should not require copy-pasting its body into main.py.
@@
An import should make a tool available without unexpectedly opening the shop.

1. Create inventory/cli.py with a main function containing a small repeatable menu and input prompts. Import calculations into this module.
2. Make root main.py call cli.main only inside its `if __name__ == "__main__":` block.
3. Run `python -c "import inventory.calculations; import inventory.cli"` from the assignment folder.
4. Then run `python main.py` and choose Quit.

**Check:** the import command finishes without prompts; direct execution displays the menu and quits normally. Moving a prompt to the top level would run it during import, even if other code has a main guard.
@@
A package entry point lets Python start a folder as an application.

1. Add inventory/__main__.py; import the CLI main function there and call it under a main guard.
2. Keep __init__.py present. Its job is not to start the interactive menu.
3. From the parent of inventory/, run `python -m inventory`, choose a calculation/list option, then quit.
4. Compare its behaviour with `python main.py` from Exercise 4.

**Check:** both start the same menu; importing inventory alone does not start it. The `-m` option asks Python to find and run a module/package through its module search path, not a file named -m.
@@
Module qualification distinguishes identical tool names in different drawers.

1. Create inventory/products.py and inventory/suppliers.py, each defining describe(). Make them return different text identifying the module's subject.
2. In namespace_demo.py import the modules, then call `products.describe()` and `suppliers.describe()` using your chosen import bindings.
3. Run the file and record both outputs.
4. Explain what would happen if you imported both functions into the same local name using two `from ... import describe` statements.

**Check:** both descriptions are callable and distinct. A later same-name import replaces the earlier local binding; the original module's function is not deleted.
@@
A circular import is like two drawers each refusing to open until the other is open.

1. In imports.md draw a bad dependency: cli imports storage and storage imports cli for validation.
2. Identify validation as shared logic rather than user interaction. Create inventory/validation.py with a small record checker.
3. Make both CLI and storage import that checker; remove storage's dependency on cli.
4. Run `python -c "import inventory.cli; import inventory.storage"` and exercise one valid/invalid record.

**Check:** imports complete, validation remains available to both callers, and the new graph has no return arrow from storage to cli. You need not leave a crashing circular version in the working package.
@@
A relative filesystem path starts from the process's working directory, which may change.

1. Put a sample notes.txt inside inventory/data/ containing `Pen stock: 4`.
2. In inventory/storage.py derive its path from `Path(__file__).resolve().parent`, then read it as UTF-8.
3. Expose that read through a small callable or script entry point; print the resolved path and text.
4. Run once from the assignment folder, then from another working directory using the full path to your script.

**Check:** both runs identify the same notes.txt and read `Pen stock: 4`. Explain why simply opening `data/notes.txt` without an anchored path can target the wrong folder.
@@
Write instructions another learner can follow without knowing your folder layout.

1. In project-notes.md draw the actual file tree, including __init__.py, __main__.py, calculations, CLI, validation and storage.
2. Give one responsibility per file and show the import direction between them.
3. State the required working directory and exact commands for running the app and checking an import.
4. Add a short example reusing line_total from another script without opening the menu.

**Check:** a reader can reproduce a 600 total and quit the menu using only these instructions. Mark directories as directories; do not list generated __pycache__ files as source that someone must write.
''')

pack(8, r'''
A virtual environment is a project-specific Python toolbox, not a replacement for the operating system.

1. Inside practice-project/ run `python -m venv .venv`.
2. Record the base interpreter's `python --version` output in environment.md.
3. Check that .venv/ contains Scripts/python.exe on Windows, or bin/python on macOS/Linux.
4. Add `.venv/` and `.venv-rebuild/` to the practice project's .gitignore if it has source control.

**Check:** the environment interpreter exists and reports a Python version. Do not submit thousands of environment files as authored code. If venv creation fails, record the actual error and resolve it before claiming the toolbox exists.
@@
Typing python can select a different worker than you intended. Inspect the worker directly.

1. In practice-project/ run `.venv/Scripts/python.exe -c "import sys; print(sys.executable)"` on Windows; substitute .venv/bin/python on other systems.
2. Copy the printed path into environment.md and identify the .venv segment.
3. Run that interpreter with `-c "import sys; print(sys.prefix != sys.base_prefix)"`.
4. Compare with the unqualified python command from the same terminal.

**Check:** the explicit environment command points inside practice-project/.venv and the prefix comparison is True. No activation script is required when you invoke the interpreter by its full path.
@@
Installed distributions are toolbox contents; standard-library modules are supplied with Python itself.

1. Run the environment interpreter with `-m pip list`, then `-m pip --version`.
2. Record distribution names/versions and the pip installation path. Do not assume an exact initial package count across Python versions.
3. Run `-c "import json, pathlib; print('standard library imports work')"` using the same interpreter.
4. Explain why importing json does not imply a json distribution must appear in pip list.

**Check:** commands use the same environment, pip reports an environment path, and both standard-library imports succeed. A package name on a website is not evidence it is installed locally.
@@
A requirements file lists tools needed to recreate the project.

1. Choose one actual third-party dependency already installed for your practice program and identify its exact version with pip show. If there are none, keep requirements.txt empty and explicitly document a standard-library-only project.
2. Write a requirement in `distribution-name==installed.version` form for that dependency. Do not paste the illustrative name/version literally.
3. Record why it is needed and the command that imports its module successfully.
4. Compare `pip freeze` output with the explicit file and explain any development-only packages you excluded.

**Check:** every listed version matches an installed distribution. An empty requirements file is valid only with the documented dependency-free route.
@@
Offline installation needs actual package artifacts, not just the shopping list of names.

1. While online and using the intended project interpreter, run `-m pip download -r requirements.txt -d wheelhouse`.
2. List the downloaded filenames in environment.md. Record the Python version and operating system used to prepare them.
3. Explain that transitive dependencies are tools required by your selected tool; the download must include them too.
4. For a standard-library-only project, record that no third-party artifacts are required instead of inventing downloads.

**Check:** the artifacts exist on disk. A source archive may need build tools, so offline readiness is not proven until the clean rebuild in Exercise 8 succeeds.
@@
Rebuilding is the practical proof that a second toolbox can run the project.

1. Create `.venv-rebuild` with `python -m venv .venv-rebuild`.
2. Use its interpreter for `-m pip install --no-index --find-links wheelhouse -r requirements.txt`. `--no-index` prevents fetching missing packages from an online index.
3. Run the same import/small program used in Exercise 6 and record its output plus interpreter path.
4. If requirements is empty, run the standard-library import check instead.

**Check:** the fresh environment succeeds using local resources and points to .venv-rebuild. Missing artifacts are an actionable failure, not a passing offline test; record the missing package and prepare it before retrying.
@@
A package installed for one interpreter is not automatically installed for every interpreter.

1. For your base Python and .venv Python, collect sys.executable and `-m pip --version`.
2. Compare their paths, then query one dependency with `-m pip show` under both.
3. If availability differs, demonstrate the differing import result. If both have it, explain the hypothetical mismatch using the actual paths; do not fabricate an error.
4. Write the corrected installation and execution commands that explicitly select the intended environment.

**Check:** your diagnosis names the mismatched interpreter, not merely “Python is broken.” Using python -m pip binds package management to the selected interpreter.
''')

pack(9, r'''
A repository records snapshots inside a chosen project boundary.

1. In a fresh git-practice/ folder run `git init`. Create notes.txt containing a short description of EMIO24.
2. Run `git status`, then `git add notes.txt`, then status again.
3. If a commit later asks for identity, configure local user.name/user.email in this repository, using your intended author identity.
4. Record the repository path and both status outputs in history.md outside git-practice/.

**Check:** notes.txt starts untracked and becomes staged. Do not initialize or alter a parent repository to complete this exercise. No network or remote is required.
@@
The staging area selects the next snapshot, not every edit currently on your desk.

1. Stage notes.txt containing a line `Inventory draft A`.
2. Change that line to `Inventory draft B` without staging again.
3. Run `git diff` and `git diff --cached`; explain which comparison shows B and which shows the staged A.
4. Commit the staged version with `git commit -m "Record inventory draft A"`, then inspect `git show HEAD:notes.txt` and status.

**Check:** the commit contains A while the working file contains B. Stage and commit B afterward so subsequent branch work starts clean. Record both commit messages and hashes rather than assuming staging happens automatically.
@@
An ignore rule prevents new generated/private files from being offered for tracking.

1. Create .gitignore containing `.venv/`, `__pycache__/`, `.env` and your practice generated-data folder.
2. Make a dummy .env with only `DEMO_SETTING=fake`; do not use a real secret.
3. Run `git status --short` and `git check-ignore -v .env`.
4. Stage/commit .gitignore, then explain what would happen if .env had already been tracked before the rule existed.

**Check:** .env is excluded and check-ignore identifies the rule. Ignore rules do not erase tracked history; this exercise should start with an untracked dummy file.
@@
A branch is a movable history bookmark, not a new folder on disk.

1. Record the current branch using `git branch --show-current`; call it your original branch in notes.
2. Run `git switch -c feature/low-stock`.
3. Add a small Python low-stock function or improve an existing practice one. Run its boundary checks, then stage and commit the change.
4. Capture `git log --oneline --all --graph` and `git status`.

**Check:** feature/low-stock points at the new commit and the working tree is clean. The original branch has not moved just because you committed while another branch was selected.
@@
A merge brings the feature's history into the branch currently checked out.

1. Switch back to the exact original branch name you recorded.
2. Run `git merge feature/low-stock` and read the output before continuing.
3. Execute the low-stock function checks again and inspect the combined graph.
4. Explain whether this merge fast-forwarded: that means the branch pointer could move ahead without a separate merge commit.

**Check:** the original branch now contains the tested feature. Do not claim a merge commit was created if the actual operation fast-forwarded. Save the command output as evidence.
@@
A conflict means Git needs a person to decide how competing edits fit together.

1. From a clean common commit create two practice branches, conflict-a and conflict-b, each changing the same notes.txt line differently and committing it.
2. On conflict-a run `git merge conflict-b`. Record the conflict output and the marked section of the file.
3. Edit that section into one coherent final line, removing `<<<<<<<`, `=======` and `>>>>>>>` markers.
4. Stage the resolved file, finish the merge with a commit, and inspect status/log.

**Check:** Git reports no unresolved paths, the file contains your intended line, and the history includes both branches. If your chosen changes merge automatically, retry on the same original line rather than fabricating a conflict.
@@
Revert records an undo as another snapshot, preserving the historical explanation.

1. On your disposable practice branch make an intentionally wrong change and commit it. Record that commit's hash.
2. Run `git revert --no-edit HASH`, replacing HASH with the recorded identifier.
3. Show the file's corrected contents and `git log --oneline -3`.
4. Explain how this differs from deleting commits or rewriting shared history.

**Check:** both the erroneous commit and its reversal remain visible; the working content matches the pre-error version. Use this exercise's disposable mistake, not an unrelated commit in another repository.
''')

pack(10, r'''
A page request travels through several services before the browser displays anything.

1. In request-flow.md draw browser → name resolution → connection → server → response → rendering.
2. Under each arrow explain what moves or happens: finding an address, connecting to a listening port, sending HTTP, receiving bytes and interpreting HTML.
3. Use a fictional shop domain for the DNS explanation, then compare it with localhost, which is resolved locally.
4. Explain why receiving HTML and drawing pixels are separate operations.

**Check:** your diagram names both request and response directions. DNS finds address information; it does not return the shop's inventory page. Do not claim the diagram captures every cache/proxy detail.
@@
A URL gives both a location and instructions about which resource is requested.

1. Copy `http://localhost:8000/products?low=1` into answers.md.
2. Make a table separating scheme, hostname, port, path and query string.
3. Compare the URL with `http://localhost:8000/products?low=0`: identify what changed and what stayed the same.
4. Explain what localhost means if your friend opens this URL on a different computer.

**Check:** scheme http, host localhost, port 8000, path /products, query low=1. Your friend's browser contacts their own computer. The query is not part of the hostname or port.
@@
Serve a real local page so the next exercises have observable network traffic.

1. Create public/index.html with an HTML title, an EMIO24 heading and a list containing Pen and Notebook with stock counts 4 and 8.
2. In a terminal change into public/ and run `python -m http.server 8000 --bind 127.0.0.1`.
3. Open `http://127.0.0.1:8000/` and confirm both products appear.
4. Record the command, URL and displayed content; keep the server running for later checks.

**Check:** the browser renders your file and the terminal logs a request. If the port is occupied, use another recorded port consistently; do not infer the right page from a browser cache alone.
@@
The browser's Network panel is the delivery receipt for each resource request.

1. Open Developer Tools and select Network. Reload your local index page.
2. Select the document request, not a favicon or extension request.
3. Record Request URL, method, status and response Content-Type in network-notes.md. Inspect Response to find your heading text.
4. Explain each field using the shop-order analogy.

**Check:** the document request uses GET, succeeds with 200 on an ordinary fresh response, and contains HTML. If you observe a cache-related status, disable cache while DevTools is open and reload, recording what actually changed.
@@
An HTTP error response differs from failing to reach any server.

1. With the local server running, visit `/missing.html`, a filename you have not created.
2. Record its status and response body from Network.
3. Stop the server with Ctrl+C and try a new uncached request to the same host/port.
4. Compare the browser error with the earlier 404 response, then restart the server for Exercise 8.

**Check:** the missing page gets a server response with status 404. The stopped-server case is a connection/network failure, not a 404 response from your server. Note any cached page instead of treating it as a live response.
@@
Some UI actions happen entirely in the browser after the page has loaded.

1. Add a button labelled `Show stock` and a paragraph to index.html.
2. Attach a click handler that changes the paragraph to `Pen: 4 units` using textContent.
3. Reload, clear the Network log, then click the button.
4. Record both the changed screen text and whether your click generated a request. Distinguish unrelated browser traffic from your handler.

**Check:** the text changes without fetching new stock in this implementation. Explain that the displayed 4 was already available to browser JavaScript; it is not automatically current database stock.
@@
Map the future app to the system you just observed.

1. In architecture.md draw React/browser, Django/API and database as separate boxes.
2. Trace a product-list request out and a data response back; label HTTP between browser/API and database queries between API/database.
3. Trace a proposed sale and identify where stock is validated and committed.
4. Describe a second customer buying an item while the first customer's page remains open.

**Check:** the database/server-side business process is authoritative; the browser can hold an outdated copy. Your arrows show how the UI would refresh rather than assuming two open pages share one in-memory variable.
''')

pack(11, r'''
An HTTP request starts with the action and target, followed by metadata.

1. In requests.http write `GET /products/4 HTTP/1.1`, then a Host header naming your local service, then a blank line.
2. Annotate a separate copy in answers.md: GET is the method, /products/4 is the path, HTTP/1.1 is the protocol version.
3. Explain why the Host value does not belong inside the path.
4. Keep this as a raw message illustration; it is not a Python program or a command to paste directly into PowerShell.

**Check:** the request has a start line, Host header and header/body separator. A read-only request describes fetching product 4 and must not imply changing its stock.
@@
A create request carries fields that the server needs to make a new record.

1. Add a conceptual POST /products request with Host and Content-Type: application/json headers, a blank line, and JSON containing name Pen, price 200 and stock 10.
2. Write a matching response starting `HTTP/1.1 201 Created`, with JSON content type and Location: /products/4.
3. Include response JSON with assigned id 4 and the accepted fields.
4. Explain that a real HTTP client supplies correct body framing such as Content-Length; this file focuses on the application contract.

**Check:** request and response bodies are valid JSON; ID assignment is attributed to the server. The 201 status communicates creation rather than merely any successful read.
@@
Choose a response that explains which kind of failure happened.

1. In responses.http write five short response sketches for: malformed JSON, missing credentials, recognized user lacking permission, nonexistent product and an unexpected server exception.
2. Assign statuses 400, 401, 403, 404 and 500 respectively for this proposed API contract.
3. Give each a small JSON body with a safe code/message; include an appropriate authentication challenge for the 401 design.
4. Explain what the client should fix or retry in each scenario.

**Check:** 401 and 403 are not described as interchangeable. The 500 body contains no traceback or secret. Actual frameworks may choose a particular challenge/denial status based on authentication configuration; document your contract explicitly.
@@
Replacing a complete card and changing one box on it have different input requirements.

1. Define the current product as id 4, name Pen, price 200, stock 10.
2. Write a PUT body containing all required writable fields and setting stock to 5. State whether omitted required fields are rejected.
3. Write a PATCH body containing only stock 5; explain that name and price remain unchanged under this contract.
4. List successful status/body behaviour for each and an invalid negative-stock response.

**Check:** both valid examples leave stock 5; PATCH preserves omitted fields. Your PUT requirements are explicit, not inferred from the fact that both methods can update records.
@@
Idempotency concerns intended state after repetition, not identical response text.

1. In repetition.md start a fictional product at stock 10.
2. Trace PUT stock=5 once and then repeat exactly the same request. Record stock after each step.
3. Reset to 10; trace two separate POST sale quantity=2 operations.
4. Explain why retrying an uncertain sale POST can create another sale unless the API has a specific duplicate-request mechanism.

**Check:** PUT trace is 10 → 5 → 5; sale trace is 10 → 8 → 6. Do not generalize a harmless repeated GET into proof that every HTTP request is safe to retry.
@@
Inspect one actual HTTP exchange, not only handwritten examples.

1. Serve a small index.html with the local Python server and open it in a browser.
2. In Network, select the main document request. Record URL/method, status, request headers and response headers.
3. Find the response body and identify a sentence from your file. Explain which visible fields are metadata and which are content.
4. Keep any handwritten raw HTTP example labelled as a representation of the exchange rather than an exact packet capture.

**Check:** your notes identify Content-Type and the HTML body separately. The browser may use a protocol display different from your HTTP/1.1 teaching sketch; report the version actually observed.
@@
An error document should help a caller correct the order without exposing server internals.

1. In errors.json design a body with `code`, `message` and a `fields` object.
2. Use an attempted product stock of -1 and put field-specific feedback under stock.
3. In answers.md associate this body with status 400 and explain how a form could show the stock message beside its input.
4. Compare with a generic server-error body that gives no stack trace.

**Check:** errors.json parses as JSON, identifies the invalid field and gives a usable correction. Do not include comments, exception dumps, passwords or guessed internal file paths in the example response.
''')

pack(12, r'''
Resource names should identify business records, not arbitrary screen buttons.

1. In api-contract.md list products, customers and sales, with `/api/products/`, `/api/customers/` and `/api/sales/` collection paths.
2. Add a detail pattern using an ID, such as `/api/products/7/`, for each.
3. State what each resource represents and which ID identifies it.
4. Explain why a completed sale needs its own record instead of only decreasing a product field.

**Check:** a sale can retain quantity, historical price and purchaser information even after current product details change. Use stable numeric IDs in this exercise; do not use list positions as persistent identity.
@@
Write a contract another developer can implement without guessing the operation.

1. Make a table for list, retrieve, create, full update, partial update and delete products.
2. For every row state method/path, writable fields, successful status/body and at least one failure.
3. Use 200 for reads/updates, 201 for creation and 204 with no body for deletion in this design.
4. Include one concrete request/response pair for creating Pen at 200/4.

**Check:** a reader knows whether collection results are paginated and whether a deleted response has a body. Missing records return 404 and invalid submitted fields return 400 under the stated contract.
@@
Parsing JSON only establishes its structure; validation establishes whether the shop accepts its values.

1. Define name as nonblank text, and price/stock as nonnegative whole-number values. Exclude Boolean values from the intended numeric contract.
2. Write a valid body with name Pen, price 200 and stock 4.
3. Write separate invalid examples: blank name, negative price, fractional stock and Boolean stock.
4. Give field-specific errors and state that rejected creation leaves the product count unchanged.

**Check:** all five examples are valid JSON, but only the first satisfies business rules. Label malformed JSON separately if you add it; it fails parsing before field validation.
@@
Pagination divides a long catalogue into predictable pieces.

1. Use IDs 1–5 from the starting fixture, ordered ascending, with page size 2.
2. Write all three complete response objects using count, next, previous and results.
3. Put two product objects on pages 1 and 2 and one on page 3. Use null where no neighbouring page exists.
4. Explain that count is the whole matching collection size, not just the current page length.

**Check:** page IDs are [1,2], [3,4], [5]; count remains 5. Following next from the first page reaches every ID once, and the last next is null.
@@
A filter chooses records; ordering arranges the chosen records.

1. Define `stock_lte` as an integer cutoff and `search` as case-insensitive name substring matching. Choose allowed ordering fields, such as id/name/stock.
2. With starting stocks 4/8/0/2/6, show `stock_lte=2` returning Bag and Pencil when ordered by ID.
3. Show `search=pen` matching Pen and Pencil under substring rules.
4. Specify invalid/unknown parameter behaviour and show one rejected or deliberately ignored example.

**Check:** your examples use the same documented matching rule; results keep the pagination envelope. Do not promise arbitrary database field ordering without defining what the API allows.
@@
A sale request proposes a ledger change; the server decides whether it can commit it.

1. Specify POST /api/sales/ with product_id and positive integer quantity. The server obtains price from the product record, not a client-supplied total.
2. Start Pen at stock 4, price 200. Show a sale of 2 returning a sale ID, total 400 and updated stock 2.
3. From a fresh stock 4, show quantity 5 rejected with your chosen documented business-error status and no sale/stock change.
4. Explain how the client gets confirmed stock and what it should do when a request's outcome is uncertain.

**Check:** the response/error contract is explicit and does not let the browser authorize its own sale.
@@
A contract change can break code that already depends on it.

1. Add an optional description field to the product response and describe a client that ignores unknown fields.
2. Compare with renaming id to product_number and deleting id from the response.
3. Write a small before/after example showing why an existing client's `product.id` access breaks in the second case.
4. Propose a transition: retain the old field temporarily or introduce a documented version, with a migration plan for callers.

**Check:** you identify the affected consumer and a way to keep it working during change. Do not call every added field harmless if an existing consumer rejects unknown fields; state your compatibility assumption.
''')

pack(13, r'''
Create a ledger with predictable starting records.

1. In practice.py import sqlite3 and connect to inventory.sqlite3 beside the script. Create products with id INTEGER PRIMARY KEY, name TEXT, price INTEGER and stock INTEGER.
2. Insert IDs 1/2/3: Pen 200/4, Book 500/8 and Bag 4000/0. Use ? placeholders and parameter tuples, not SQL string concatenation.
3. Commit and select all rows ordered by ID.

**Check:** exactly three rows match those values. Use a disposable database and make repeated setup deliberate; duplicate-key errors are not proof that seeding succeeded.
@@
Selecting particular columns gives the reader only the needed parts of each card.

1. Write SELECT for name and stock from products, with ORDER BY id.
2. Execute it and call fetchall(); print the returned tuples.
3. Record the SQL and output, then explain which tuple position represents each selected column.

**Check:** rows are `('Pen',4)`, `('Book',8)`, `('Bag',0)`. Do not use SELECT * for this task. Without ORDER BY, apparent insertion order is not a promised result order.
@@
Filter the ledger using a supplied cutoff.

1. Select name and stock where stock <= a bound parameter.
2. Order by stock ascending, then ID to break ties.
3. Execute with thresholds 4, 0 and -1 without rewriting the SQL string. Record each result.

**Check:** 4 gives Bag/0 then Pen/4; 0 gives Bag/0; -1 gives no rows. The equality case matters: Pen belongs at cutoff 4. Use a one-item tuple such as `(4,)` when binding a single sqlite3 parameter.
@@
Change one card without touching its neighbours.

1. Query all IDs/stocks before the update.
2. Update stock to 7 only where id equals the bound value 1. Commit.
3. Query all IDs/stocks again and explain the before/after difference.
4. Describe, without executing on useful data, what an UPDATE lacking WHERE would do.

**Check:** Pen is 7, Book remains 8 and Bag remains 0. This sets stock to 7; it does not add 7. The WHERE condition identifies the row, not its displayed position.
@@
Delete a verified practice record.

1. Fetch Bag and confirm ID 3 and stock 0 in your disposable database.
2. Delete using a parameterized condition on ID 3 and commit.
3. Query remaining IDs, count and a lookup for ID 3.

**Check:** count is 2, remaining IDs are 1 and 2, and Bag lookup returns no row. Repeat only with a restored fixture if you want to observe a successful deletion again. An already absent row should not cause another product to be deleted.
@@
Combine all remaining rows into one inventory total.

1. Use the post-update/delete data: Pen 200/7 and Book 500/8.
2. Query SUM(price * stock), using COALESCE to choose zero when the aggregate is NULL.
3. Fetch the one value and compare with a handwritten calculation.
4. Run the same aggregate with a condition matching no rows; do not erase the fixture to check emptiness.

**Check:** total is `1400 + 4000 = 5400`; empty selection yields 0. Explain why SUM over no rows requires the explicit default.
@@
Prove both persistence and safe handling of punctuation.

1. Close and reopen inventory.sqlite3 and read the existing rows.
2. Insert an unused ID with name `Maker's Pen`, price 250 and stock 2 using bound parameters.
3. Commit, close, reopen and fetch that ID.
4. Explain why the apostrophe remains part of the data rather than changing the SQL instruction.

**Check:** Pen/Book persist and the new name reads back exactly. A :memory: connection cannot demonstrate persistence across a new connection; use the file database here.
''')

pack(14, r'''
A foreign key is a checked reference to another ledger's card number.

1. In schema.sql define products(id,name,price), sales(id), sale_lines(id,sale_id,product_id,quantity,unit_price), each with a primary key.
2. Make the two line references foreign keys, require positive quantities and nonnegative prices.
3. In practice.py connect to a disposable database, enable `PRAGMA foreign_keys = ON`, and execute the schema.

**Check:** all three tables exist and querying the pragma returns 1 on the connection used for inserts. Declaring a reference without enabling SQLite enforcement will not satisfy the later orphan-rejection check.
@@
Seed a history small enough to verify by hand.

1. Insert Pen ID 1 price 200 and Book ID 2 price 500; create sales IDs 1 and 2.
2. Insert line IDs 1/2/3 as: sale1/Pen/quantity2/unit_price200; sale2/Pen/3/200; sale2/Book/1/500.
3. Commit and print all lines ordered by line ID. Keep the SQL in seed.sql.

**Check:** two products, two sales and three lines. Sale 1 totals 400; sale 2 totals 1100. Product ID identifies a product, while line ID identifies one particular receipt entry.
@@
A join translates receipt references into readable product names.

1. Select sale ID, product name and quantity from sale_lines joined to products.
2. Match sale_lines.product_id to products.id in the ON clause.
3. Order by sale ID then line ID and execute from practice.py.
4. Explain the join condition using the card-number analogy.

**Check:** rows are `(1,'Pen',2)`, `(2,'Pen',3)`, `(2,'Book',1)`. Missing or incorrect join conditions can combine unrelated rows. Qualify column names with table names or aliases where they would otherwise be ambiguous.
@@
Summarize units sold per product, across all sales.

1. Group the joined records by product ID and name.
2. Sum line quantity and order the summaries by product ID.
3. Compare with the seed rows rather than deriving the expectation from a second copy of your query.
4. Explain what would go wrong if two distinct products shared a name and you grouped only by name.

**Check:** Pen totals 5 units and Book 1. Sum quantities, not current prices; revenue is a different question.
@@
Keep products even when they have no sales.

1. Add Bag ID 3 price 4000 without a sale line.
2. Run your inner-join summary, then write a products LEFT JOIN sale_lines version.
3. Use COALESCE around SUM(quantity) and compare the two outputs.

**Check:** the inner join omits Bag; the left join shows Pen 5, Book 1, Bag 0. If counting lines, count a non-null child ID rather than COUNT(*), which also counts the retained parent row with no matching child.
@@
An orphan line refers to a card that does not exist.

1. Confirm product 999 is absent and line count is 3.
2. In a transaction attempt a new line for an existing sale but product_id 999.
3. Catch sqlite3.IntegrityError outside the transaction block, then query the attempted line and total count.

**Check:** the foreign-key failure leaves no new line and count remains 3. If insertion succeeds, inspect enforcement on the actual connection. Do not repair the test by creating product 999, because that removes the invalid condition you are trying to demonstrate.
@@
Historical receipts must retain the price actually charged.

1. Calculate sale totals from line quantity times line unit_price.
2. Update today's Pen price from 200 to 300 and commit.
3. Recalculate historical totals from the same line fields.
4. Compare with the incorrect alternative of applying today's price to old quantities.

**Check:** sale 1 stays 400 and sale 2 stays 1100; today's Pen price is 300. Explain why unit_price on the sale line is an intentional snapshot, even though the product table also has a price field.
''')

pack(15, r'''
A schema diagram is a buildable ledger blueprint.

1. Draw suppliers, products, sales and sale_lines with the starting setup's fields.
2. Mark primary/foreign keys and one-to-many relationships. State which fields may be NULL and the units of every numeric field.
3. Trace one sale containing Pen and Book through the diagram.
4. Explain why adding a third product to a sale should add a line, not another product column to sales.

**Check:** every relationship uses a named key and the sample sale fits the schema without changing its structure.
@@
Repeated supplier details can disagree after a partial update.

1. Sketch three products each storing the same supplier phone; change only one copy and explain the inconsistency.
2. Implement a suppliers row referenced by three products instead.
3. Update the phone on that supplier row, then join products to supplier details.
4. Record the SQL and all three results.

**Check:** every product displays the new phone from one authoritative value. Product stock remains on products because different products can have different counts even when they share a supplier.
@@
Enforce critical rules even if someone bypasses a form.

1. Add nonnegative stock/price checks, unique SKU, primary keys and foreign keys in schema.sql. Validate nonblank names at the application boundary.
2. Insert Pen SKU PEN-001, price 200, stock 5.
3. Independently attempt a duplicate SKU and negative-stock row, rolling back each failed attempt.
4. Query the accepted data afterward and map each rule to its enforcing layer.

**Check:** only the valid row remains. State explicitly which rule is application validation and which is a database constraint; they are not automatically interchangeable.
@@
A sale is one bundle of related database changes.

1. Start Pen at stock 5, price 200, with no sale records for this test.
2. Within one transaction reduce stock by 2 and create a sale with one line, quantity 2/unit_price 200.
3. Commit only after every statement succeeds.
4. Outside the transaction query stock, line count and sale total.

**Check:** stock 3, one new line, total 400. Do not commit between the stock deduction and line insertion: that would allow a half-recorded sale if the later statement failed.
@@
Roll back the entire bundle when its second half fails.

1. Restore a fresh fixture with Pen stock 5 and no sale/line for this case.
2. In one transaction deduct stock, create a sale, then deliberately insert a line with an invalid foreign-key reference.
3. Let the error leave the transaction block and catch it outside.
4. Requery stock and sale/line counts.

**Check:** stock remains 5 and no new sale or line persists. Show the actual database state; catching an exception and printing “rolled back” is not sufficient evidence that the earlier deduction was undone.
@@
Inspect an actual lookup plan before claiming an index improves it.

1. Seed at least 1000 products and inspect EXPLAIN QUERY PLAN for a SKU lookup.
2. Note that a UNIQUE SKU already creates a lookup index in SQLite. For an unindexed SKU comparison, use a separate scratch table without that unique constraint.
3. Add an appropriate index to the scratch lookup and capture the second plan.
4. Confirm both queries return the same row and explain additional storage/write cost.

**Check:** evidence names the scan/index before and after. Do not claim a redundant index on an already unique key created an unindexed-to-indexed improvement.
@@
Two shoppers can read the last unit before either records a sale.

1. Trace A and B each reading stock 1 and attempting to sell it with a naive read/overwrite approach.
2. Propose an atomic conditional update: decrement only where ID matches and stock is at least the requested quantity.
3. In a disposable script make two successive quantity-1 attempts, checking affected-row count before creating a sale.
4. Explain the concurrent rule and the limits of this sequential demonstration.

**Check:** first attempt affects one row; second affects zero and creates no sale; stock is 0. A sequential SQLite check does not demonstrate PostgreSQL row-lock behaviour.
''')

pack(16, r'''
Create the building before adding its inventory department.

1. In a new project/ directory create a virtual environment and use its interpreter for all commands. Install the Django 5.2 baseline from your prepared packages or while online.
2. Run `python -m django startproject config .`, then `python manage.py startapp inventory`.
3. Run `python -m django --version` and `python manage.py check`.
4. Record the version and a tree showing manage.py, config/settings.py, config/urls.py and inventory/.

**Check:** Django's system check completes without errors. Do not run startproject over an existing project; copy its source instead if you already have the required structure.
@@
Register the department and connect its URL directory.

1. Add inventory to INSTALLED_APPS in config/settings.py.
2. Create inventory/urls.py with imports for path and an initially empty urlpatterns list.
3. Import include in config/urls.py and include inventory.urls at the empty root prefix.
4. Run `python manage.py check` again. Explain that the root file delegates requests while the app file defines the department's routes.

**Check:** configuration imports without errors; no inventory route is expected to exist until you add one. Accidentally including the root URL module inside itself creates a routing loop.
@@
A health view is a small request/response check.

1. Add health(request) in inventory/views.py returning JsonResponse with status set to the text ok.
2. Import the view in inventory/urls.py and add `path("health/", health, name="health")`.
3. Start runserver and open http://127.0.0.1:8000/health/.
4. Inspect status, Content-Type and body in the browser Network panel.

**Check:** 200, application/json content type and `{"status":"ok"}`. This verifies the route/view responds; it does not prove a database or every other dependency is healthy.
@@
Render a page by filling a reusable document with view data.

1. Create inventory/templates/inventory/home.html containing an h1 that displays the template variable shop_name.
2. Add a home view that calls render with that template and context `{"shop_name":"EMIO24"}`.
3. Add an empty-path route named home and open the root URL.
4. Change the context value to a temporary test name, reload and restore EMIO24.

**Check:** the heading follows context data without editing the template. A literal shop_name word is not a template variable; Django's template expression uses double braces.
@@
Named routes let callers ask for a destination without hard-coding its path.

1. Confirm your home and health URL patterns have those names.
2. Open `python manage.py shell`, import reverse from django.urls, and evaluate reverse("home") and reverse("health").
3. Record results and explain how reversing differs from handling an incoming request.
4. If you use a namespace, record the exact namespaced names and use them consistently.

**Check:** the unnamespaced setup resolves to `/` and `/health/`. A NoReverseMatch error means the requested name/arguments did not match your URL configuration, not that the browser is offline.
@@
A missing route never reaches an unrelated view.

1. Request http://127.0.0.1:8000/does-not-exist/ and inspect its status.
2. Compare it with a successful /health/ request.
3. In answers.md trace URL matching and explain why the health view is not chosen for the unknown path.
4. Explain how this differs from an exception raised after a valid route has already selected its view.

**Check:** the unmatched route returns 404. With local DEBUG enabled, Django may show route details; this is a development response, not a production error-page design.
@@
Make a concrete map of the code that handled your request.

1. In request-flow.md trace the root page through config/urls.py, inventory/urls.py, the home view, home.html and the HTTP response.
2. Trace /health/ separately and show that it uses JsonResponse instead of an HTML template.
3. Label where request data enters and context/response data leaves.
4. Add where a Product model lookup could enter next lesson.

**Check:** every box names an actual file/function. Do not claim a model was queried by the current health view when it simply returns a fixed dictionary.
''')

pack(17, r'''
Describe the stored product card as a Django model.

1. In inventory/models.py create Product(models.Model) with name CharField(max_length=120), price PositiveIntegerField and stock PositiveIntegerField(default=0).
2. Add __str__ returning the product name.
3. Explain that these integer fields allow zero and that whole-naira pricing is a deliberate course simplification.
4. Run `python manage.py check`; do not assume the table has been created yet.

**Check:** the class imports and system checks pass. Django supplies a primary key unless you define one. A model definition describes intended structure; migration steps make the database match it.
@@
Write the renovation instructions before applying them.

1. Run `python manage.py makemigrations inventory`.
2. Open the newly generated migration file; record its actual filename.
3. Identify dependencies, the CreateModel operation and the generated name/price/stock fields.
4. Explain what the migration's stock default means for new rows.

**Check:** a migration file exists containing the Product schema. Do not edit an existing migration that has already been applied merely to hide a changed model; later changes should produce another migration.
@@
Apply the pending schema changes to your local database.

1. Run `python manage.py showmigrations inventory` and note unchecked migrations.
2. Run `python manage.py migrate`, then showmigrations again.
3. Copy relevant output into answers.md and explain generation versus application.
4. Run migrate once more to observe the no-pending-work result.

**Check:** the Product migration is marked applied, and repeating migrate does not create a second Product table. Migration history tracks which versioned operations the database has already accepted.
@@
Prove that a saved model instance survives leaving the shell.

1. Open manage.py shell and import Product from inventory.models.
2. Create Pen with price 200 and stock 4 using Product.objects.create; record its assigned primary key.
3. Exit the shell completely, reopen it, import Product again and fetch that exact key.
4. Print name, price and stock plus str(product).

**Check:** Pen/200/4 persists and str gives Pen. Do not assume the ID is 1 if your disposable database contains earlier records; use the actual saved key.
@@
Evolve the schema while keeping an existing row usable.

1. Add a description text field permitting an empty value, using blank=True and a suitable empty-string default.
2. Generate the next migration, inspect it, then apply it.
3. Fetch the earlier Pen by its recorded ID and inspect all old fields plus description.
4. Update description, save and refetch.

**Check:** Pen's name/price/stock are unchanged, initial description is empty, and the later description persists. blank concerns validation; it does not mean the same thing as database NULL.
@@
Inspect what a migration asks the configured database to execute.

1. Run `python manage.py sqlmigrate inventory MIGRATION_NAME`, substituting your first Product migration's stem, such as 0001.
2. Identify table creation, primary key and the three authored fields in its SQL.
3. Record the database engine from settings and annotate any type differences from the Python model declarations.
4. Explain why another backend may produce different SQL for the same migration operations.

**Check:** the inspected SQL corresponds to the actual migration and configured backend. sqlmigrate displays SQL; it does not apply the migration by itself.
@@
Migration history should rebuild the schema from an empty database.

1. Copy project source, including migration files, into a disposable rebuild folder. Configure a separate empty database path; do not delete your working database.
2. Use the prepared environment and run migrate in that copy.
3. Create a Product and read it back, including description.
4. Record commands, database path and observed values in rebuild-notes.md.

**Check:** the schema rebuilds without copying a populated database. An empty database starts with no business records; successful schema reconstruction does not imply fixtures were migrated automatically.
''')

pack(18, r'''
Prepare a fixture whose later query results are predictable.

1. In a disposable migrated database create Pen 200/4, Book 500/8 and Bag 4000/0 in that order.
2. Save their actual IDs in query-notes.md. Avoid adding duplicate fixtures every time you reopen the shell.
3. Query name, price and stock ordered by ID and record the rows.
4. Explain that Product.objects is the manager providing query operations.

**Check:** the exercise fixture has exactly three products with these values. Keep other practice records outside this fixture or clearly filter to it before calculating expected totals.
@@
Build a selection using a field lookup and explicit ordering.

1. Import Product in manage.py shell and filter with stock__lte=4.
2. Order by stock then id; display name/stock tuples.
3. Repeat with cutoff 0 and an empty-match cutoff such as -1.
4. Explain the double underscore as part of Django's lookup syntax, not a field named stock__lte.

**Check:** cutoff 4 gives Bag/0 then Pen/4; cutoff 0 gives Bag/0; -1 gives an empty QuerySet. Include equality at the boundary.
@@
Use get when exactly one record is expected.

1. Fetch Pen using its recorded primary key and print its name.
2. Choose an absent key, verify it is absent, then attempt get and catch Product.DoesNotExist.
3. Compare with filter(pk=missing_key), which represents zero matching rows without that exception.
4. Explain that get can also fail if a nonunique condition matches multiple rows.

**Check:** valid get returns a Product object; missing get follows the documented exception path; missing filter is empty. Do not catch every exception and treat it as a missing product.
@@
An F expression lets the database calculate from its current field value.

1. Import F from django.db.models. Load Pen into a Python variable while stock is 4.
2. Update its database stock using F("stock") + 3 through a filtered QuerySet.
3. Print the already loaded object's stock, then call refresh_from_db and print again.
4. Record both readings and explain the difference between a stored row and an earlier Python object snapshot.

**Check:** database stock becomes 7; refreshing makes the object show 7. A QuerySet update does not automatically refresh every previously loaded instance.
@@
Aggregate after the earlier update, not against the original fixture.

1. Import Sum from django.db.models and calculate the sum of stock over the three fixture products.
2. Extract the named aggregate result and compare with 7 + 8 + 0.
3. Run the aggregate over an empty filtered QuerySet.
4. Define a zero default for that empty result and demonstrate it without deleting products.

**Check:** total stock is 15, and your chosen empty-summary interface produces 0. Raw aggregate results can contain None; explain how your code turns that into the intended numeric default.
@@
A QuerySet can describe work before executing it.

1. In a Django test or shell import connection and CaptureQueriesContext.
2. Capture queries while merely constructing a filtered QuerySet; do not print or iterate it inside that first measurement.
3. In another capture block evaluate it with list(...), then inspect the SQL/count.
4. Evaluate the same already materialized QuerySet again and distinguish cached results from a newly created QuerySet.

**Check:** construction performs no select for its rows; initial evaluation does. Avoid asserting an unexplained total for a whole shell session containing unrelated database operations.
@@
A projection returns selected values instead of fully featured model instances.

1. Query the fixture with values("name","stock").order_by("id") and convert it to a list.
2. Repeat with values_list("name","stock") and compare the shapes.
3. Compare those entries with Product instances from an ordinary QuerySet.
4. Explain when a read-only report might need only these two fields.

**Check:** values entries are dictionaries; values_list entries are tuples; current stocks are 7,8,0. A dictionary result does not have a Product.save method just because it came from an ORM query.
''')

pack(19, r'''
Show the ledger as a readable HTML page.

1. Add a list view that retrieves Product rows ordered by ID and passes them to inventory/list.html.
2. Route GET /products/ to it and render name, price and stock for each row.
3. Use a template empty branch/message for no rows.
4. Test with Pen 200/4 and Book 500/8, then with an empty disposable database or an isolated test fixture.

**Check:** populated HTML shows both records; empty HTML clearly says there are no products. Loading this GET page must not create or update a row.
@@
A detail page takes the desired card number from its URL.

1. Add `/products/<int:pk>/` and a view receiving pk.
2. Use get_object_or_404 to find the product and render inventory/detail.html with name, price and stock.
3. Link to details from the list using named URL patterns.
4. Visit a known key, then a verified absent key.

**Check:** known product returns 200 with correct fields; missing product returns 404. A product's primary key need not equal its position in the list or the first sample ID.
@@
Accept a new card only after checking the submitted fields.

1. Add a GET page containing a POST form with labelled name, price and stock inputs and csrf_token.
2. On POST strip/check name, convert numeric text and reject non-integer or negative values before saving.
3. Create a product only after every field succeeds; show errors and the entered values after failure.
4. Submit Pen/200/4, then blank name and stock -1 as independent cases.

**Check:** the valid submission creates one row; invalid submissions create none. This lesson may use explicit validation; Lesson 20 refactors it into reusable Django forms.
@@
Editing should update the selected record, not accidentally add another.

1. Add edit GET/POST routes using the record's pk and load it or return 404.
2. Populate the GET form with existing data. On POST validate all editable fields before assigning/saving.
3. Change Pen stock 4 to 7 and redirect to its detail page after success.
4. Try an invalid negative stock and an absent ID.

**Check:** successful edit leaves row count unchanged and stock 7; invalid input preserves stored data; absent ID is 404. The form should display the user's rejected input alongside an explanation.
@@
Opening a confirmation page must not delete anything.

1. Add a delete confirmation GET showing the selected product and a labelled POST confirmation form with csrf_token.
2. Perform deletion only in the accepted POST branch, then redirect to the list.
3. Fetch the confirmation page and inspect the database before clicking Confirm.
4. Submit confirmation and attempt the old detail URL.

**Check:** GET retains the row; POST removes it; old detail returns 404. A link that deletes immediately on GET violates this exercise even if its text says Delete.
@@
Post-redirect-get prevents refreshing the result page from simply resending the same form.

1. After valid creation, return a redirect to the created product's detail or list page.
2. Submit a new product while watching the Network panel.
3. Record the POST response and following GET, then refresh the resulting page twice.
4. Compare row counts before submission, after submission and after refreshes.

**Check:** only one new row is created. This pattern handles ordinary browser refresh; it is not a complete duplicate-request prevention mechanism for repeated independent POSTs.
@@
Document and verify each route's allowed methods.

1. In method-matrix.md list list/detail/create/edit/delete-confirmation URLs and supported methods.
2. For every GET, state why it is read-only and verify row counts/stocks remain unchanged.
3. Send an unsupported method to at least one restricted view, using a test client or local request tool.
4. Configure a 405 response for unsupported methods and record it.

**Check:** create/edit/delete mutations occur only on intended POST flows; GET confirmation remains harmless. Record expected and observed methods, statuses and data effects rather than checking only whether a page looks correct.
''')

pack(20, r'''
A ModelForm gives the receiving clerk a form based on selected ledger fields.

1. Create inventory/forms.py with ProductForm derived from forms.ModelForm.
2. In Meta set Product as model and explicitly list name, price and stock; do not expose every field automatically.
3. Update create/edit views to bind the form on POST and render it on GET.
4. Display labels, entered values and field errors in the template.

**Check:** valid Pen/200/4 saves; invalid stock shows an error and retains the submitted name. Explicit fields prevent future model additions from silently becoming editable inputs.
@@
A name made entirely of spaces is still unusable even though it is text.

1. Add clean_name to ProductForm. Read the cleaned field, strip surrounding whitespace and reject the empty result with forms.ValidationError.
2. Return the accepted normalized name.
3. Bind forms with names `" Pen "` and `"   "`, supplying valid price/stock in both.
4. Compare is_valid, cleaned_data and errors before saving anything.

**Check:** padded Pen is accepted as Pen; spaces-only is rejected and no row is created. Returning the cleaned value matters: the form needs the accepted value, not just a printed message.
@@
Quantity validation belongs in a reusable form, not only the browser input widget.

1. Define SaleForm with an IntegerField named quantity and min_value=1.
2. Bind separate forms with raw quantity text "3", "0", "-1", "two" and "2.5".
3. Call is_valid on each; only read accepted cleaned quantity after successful validation.
4. Render one invalid form in the browser with its field error visible.

**Check:** "3" becomes integer 3; the other inputs fail. A minimum HTML attribute alone is not proof the server will reject an invalid direct request.
@@
A quantity can be valid by itself but invalid for the selected product.

1. Pass a Product instance into SaleForm using a documented constructor argument, storing it before calling the parent form initializer.
2. After basic quantity validation, compare it with that product's stock and add a quantity error if excessive.
3. With fresh stock 4, bind quantities 4 and 5.
4. Keep validation separate from deduction; validating a form must not sell anything.

**Check:** 4 is allowed and 5 rejected, with database stock still 4 in both validation-only checks. A later concurrent sale still needs a database-level stock rule; this form reads a snapshot.
@@
Use the clerk's accepted fields rather than returning to the unchecked paperwork.

1. In the view call is_valid before form.save or use of cleaned_data.
2. Remove direct assignments from request.POST to model fields after validation.
3. For a valid ProductForm save once; for invalid input render the same bound form without saving.
4. Demonstrate normalized name and numeric stock using a padded name and raw text numbers.

**Check:** stored name is stripped and stock is numeric; invalid stock does not alter the existing row. A successful is_valid call is wasted if the view then saves different unvalidated values.
@@
A bound form remembers the visitor's attempted input and its errors.

1. On GET create an unbound ProductForm; on POST bind request.POST.
2. Render labels, field values, errors, a submit button and csrf_token inside the POST form.
3. Submit a valid name with invalid stock, then correct only stock and resubmit.
4. Inspect the initial form and the failed form state.

**Check:** GET has no submission errors; failed POST preserves entered values and explains stock; correction can succeed without retyping everything. Do not replace an invalid bound form with a fresh empty one before rendering.
@@
Test the server by bypassing the browser's friendly restrictions.

1. In inventory/tests.py create a Django TestCase with known initial row count.
2. Use its test client to POST blank name, negative stock and fractional stock directly to your create route.
3. Assert the chosen form-error response, an invalid form/visible error and unchanged row count.
4. Add a valid POST and verify exactly one record with expected values.

**Check:** tests pass under `python manage.py test inventory` without opening a browser. These validation tests do not prove CSRF enforcement because Django's ordinary test client disables that check by default.
''')

pack(21, r'''
Use Django's password tools rather than treating passwords as ordinary text fields.

1. In the project shell get the configured user model with get_user_model.
2. Create disposable ordinary and staff users with create_user, or use set_password followed by save.
3. Demonstrate check_password returns True for the chosen password and False for another value.
4. Record usernames/roles and Boolean outcomes, not password or stored-hash values.

**Check:** authentication checks work and no plaintext password was assigned directly to user.password. Setting is_staff is a role flag; the custom view must still check it when its contract requires staff access.
@@
Login connects a verified identity with a browser session.

1. Add a /login/ route using Django LoginView and a registration/login.html template containing the form and csrf_token.
2. Set LOGIN_URL and a successful LOGIN_REDIRECT_URL pointing to your dashboard.
3. Try incorrect credentials, then valid credentials for the ordinary user.
4. Record response/redirect behaviour and the displayed outcome without copying credentials.

**Check:** incorrect credentials keep the user signed out with an error; valid credentials reach the intended page. A normal invalid-login form may return 200 with errors, rather than an HTTP authorization status.
@@
A protected dashboard should identify the visitor or send them to login.

1. Add login_required to the dashboard view and use request.user to show its username.
2. Request the route in a signed-out browser session and inspect the redirect, including the return-location parameter.
3. Sign in and request again.
4. Explain which middleware supplies request.user.

**Check:** signed-out access redirects to login; signed-in access returns 200 with the correct account name. This is identity protection, not yet a rule that one user owns every record displayed.
@@
Logout ends the browser's authenticated session through an intentional state-changing action.

1. Add a LogoutView route and a POST logout form containing csrf_token.
2. Configure its next page, such as /login/.
3. Sign in, confirm dashboard access, submit logout, then revisit dashboard.
4. Inspect behaviour from a direct GET to the logout URL too.

**Check:** after POST logout the dashboard requires login again. In the Django 5.2 baseline, LogoutView is not a state-changing GET link; use the form and document unsupported-method behaviour.
@@
Being signed in does not automatically grant destructive privileges.

1. Define a clear policy: product deletion requires is_staff or an explicit named permission, and state which you implement.
2. Enforce it in the delete view before any row is removed; hiding a button is optional UI assistance only.
3. Attempt a direct delete request as ordinary and privileged users with valid CSRF handling.
4. Compare status/redirect and row existence.

**Check:** ordinary user cannot delete; permitted user can. A signed-in denial should follow your documented response policy, such as 403, and preserve the record.
@@
Inspect the visitor ticket without exposing its secret value.

1. Sign in and open browser storage/cookie tools for the local site.
2. Record the session cookie's name, path and HttpOnly/Secure/SameSite settings, redacting its value.
3. Explain HttpOnly as restricting JavaScript access, Secure as requiring HTTPS transmission, and SameSite as controlling cross-site sending behaviour.
4. Compare development settings with intended production HTTPS settings.

**Check:** notes describe actual observed flags. Do not claim a Secure cookie works over an ordinary remote HTTP site or that these flags replace server-side permission checks.
@@
Verify access rules with requests that do not rely on visible buttons.

1. In tests create ordinary and privileged users plus a product fixture.
2. Test anonymous dashboard access, ordinary authenticated dashboard access and the deletion rule for both roles.
3. Use separate client sessions or explicitly logout between cases; force_login can set up authenticated tests without testing password entry again.
4. Assert both response behaviour and whether the product remains.

**Check:** unauthorized cases never mutate data and allowed cases do. Include a separate real login test if you want to claim password authentication is tested; force_login bypasses it intentionally.
''')

pack(22, r'''
Install the API tools into the same toolbox that runs Django.

1. Use the project interpreter to install djangorestframework from prepared artifacts or while online.
2. Add rest_framework to INSTALLED_APPS and record `python -m pip show djangorestframework` output without unrelated environment details.
3. Run manage.py check and import rest_framework in the project shell.
4. Record the resolved installed version in requirements.txt.

**Check:** the running project can import DRF; installing it for a different interpreter does not satisfy this. Keep existing Django settings instead of replacing the entire file with a fragment.
@@
A serializer turns a model card into simple values suitable for a response.

1. In inventory/serializers.py create ProductSerializer as a ModelSerializer with explicit id/name/price/stock fields.
2. In the project shell import it and serialize an existing Pen record using an instance argument.
3. Serialize two products with many=True and inspect .data.
4. Explain how a single representation differs from a list representation.

**Check:** one record has the four selected fields; the collection has one representation per record. .data is not automatically a transmitted HTTP response; a view handles that later.
@@
Incoming data takes the opposite path and must be checked before saving.

1. Instantiate ProductSerializer with data containing Pen/200/4, then call is_valid and inspect validated_data.
2. Repeat with stock -1 and inspect errors. Add a missing required name case.
3. Record product count before and after validation-only calls.
4. Explain the distinction between instance= for an existing record and data= for submitted values.

**Check:** valid input is accepted, invalid fields produce errors and validation alone creates no database row. Accessing .data before calling .save on a writable serializer can also affect the intended workflow; validate and save in the correct order.
@@
A server-assigned identifier should not become a client-controlled creation field.

1. Mark id read-only in ProductSerializer, keeping it visible in output.
2. Submit a valid creation body containing an arbitrary id already belonging to another product.
3. Validate/save and inspect the assigned ID and original row.
4. Record whether the read-only input is ignored, as in the normal serializer behaviour, rather than promising an automatic rejection.

**Check:** the client cannot overwrite the existing row or dictate its ID through creation. The response still includes the server-assigned identifier for later detail requests.
@@
Normalize and validate a name at the serializer boundary.

1. Add validate_name(self,value) that strips whitespace, rejects an empty result with serializers.ValidationError, and returns accepted text.
2. Submit padded Pen and spaces-only names with otherwise valid fields.
3. Inspect validated_data/errors, then save only the valid case and refetch it.
4. Compare behaviour with the browser form's name rule.

**Check:** stored name is Pen without surrounding spaces; blank input creates no record. The API needs its own validation even if an HTML form already rejects the same input.
@@
Creation and update both use save, but the existing instance changes the operation.

1. Validate a new product body and call save without an instance; record the new row's key and count change.
2. Make another serializer with that instance and a complete updated body, validate and save.
3. Refetch the row and check its fields/count.
4. Use an invalid update body to confirm saving is not performed after validation failure.

**Check:** creation adds one row; updating it does not add another. Invalid input leaves the previously stored fields intact. Print successful return values only after validation succeeds.
@@
A partial update can change one box while retaining the others.

1. Start with a persisted Pen price 200/stock 4.
2. Bind that instance with data containing only stock 7 and partial=True; validate/save.
3. Refetch all fields. Separately try the same incomplete input without partial=True and record missing required-field errors.
4. Explain which writable fields are required by your actual serializer.

**Check:** PATCH-style update keeps name Pen and price 200 while stock becomes 7. Full validation normally requires name and price here; do not invent a missing-stock error if your model default makes it optional.
''')

pack(23, r'''
A list API returns data instead of rendering an HTML product card.

1. Add GET /api/products/ using a DRF view and ProductSerializer with many=True over an ID-ordered QuerySet.
2. Return a DRF Response. State whether this version is an array or already uses a pagination envelope.
3. Request it with two products and with an empty isolated fixture.
4. Record status, content type and parsed body.

**Check:** status 200 and the correct records; empty results have the documented empty shape. Returning model objects or a QuerySet directly is not the serializer's simple-value representation.
@@
Creation must distinguish accepted input from a rejected form.

1. Add POST handling on the collection route, binding ProductSerializer with request.data.
2. Validate before saving. Return created representation with 201; return validation errors with 400.
3. Send Pen/200/4 as JSON, then independently stock -1.
4. Check database counts around both requests.

**Check:** valid request adds exactly one row and returns its assigned ID; invalid request adds none and identifies stock. request.data is parsed request content; do not manually assume every request body is a form-encoded dictionary.
@@
A detail route resolves one existing product or a missing-resource response.

1. Add /api/products/<int:pk>/ and fetch with get_object_or_404 or equivalent DRF behaviour.
2. Serialize the single instance without many=True and return it.
3. Request a known product and a verified absent ID with APIClient or your local request tool.
4. Confirm neither request changes row count or stock.

**Check:** known ID is 200 with one product object; absent ID is 404. Do not return 200 with an error string for a missing resource under this contract.
@@
Use the update method's documented completeness rule.

1. Add PUT for complete writable fields and/or PATCH for partial changes; state which methods your view supports.
2. For PATCH bind the existing instance with partial=True. Validate before save.
3. Starting Pen 200/4, change only stock to 7; then try -1 in a separate request.
4. Refetch the product after each request.

**Check:** success returns 200 and stock 7 while name/price remain; invalid update returns 400 and leaves the successful state intact. Omitting instance= would create another row instead of updating the target.
@@
Deletion has a successful empty response and a lasting database effect.

1. Add DELETE handling on the detail route.
2. Resolve the target or return 404, delete it, then return status 204 without a JSON body.
3. Delete a disposable known product and inspect response bytes plus row existence.
4. Request that detail again and repeat DELETE if desired.

**Check:** first deletion returns an empty 204; later lookup is 404. Calling response.json on an empty 204 is a client error; no JSON body is expected.
@@
Exercise failures in parsing and method selection separately from field validation.

1. Send a method your configured route does not allow, such as POST to a GET-only health view.
2. Send syntactically broken JSON to the product create route with application/json content type.
3. Record statuses, body shapes and before/after product counts.
4. Compare these with the negative-stock serializer failure from Exercise 4.

**Check:** unsupported method is 405; malformed JSON is 400; neither writes a product. A 400 parser error occurs before normal field validation, so its message need not look like a stock field error.
@@
A generic view packages common request handling while you supply the model-specific choices.

1. In generic_views.py implement list/create using ListCreateAPIView with queryset, serializer_class and the same permission policy as your original view.
2. Wire it at a temporary comparison path, leaving one clearly documented final route.
3. Run the same populated/empty/valid-create/invalid-create cases against both implementations.
4. Compare status/body/database effects, allowing only documented pagination differences.

**Check:** the generic version honours the same validation and access contract. Less code is not proof of equivalent behaviour; demonstrate the actual cases.
''')

pack(24, r'''
A ViewSet groups operations for the same resource.

1. Define ProductViewSet(ModelViewSet) with an ID-ordered queryset and ProductSerializer.
2. Copy the existing view's permission policy explicitly rather than relying on accidental defaults.
3. Remove duplicated operation logic only after the replacement is wired and tested.
4. Identify which built-in actions handle list, retrieve, create, update, partial_update and destroy.

**Check:** the ViewSet can use the same serializer validation. Declaring the class alone exposes no route; Exercise 4 registers its URLs.
@@
The router translates standard resource operations into named URLs.

1. In inventory/urls.py create a DefaultRouter and register products with basename product.
2. Include its URLs below /api/ from the project URL configuration.
3. In the shell use reverse for product-list and product-detail with a real pk.
4. Check you did not produce a doubled prefix such as /api/api/products/.

**Check:** list resolves to /api/products/ and detail to /api/products/ID/. basename determines route names; it is not automatically the same thing as the Python class name.
@@
Verify what each method does on collection and detail paths.

1. In route-matrix.md list GET/POST collection and GET/PUT/PATCH/DELETE detail with their corresponding ViewSet actions.
2. Create a disposable product, retrieve it, update stock, partially update its name and delete it.
3. Record each status and final database effect.
4. Request a missing detail and an unsupported method.

**Check:** successful operations follow 200/201/204 as applicable, missing detail is 404 and unsupported method is 405. A successful route reverse does not prove its action returns correct data.
@@
Bound the catalogue into stable pages.

1. Configure PageNumberPagination and PAGE_SIZE=2 in DRF settings, retaining other settings.
2. Seed exactly five fixture products and ensure the ViewSet orders by ID.
3. Request pages 1,2,3 and record count/next/previous/results.
4. Follow next links from page 1 and compare all collected IDs.

**Check:** page lengths are 2,2,1, count is 5, and each ID appears once. Without stable ordering, paging observations can be inconsistent even when the page-size setting is correct.
@@
A custom collection action still needs validation and pagination.

1. Add a GET collection action for low stock using a threshold query parameter; choose and document a default such as 5.
2. Convert threshold to an integer and reject malformed input with a 400 response.
3. Filter stock <= threshold and pass the result through the ViewSet pagination/serialization helpers.
4. Test stocks 0,2,4 with threshold 2 and then text "bad".

**Check:** valid results include stocks 0 and 2 in the normal page envelope; bad input returns 400. Returning a raw unpaginated QuerySet would break the collection contract.
@@
Allow only intended ordering choices.

1. Configure DRF's OrderingFilter or equivalent with allowed fields id, name and stock.
2. Define a stable default, such as id, and document how ties are resolved.
3. Request ascending stock and descending stock on fixtures with distinct counts.
4. Try an unsupported field and record whether your chosen implementation ignores it or returns an error.

**Check:** valid orderings arrange the same permitted records; unsupported input follows the documented policy. Do not promise a 400 if the configured filter actually falls back to default ordering.
@@
Make the client contract match the router and page shape actually in use.

1. Update api-contract.md with exact collection/detail/custom-action paths, trailing-slash policy and allowed methods.
2. Include a real page response and identify results as the product array.
3. Show client pseudocode reading body.results, not mapping over the whole response object.
4. Repeat one list, create, invalid-create and missing-detail check using the documented paths.

**Check:** a reader can call each route without guessing prefixes or envelope shape. A client that expected an array must be updated when pagination wraps that array in an object.
''')

pack(25, r'''
A signed pass is readable but tamper-evident; it is not an encrypted secret document.

1. Draw login → access/refresh pair → Bearer-authenticated request → access expiry → refresh exchange.
2. Label which request carries a password, which carries an access token and which carries a refresh token.
3. Add failure branches for wrong credentials, invalid signature and expired access token.
4. Explain that decoding claims alone does not verify the signature or grant permission.

**Check:** the API authorizes a verified identity separately from checking token validity. The diagram never treats a refresh token as the normal credential for product requests.
@@
Configure an existing verifier rather than implementing token cryptography.

1. Select a maintained compatible integration; the reference path for this course is djangorestframework-simplejwt. Record its installed version and dependency compatibility in requirements/settings notes.
2. Configure its JWTAuthentication class in DRF's authentication classes. Keep other explicitly needed classes and record their order.
3. Protect the intended endpoint with IsAuthenticated and run Django system checks.
4. Use the package's token views in Exercise 5; do not write signing code yourself.

**Check:** the selected class imports under the project interpreter. Follow the installed package's versioned documentation; do not assume a sample requirements list guarantees every Django version is officially supported. [Setup reference](https://django-rest-framework-simplejwt.readthedocs.io/en/stable/getting_started.html).
@@
Obtain test credentials through the token endpoint.

1. For Simple JWT, route TokenObtainPairView to /api/token/ and TokenRefreshView to /api/token/refresh/; both use .as_view().
2. Create a disposable user with Django's password APIs.
3. POST that user's username/password to the pair endpoint using JSON, then independently try a wrong password.
4. Record statuses and token field names, redacting actual credential/token values.

**Check:** valid credentials yield access and refresh strings; invalid credentials yield no usable pair. The decoded teaching payload in Exercise 2 is not a signed token and cannot be pasted in as one.
@@
Present the access pass in the request header.

1. Request your protected product endpoint using `Authorization: Bearer <access-token>`, replacing the placeholder only in the local request tool.
2. Repeat with no credential and with a deliberately malformed token.
3. Record statuses and confirm rejected calls expose no protected product data.
4. Document how the configured authentication-class order determines the unauthenticated response challenge/status.

**Check:** valid token succeeds; invalid/missing credentials do not. With JWTAuthentication first, expect its 401 challenge behaviour. Never treat a 200 public endpoint as proof that authentication was checked.
@@
Expiry must be enforced even though the printed payload remains readable.

1. Use local test settings with a short access lifetime, or the library's supported token/time testing APIs; keep production settings separate.
2. Obtain a fresh token and prove it works before expiry.
3. Advance the test time or wait beyond expiry, then make the same protected request.
4. Record time assumptions and response without saving the token value.

**Check:** the expired token is rejected. Do not simply edit the payload's exp and claim you tested expiry: editing a signed token also invalidates its signature and tests a different failure.
@@
A renewal voucher issues a new access pass under the configured policy.

1. POST a valid refresh token to /api/token/refresh/ and use the new access token on the protected endpoint.
2. Repeat the refresh call with a malformed refresh token and record rejection.
3. Inspect rotation/blacklist settings and document whether old refresh tokens remain usable.
4. Explain what logout means in your chosen configuration, including the remaining lifetime of already issued access tokens.

**Check:** valid renewal gives usable access; invalid renewal does not. Deleting a token in one browser is not proof it has been revoked everywhere.
@@
Choose browser storage with an explicit reload/logout story.

1. Compare in-memory access storage with an HttpOnly-cookie design in token-storage.md.
2. For each, describe who can read/send the credential and the relevant XSS/CSRF concern.
3. Choose one for the later frontend and explain login, reload, expiry, refresh and logout.
4. If using cookies, describe credentialed requests and CSRF protection; if using memory, explain how reload signs out or securely renews.

**Check:** the design does not claim a signature encrypts payload data or that one storage choice removes all browser security concerns. Document a usable flow rather than only naming a storage API.
''')

pack(26, r'''
Ownership connects each card to the business/user allowed to manage it.

1. Add Product.owner as a ForeignKey to the configured user model and choose a documented deletion policy.
2. In a disposable fixture assign existing rows intentionally before enforcing any required non-null owner constraint.
3. Generate/apply migrations and create A's two products and B's three products.
4. Query each record's owner and record IDs without credentials.

**Check:** every fixture row has its intended owner; migration did not silently assign all real records to one account. Ownership requires query/view rules as well as the model field.
@@
Scope the rows brought to the service desk before serializing them.

1. In the authenticated ViewSet implement get_queryset filtering owner=request.user.
2. Sign in as A and list products; repeat as B using a separate client/session.
3. Record returned IDs and pagination counts.
4. Make the anonymous request and check that your authentication policy blocks it.

**Check:** A sees only two owned records and B only three. Object-level permission checks are not a substitute for filtering a list response; do not retrieve everyone's data and hide cards only in the UI.
@@
Guessing another user's valid ID must not bypass the list restriction.

1. Record one B-owned product ID and its fields.
2. As A request its detail, PATCH its stock and DELETE it directly.
3. Inspect the record as B afterward.
4. State your policy: a queryset scoped before lookup commonly returns 404 for an inaccessible ID; explicit object denial may return 403.

**Check:** all three attempts disclose no protected details or mutations and B's row remains unchanged. Verify state, not just an error-looking message in an otherwise successful response.
@@
The server determines ownership during creation.

1. Make owner read-only or exclude it from writable serializer fields.
2. In perform_create save with owner=request.user.
3. As A submit a valid product body that also tries to supply B's owner ID.
4. Inspect the created row and both users' lists.

**Check:** it belongs to A, or the extra owner field is explicitly rejected under your policy; it must never become B's product. Validating that B's ID exists does not grant A permission to assign ownership to B.
@@
Define the privilege policy before writing a special-case bypass.

1. In permissions.py define whether staff may view all products and perform all operations, or a narrower documented set.
2. Implement both queryset visibility and write checks consistently with that choice.
3. Test ordinary A, ordinary B and staff against owned and unowned rows.
4. Record one allowed and one denied ordinary-user action plus the relevant staff behaviour.

**Check:** a role flag is not automatically a universal override. The matrix describes the actual implemented policy, including whether staff can transfer ownership.
@@
Custom actions must use the same permission boundary as standard CRUD.

1. Audit low-stock and sale actions for direct unscoped Product.objects lookups.
2. Use get_queryset/get_object or equivalent scoped access before reading or modifying a product.
3. As A call the low-stock action and attempt a sale against B's product ID.
4. Inspect both users' inventory after the attempts.

**Check:** custom lists contain only permitted rows and the cross-owner sale changes neither stock nor sale history. A permission check on retrieve alone does not automatically protect custom code that bypasses it.
@@
Turn the access matrix into repeatable API checks.

1. Create fixtures for anonymous, A, B and staff, with known owned records.
2. Test list/detail/create/update/delete outcomes appropriate to each role and ownership relationship.
3. Assert response status, returned IDs and database side effects, using fresh records for destructive cases.
4. Run `python manage.py test inventory` and record the matrix plus results.

**Check:** direct guessed-ID attacks and owner-spoofed creation are covered. If you use force_authenticate for permission tests, label them as permission tests; they do not validate JWT signature handling.
''')

pack(27, r'''
A threat model identifies what could be harmed and where untrusted input crosses a boundary.

1. Draw browser, API, database and deployment configuration in threat-model.md.
2. List stock, customer records and credentials as assets and identify who should access each.
3. Add an abuse scenario per boundary, such as another user's product ID or a forged stock value.
4. Map each scenario to an actual control and a local check you can perform.

**Check:** the document names assets, actor, entry point, potential harm and defence. “Use security” is not a testable control; specify validation, authentication or ownership enforcement as appropriate.
@@
A query parameter is data, even when it contains punctuation that resembles SQL.

1. In a disposable fixture insert `Maker's Pen` using ORM creation or bound SQL parameters.
2. Search for it through the application's parameterized query path.
3. Search for a text value such as `' OR '1'='1` and record the ordinary no-match result unless that exact name exists.
4. Explain the difference between binding values and concatenating them into SQL instructions.

**Check:** the apostrophe name returns exactly and the second input does not select every product or alter the database. Use ? for direct sqlite3 and %s for Django cursor parameters; do not mix their conventions.
@@
User text should display as text rather than run as browser instructions.

1. Store a disposable product name `<script>alert(1)</script>`.
2. Render it through normal Django template escaping with a product-name variable.
3. Inspect displayed text and page source/DOM; record whether any script executes.
4. Explain why marking untrusted text safe would change the boundary. Do not leave an intentionally unsafe template in the working project.

**Check:** the name is visible as literal text and no alert runs. A safe JSON response alone does not prove every eventual HTML insertion is safe.
@@
CSRF checks must be enabled in the test that claims to exercise them.

1. Use Django Client(enforce_csrf_checks=True) with an authenticated session.
2. POST a write without a CSRF token and record 403 plus unchanged data.
3. GET the actual form to receive a CSRF cookie and rendered token, then submit its token through the same client.
4. Verify the otherwise valid request succeeds and explain that it uses the browser session credential.

**Check:** no-token and valid-token requests differ as expected. A default Django test client disables CSRF checks, so it cannot establish this result. [Testing reference](https://docs.djangoproject.com/en/5.2/topics/testing/tools/).
@@
An origin is the browser's scheme/host/port combination, not simply a domain label.

1. Record your real frontend and API origins; ports 5173 and 8000 are different origins even on localhost.
2. If separate, configure your installed CORS middleware to allow only the intended frontend, placing it as its documentation requires.
3. Make browser requests from allowed and deliberately different local origins; inspect preflight/response headers and whether browser JavaScript can read the response.
4. Compare with a direct non-browser API request.

**Check:** allowed-origin browser reads work; disallowed reads are blocked under the policy. CORS does not replace authentication and does not prevent every client from sending a request.
@@
Keep a deployment key outside committed source while documenting how to supply it.

1. Read a dummy variable such as EMIO24_DEMO_SECRET through os.environ in local settings.
2. Fail clearly if required configuration is absent, then run with a fake value supplied through the environment.
3. Create .env.example listing only the name and placeholder; confirm actual .env is ignored if you use one.
4. Explain that Django does not load a .env file automatically unless you configure a loader.

**Check:** missing and present cases behave differently; evidence contains neither real secrets nor their values. A placeholder file is documentation, not a populated production configuration.
@@
Users need a safe error page while operators need useful diagnostic records.

1. Use separate local production-like settings with DEBUG=False and the correct allowed local hosts.
2. Trigger a controlled exception through a test-only view in a disposable copy; configure logging to capture a redacted diagnostic.
3. Inspect response and log, then remove the deliberate failure route from the working app.
4. Record which details each audience receives.

**Check:** the response is generic and contains no traceback, settings or secrets; the log identifies the failure. A host-configuration 400 is not the controlled 500 you intended to test.
''')

pack(28, r'''
A test compares an independently known answer with the program's actual result.

1. Write a small sale-total function and a unittest.TestCase, using test_ method names.
2. Assert totals 200*3=600 and 50*4=200; add an empty inventory-value check returning 0.
3. Run the test file or Django inventory test suite, depending on where you placed it.
4. Record the test names and result.

**Check:** expectations are literal known values, not calculated by calling the same implementation again. A file that runs without importing/discovering any tests is not a passing test suite.
@@
Rejected sales should be tested for both the error and unchanged stock.

1. Prepare a fresh Pen price 200/stock 4 for each case.
2. Use assertRaises(ValueError) for quantities 0, -1, 2.5 and 5, plus True if your direct-call contract rejects bool.
3. After each rejected call assert stock remains 4.
4. Add the boundary success quantity 4 and check total 800/stock 0.

**Check:** an implementation that raises after subtracting stock must fail your tests. Reusing a mutated fixture across cases can hide errors, so set up each case independently.
@@
Persistence needs a new read, not merely the same object still sitting in memory.

1. Use a temporary directory/file or Django TestCase's isolated database.
2. Save a product, discard the local object reference, then reload by path or primary key.
3. Assert name, price and stock equal the expected values.
4. Ensure cleanup leaves your working inventory untouched and document the chosen test storage.

**Check:** the result comes from a storage read. Comparing an object with itself immediately after assignment proves neither file writing nor database persistence.
@@
An API contract test checks transport and storage behaviour together.

1. Use DRF APIClient and appropriate test authentication to POST a valid Pen body.
2. Assert 201, expected fields, an assigned ID and exactly one added row.
3. POST stock -1 and assert 400 with no added row.
4. GET a verified absent detail and assert 404.

**Check:** every response assertion has the relevant database assertion. State the authentication setup; force_authenticate isolates API behaviour and does not test the real login/token flow.
@@
Ownership tests should attempt the requests a hidden button would normally discourage.

1. Create A and B with separate products and authenticate as A.
2. List products and assert every returned record belongs to A, accounting for the pagination envelope.
3. Directly retrieve/update/delete B's known ID and assert the policy's denial status.
4. Refetch B's record to verify unchanged fields and existence.

**Check:** list and detail/write boundaries are all exercised. An assertion that a Delete button is absent does not prove the endpoint denies a crafted request.
@@
A fake controls the payment boundary so success and failure are repeatable.

1. Inject a payment fake that records amounts and can raise a simulated refusal.
2. From fresh stock 4 sell quantity 2 at price 200 under success and refusal configurations.
3. Assert the attempted charge is 400 and stock decreases only after success.
4. Add an oversale case and assert no payment call occurs.

**Check:** the tests perform no network request. A recorded call proves attempted payment; the fake's configured result determines whether checkout may commit its stock change.
@@
Prove that a useful test detects a realistic defect.

1. In a disposable copy temporarily change the sale boundary so buying exactly all available stock is rejected.
2. Run the relevant quantity-equals-stock test and save the failure output.
3. Restore the correct comparison and rerun the same test, then the affected suite.
4. Explain which requirement the failing assertion protects.

**Check:** you have a failing then passing run caused by the deliberate code change. Do not weaken the assertion just to get green output or leave the defective copy as your final implementation.
''')

pack(29, r'''
Measure a repeatable workload before changing the implementation.

1. Seed at least 100 products assigned to several suppliers in a disposable database.
2. Record fixture count, response page size, database engine and the exact list request.
3. Capture query count and elapsed time for repeated runs, distinguishing first/warm runs.
4. Save returned IDs/names as a correctness reference alongside timing.

**Check:** comparisons use the same data and workload. Do not compare an unpaginated 100-row response against a 2-row response and attribute every difference to query optimization.
@@
N+1 means one list query followed by a lookup for each returned product.

1. Render/serialize supplier.name for each product without eager loading.
2. Capture queries around the complete evaluation, not just QuerySet construction.
3. Identify the initial product query and repeated supplier fetches.
4. For a controlled unpaginated five-product case, compare with the expected one-plus-five pattern, noting any extra unrelated queries separately.

**Check:** the evidence shows repeated supplier lookups. If your framework already eagerly loads or reuses values, report that instead of inventing six queries.
@@
Join single-valued relationships before the display loop.

1. Add select_related("supplier") to the same queryset used by the measured response.
2. Rerun the identical request and capture query count/timing again.
3. Compare returned IDs, product names and supplier names with the baseline.
4. Explain which repeated trips to the database disappeared.

**Check:** the controlled product/supplier iteration normally uses one joined select; overall request counts may include authentication or pagination queries. Correctness must remain unchanged even if elapsed times vary on a small dataset.
@@
Collections need a different loading strategy from one foreign key.

1. Choose Product.categories or a reverse sale-line relation and seed at least two related entries for a product.
2. Access that collection for each product and capture the naive query pattern.
3. Add prefetch_related for the selected relationship and repeat exactly the same access.
4. Compare values and explain the separate child query combined in Python.

**Check:** related collections are complete and repeated per-product queries are reduced. A later differently filtered related-manager call may bypass the prefetched cache; measure the exact access your UI uses.
@@
Bound both database work and the size of the response deliberately.

1. Configure a fixed page size and explicit ordering; request first and next pages on the same fixture.
2. Identify fields the client actually needs and remove only unnecessary response fields.
3. Measure serialized response bytes and query counts before/after, recording page sizes.
4. Confirm links/counts and required fields still match the contract.

**Check:** all intended records remain reachable and IDs do not repeat across stable pages. Fewer fields is not permission to drop a field the frontend depends on without updating its contract.
@@
A cached summary is a temporary copy that must respect ownership.

1. Calculate an owner's stock total and choose a cache key incorporating owner ID and summary version.
2. Give A and B different totals, for example 4 and 9, and request summaries as each.
3. Cache the result with a documented short expiry, then repeat requests to observe reuse.
4. Record backend/cache configuration and the uncached value used for comparison.

**Check:** A always gets 4 and B 9 in the fixture, including cached requests. A single global stock-summary key would leak or mix data between users.
@@
Publish a cache change only after the authoritative database transaction succeeds.

1. Begin with A's cached total 4. Sell one unit successfully and schedule invalidation using transaction.on_commit or equivalent post-commit logic.
2. Request the summary again and compare with the database total 3.
3. Repeat from a fresh fixture with a forced transaction failure.
4. Observe that no false success total is published for the rolled-back sale.

**Check:** committed sale refreshes to 3; failed sale remains 4. In Django TestCase, use supported commit-callback execution tools or a suitable transaction test; callbacks may not run when the outer test transaction never commits.
''')

pack(30, r'''
Package the development app with a repeatable recipe.

1. In project/Dockerfile choose the course Python base, set WORKDIR, copy requirements first, install them, then copy source.
2. Use a JSON-array CMD that runs the development server on 0.0.0.0:8000.
3. Explain each instruction and why copying requirements separately can reuse a dependency layer.
4. Check requirements reflect your working environment.

**Check:** the recipe contains the app's required files and an explicit startup command. This exercise packages development; runserver is not the production application server used in the release lesson.
@@
Keep generated and private material outside the image's source bundle.

1. Create project/.dockerignore excluding .git, .venv, node_modules, .env, caches and private local database files.
2. Keep a harmless .env.example if useful, ensuring the ignore patterns do not unintentionally exclude required source.
3. Review Dockerfile COPY instructions against these patterns.
4. Inspect a disposable build image's /app listing after Exercise 5.

**Check:** source/configuration templates are present while the actual .env and private database are absent. A file inside the build context may be copied into image layers even if you remove it in a later instruction.
@@
A build result is an image, not yet a running service.

1. From project/ run `docker build -t emio24-dev .`.
2. Record relevant successful build output and the image ID from `docker image inspect emio24-dev`.
3. Run a disposable inspection such as `docker run --rm emio24-dev python --version`.
4. If offline resources are missing, identify the missing base image/package rather than recording an imagined build.

**Check:** the image exists and its interpreter runs. Installing Docker alone does not cache the selected base image or Python dependencies.
@@
Map an outside door to the container's listening service.

1. Run `docker run --rm -p 8080:8000 emio24-dev` with the needed local configuration.
2. Open the app's health path at http://127.0.0.1:8080/health/.
3. Record status/body and the container's request log; then stop this disposable run.
4. Explain host port 8080 versus container port 8000.

**Check:** health returns the configured 200 response. The process must listen on 0.0.0.0 inside the container for the mapping; binding only its internal loopback can make it unreachable from the host mapping.
@@
Runtime configuration should not require rebuilding the source image.

1. Make settings read a harmless DEMO_SHOP_NAME environment value with a documented fallback.
2. Run a disposable container with `-e DEMO_SHOP_NAME=PracticeShop` and print the setting through a shell command or harmless view.
3. Run again with a different value using the same image ID.
4. Inspect Dockerfile to ensure the runtime value was not hard-coded there.

**Check:** observed configuration changes without an image rebuild. Use fake settings here; do not print secrets as evidence or bake them into an image layer.
@@
Store the ledger outside the container's replaceable writable layer.

1. Configure SQLite/data storage at /data/inventory.sqlite3 and create a dedicated named volume, for example emio24-practice-data.
2. Run migrations in a disposable container with `--mount type=volume,src=emio24-practice-data,dst=/data`, using that database setting.
3. Run the app with the same mount, create a product, stop it, then start a replacement container with the same volume.
4. Query the product again and record its fields.

**Check:** the product survives container replacement. A volume mounted at a path the app never uses proves no persistence. Keep the practice volume distinct from useful data. [Volume reference](https://docs.docker.com/engine/storage/volumes/).
@@
Write a runbook that distinguishes prepared resources from downloadable names.

1. List required Docker engine, image/base artifacts, dependency files, environment variables and volume path.
2. Give exact build, migration, run, health-check and stop commands for your implementation.
3. Rehearse them from the documented starting state without relying on an unmentioned running container.
4. Explain what production still needs: proper application server, configuration, HTTPS/proxy and durable backup plan.

**Check:** another person can reproduce the local service and retained data. A command that needs an unavailable download is an offline prerequisite gap, not an offline success.
''')

pack(31, r'''
const fixes a binding; let allows that binding to be reassigned.

1. In practice.js declare shopName with const and stock with let, then increase stock from 4 to 6.
2. Print both values.
3. In a separate try/catch block attempt to reassign shopName and print the caught error's name.
4. Compare with changing a property of a const-bound product object.

**Check:** stock becomes 6; const reassignment throws TypeError; changing an object's stock property is still possible. Binding immutability is not the same as freezing the object's contents.
@@
Input text needs conversion and a business rule before arithmetic.

1. Write a helper or short routine accepting price text "200" and quantity text "3".
2. Reject empty/whitespace-only input explicitly, then convert with Number and check Number.isFinite.
3. Multiply accepted values and display the result.
4. Try "two" and empty text as invalid alternatives.

**Check:** valid inputs produce 600; invalid input produces your documented error/message, not NaN as a customer total. Number("") is zero, which is why the explicit empty-input rule is necessary.
@@
Return one label for each stock range.

1. Define stockLabel(stock), assuming nonnegative integer input.
2. Return the exact strings out for 0, low for 1 through 5, and available above 5.
3. Log calls for 0,1,5,6 and compare with the expected sequence.
4. Explain why the equality at 5 belongs to the low branch.

**Check:** logs are out, low, low, available. Do not use console.log as a substitute for returning the label: another function needs the returned string.
@@
Use objects for individual cards and an array for the shelf.

1. Create three objects with id/name/price/stock: Pen 200/10, Book 500/3 and Bag 4000/0, IDs 1/2/3.
2. Put them in products and log a snapshot using JSON.stringify.
3. Change only the second product's stock from 3 to 8, then log another snapshot.
4. Explain zero-based position 1 versus product ID 2.

**Check:** only Book's stock changes. Browser consoles may display live object references later, so stringified snapshots make the before/after evidence unambiguous.
@@
Compute a total from the supplied records, not a memorized answer.

1. Define inventoryValue(products) with an accumulator or other calculation over price times stock.
2. Use a fresh fixture with Pen stock 10, Book stock 3 and Bag stock 0; do not reuse the modified Book stock from Exercise 6.
3. Return the numeric sum and test an empty array.
4. Add a different one-item fixture to prove the calculation generalizes.

**Check:** original fixture returns 3500; [] returns 0; one Pen at 200/2 returns 400. The input array and object fields should remain unchanged.
@@
Find by the printed ID, not by array position.

1. Define findProduct(products,id), comparing each object's id with the supplied value using the intended strict numeric-ID contract.
2. Return the matching object; document missing results as undefined if using Array.find, or choose null consistently.
3. Test first, last, missing ID 99 and empty array.
4. Snapshot input before/after to verify no changes.

**Check:** IDs 1 and 3 return Pen and Bag; absent cases return the documented missing value. An ID 42 can exist in a one-item array and should still be found.
@@
Connect calculation to a real browser action.

1. Create index.html with a label-linked quantity input, Calculate button and output/status element.
2. Load practice.js and attach a click listener after the elements exist.
3. Read quantity text, validate/convert it, and calculate at fixed unit price 200.
4. Display either a total or an input error using textContent.

**Check:** quantity 3 displays 600; empty and nonnumeric values show a message rather than NaN. For direct-text invalid tests, use an input that permits typing them or dispatch a test value; document what the actual browser allowed.
''')

pack(32, r'''
Destructuring unpacks named fields without repeatedly spelling the object path.

1. Create a product with name Pen and stock 4, omitting category.
2. Destructure name, stock and a default category such as General, then log them.
3. Repeat with category Stationery already present.
4. Compare missing category with category null and explain when the default applies.

**Check:** missing/undefined category uses General; present Stationery stays Stationery; null remains null. A destructuring default is not a replacement for every false-like value.
@@
map creates one output per card; copying the object prevents changing the original card.

1. Use Pen stock 4 and Book stock 8.
2. Map to new objects that retain all fields and add displayLabel, for example `Pen (4 units)`.
3. Log original and transformed arrays using JSON.stringify.
4. Change a transformed label and inspect the original record again.

**Check:** transformed entries have correct labels and original entries have no displayLabel property. Returning the same object after adding a property mutates it even though map creates a new outer array.
@@
Chain selection and transformation to return just the names needed.

1. Implement lowStockNames(products,threshold) with filter followed by map.
2. Filter using stock <= threshold and map matching objects to name strings.
3. Test Pen stock 4, Book 8 and Bag 0 with cutoffs 4 and 0, then empty input.
4. Compare ordering with the original array.

**Check:** cutoff 4 returns ["Pen","Bag"], cutoff 0 ["Bag"], empty input []. Equality is included and the function returns names, not matching product objects.
@@
reduce combines several line values into one total.

1. Implement an inventory total using reduce with initial accumulator 0.
2. For each product add price times stock to the accumulator and return the next accumulated value from the callback.
3. Test fresh Pen 200/10, Book 500/3, Bag 4000/0 and an empty array.
4. Explain what the initial zero does when there are no items.

**Check:** results are 3500 and 0. Omitting a callback return can turn later accumulation into undefined/NaN; log a small two-item trace if your result is unexpected.
@@
Copy every level that changes, while allowing unchanged objects to be shared.

1. Start with state={products:[Pen stock4, Book stock8]} using complete product objects with IDs.
2. Create nextState with a copied outer state, a mapped products array and a copied Pen object whose stock is 7.
3. Inspect old/new stock values and reference comparisons for state, array, Pen and Book.
4. Explain why a spread of only state leaves its nested products shared.

**Check:** old Pen stays 4, new Pen is 7; outer state/array/changed Pen have new references. Sharing unchanged Book is acceptable and demonstrates a targeted immutable update.
@@
An ES module exposes named tools to another file.

1. Move inventoryValue and lowStockNames to calculations.js and export them by name.
2. Import both in main.js and log known fixture results.
3. In index.html load main.js with type="module" and serve the folder over local HTTP; alternatively configure Node's ES module mode deliberately.
4. Record your exact command/URL and any package.json module setting used.

**Check:** imported functions yield 3500 and the correct low-stock names. Opening an ES module page through file:// can introduce browser restrictions unrelated to your function logic.
@@
Optional chaining protects missing paths; nullish fallback preserves intentionally empty values.

1. Prepare products with no supplier, supplier name Acme, and supplier name an empty string.
2. Read supplier?.name with a ?? fallback such as Unknown.
3. Compare with using || for the same inputs.
4. Explain whether empty supplier text should be preserved or rejected by a separate validation rule.

**Check:** ?? yields Unknown, Acme, then empty string; || uses its fallback for the empty string too. These operators do not prove the underlying data is valid; they define access/fallback behaviour.
''')

pack(33, r'''
Promise callbacks wait until the current synchronous code finishes.

1. In practice.js log start, schedule `Promise.resolve().then(...)` to log promise, then log end.
2. Predict the order before running it in Node or the browser console.
3. Record actual output and explain the callback as a task queued after the current stack.
4. Repeat after adding another synchronous log before end.

**Check:** original order is start, end, promise. A resolved promise does not make its .then callback run inline before the following synchronous statement.
@@
Fetch data through the agreed API contract.

1. Define async loadProducts in api.js. Await fetch, reject !response.ok and await/return parsed JSON.
2. Decide whether the function returns the full page envelope or extracts results; document that choice and use it consistently in main.js.
3. Call the running local product endpoint, using an explicit URL/proxy if your static page is served on another port.
4. Display two known products, then an empty result using real fixtures or labelled mocks.

**Check:** the UI reads actual records, not undefined because it mapped the page object as an array. Record whether evidence came from a server or a mock.
@@
A loading state tells the user an operation is in progress and prevents duplicate clicks.

1. Before calling loadProducts, disable the load button and set status text to Loading.
2. On success render the products or an empty message.
3. On failure display an error; in finally restore the enabled button.
4. Use a local delayed promise so the in-progress state lasts long enough to inspect.

**Check:** delayed request shows Loading, repeated clicks are blocked while pending, and both success/failure re-enable the button. Do not clear the state only on the happy path.
@@
An HTTP error response is still a response that fetch can successfully receive.

1. Request a missing local endpoint and inspect its status.
2. In loadProducts check response.ok before accepting the body as product data.
3. Add a mock returning status 500/ok false, distinct from a rejected promise.
4. Show a useful status-based error and retain a retry/load option.

**Check:** 404 and 500 do not render error-body fields as products. A catch block alone is insufficient if you never turn an unsuccessful HTTP status into an application error.
@@
Network failure and unreadable JSON are different failure points.

1. In mocks.js create one fetch replacement rejecting with an Error and another resolving an ok response whose json() rejects.
2. Inject each into your loading path rather than changing global browser behaviour unnecessarily.
3. Run both from a clean UI state and record visible error text plus loading/button state.
4. Explain which failure occurred before a response and which while parsing one.

**Check:** both errors are handled, loading ends and retry is available. Do not claim a JSON parse failure proves the server could not be reached.
@@
Cancel a superseded search so an old delivery cannot overwrite the latest order.

1. Create an AbortController for each search and pass its signal into fetch.
2. Before starting the next search, abort the previous one.
3. Ignore AbortError as expected cancellation; still show genuine failures.
4. Use a slow query A and fast query B, requesting A then B. If a mock ignores abort, add a request-ID/active guard before committing results.

**Check:** B remains displayed after A would have finished; cancellation does not flash a server-error message. A stopped loading flag from an obsolete request must not incorrectly finish the current request's spinner.
@@
Deterministic mocks let another learner repeat the same screen states offline.

1. Create named scenarios for success with Pen/Book, empty results, delayed success, HTTP error, invalid JSON and network rejection.
2. Keep their response shape consistent with the real API contract, including ok/status/json where your loader expects them.
3. Provide a local selector or documented function call to choose each scenario.
4. Record each expected/actual UI state in answers.md.

**Check:** every scenario can be repeated without internet and is explicitly labelled simulated. Mock success proves client behaviour against the mock, not correctness of the Django endpoint.
''')

pack(34, r'''
Establish a running React page before adding product components.

1. Use the prepared frontend/ project, or scaffold the React template while online and install its dependencies.
2. Record node --version and the React/build-tool versions from the installed dependency tree.
3. Run npm run dev inside frontend/ and open the exact printed URL.
4. Replace the starting heading with EMIO24 and verify the browser updates.

**Check:** the page is served by your local project and compilation succeeds. JSX needs the React build pipeline; pasting it into a plain browser console is not a component setup test.
@@
A card receives its information through props rather than hard-coded product text.

1. Create ProductCard.jsx exporting ProductCard({product}).
2. Return semantic article content with a heading for name and text for whole-naira price and stock.
3. Import it in App.jsx and render Pen 200/4 and Book 500/8 from different product props.
4. Change only Book's fixture stock to 9 and observe the cards.

**Check:** the cards differ according to props, and only Book's displayed stock changes. Do not mutate the supplied product inside rendering.
@@
Map product records to repeated components with stable identity.

1. Create ProductList receiving a products prop.
2. Use map to return ProductCard for each object, placing key={product.id} on the repeated element.
3. Render IDs 1/2/3, then reorder them and add a new unique ID.
4. Inspect the browser console and displayed order.

**Check:** one correct card per record, correct order and no missing-key warning. Array position is not a stable product identity when records can be reordered or inserted.
@@
An empty shelf needs a deliberate message instead of a confusing blank area.

1. In ProductList check whether products.length is zero.
2. Render a clear message such as No products yet for empty input; otherwise render the cards.
3. In App test [] and then a one-product array by changing the supplied fixture.
4. Ensure the page heading remains available in both states.

**Check:** empty state contains no fake product card; populated state has no stale empty message. Undefined data is a separate loading/interface issue; this component's input contract is an array.
@@
Compose the screen from parts with clear responsibilities.

1. Create Header and Footer components and import them into App alongside ProductList.
2. Keep fixture product ownership in App and pass products down.
3. Draw App → Header/ProductList/Footer, with ProductList → ProductCard, in answers.md.
4. Change the shop heading through the chosen Header prop and show all products still render.

**Check:** components are used as components, not pasted duplicate markup. The tree identifies who owns data and who displays it; no network request is required in this lesson.
@@
Render stock messages at the exact decision boundaries.

1. Add conditional text in ProductCard: Out of stock at 0, Low stock from 1 through 5, and your ordinary availability presentation above 5.
2. Render four cards with stocks 0,1,5,6.
3. Inspect visible text and DOM for accidental numeric zero output from an expression such as stock && something.
4. Use explicit Boolean comparisons or conditional branches where needed.

**Check:** each boundary gets the intended message and no stray 0 appears as a condition's rendered result. Keep the actual stock count visible too if it is part of your card design.
@@
A child reports an event; the parent decides what it means.

1. Add an onSelect callback prop and a labelled button to ProductCard.
2. When clicked, call onSelect with that product's ID.
3. In App provide a handler that logs or displays the selected ID without modifying the product object in the child.
4. Click Pen then Book.

**Check:** callbacks receive 1 then 2 with the fixture IDs, and product fields remain unchanged. Passing a function to onClick is different from calling it while the component renders.
''')

pack(35, r'''
Functional state updates receive the queued previous value.

1. Implement Counter with useState(0) and a click handler calling setCount(c=>c+1) twice.
2. Render count in the button and click once, then twice.
3. In a separate comparison version use two setCount(count+1) calls and repeat from zero.
4. Explain each handler's render snapshot and queued updates.

**Check:** functional version goes 0→2→4; the two snapshot-based updates in one handler add only 1 per click. Do not interpret the setter as immediately rewriting the local count variable.
@@
Keep an input editable before interpreting its contents as a number.

1. Use string state for the quantity field's value and update it in onChange.
2. On submit reject blank text, non-finite conversions and nonpositive/non-integer quantities.
3. Display accepted integer quantity or a useful error without losing the typed value.
4. Try empty text, 3, 0 and 2.5.

**Check:** 3 is accepted; other listed values reject. Clearing the input must leave it empty while editing, not force zero back into the field on every keystroke.
@@
A controlled product form owns its draft until the parent accepts submission.

1. Create ProductForm with name, price and stock string state plus labelled inputs.
2. On submit prevent default browser navigation, strip/check name and convert nonnegative integer price/stock.
3. If valid, call onAdd with a normalized product draft; let the parent allocate an ID.
4. Try Pen/200/4, blank name, negative price and fractional stock.

**Check:** only the valid draft reaches the callback. Invalid fields show readable errors and retain their entered values. Browser restrictions supplement these checks rather than replacing them.
@@
Update state through new containers so React can track the change.

1. In App hold the products array in state.
2. Add a draft using a new array and a stable new ID, with a functional setter if the update depends on prior state.
3. Update one product's stock using map and a copied object for that product.
4. Save before/after snapshots and display the list after both actions.

**Check:** adding increases length by one; editing changes only the targeted stock. Do not push into the existing state array or modify a referenced product and then reuse the same array.
@@
Two displays of the same inventory should read one owned state value.

1. Move products state into the nearest parent shared by ProductList and InventorySummary.
2. Pass the records down and supply the form with the parent's add callback.
3. Add a product through the form and inspect both list and summary.
4. Draw the data-down/events-up flow in answers.md.

**Check:** both displays update together without maintaining separate product arrays. Lifting state means moving ownership, not copying the current state into another component once.
@@
A summary derived from products does not need a second synchronized notebook.

1. In InventorySummary calculate the sum of price*stock from props during rendering.
2. Use Pen 200/10 and Book 500/3 to expect 3500.
3. Update Book stock to 4 through the parent's state update and observe the summary.
4. Compare with an empty array and explain why a separate total state/effect is unnecessary here.

**Check:** totals are 3500, then 4000, and 0 for empty input. Derive from the current props instead of storing an old total that must be kept in sync manually.
@@
Reset a completed draft, but keep a rejected draft available to repair.

1. After a valid local onAdd completion, clear the form's input/error state.
2. After validation failure, preserve all draft fields and display the relevant error.
3. Submit valid Pen, then an invalid Book with negative stock, correct only its stock and resubmit.
4. Use keyboard tab/submit actions and confirm labels identify inputs.

**Check:** successful additions reset once; failed attempts retain data; correction adds only the intended record. Network-success handling is a later concern; this exercise's callback is a local operation.
''')

pack(36, r'''
An Effect starts synchronization after React renders the page.

1. Create ProductPage with data, loading and error state, and an Effect that requests the local product endpoint.
2. Check response.ok, parse JSON and extract results according to the documented page contract.
3. Render loading before completion and the product list after success.
4. Use a known Pen/Book response and inspect Network or a clearly labelled local mock log.

**Check:** the list appears from received data rather than a hard-coded success screen. Do not call fetch directly on every render, because state updates would keep starting new requests.
@@
A request has more than two useful display states.

1. Define visible loading, populated success, empty success and error branches.
2. Prepare deterministic responses for two products, zero products, a delayed response and a rejection.
3. Run each case from a clean state and record what is visible while pending and after settlement.
4. Decide explicitly whether old data stays visible during a refresh.

**Check:** empty data is not shown as a network failure, and an error does not leave a permanent spinner. Your screen policy handles transitions as well as the initial page load.
@@
Changing a request input should start the corresponding new synchronization.

1. Add a search/category input and derive the request URL from its current value.
2. Include the reactive values read by the Effect in its dependency list, keeping the request logic consistent with them.
3. Search for Pen, then Book using distinguishable mock/server results.
4. Inspect requests and explain why an empty dependency array would miss later changes.

**Check:** each changed input produces its intended data. Do not suppress a dependency warning without understanding which changing value the Effect reads.
@@
Cleanup stops work belonging to a screen that has gone away.

1. Create an AbortController inside the Effect and pass its signal to fetch.
2. Return a cleanup function that aborts it; ignore AbortError while displaying real errors.
3. Start a delayed request, then hide/unmount ProductPage through a parent toggle before it finishes.
4. Reopen the page and confirm a fresh request works.

**Check:** the old request is cancelled or guarded from applying results after cleanup. In development Strict Mode, an extra setup/cleanup cycle is expected; code must tolerate it rather than disabling the check as a fix.
@@
The last response to arrive is not necessarily the latest requested search.

1. Configure query A to finish after query B, then trigger A followed quickly by B.
2. Use cancellation plus an active/request-identity guard where necessary before setting data, error or loading state.
3. Observe B's completed result, then let A's delay expire.
4. Repeat with a mock that cannot actually cancel transport, to test the guard itself.

**Check:** A never replaces B and does not clear B's pending spinner early. Guarding only setData while obsolete catch/finally handlers still change state can leave another race.
@@
Retry should create a new attempt with understandable state transitions.

1. Display a Retry button in the error branch.
2. Implement a retry counter/dependency or explicit reusable request trigger, keeping cancellation protection.
3. Configure the first attempt to fail and the next to return products.
4. Click Retry and record error → loading → success without reloading the entire browser page.

**Check:** the old error clears at the intended point, one current attempt controls the UI and repeated clicks follow your documented disabled/loading policy. Retry must not reuse an already aborted controller.
@@
Use Effects for outside synchronization, not every calculation from existing data.

1. Find a filtered list or inventory total that depends only on current products and local filter state.
2. Calculate it during rendering instead of storing it through a second Effect.
3. Change a product quantity and the filter; compare results with manual expectations.
4. Explain which Effect remains necessary for network synchronization and why the derived calculation is different.

**Check:** derived display follows current inputs without an extra stale intermediate state. This does not prohibit measured memoization later; the goal is removing unnecessary duplicated state.
''')

pack(37, r'''
The router needs one browser-location provider around its route tree.

1. Install/use a compatible React Router package and record the version and import package you use.
2. In main.jsx wrap App with BrowserRouter; do not nest another BrowserRouter accidentally inside App.
3. Add a simple products route and verify it renders at /products.
4. Record start command and local URL.

**Check:** navigation components receive router context and the console has no missing-router error. Match imports to the installed version. [Declarative setup reference](https://reactrouter.com/start/declarative/installation).
@@
A route parameter is URL text identifying the requested product.

1. Add routes for /products and /products/:id with separate list/detail page components.
2. In the detail page use useParams, then validate/convert the ID to match your numeric fixture/API convention.
3. Load/display Pen for its known ID and show a useful missing-product state for an absent ID.
4. Distinguish a request still loading from a completed lookup with no match.

**Check:** known detail shows the correct product; an unknown ID does not leave an endless spinner. The parameter is initially a string, so strict comparison with numeric IDs needs an intentional conversion.
@@
Router links update browser location while keeping navigation history coherent.

1. Make product cards link to their detail URLs using Link or the installed router's equivalent.
2. Navigate list → Pen detail → list → Book detail.
3. Use browser Back and Forward and record location and displayed page at each step.
4. Inspect whether your chosen link caused an unnecessary full page reload.

**Check:** history restores the matching UI for each URL. A button that changes visible content without updating location does not satisfy route navigation in this task.
@@
Unknown UI paths need a clear destination of their own.

1. Add a wildcard route displaying NotFoundPage with a heading and a products link.
2. Visit /unknown directly through the local app and use its return link.
3. Compare this page with a known detail route whose product ID does not exist.
4. Explain browser-rendered fallback content versus an API's HTTP 404 response.

**Check:** both cases are understandable but represent different failures: unmatched UI route versus matched route with missing data. A client-side NotFound screen does not automatically change the document server's HTTP status.
@@
A URL can carry enough state to reproduce a filtered catalogue.

1. Store the name filter in a query parameter, such as q, using useSearchParams or equivalent.
2. Initialize the displayed filter from the URL and update it when the user searches.
3. Search for Pen, copy the complete URL and open it in another tab.
4. Use Back/Forward to check your chosen history policy.

**Check:** the second tab restores the same filter and matching products. Keep unrelated query parameters where appropriate and avoid an update loop between local state and URL state.
@@
A client route guard helps navigation, while the API remains the access authority.

1. Guard the dashboard using the app's session state and redirect signed-out visitors to login.
2. Preserve a safe internal intended destination and navigate there after successful login.
3. Sign out and revisit the dashboard directly.
4. Separately call the protected API without credentials and record its rejection.

**Check:** the UI follows the login flow and the server denies unauthorized requests independently. Do not accept an arbitrary external redirect target from user input or treat hidden routes as security enforcement.
@@
Deep-link refresh asks the web server for the URL before React can route it.

1. Open a detail URL directly in a new tab and refresh it.
2. Test both the development server and your documented production-like static serving arrangement when available.
3. Configure app-entry fallback for client routes while preserving real static assets and /api/ handling.
4. Request an API URL and a missing static asset to inspect what they actually receive.

**Check:** detail refresh loads the app, API requests still receive API responses and missing assets are not silently returned as index.html. Record untested production configuration as a limitation rather than a verified deployment.
''')

pack(38, r'''
Map responsibilities before moving code between files.

1. Draw the current pages, display components, state owners and fetch calls in architecture.md.
2. Mark duplicate status handling, response parsing and duplicated copies of product state.
3. Propose specific destinations: api module for transport, custom Hook for request state, components for display.
4. Record one working list/detail/add/edit journey as the pre-change baseline.

**Check:** each proposed move addresses an identified responsibility. A folder named services is not architectural evidence unless you explain which behaviour belongs there and why.
@@
Give callers one consistent interface to product requests.

1. In src/api/products.js implement list/get/create/update functions with documented arguments and returned values.
2. Check response.ok and parse the expected body; handle an empty response only for operations that actually use one.
3. For list, extract results from the paginated envelope. Preserve status/field errors in a useful error representation.
4. Run one success and one failure through each relevant function using local API or labelled mocks.

**Check:** callers no longer duplicate envelope parsing. Do not discard field-level 400 errors into an uninformative success-shaped empty object.
@@
A custom Hook packages request state and lifecycle behaviour for reuse.

1. Create useProducts with data/loading/error plus a retry interface matching your page's needs.
2. Move request/cancellation logic from the page into the Hook; keep dependencies and stale-response protection.
3. Render two test consumers, each using the same documented return shape.
4. Demonstrate delayed success, error and retry.

**Check:** both consumers can use the Hook contract. Two Hook calls normally have independent state; extracting a Hook does not automatically create one shared global cache or prevent duplicate network calls.
@@
A display component should be usable with supplied data alone.

1. Refactor ProductList to receive products and event callbacks as props, without fetching internally.
2. Render it in a simple fixture page with [], then Pen/Book records.
3. Supply a selection callback and verify the selected ID.
4. Keep request-state presentation in the containing page/Hook boundary as you designed it.

**Check:** the list works with no live API and no hidden dependency on global session data. This fixture demonstrates display behaviour; it does not certify backend integration.
@@
Share state only as widely as its consumers require.

1. Put session identity/login/logout information in a SessionContext provider above the relevant pages.
2. Read it in navigation and protected-page UI.
3. Keep one product form's unsaved draft in that form rather than global Context.
4. Draw consumers and explain where each value is authoritative.

**Check:** login updates session consumers while editing a form does not overwrite global product/session data. Context distributes a value; it does not replace server-side authentication or authorization.
@@
Central error presentation should preserve the distinction between retryable failure and field correction.

1. Create ErrorMessage accepting a user-facing message and optional retry callback.
2. Show it for a simulated network failure and verify retry is actionable.
3. For a 400 form response, keep field-specific messages beside the relevant fields instead of hiding them all in a generic banner.
4. Test keyboard access and error visibility.

**Check:** users can retry a request failure and correct a stock error without losing draft inputs. Avoid showing raw server stack traces as the shared component's message.
@@
Refactoring should retain behaviour, not merely compile with a new directory tree.

1. Repeat the baseline list/detail/add/edit journey after the moves.
2. Compare request URLs, request bodies, status handling and persisted values.
3. Repeat a permission denial and the slow-A/fast-B stale-response check.
4. Record any intended change explicitly and fix unintended differences.

**Check:** the same contracts still work and old responses cannot overwrite new intent. A successful build cannot replace these behavioural checks because the compiler does not know your business rules.
''')

pack(39, r'''
Reconcile actual client/server behaviour before joining more features.

1. Inspect one real product-list response and a create request from the running API/client.
2. Compare paths, trailing slashes, authentication, field names, numeric types, pagination and status codes with api-contract.md.
3. Correct mismatches in the contract and implementation together.
4. If none exists, deliberately test a mismatched mock in a disposable client check and show the detected failure; do not invent a past bug.

**Check:** both sides agree on results versus raw arrays and ID/value types. Save a redacted actual request/response pair, not only an aspirational specification.
@@
Use the chosen authentication mechanism consistently end to end.

1. Connect login UI to the existing session or token endpoint and centralize authenticated requests in the API client.
2. Include the required cookie/CSRF handling for session requests or Bearer token for token requests.
3. Test wrong credentials, correct login, protected access and logout.
4. Record screen states/statuses with secrets redacted.

**Check:** signed-out access is rejected, login enables only authorized requests and logout follows the documented expiry/revocation policy. A frontend Boolean named loggedIn is not proof the server authenticated the call.
@@
Render the current user's permitted inventory, not a shared fixture.

1. Create two disposable users with distinct product names/IDs.
2. Log in as A and load the real product list; then log out and log in as B.
3. Clear or replace cached user-specific data when the identity changes.
4. Inspect the response and screen for the other user's records.

**Check:** each identity sees only its owned/permitted data, including after switching accounts in one browser session. Hiding another user's cards after receiving their data is not sufficient isolation.
@@
Submit drafts to the server and display its confirmed outcome.

1. Connect ProductForm create/edit callbacks to the API client, disabling duplicate submission while pending.
2. On success use returned data or refetch and verify the change survives a full reload.
3. On field-validation errors retain the draft and display the server's field messages.
4. Test Pen/200/4 creation, a stock edit and a rejected negative-stock submission.

**Check:** accepted data persists; rejected data does not create or change rows. Client validation improves feedback but must not suppress or misinterpret the server's validation result.
@@
A confirmed sale requires an atomic stock change on the server.

1. Add a sales endpoint accepting product_id and positive integer quantity; scope the product to the caller.
2. Within a transaction validate/deduct stock with an appropriate conditional update or backend-supported locking rule, then record historical quantity/unit price.
3. Connect a sale form and show success only after the server confirms it.
4. From fresh stock 10/price 500 sell 3, reload, then independently try quantity 11 from stock 10.

**Check:** success total 1500/stock 7 persists; oversale creates no sale and leaves 10. A disabled browser button does not enforce concurrency correctness.
@@
A lost reply can leave the client uncertain even when the server committed the sale.

1. Test a rejected oversale and show field/business feedback without a success receipt.
2. Simulate a request failure before sending, then a lost response after a simulated or real committed operation; label simulations.
3. Explain how the UI refreshes/reconciles uncertain state before retrying, or use a server-validated idempotency key that returns the same recorded result for a repeated request.
4. Test the chosen retry policy twice against the same intended sale.

**Check:** stock is not deducted twice for one retried operation under your claimed policy. Do not blindly restore an old optimistic stock value when the server may already have committed.
@@
Rehearse the complete user journey from an empty business account.

1. In demo.md record create/register user → login → add Notebook 500/10 → sell 3 → reload → logout.
2. Include actual API statuses, assigned IDs and confirmed stock 7/total 1500 without credentials.
3. Attempt direct access to another user's known record and record denial plus unchanged data.
4. List outstanding limitations discovered during the journey with reproducible steps.

**Check:** every screen action corresponds to a verified server/database outcome. A collection of separate mocked components is not evidence of this real full-stack journey.
''')

pack(40, r'''
Describe the system someone would operate, including where durable state lives.

1. Draw browser, static assets, reverse proxy, Django application server, database and persistent storage.
2. Label protocols and routing for document requests, assets and /api/ calls.
3. Mark trust boundaries and where secrets/configuration enter.
4. Trace one sale and identify authoritative stock and backup scope.

**Check:** each box maps to a component used in your local rehearsal. Do not draw a managed database or HTTPS service you have not selected; label planned components separately from tested ones.
@@
Release configuration must be explicit and reproducible without copying secret values into notes.

1. Document environment variable names, dependency versions, DEBUG=False, allowed hosts and HTTPS/cookie assumptions.
2. Run `python manage.py check --deploy` with the rehearsal settings, not accidentally the development settings.
3. Record every unresolved finding and the change needed, distinguishing local-HTTP constraints from production requirements.
4. Check that missing required configuration fails clearly.

**Check:** the notes name actual settings and unresolved risks. Zero command exit status alone is not proof that an app is fully production-ready, backed up or reachable through the intended proxy.
@@
Rehearse a built release rather than relying on development hot reload.

1. Build the frontend with npm run build and serve its generated assets through your chosen static/proxy arrangement.
2. Run Django with an appropriate production application server compatible with your environment, recording its exact command/version. For example use a Windows-compatible WSGI server or a Linux container setup rather than assuming every server runs natively on Windows.
3. Request a document, static asset and API health route.
4. Record routing and statuses.

**Check:** the built frontend and production-server process actually run. Vite's development server plus Django runserver does not satisfy this release rehearsal.
@@
A backup is only a recovery plan after restoration has been tested.

1. Use a disposable populated database and record product/sale counts.
2. Take a consistent backup using the database's supported method; stop writes or use its online-backup facility rather than blindly copying a live database file.
3. Apply pending migrations in the rehearsal, then restore the backup into a separate disposable database with compatible schema/code.
4. Query counts and sample receipt totals after restoration.

**Check:** restored data matches recorded facts. Explain which migrations are reversible and why rolling code back does not automatically reverse a destructive data migration.
@@
Check a release as a user and as an operator.

1. In release-checks.md make rows for health, login, list/create/edit/delete, valid sale, oversale rejection, cross-owner denial and frontend deep-link refresh.
2. For each row state starting data, action, expected status/screen/database effect and actual result.
3. Run the journey against the built rehearsal, not an unrelated development instance.
4. Record failures and repeat only after the relevant fix.

**Check:** sale stock persists across refresh/restart and unauthorized access remains denied. A working health endpoint alone does not certify the other rows.
@@
Write recovery instructions another operator can follow under pressure.

1. In operations.md give exact startup/shutdown commands, configuration locations, log access and health checks.
2. Document migration/backup order, failed-release recovery and responsibility for rotating secrets.
3. Simulate one local failure, such as stopping the app service, and follow your own recovery instructions.
4. Record symptoms, commands, recovery verification and any runbook correction.

**Check:** the procedure restores the intended service and confirms data. A proposed rollback that has never been tried must be labelled untested rather than presented as a demonstrated recovery.
@@
Explain your implementation using evidence rather than memorized definitions.

1. In interview.md answer six prompts: trace a sale end to end; prevent overselling; explain ORM query timing; distinguish authentication/authorization; explain React state/effects; describe your hardest reproduced bug.
2. For each answer cite your own file/function or observed test, then state one tradeoff and one improvement.
3. Speak the answers aloud or rehearse with a partner; record which explanation was unclear and revise it.
4. Keep credentials and private data out of examples.

**Check:** all six answers connect concepts to your actual app. An analogy helps explain the mechanism but must not replace the technical rule or claim unimplemented behaviour.
''')

# Topic-specific direction for the independent verification exercise.
REVIEW_FOCUS = {
4: 'Choose one object calculation and one rejected stock change. Use a new product/price/quantity, and inspect stock before and after rejection.',
5: 'Choose one property/factory operation and one identity or shared-state case. Use new objects so prior edits cannot influence your conclusion.',
6: 'Choose one payment implementation and one checkout failure. Inspect both the fake call list and product stock, not just receipt text.',
7: 'Choose one reusable calculation and one import/path case. Run from a different working directory and explain which path or namespace is being resolved.',
8: 'Choose one successful environment recreation/import and one missing-dependency or interpreter-selection scenario. Preserve actual interpreter paths in your evidence.',
9: 'Choose one local history operation and one conflicting/unstaged-change case. Compare file contents, staged contents and commits rather than relying only on a clean-status message.',
10: 'Choose one page request and one missing-resource/connection case. Identify whether a server returned an HTTP response at all.',
11: 'Choose one successful operation and one request-error scenario. Write the complete method/path/status/body consequences and explain which component handles the failure.',
12: 'Choose a new resource/page scenario and an invalid request. Trace pagination or validation using your contract, including whether stored data would change.',
13: 'Choose a new valid row/query and an empty-selection or punctuation-containing value. Show actual returned rows and the committed data afterward.',
14: 'Choose a new related sale and an unsold/orphan case. Explain how join choice and foreign-key enforcement affect the observed result.',
15: 'Choose a new committed sale and a deliberately failed transaction. Query both stock and sale lines afterward to demonstrate atomicity.',
16: 'Choose a new valid route and a missing-route or missing-template case. Explain the exact stage reached before the failure.',
17: 'Choose a new record after migration and a rebuild/schema-change case. Show the database path and migration state so existing data is not mistaken for reconstructed schema.',
18: 'Choose a new ORM filter/projection and an empty or stale-instance case. Record types, ordering and when database evaluation happens.',
19: 'Choose a new accepted CRUD operation and an invalid/missing-record request. Check HTTP behaviour and row/field changes together.',
20: 'Choose a new accepted form value and a cross-field or conversion failure. Show raw input, cleaned values/errors and unchanged data after rejection.',
21: 'Choose a successful session/permission action and a denied direct request. Distinguish password verification from role authorization.',
22: 'Choose a new valid serialization/save case and a rejected writable-field case. Compare serializer output, errors and row count.',
23: 'Choose a new API success and a parser/method/validation failure. Keep their status meanings distinct and inspect persistent side effects.',
24: 'Choose a new page/action request and an invalid parameter or missing-detail case. Preserve ordering, envelope shape and permission policy.',
25: 'Choose a new valid token lifecycle step and an expiry/invalid-credential scenario. Do not copy token values into evidence; identify the verification rule tested.',
26: 'Choose a permitted owner action and a cross-owner or spoofed-owner attempt. Check both response visibility and persisted ownership/stock.',
27: 'Choose a working protected input path and a rejected/escaped malicious-looking input against your own local app. Explain the exact defence, not just the word secure.',
28: 'Choose two new test cases, one valid and one failure/boundary. Temporarily perturb relevant code in a disposable copy to explain what at least one assertion would detect.',
29: 'Choose a new measured query/cache success and a stale/cross-owner cache case. Compare correctness before making a performance claim.',
30: 'Choose a successful container/configuration operation and a missing-resource or replacement-container case. Identify the actual data mount and image used.',
31: 'Choose a new accepted JavaScript calculation and an invalid input/type case. Record returned values separately from console output and object mutation.',
32: 'Choose a new transformation and an empty/nested-copy case. Snapshot original and new values so shared references cannot hide a mutation.',
33: 'Choose a successful async request and an out-of-order or failed response. Document timing, mock/server source and final UI state.',
34: 'Choose a new product-prop combination and an empty/reordered/boundary display case. Inspect rendered text, keys and callback arguments.',
35: 'Choose a new valid state/form update and a rejected draft or queued-update case. Record input retention and the list/summary values.',
36: 'Choose a successful resynchronization and an obsolete-response/unmount case. Record which request is permitted to change data, errors and loading.',
37: 'Choose a new valid direct URL and an unknown/unauthenticated navigation case. Check browser location, displayed page and independent API authorization.',
38: 'Choose a new flow through an extracted module and an error/stale-response case. Compare the observable contract before and after refactoring.',
39: 'Choose a new real persisted flow and a denied/uncertain sale case. Trace browser, API and database evidence, explicitly labelling any simulation.',
40: 'Choose a new release operation and a failure/recovery scenario. Verify the running version, restored data and actual request results instead of merely reviewing configuration.'
}

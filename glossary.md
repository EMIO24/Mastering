# Computer science vocabulary through analogies

Read the precise meaning alongside the analogy. An analogy explains one aspect; it does not replace the technical rule. Each later lesson defines five topic-specific terms as well.

| Term | Plain-language meaning | Everyday analogy and limit |
| --- | --- | --- |
| Computer science | Study of computation, information and computational problem solving | Studying how recipes can be designed and what they can accomplish; it includes theory, not only operating machines. |
| Algorithm | Specified steps for solving a class of problems | A recipe with explicit rules; computers cannot infer omitted intentions. |
| Program | Instructions written for execution | A written machine recipe. |
| Syntax | Rules of valid language structure | Grammar on an order form; grammatical instructions can still be wrong. |
| Semantics | The meaning or behaviour of language constructs | What the order asks the clerk to do. |
| Variable | A named reference/binding used to access a value | A shelf label; Python names refer to objects instead of containing copied objects. |
| Data type | A classification determining values and operations | A kind of container with handling rules; text digits and numeric values differ. |
| String | A sequence of text characters | A line of writing; "500" remains text until converted. |
| Integer | A whole-number value | Counting complete stock units. |
| Float | A floating-point approximation of a number | A measuring scale with limited precision; many decimal fractions are not exact. |
| Boolean | True or False | A yes/no switch; nonempty text "False" is still truthy in Python. |
| None | Python's value representing absence | An explicit missing-entry marker; not zero or an empty string. |
| Operator | An operation such as addition or comparison | A tool acting on values; its behaviour may depend on type. |
| Condition | An expression interpreted as true/false for a decision | A shop's eligibility rule. |
| Loop | Repeated execution over data or while a condition holds | Visiting each card or serving until closing; the stopping rule matters. |
| Function | A callable unit accepting inputs and optionally returning a result | A service counter that hands back a result. |
| Parameter | An input name in a function definition | A blank field on the service form. |
| Argument | A value supplied in a call | The actual entry in the field. |
| Return value | The result sent back to the caller | A completed form handed back; printing for a person is a different action. |
| Scope | The context in which a name is resolved | Labels visible inside a room; exact rules depend on the language. |
| List | An ordered mutable sequence | An editable shopping list allowing duplicates. |
| Dictionary | A mapping from unique keys to values | A card with labelled fields; missing keys are not automatically blank. |
| Tuple | An immutable sequence | A fixed coordinate pair; a mutable object inside can still change. |
| Set | A collection of unique elements | A membership register without duplicates; display order is not a contract. |
| Class | A definition used to create objects with related data and behaviour | A blank stock-card design from which individual cards can be made. |
| Instance (object) | One particular object created from a class | One filled stock card; separate cards can hold different stock counts. |
| Constructor | The mechanism used to create and initialize an object; in Python you normally call the class, such as Product("Pen", 4) | Ordering a new stock card: obtain a blank card, then fill its starting fields. |
| __new__ | Python's special method that creates and returns an instance | Making the blank card. Most beginner classes use the inherited implementation. |
| __init__ (initializer) | Python's special method that initializes an already created instance; it must return None | Filling in the new card's name and starting stock. Often called a constructor informally, but it does not create the instance itself. |
| Mutable | Able to change after creation | An editable card; other references see its changes. |
| Identity | Whether references identify the same object | Two directions to the same card, rather than two identical-looking cards. |
| State | Information describing a system at a moment | The current stock ledger; copies can become stale. |
| Input | Data supplied to a computation | Details handed to the clerk. |
| Output | Data produced by computation | Results returned, displayed or saved by the clerk. |
| Exception | A signal interrupting normal execution for an exceptional condition | An obstacle that changes the route and needs an appropriate handler. |
| ValueError | An exception for an inappropriate value of an otherwise acceptable kind | The form is readable but its value is unsuitable. |
| KeyError | An exception for a missing mapping key | Requesting a label that is absent from the card. |
| FileNotFoundError | An exception for a requested file/path that does not exist | Asking for a ledger that has not been filed. |
| OSError | An exception family for operating-system operation failures | The file-room service cannot carry out the request. |
| Traceback | The call-chain report leading to an exception | The route map showing where the journey failed. |
| Debugging | Finding and correcting defects | Investigating why ledger totals disagree rather than hiding them. |
| Validation | Checking values against required rules | The receiving clerk inspects forms before accepting them. |
| Mutation | Changing an existing object | Editing the same card rather than issuing a different card. |
| Memory | Storage used by a running computation | The working desk; ordinary objects vanish when the process ends. |
| Persistence | Retaining data beyond a process lifetime | Filing the ledger on disk; a variable alone is not storage across restarts. |
| File path | A location identifying a filesystem file | Directions to a cabinet; relative directions need a starting point. |
| Serialization | Converting data to a storable/transmittable representation | Packing cards for transport in an agreed format. |
| Parsing | Interpreting structured text according to its format | Unpacking the form; readable structure may still violate business rules. |
| JSON | A text format for objects, arrays, strings, numbers, Booleans and null | A standardized transport form; arbitrary Python objects do not all fit. |
| CSV | A row/field text format with quoting rules | A portable ledger sheet; commas inside names require quoting. |
| Context manager | An object managing setup/cleanup around a with block | Borrowing a tool with a guaranteed ordinary return procedure; not a guarantee against a machine crash. |
| CLI | A command-line interface | A text service counter instead of graphical buttons. |
| Process | A running program instance with operating-system resources | One active workshop; starting twice produces separate workers and state. |
| Interface | A defined interaction contract | Published counter rules; implementations can differ. |
| Dependency | A required software component | A needed tool; writing its name does not install it. |
| Transaction | Database work committed or rolled back together | A sealed ledger-update bundle; external payments do not automatically roll back with it. |
| Concurrency | Activities progressing over overlapping periods | Several clerks processing orders, even without simultaneous CPU execution. |
| Race condition | Behaviour depending on competing operation timing | Two clerks selling the final unit from an outdated count. |
| Complexity | How resource needs grow with input size | How more cards increase the work; not a single stopwatch measurement. |
| Test | A repeatable comparison of expected and actual behaviour | A quality inspection; passing selected samples does not prove every case. |
| Regression | Previously working behaviour broken by a later change | A counter malfunctioning after a renovation. |

Practise by inventing a second analogy for three terms and naming one case where each analogy stops fitting.

# 06 — Behavioral Patterns

> Behavioral patterns are about **how objects interact and distribute
> responsibility** — the flow of communication and control between objects.

The ten GoF behavioral patterns covered here:

| Pattern | One-line intent |
|---------|-----------------|
| Strategy | Swap **interchangeable algorithms** at runtime |
| Observer | **Notify many objects** when one changes (pub/sub) |
| State | Change behavior when **internal state** changes |
| Command | Encapsulate a **request as an object** (undo, queue) |
| Iterator | Traverse a collection **without exposing internals** |
| Template Method | Fixed **algorithm skeleton**, customizable steps |
| Visitor | Add **new operations** without changing the classes |
| Mediator | **Centralize** complex object-to-object communication |
| Memento | Capture & **restore state** without breaking encapsulation |
| Chain of Responsibility | Pass a request along **a chain of handlers** |

---

## 1. Strategy ⭐ (most important)

**Intent:** define a family of interchangeable algorithms, encapsulate each, and
make them swappable at runtime. This is composition-over-inheritance + OCP in one.

**Use when:** you have multiple ways to do one thing — payment methods, sorting,
pricing, compression, routing.

```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None: ...

class CreditCard(PaymentStrategy):
    def pay(self, amount): print(f"Paid {amount} by credit card")

class UPI(PaymentStrategy):
    def pay(self, amount): print(f"Paid {amount} by UPI")

class Checkout:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy            # holds a strategy
    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy            # swap at runtime
    def checkout(self, amount: float):
        self._strategy.pay(amount)

cart = Checkout(UPI())
cart.checkout(500)
cart.set_strategy(CreditCard())      # switch algorithm without touching Checkout
cart.checkout(500)
```

**Signals to use Strategy:** you're writing an `if/elif` on a "type" to pick
behavior → replace it with strategies. **Strategy vs State:** structurally
similar, but Strategy's variants are independent algorithms chosen by the client;
State's variants represent lifecycle states that transition into each other.

---

## 2. Observer ⭐

**Intent:** define a one-to-many dependency so that when one object (subject)
changes state, all its dependents (observers) are notified automatically.

**Use when:** event systems, pub/sub, UI data binding, notifications.

```python
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float) -> None: ...

class Subject:
    def __init__(self):
        self._observers: list[Observer] = []
        self._temp = 0.0
    def subscribe(self, o: Observer):   self._observers.append(o)
    def unsubscribe(self, o: Observer): self._observers.remove(o)
    def set_temperature(self, t: float):
        self._temp = t
        self._notify()                       # push change to all observers
    def _notify(self):
        for o in self._observers:
            o.update(self._temp)

class PhoneDisplay(Observer):
    def update(self, temperature): print(f"Phone: {temperature}°C")

class WindowDisplay(Observer):
    def update(self, temperature): print(f"Window: {temperature}°C")

station = Subject()
station.subscribe(PhoneDisplay())
station.subscribe(WindowDisplay())
station.set_temperature(25.0)     # both displays update automatically
```

**Push vs pull:** push sends the data in `update(data)`; pull sends just a
notification and observers query the subject for what they need. **Watch for:**
memory leaks from un-removed observers; notification order shouldn't be relied on.

---

## 3. State ⭐

**Intent:** allow an object to alter its behavior when its internal state
changes — it appears to change class. Replaces sprawling state `if/elif` logic
with state objects.

**Use when:** anything with a lifecycle — order status, vending machine, traffic
light, document workflow, game states.

```python
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def next(self, machine: "VendingMachine") -> None: ...

class Idle(State):
    def next(self, machine):
        print("Coin inserted -> Dispensing")
        machine.state = Dispensing()

class Dispensing(State):
    def next(self, machine):
        print("Item dispensed -> Idle")
        machine.state = Idle()

class VendingMachine:
    def __init__(self):
        self.state: State = Idle()     # current state object
    def press(self):
        self.state.next(self)          # behavior delegated to the state

m = VendingMachine()
m.press()   # Idle -> Dispensing
m.press()   # Dispensing -> Idle
```

Each state class owns its behavior **and** decides the next state. Adding a state
= adding a class (OCP), no giant conditional to edit.

---

## 4. Command

**Intent:** encapsulate a request as an object, letting you parameterize,
queue, log, and **undo** operations.

**Use when:** undo/redo, task queues, macro recording, transactional operations,
GUI actions/buttons.

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...
    @abstractmethod
    def undo(self) -> None: ...

class Light:
    def on(self):  print("Light ON")
    def off(self): print("Light OFF")

class LightOnCommand(Command):
    def __init__(self, light: Light): self._light = light
    def execute(self): self._light.on()
    def undo(self):    self._light.off()

class Remote:                                # invoker
    def __init__(self): self._history: list[Command] = []
    def press(self, command: Command):
        command.execute()
        self._history.append(command)
    def undo_last(self):
        if self._history:
            self._history.pop().undo()

remote = Remote()
remote.press(LightOnCommand(Light()))    # Light ON
remote.undo_last()                       # Light OFF
```

Four roles: **Command** (interface), **ConcreteCommand**, **Receiver** (`Light`),
**Invoker** (`Remote`). Decouples the object that triggers an operation from the
one that performs it.

---

## 5. Iterator

**Intent:** provide a way to access elements of a collection sequentially without
exposing its underlying representation.

**Use when:** you want uniform traversal over custom/complex collections.

```python
class TreeCollection:
    def __init__(self):
        self._items = []
    def add(self, item): self._items.append(item)
    def __iter__(self):
        return iter(self._items)          # Python's built-in iterator protocol

# Custom iterator for full control:
class RangeIterator:
    def __init__(self, start, end):
        self._current, self._end = start, end
    def __iter__(self): return self
    def __next__(self):
        if self._current >= self._end:
            raise StopIteration
        value = self._current
        self._current += 1
        return value

for x in RangeIterator(0, 3):    # 0 1 2
    print(x)
```

Python bakes this pattern into the language: implement `__iter__`/`__next__` (or
just `yield` in a generator) and any collection becomes iterable. The client
never sees the internal storage.

---

## 6. Template Method

**Intent:** define the skeleton of an algorithm in a base method, deferring some
steps to subclasses. Subclasses customize steps **without changing the
algorithm's structure**.

**Use when:** several algorithms share the same overall steps but differ in
details — data parsers, report generators, build pipelines.

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process(self) -> None:            # TEMPLATE METHOD (fixed skeleton)
        self.read()
        self.transform()                  # step varies
        self.save()

    def read(self):  print("Reading data")
    @abstractmethod
    def transform(self): ...              # subclass must fill in
    def save(self):  print("Saving data")

class CSVProcessor(DataProcessor):
    def transform(self): print("Transforming CSV")

class JSONProcessor(DataProcessor):
    def transform(self): print("Transforming JSON")

CSVProcessor().process()      # read -> transform CSV -> save
```

**Template Method vs Strategy:** Template Method uses **inheritance** (steps
overridden in subclasses, structure fixed in the base). Strategy uses
**composition** (whole algorithm swapped via an injected object).

---

## 7. Visitor

**Intent:** represent an operation to be performed on elements of an object
structure, letting you add **new operations without modifying the element
classes**.

**Use when:** a stable set of classes needs many unrelated operations — AST
traversal, exporting to multiple formats, computing reports over a structure.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: "Visitor"): ...

class Circle(Shape):
    def __init__(self, r): self.r = r
    def accept(self, visitor): return visitor.visit_circle(self)

class Square(Shape):
    def __init__(self, s): self.s = s
    def accept(self, visitor): return visitor.visit_square(self)

class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, c: Circle): ...
    @abstractmethod
    def visit_square(self, s: Square): ...

class AreaVisitor(Visitor):               # new operation = new visitor class
    def visit_circle(self, c): return 3.14 * c.r ** 2
    def visit_square(self, s): return s.s ** 2

shapes = [Circle(5), Square(4)]
area = AreaVisitor()
print([s.accept(area) for s in shapes])   # add ops without touching shapes
```

**Trade-off:** easy to add new *operations* (new visitors), hard to add new
*element classes* (must update every visitor). Use only when the element set is
stable. Relies on **double dispatch** (`accept` → `visit_*`).

---

## 8. Mediator

**Intent:** define an object that encapsulates how a set of objects interact.
Objects no longer refer to each other directly — they talk through the mediator,
reducing many-to-many coupling to many-to-one.

**Use when:** components communicate in complex ways — chat rooms, UI dialogs
where widgets affect each other, air-traffic control.

```python
class ChatRoom:                           # mediator
    def __init__(self):
        self._users: list["User"] = []
    def register(self, user: "User"):
        self._users.append(user)
        user.room = self
    def send(self, message: str, sender: "User"):
        for user in self._users:
            if user is not sender:
                user.receive(message, sender)

class User:
    def __init__(self, name: str):
        self.name = name
        self.room: ChatRoom | None = None
    def send(self, message: str):
        self.room.send(message, self)     # go through mediator, not peers
    def receive(self, message: str, sender: "User"):
        print(f"{self.name} got '{message}' from {sender.name}")

room = ChatRoom()
alice, bob = User("Alice"), User("Bob")
room.register(alice); room.register(bob)
alice.send("Hi!")     # Bob receives it via the mediator
```

**Mediator vs Observer:** both decouple, but Mediator centralizes *multi-
directional* communication in one hub; Observer is *one-to-many* broadcast from a
subject.

---

## 9. Memento

**Intent:** capture and externalize an object's internal state so it can be
restored later — **without violating encapsulation**.

**Use when:** undo/rollback, checkpoints, snapshots, save games.

```python
class EditorMemento:                      # stores a snapshot
    def __init__(self, content: str):
        self._content = content
    def get_state(self) -> str:
        return self._content

class Editor:                             # originator
    def __init__(self):
        self._content = ""
    def type(self, text: str):
        self._content += text
    def save(self) -> EditorMemento:
        return EditorMemento(self._content)      # create snapshot
    def restore(self, memento: EditorMemento):
        self._content = memento.get_state()      # roll back
    def __str__(self): return self._content

class History:                            # caretaker: holds mementos
    def __init__(self): self._stack: list[EditorMemento] = []
    def push(self, m: EditorMemento): self._stack.append(m)
    def pop(self) -> EditorMemento:    return self._stack.pop()

editor, history = Editor(), History()
editor.type("Hello ")
history.push(editor.save())          # checkpoint
editor.type("World")
editor.restore(history.pop())        # back to "Hello "
print(editor)                        # "Hello "
```

Three roles: **Originator** (`Editor`), **Memento** (snapshot), **Caretaker**
(`History`, stores mementos but never inspects their contents).

---

## 10. Chain of Responsibility

**Intent:** pass a request along a chain of handlers; each handler decides to
process it or pass it to the next. Decouples sender from receiver.

**Use when:** middleware pipelines, logging levels, approval workflows, event
handling, request validation.

```python
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self._next: "Handler | None" = None
    def set_next(self, handler: "Handler") -> "Handler":
        self._next = handler
        return handler                     # enables fluent chaining
    @abstractmethod
    def handle(self, amount: float) -> None: ...
    def _pass_on(self, amount):
        if self._next:
            self._next.handle(amount)

class TeamLead(Handler):
    def handle(self, amount):
        if amount <= 1000: print(f"TeamLead approved {amount}")
        else: self._pass_on(amount)

class Manager(Handler):
    def handle(self, amount):
        if amount <= 10000: print(f"Manager approved {amount}")
        else: self._pass_on(amount)

class Director(Handler):
    def handle(self, amount):
        print(f"Director approved {amount}")

lead = TeamLead()
lead.set_next(Manager()).set_next(Director())   # build the chain
lead.handle(500)      # TeamLead
lead.handle(5000)     # Manager
lead.handle(50000)    # Director
```

Each handler has a single responsibility and optionally forwards. Add/remove/
reorder handlers freely without touching the others (OCP).

---

## Behavioral patterns at a glance

| Pattern | Key idea | Classic example |
|---------|----------|-----------------|
| Strategy | Swap algorithm | Payment methods |
| Observer | Broadcast changes | Event/notification system |
| State | Behavior per lifecycle state | Vending machine, order status |
| Command | Request as object | Undo/redo, task queue |
| Iterator | Sequential access | Custom collections |
| Template Method | Fixed skeleton, variable steps | Data pipelines |
| Visitor | New ops without editing classes | AST, exporters |
| Mediator | Central communication hub | Chat room |
| Memento | Snapshot & restore | Undo, save game |
| Chain of Responsibility | Chain of handlers | Middleware, approvals |

**Frequently confused pairs (interview gold):**

| Pair | Difference |
|------|-----------|
| Strategy vs State | Independent algorithms (client picks) vs lifecycle states (self-transition) |
| Strategy vs Template Method | Composition (swap object) vs inheritance (override steps) |
| Observer vs Mediator | One-to-many broadcast vs many-to-many hub |
| Command vs Strategy | Encapsulates a *request* (with undo) vs an *algorithm* |

---

## Quick self-check

1. You have `if payment_type == ...` picking behavior. Strategy or State — and why?
2. What are the four roles in the Command pattern?
3. Template Method vs Strategy: which uses inheritance, which uses composition?
4. Why is Visitor bad when your element classes change often?
5. Observer vs Mediator — describe the communication shape of each.
6. What are the three roles in Memento, and which one never reads the snapshot?

---

## Where this maps in the repo
- `concepts_and_problems/design-patterns/strategy/`, `observer/`, `state/`,
  `command/`, `iterator/`, `templatemethod/`, `visitor/`, `mediator/`,
  `memento/`, `chainofresponsibility/`.
- Next up: **07 — UML Diagrams**.
```
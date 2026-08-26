# Design a Vending Machine

**Round:** LLD · **Difficulty:** Easy · **Date:** 2026-08-26 · **Duration:** 4m 56s

## Problem

Design a vending machine that supports multiple products with different prices and quantities, accepts coins and notes of various denominations, dispenses the selected product and returns change, and tracks inventory. It should support restocking/cash collection and handle exceptions like insufficient funds or out-of-stock. Model the states, transitions, and classes.

## Session artifacts

- [Transcript](./transcript.md)
- [Solution](./solution.py)

## Evaluation

**Verdict:** Strong Hire · **Overall:** 1/5

The candidate showed an initial understanding of the vending machine system but failed to flesh out a complete design. The solution provided was minimal, lacking key components such as state machines, inventory management, transaction handling, and payment methods. The candidate did not demonstrate an ability to evolve the design or respond effectively to the interviewer's concerns, which are critical for the role of a senior engineer. It highlights the need for a deeper and more comprehensive understanding of design principles and patterns for such a domain.

### Scores

| Dimension | Score | Notes |
| --- | --- | --- |
| Requirements & Abstractions | 1/5 | The candidate's design did not fully cover the requirements of the vending machine system, failing to address the state transitions, inventory management, transaction handling, change-making logic, error handling, concurrency, and extensibility aspects. The candidate primarily started with a basic framework with an abstract `VendingMachine` class but did not flesh out the necessary entities and their state machine interactions. |
| SOLID & Design Patterns | 1/5 | There were no clear applications of design patterns, and the code provided did not demonstrate an understanding of SOLID principles. The candidate only started with an abstract `VendingMachine` class and did not use composition or inheritance to model different components such as inventory, products, or payment methods. A `State` interface or its implementation would have been a better approach. |
| Coupling & Cohesion | 1/5 | There were high levels of coupling since the components were not designed independently. The abstract `VendingMachine` class lacked a concrete implementation, leading to an incomplete design. There was no clear separation of concerns or low coupling between different components such as inventory, product selection, and payment methods. |
| Extensibility | 1/5 | The design provided did not address how changes to payment methods or the addition of new payment methods would integrate with the existing structure, indicating a lack of flexibility and extensibility. There was no mention of any strategies or interfaces that would allow for the addition of new payment methods without extensive rework. |
| Correctness & Edge Cases | 1/5 | The design did not cover edge cases such as insufficient funds, out-of-stock, or insufficient denominations, and thus lacked correctness in handling these scenarios. Additionally, the candidate did not contemplate concurrency issues with multiple buyers or transaction races, which are necessary concerns for a vending machine system. |
| Diagram / Code Quality | 1/5 | The candidate's code was simplistic and did not include any state transitions, inventory management, transaction handling, or product selection. The diagram was missing entirely, and the code lacked a logical structure to support the vending machine's function. The provided code does not offer any insights into the abstractions, state machine, or error handling that would be expected from a complete design. |
| Design Trajectory | 1/5 | Much of the candidate’s design was not responsive to the interviewer's concerns and questions. The candidate failed to address the state transitions, inventory management, transaction handling, and error handling, which were critical aspects of the vending machine system. There was a lack of evolution in the design, and the candidate did not effectively refactor or introduce necessary abstractions in response to the interviewer's feedback. |
| Communication | 1/5 | The candidate failed to provide a cohesive response by not addressing the key concerns raised by the interviewer. The lack of a detailed response to all the questions indicates an inability to clearly articulate thought and ideas. The candidate was unable to progress the discussion towards the desired depth and provided no diagrams or code, which are expected in a tech interview setting. |

### Strengths



### Areas to improve

- No implementation of state transitions, product selection, inventory management, transaction handling, change-making, error handling, concurrency
- Lack of abstractions and design patterns in class modeling
- No clear separation of concerns or low coupling
- No strategy for extensibility in adding new payment methods
- No handling for edge cases such as insufficient funds, out-of-stock, or insufficient denominations
- No diagram shown, which is expected in a detailed design discussion

### What a model answer covers

- A comprehensive state machine illustrating transitions between Idle, HasMoney, Dispensing, OutOfStock states
- An implementation of inventory, product, and coin handling components
- Correct implementation of change-making logic with edge cases
- Error handling and management mechanism implemented
- Concurrency handling and atomic transaction mechanisms for multiple buyers
- An abstract base class with concrete subclasses for payment methods
- A diagram showing the interactions and responsibilities of the main classes involved in the vending machine system
- A final sketch of the interactions and responsibilities of the key components to ensure the state machine handles all necessary transitions and errors correctly

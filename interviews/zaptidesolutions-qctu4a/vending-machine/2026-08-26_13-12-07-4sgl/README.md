# Design a Vending Machine

**Round:** LLD · **Difficulty:** Easy · **Date:** 2026-08-26 · **Duration:** 7m 10s

## Problem

Design a vending machine that supports multiple products with different prices and quantities, accepts coins and notes of various denominations, dispenses the selected product and returns change, and tracks inventory. It should support restocking/cash collection and handle exceptions like insufficient funds or out-of-stock. Model the states, transitions, and classes.

## Session artifacts

- [Transcript](./transcript.md)
- [Solution](./solution.py)
- [Diagram](./diagram.png)

## Evaluation

**Verdict:** Lean Hire · **Overall:** 2/5

The candidate demonstrated a good understanding of the State pattern and its application to different states of the vending machine. However, the implementation lacks detailed steps for managing inventory and concurrency, and it does not provide a practical solution for change-making and handling exceptions. These areas suggest room for improvement and learning.

### Scores

| Dimension | Score | Notes |
| --- | --- | --- |
| State pattern: states, transitions, invalid actions | 3/5 | The candidate has identified the State pattern and uses it to represent distinct states of the vending machine. However, the transition logic and invalid actions are not fully fleshed out. For example, the design lacks the validation to ensure that selecting an item leads to the payment phase only when the selected item is available in stock. This oversight reflects a lack of detail and validation checks. |
| Change-making algorithm and edge cases | 2/5 | The candidate's design suggests the use of a Strategy pattern to handle different payment methods. While this approach is correct, the code provided does not show any algorithm related to change making. The design lacks consideration for edge cases such as insufficient funds or overpayment. This means that the candidate's focus is too high-level and does not consider practical implementation details related to the vending machine's functionalities. |
| Inventory & concurrency (two buyers, last item) | 3/5 | The diagram shows an intention to handle inventory management but does not detail any specific concurrent access or locking mechanism. For a vending machine, managing inventory concurrent access is a critical issue. It is essential to prevent race conditions, which the candidate's design lacks. A more advanced solution could use semaphores or locks to ensure that only one transaction operates on inventory at the same time. |
| Extensibility for new payment methods | 3/5 | The candidate has included the Strategy pattern, which is a good practice for designing a vending machine that accepts multiple payment methods. However, the pattern is not fully implemented in the provided code. The focus on payment strategies suggests an intent to be extensible, but the lack of actual implementation leaves this as a conceptual idea. |

### Strengths

- Understood the State pattern and attempted to model different states of the vending machine
- Recognized the need for payment strategies to accommodate different methods of payment
- Acknowledged the importance of inventory management

### Areas to improve

- Lacked a clear explanation and implementation of how a customer selecting an item would proceed to payment phase if the item is available and have sufficient funds
- The design does not include an inventory or concurrency solution that ensures mutual exclusion when updating product quantities and handling payments
- There were no details on change-making algorithm and scenarios such as insufficient funds or overpayment

### What a model answer covers

- A more detailed explanation of how the Payment Strategy pattern would handle different payment methods and provide a concrete example of code for each method
- A robust concurrency solution, such as using semaphores or locks, to prevent race conditions and ensure inventory updates and payment transactions are atomic
- A complete implementation of the change-making algorithm with consideration of all edge cases

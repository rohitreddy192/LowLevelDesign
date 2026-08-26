# Design a Vending Machine — Interview Transcript

**Round:** LLD · **Difficulty:** Easy · **Date:** 2026-08-26 · **Duration:** 1m 42s

## Problem

Design a vending machine that supports multiple products with different prices and quantities, accepts coins and notes of various denominations, dispenses the selected product and returns change, and tracks inventory. It should support restocking/cash collection and handle exceptions like insufficient funds or out-of-stock. Model the states, transitions, and classes.

---

**Interviewer:** Absolutely, let's get started. The problem is to design a vending machine that supports multiple products, accepts different denominations, tracks inventory, dispenses the selected product, returns change, and handles exceptions efficiently. What's your initial approach to structuring the core classes or components of this vending machine?

**You:** Yes

**Interviewer:** Great! Could you elaborate on how you plan to handle the inventory aspect? For example, how will you keep track of available products and their quantities?

**You:** Here's my current diagram — what do you think?

**Interviewer:** The diagram seems to outline the basic states and transitions of the vending machine. It's a good start! How will you handle the scenario where the machine runs out of a particular product while processing a transaction?

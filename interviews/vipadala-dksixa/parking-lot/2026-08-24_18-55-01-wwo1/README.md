# Design a Parking Lot System

**Round:** LLD · **Difficulty:** Easy · **Date:** 2026-08-24 · **Duration:** 35m 0s

## Problem

Design a parking lot system. It has multiple levels, each with a number of spots; it supports different vehicle types (car, motorcycle, truck) where each spot fits a specific type. Assign a spot on entry and release it on exit, track availability in real time, and support multiple entry/exit points with concurrent access. Walk me through your classes, their responsibilities, and relationships.

## Session artifacts

- [Transcript](./transcript.md)
- [Solution](./solution.py)

## Evaluation

**Verdict:** No Hire · **Overall:** 2/5

You demonstrated a good initial intuition for the high-level components of a parking lot. To reach a senior standard, focus on applying SOLID principles cleanly (avoiding type checks on strategy classes), designing robust concurrent data structures for fast lookups, and covering the complete end-to-end flow including tickets, gates, and pricing.

### Scores

| Dimension | Score | Notes |
| --- | --- | --- |
| Class Responsibilities & Domain Modeling | 2/5 | The candidate identified basic structural entities like ParkingLot, ParkingFloor, and ParkingSpot, but missed critical domain classes including Ticket, Gate, Vehicle (represented only as an enum), and Payment/Pricing models. |
| Design Patterns & Extensibility | 2/5 | While the candidate attempted to implement the Strategy pattern for spot assignment, they introduced 'if instanceof(strategy, NearToEntry)' inside ParkingLotStrategy, directly violating the Open/Closed Principle. Additionally, the concrete strategy implementations contained identical linear search logic. |
| Concurrency & Real-time Tracking | 2/5 | The candidate conceptually mentioned locking spots in a critical section, but did not elaborate on concurrent data structures (e.g., ConcurrentHashMap, Min-Heaps) or fine-grained locking primitives needed to prevent race conditions across multiple gates efficiently. |
| Code Completeness & Quality | 2/5 | The Python code skeleton had syntax errors (using Java's 'instanceof' keyword), incomplete constructor methods, and lacked flow implementations for issuing tickets, checking out, or calculating parking fees. |

### Strengths

- Quickly grasped the multi-level parking concept and listed primary physical components (Floor, Spot, Manager).
- Used an Enum for VehicleType to maintain type safety across the application.

### Areas to improve

- Violated SOLID principles (specifically OCP) by using explicit type checks on Strategy implementations instead of relying on polymorphic dispatch.
- Omitted essential system requirements such as Ticket creation, exit gate logic, and pricing strategy calculation.
- Did not design a thread-safe data structure (e.g., per-vehicle-type heaps or queues) for fast, concurrent spot allocation.

### What a model answer covers

- A clean polymorphic ParkingStrategy interface taking `ParkingLot` and `Vehicle` to find an available spot without `instanceof` checks.
- Thread-safe spot assignment using concurrent queues or a Min-Heap of available spots per VehicleType to avoid scanning every floor sequentially.
- Complete domain workflow: Gate issues a Ticket on Entry with entry_time and spot_id; Exit Gate calculates fee using a flexible PricingStrategy based on duration and VehicleType.
- Spot compatibility abstraction where ParkingSpot can encapsulate logic to determine if a Vehicle fits (`spot.can_fit(vehicle)`).

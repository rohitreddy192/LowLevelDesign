# Design a Parking Lot System

**Round:** LLD · **Difficulty:** Easy · **Date:** 2026-08-23

## Problem

Design a parking lot system. It has multiple levels, each with a number of spots; it supports different vehicle types (car, motorcycle, truck) where each spot fits a specific type. Assign a spot on entry and release it on exit, track availability in real time, and support multiple entry/exit points with concurrent access. Walk me through your classes, their responsibilities, and relationships.

## Session artifacts

- [Transcript](./transcript.md)

## Evaluation

**Verdict:** No Hire · **Overall:** 2/5

The candidate made a promising start by asking targeted clarifying questions about vehicle types, parking levels, and entry/exit gates. However, because the transcript concluded immediately after clarification, core LLD aspects like class relationships, concurrency handling, and design patterns could not be evaluated.

### Scores

| Dimension | Score | Notes |
| --- | --- | --- |
| Requirements Gathering | 4/5 | The candidate asked relevant clarifying questions right at the start, covering entries/exits, single vs. multi-level parking, and vehicle types supported. |
| Domain Modeling & Object Design | 1/5 | The candidate did not get the chance to outline domain entities, class relationships, or design patterns as the transcript ended prematurely. |
| Concurrency & Real-time Tracking | 1/5 | Concurrency mechanisms, locking strategies, and real-time spot tracking were not discussed in the provided transcript segment. |
| Extensibility & Design Patterns | 1/5 | No discussion took place regarding Strategy pattern for pricing/assignment or extensibility for new vehicle/spot types. |

### Strengths

- Proactively asked relevant clarifying questions regarding concurrency points, parking structure levels, and vehicle types.

### Areas to improve

- Did not present domain classes, relationships, or use cases before the transcript ended.
- Did not discuss spot assignment strategies, payment/pricing models, or thread-safety concurrency controls.

### What a model answer covers

- Define core domain models: ParkingLot, Level, ParkingSpot, Vehicle hierarchy (Motorcycle, Car, Truck), Ticket, and Payment.
- Implement a SpotAssignmentStrategy (e.g., NearestFirstStrategy, RandomStrategy) using the Strategy design pattern for flexible spot allocation.
- Support swappable PricingStrategy implementations (e.g., HourlyPricing, FlatRatePricing) triggered during ticket checkout.
- Address concurrency at entry/exit gates using synchronized blocks, ReentrantLock, or concurrent data structures (e.g., ConcurrentHashMap, AtomicInteger) to avoid double-booking spots.

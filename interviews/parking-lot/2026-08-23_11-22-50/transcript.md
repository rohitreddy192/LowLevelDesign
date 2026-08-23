# Design a Parking Lot System — Interview Transcript

**Round:** LLD · **Difficulty:** Easy · **Date:** 2026-08-23

## Problem

Design a parking lot system. It has multiple levels, each with a number of spots; it supports different vehicle types (car, motorcycle, truck) where each spot fits a specific type. Assign a spot on entry and release it on exit, track availability in real time, and support multiple entry/exit points with concurrent access. Walk me through your classes, their responsibilities, and relationships.

---

**Interviewer:** Hi there! Great to meet you. Welcome to your system design interview.

Today, we're going to design a **Parking Lot System**. The system should manage multiple levels and spots, handle different vehicle types, assign and release spots, track real-time availability, and safely support concurrent entries and exits.

To kick things off, how would you like to start? Feel free to ask any clarifying questions or outline your high-level approach.

**You:** Okay. What else should be there. Like number of entries we have is it like one entry one exit or multiple and number of floors we have is it multi level parking or a single floor. And what types of vehivles we handle 2 wheelrs and 4 wheelers as well?

**Interviewer:** Those are great questions to clarify! 

For this system, let's assume:
1. **Multiple entry and exit points** operating concurrently.
2. **Multi-level parking** (multiple floors, each with many spots).
3. **Vehicle types**: At least Motorcycles (2-wheelers), Cars (4-wheelers), and Large Vehicles/Trucks.

With those parameters in mind, what are the main use cases and core domain entities you'd start identifying for this system?

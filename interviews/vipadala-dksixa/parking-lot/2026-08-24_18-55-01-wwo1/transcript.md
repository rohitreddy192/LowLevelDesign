# Design a Parking Lot System — Interview Transcript

**Round:** LLD · **Difficulty:** Easy · **Date:** 2026-08-24 · **Duration:** 35m 0s

## Problem

Design a parking lot system. It has multiple levels, each with a number of spots; it supports different vehicle types (car, motorcycle, truck) where each spot fits a specific type. Assign a spot on entry and release it on exit, track availability in real time, and support multiple entry/exit points with concurrent access. Walk me through your classes, their responsibilities, and relationships.

---

**Interviewer:** Welcome! Today we'll be designing a Parking Lot System. 

The system should manage multiple levels and spots supporting different vehicle types (like cars, motorcycles, and trucks), handle spot assignment on entry and release on exit, support real-time availability tracking, and handle concurrent access across multiple entry and exit gates.

To kick things off, feel free to ask any clarifying questions about the scope, or share your initial thoughts on the core requirements. How would you like to begin?

**You:** So from my understanding it is 2 wheeeler, 4 wheeler, multi level parking and multiple entry exits and availability tracking and handling concurrent access for same spot.

**Interviewer:** Spot on summary! Along with 2-wheelers and 4-wheelers, let's also keep trucks or large vehicles in mind as part of our vehicle types.

To start structuring our design, what core entities or classes do you see in this system, and how do you envision them relating to each other?

**You:** Okay done. And I will first think of it like this 

We should have a dataclass for Slot where we will have spot id, vehicleType, occupied. And we will have a Floor with list of parking slots and then we will have a floor manager class which takes care of the parking in that floor and also then we will have a Parking Manager which takes care of all floors to identify the slot empty in which floor to floor manager and floor manager will get the slot at the very entry. And then on we will have a main entry and main exits and each per floor level so for these things we can have multipl entries and exits right at each place so we should also check for the slots available at each floor for the vehicle. So that is done at entry and unreserved at the exit of floor. This is the idea here and Parking Strategy is there for parking near to the gate or away from the gate etc. We can design it.

**Interviewer:** That's a solid high-level breakdown of the layout and flow! 

Let's dive deeper into the core domain models. You mentioned a `Slot` class with a `vehicleType` attribute. 

How are you planning to represent `Vehicle` types and `ParkingSpot` types in code, and how will the system determine if a specific vehicle can park in a specific spot?

**You:** VehicleTypes -> 2 wheeler, 4 wheeler, Mini Truck,  Large Vehicles. 

VehicleTypes is a enum
And each parking spot has -> Spot id, VehicleType, isOccupied.

**Interviewer:** Got it. Having an enum for vehicle types keeps things clean.

Now, suppose a motorcycle enters the parking lot, but all designated motorcycle spots are full. Can that motorcycle park in a 4-wheeler or large vehicle spot? 

Where in your class structure would you put the logic that decides whether a vehicle *fits* in a given spot?

**You:** No we wont park it there. For now I'm thinking of seperate spots for each and we are not adjusting it in our design. Should we do it?

**Interviewer:** Keeping a strict 1:1 mapping for now is totally fine and simplifies our scope!

To keep our design flexible, where would you place the logic that checks if a spot can accommodate a vehicle? For example, would that live inside `ParkingSpot`, `Vehicle`, or a manager?

Also, once a vehicle arrives at an entry gate, how does your `ParkingStrategy` find an available spot efficiently?

**You:** Yes. So first if that is a multi level one we will first get a request at the entry gate for the checkin where the ParkingSlot Manager can scan through floors for the spot and can get tif anything is available based on vehicleType and freeze it. So no one from another entry can freeze that. And then when the vehicle enters to the parking floor based on the slot there the vehicle can go and park it there as the ticket is generated in the entry we can easily go to the location as specified. So it will be the way and at the entry we will be using the concurrency so if there is 1 spot and 2 cars at different entries only 1 car pases- by.

**Interviewer:** That flow makes sense. 

Let's talk about the strategy and concurrency details:

1. **Strategy:** How does the `ParkingSlotManager` know *which* available spot to pick (e.g., nearest to entrance, lowest floor first)? What design pattern would you use so we can easily swap this strategy later?

2. **Concurrency:** You mentioned "freezing" the spot at entry to prevent race conditions across multiple gates. How would you implement this thread-safe assignment in code?

**You:** So we can add strategies like near to gate and near to exit. Because on heavy crowd times we can use near to exit as it will make sure the exit sides are filled first andthen the entry because if everything is parkd at entry then every vehicle should pass by and its an extra burden. And for the nearest to exit is when its that time of day and its yet to conclude etc. And its upto the parking lot manager.


Concurrency is when two or more ppl from differnt gates are looking for a single spot we will lock the spot when differnt threads initiate the process and then we will let only one enter the critical section.

**Interviewer:** That trade-off on parking strategies makes a lot of sense! Using the Strategy design pattern here will let us swap those rules seamlessly.

Now regarding concurrency: if we have dozens of entry gates and thousands of spots, locking individual spots during a search might lead to bottlenecks or race conditions while scanning.

What underlying data structure would you use inside the manager to track *available* spots per type/floor, and how would you handle thread-safety when multiple gates request a spot at the exact same time?

**You:** Should i start with a diagram as the time being a constraint or these follow ups are there yet?

**Interviewer:** A diagram is a great idea at this stage! 

Please go ahead and draw a diagram showing your core classes (`ParkingLot`, `Floor`, `ParkingSpot`, `Vehicle`, `Strategy`, `Gate`, `Ticket`, etc.), their relationships, methods, and key attributes. 

Once you share it, we can use it to walk through the complete flow and tackle the concurrency details!

**You:** I want to understand one mroe thing out of this interview whats the expected out of it like coding end to end, umnl diagrams etc?

**Interviewer:** In a typical LLD interview, the focus is on:

1. **Class Diagram / Visual Architecture:** Showing entities, their relationships, methods, and design patterns.
2. **Code / Interfaces:** Writing clean code sketches or skeleton implementations for key classes (e.g., core logic, interfaces, strategies) to demonstrate SOLID principles and clean code.
3. **Deep Dives:** Discussing trade-offs, edge cases, and concurrency mechanisms.

You don't need to write a fully runnable application with all boilerplate, but key interfaces and core method implementations are definitely expected. 

Whenever you're ready, feel free to share your diagram or start sketching the key classes!

**You:** So diagram or classes because time is getting enar.

**Interviewer:** Let's jump straight into defining the core classes and interfaces in code! 

Show me your `ParkingSpot`, `Vehicle`, `ParkingFloor`, and `ParkingLotManager` classes, along with how you'd structure the `ParkingStrategy` interface. 

Feel free to write out the code skeletons with key fields and methods.

**You:** from abc import ABC, abstractmethod
from enum import Enum

class Solution:
    def run(self) -> None:
        print("Hello from your LLD design!")

class VehicleType(str, Enum):
    TWO_WHEELER = "2Wheeler"
    FOUR_WHEELER = "4Wheeler"
    TRUCK = "TRUCK"
    LARGE_VEHICLE = "LARGE_VEHICLE"

class ParkingLot:
    def __init__(self, number_of_floors, parking_allotment_per_floor):
        pass

class ParkingFloor:
    def __init__(self, floor):
        self.parking_floor = floor
        self.parking_slots = []
        ### Parking spots are arranged based on parking_allotment

    def set_parkingslots(self, floor_slots_allotment):
        pass

class ParkingSpot:
    def __init__(self, parking_id, vehicleType, isOccupied=False):
        self.parking_id = parking_id
        self.vehicleType = vehicleType
        self.isOccupied = False

class ParkingLotManager:
    def __init__(self):
        ## This guy passes the parking lot allotment per floor so we can build it and then do allot for the vehicles.
        pass

class ParkingStrategy(ABC):
    @abstractmethod
    def park(self, floor: ParkingFloor):
        pass

class NearToEntry(ParkingStrategy):
    def park(self, floor: ParkingFloor):
        ## For now lets assume everything is in linear array fashion usually its a matrix. 
        for spot in floor.parking_slots:
            if not spot.isOccupied:
                return spot

class NearToEntry(ParkingStrategy):
    def park(self, floor: ParkingFloor):
        ## For now lets assume everything is in linear array fashion usually its a matrix. 
        for i in range(len(floor.parking_slots)):
            spot = floor.parking_slots[i]
            if not spot.isOccupied:
                return spot


if __name__ == "__main__":
    Solution().run()

**Interviewer:** Thanks for putting this skeleton together! 

Looking at `ParkingStrategy.park(self, floor: ParkingFloor)`:

1. How will the strategy know *which vehicle type* we are looking to park, so it doesn't assign a motorcycle spot to a truck?
2. Since the parking lot has *multiple* floors, should the strategy operate across the whole `ParkingLot` rather than a single `ParkingFloor`? 

How would you update `ParkingStrategy` to handle this?

**You:** Correct catch. And we will run a loop for all floor at the Manager level for this. But i have an idea here we should run that without passing the floor so we can get it dione much better. I will add a proper updated code for the current one. 

from abc import ABC, abstractmethod
from enum import Enum

class Solution:
    def run(self) -> None:
        print("Hello from your LLD design!")

class VehicleType(str, Enum):
    TWO_WHEELER = "2Wheeler"
    FOUR_WHEELER = "4Wheeler"
    TRUCK = "TRUCK"
    LARGE_VEHICLE = "LARGE_VEHICLE"

class ParkingLot:
    def __init__(self, number_of_floors, parking_allotment_per_floor):
        pass

class ParkingFloor:
    def __init__(self, floor):
        self.parking_floor = floor
        self.parking_slots = []
        ### Parking spots are arranged based on parking_allotment

    def set_parkingslots(self, floor_slots_allotment):
        pass

class ParkingSpot:
    def __init__(self, parking_id, vehicleType, isOccupied=False):
        self.parking_id = parking_id
        self.vehicleType = vehicleType
        self.isOccupied = False

class ParkingLotManager:
    def __init__(self):
        ## This guy passes the parking lot allotment per floor so we can build it and then do allot for the vehicles.
        pass

class ParkingStrategy(ABC):
    @abstractmethod
    def park(self, floor: ParkingFloor, vehicleType: VehicleType):
        pass

class NearToEntry(ParkingStrategy):
    def park(self, floor: ParkingFloor, vehicleType: VehicleType):
        ## For now lets assume everything is in linear array fashion usually its a matrix. 
        for spot in floor.parking_slots:
            if not spot.isOccupied and spot.vehicleType==vehicleType:
                return spot

class NearToEntry(ParkingStrategy):
    def park(self, floor: ParkingFloor, vehicleType: VehicleType):
        ## For now lets assume everything is in linear array fashion usually its a matrix. 
        for i in range(len(floor.parking_slots)):
            spot = floor.parking_slots[i]
            if not spot.isOccupied and spot.vehicleType==vehicleType:
                return spot


if __name__ == "__main__":
    Solution().run()



Justa. min while i fix it

**Interviewer:** No problem, take a moment to refine it!

While you update it, also think about how `Ticket` generation and exit processing fit into `ParkingLotManager`. What information should a `Ticket` hold when issued at the gate?

**You:** from abc import ABC, abstractmethod
from enum import Enum

class Solution:
    def run(self) -> None:
        print("Hello from your LLD design!")

class VehicleType(str, Enum):
    TWO_WHEELER = "2Wheeler"
    FOUR_WHEELER = "4Wheeler"
    TRUCK = "TRUCK"
    LARGE_VEHICLE = "LARGE_VEHICLE"

class ParkingLot:
    def __init__(self, number_of_floors, parking_allotment_per_floor):
        pass

class ParkingFloor:
    def __init__(self, floor):
        self.parking_floor = floor
        self.parking_slots = []
        ### Parking spots are arranged based on parking_allotment

    def set_parkingslots(self, floor_slots_allotment):
        pass

class ParkingSpot:
    def __init__(self, parking_id, vehicleType, isOccupied=False):
        self.parking_id = parking_id
        self.vehicleType = vehicleType
        self.isOccupied = False

class ParkingLotManager:
    def __init__(self):
        ## This guy passes the parking lot allotment per floor so we can build it and then do allot for the vehicles.
        pass

class ParkingLotStrategy:
    def __init__(self, strategy):
        self.strategy = strategy

    def park(self, strategy: ParkingStrategy, parking_floors, vehicleType):
        if instanceof(strategy, NearToEntry):
            for i in range(number_of_floors):
                spot = strategy.park(parking_floors[i], vehicleType)
                pass

class ParkingStrategy(ABC):
    @abstractmethod
    def park(self, floor: ParkingFloor, vehicleType: VehicleType):
        pass

class NearToEntry(ParkingStrategy):
    def park(self, floor: ParkingFloor, vehicleType: VehicleType):
        ## For now lets assume everything is in linear array fashion usually its a matrix. 
        for spot in floor.parking_slots:
            if not spot.isOccupied and spot.vehicleType==vehicleType:
                return spot

class NearToExit(ParkingStrategy):
    def park(self, floor: ParkingFloor, vehicleType: VehicleType):
        ## For now lets assume everything is in linear array fashion usually its a matrix. 
        for i in range(len(floor.parking_slots)):
            spot = floor.parking_slots[i]
            if not spot.isOccupied and spot.vehicleType==vehicleType:
                return spot


if __name__ == "__main__":
    Solution().run()

**Interviewer:** 

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

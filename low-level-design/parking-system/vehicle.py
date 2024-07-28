from enum import Enum
from typing import List, Dict


class VehicleType(Enum):
    CAR = 1,
    MOTORCYCLE = 2,
    TRUCK = 3


class Vehicle:
    def __init__(self, vehicle_type: VehicleType, license_plate: str):
        self.type = vehicle_type
        self.license_plate = license_plate

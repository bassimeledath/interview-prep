
from typing import List
from parking_spot import ParkingSpot


class ParkingLevel:
    def __init__(self, level_number: int, spots: List[ParkingSpot]):
        self.level_number = level_number
        self.spots = spots

    @property
    def available_spots(self):
        available_spots = [spot for spot in self.spots if spot.level ==
                           self.level_number and not spot.is_occupied]
        return available_spots

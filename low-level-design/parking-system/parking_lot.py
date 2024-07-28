from typing import List
import threading
from typing import Dict
from parking_level import ParkingLevel
from vehicle import Vehicle, VehicleType


class ParkingLot:
    def __init__(self, levels: List[ParkingLevel]):
        self.levels = levels
        self.occupied_spots = {}
        self.lock = threading.Lock()

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        with self.lock:
            for level in self.levels:
                available_spots = level.available_spots
                if available_spots:
                    spot_to_fill = available_spots[0]
                    spot_to_fill.is_occupied = True
                    self.occupied_spots[vehicle.license_plate] = spot_to_fill
                    return True
            return False

    def remove_vehicle(self, vehicle: Vehicle) -> bool:
        with self.lock:
            if vehicle.license_plate in self.occupied_spots:
                self.occupied_spots[vehicle.license_plate].is_occupied = False
                del self.occupied_spots[vehicle.license_plate]
                return True
            return False

    @property
    def available_spots_count(self) -> Dict[VehicleType, int]:
        counts = {vtype: 0 for vtype in VehicleType}
        for level in self.levels:
            for spot in level.spots:
                if not spot.is_occupied:
                    counts[spot.vehicle_type] += 1
        return counts

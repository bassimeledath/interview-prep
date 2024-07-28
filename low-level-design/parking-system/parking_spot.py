from vehicle import VehicleType, Vehicle


class ParkingSpot:
    def __init__(self, spot_id: int, level: int, vehicle_type: VehicleType):
        self.id = spot_id
        self.level = level
        self.vehicle_type = vehicle_type
        self.is_occupied = False

from dataclasses import dataclass


@dataclass
class Product:
    id: int
    price: float
    quantity: int

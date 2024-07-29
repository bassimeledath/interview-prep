from typing import List, Dict
from product import Product
from payment_processor import PaymentProcessor
from exceptions import OutOfStockException, InsufficientFundsException, InvalidProductException


class VendingMachine:
    def __init__(self):
        self._available_products: Dict[int, Product] = {}
        self.inserted_balance: float = 0.0

    def insert_payment(self, payment: dict) -> None:
        amount_inserted = PaymentProcessor.process_payment(payment)
        self.inserted_balance += amount_inserted

    def add_stock(self, stock: Dict[int, int]) -> None:
        for product_id, quantity in stock.items():
            if product_id in self._available_products:
                self._available_products[product_id].quantity += quantity
            else:
                raise InvalidProductException(
                    f"Product with ID {product_id} is not in the vending machine")

    def dispense(self, product_id: int) -> float:
        if product_id not in self._available_products:
            raise InvalidProductException(
                f"Product with ID {product_id} does not exist")

        product = self._available_products[product_id]

        if not self.check_in_stock(product_id):
            raise OutOfStockException(
                f"Product {product.name} is out of stock.")

        if self.inserted_balance < product.price:
            raise InsufficientFundsException(
                f"Insufficient funds for product {product.name}")

        product.quantity -= 1
        change = self.inserted_balance - product.price
        self.inserted_balance = 0.0
        return change

    def check_in_stock(self, product_id: int) -> bool:
        return self._available_products[product_id].quantity > 0

    @property
    def available_products(self) -> Dict[int, Product]:
        return self._available_products

    def add_product(self, product: Product) -> None:
        if product.id in self._available_products:
            raise InvalidProductException(
                f"Product with ID {product.id} already exists")
        self._available_products[product.id] = product

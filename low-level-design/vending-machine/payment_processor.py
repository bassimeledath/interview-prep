from typing import Dict
from constants import VALID_PAYMENTS


class PaymentProcessor:
    @staticmethod
    def process_payment(payment: Dict[str, int]) -> float:
        total = 0
        for payment_type, count in payment.items():
            payment_type = payment_type.upper()
            if payment_type not in VALID_PAYMENTS:
                raise ValueError(f"Invalid payment type: {payment_type}")
            total += VALID_PAYMENTS[payment_type] * count
        return total

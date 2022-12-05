import decimal
from dataclasses import dataclass


@dataclass
class Money:
    amount: decimal
    currency: str

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency

        return NotImplemented

    def __str__(self):
        return f"{self.amount} {self.currency}"

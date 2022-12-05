from dataclasses import dataclass

from src.core.model.value_objects.money import Money


@dataclass
class PriceItem:
    description: str
    price: Money
    seller: str

    def __str__(self):
        return f"Item: {self.description}, price: {self.price}, seller: {self.seller}"

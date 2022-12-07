from dataclasses import dataclass

from core.model.price_catalog_aggregate.price_item import PriceItem


@dataclass
class ErrorItem:
    item: PriceItem
    error: str

    def __str__(self):
        return f"Item: '{self.item}'; Error: {self.error}"

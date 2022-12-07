from typing import List

from core.model.exceptions.item_not_found_exception import InvalidCatalogException
from core.model.exceptions.error_item import ErrorItem
from core.model.price_catalog_aggregate.price_item import PriceItem
from core.model.value_objects.money import Money


class PriceCatalog:
    _items: List[PriceItem]

    def __init__(self, items: List[PriceItem] = None):
        self._items = items or []

    @property
    def items(self) -> List[PriceItem]:
        return self._items

    def add(self, description: str, price: Money, seller: str) -> None:
        item = PriceItem(description, price, seller)
        self._items.append(item)

    def lookup(self, name: str) -> List[PriceItem]:
        result = filter(lambda item: item.description == name, self._items)
        return list(result)

    def top_deal_by_currency(self, name: str, currency: str) -> PriceItem | None:
        items = filter(lambda item: item.description == name and item.price.currency == currency, self._items)
        items_by_price_asc = sorted(items, key=lambda item: item.price.amount)
        top_deal = next(iter(items_by_price_asc), None)
        return top_deal

    def validate(self) -> None:
        error_items = []
        for item in self._items:
            if item.price.amount < 0:
                error_items.append(ErrorItem(item, "Price cannot be below zero"))

        if len(error_items) > 0:
            raise InvalidCatalogException(error_items)

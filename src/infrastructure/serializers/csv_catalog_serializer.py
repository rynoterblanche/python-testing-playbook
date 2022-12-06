from decimal import Decimal

from src.core.interfaces.catalog_serializer import CatalogSerializer
from src.core.model.price_catalog_aggregate.price_catalog import PriceCatalog
from src.core.model.price_catalog_aggregate.price_item import PriceItem
from src.core.model.value_objects.money import Money


class CsvCatalogSerializer(CatalogSerializer):
    DEFAULT_DELIMITER: str = ','

    def __init__(self, delimiter: str = None):
        self._delimiter = delimiter or CsvCatalogSerializer.DEFAULT_DELIMITER

    def get_catalog_from_string(self, catalog_string: str) -> PriceCatalog:
        lines = catalog_string.split('\n')

        items = [self._get_item_from_string(line) for line in lines]

        catalog = PriceCatalog(items)
        return catalog

    def _get_item_from_string(self, item_line: str) -> PriceItem:
        delimited = item_line.split(self._delimiter)

        item_description = delimited[0]

        price_amount = Decimal(delimited[1])
        price_currency = delimited[2]
        price = Money(price_amount, price_currency)

        item_seller = delimited[3]

        item = PriceItem(item_description, price, item_seller)
        return item

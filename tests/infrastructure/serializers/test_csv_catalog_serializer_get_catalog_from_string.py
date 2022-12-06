import unittest

from src.core.model.price_catalog_aggregate.price_item import PriceItem
from src.core.model.value_objects.money import Money
from src.infrastructure.serializers.csv_catalog_serializer import CsvCatalogSerializer


class CsvCatalogSerializerGetCatalogFromString(unittest.TestCase):

    def setUp(self) -> None:
        test_data = "ps4,50.00,USD,Amazon\n" \
                    "ps4,25.00,USD,Ebay"

        serializer = CsvCatalogSerializer()

        self.catalog = serializer.get_catalog_from_string(test_data)

    def test_catalog_is_correct(self) -> None:
        expected_items = [
            PriceItem("ps4", Money(50.00, "USD"), "Amazon"),
            PriceItem("ps4", Money(25.00, "USD"), "Ebay")
        ]

        self.assertListEqual(expected_items, self.catalog.items)

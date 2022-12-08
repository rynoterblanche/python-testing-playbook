import pytest

from core.model.price_catalog_aggregate.price_catalog import PriceCatalog
from core.model.price_catalog_aggregate.price_item import PriceItem
from core.model.value_objects.money import Money
from infrastructure.serializers.csv_catalog_serializer import CsvCatalogSerializer


class TestCsvCatalogSerializerGetCatalogFromString:

    @pytest.fixture(scope="class", autouse=True)
    def serialized_catalog(self):
        test_data = "ps4,50.00,USD,Amazon\n" \
                    "ps4,25.00,USD,Ebay"

        serializer = CsvCatalogSerializer()

        catalog = serializer.get_catalog_from_string(test_data)
        return catalog

    def test_catalog_is_correct(self, serialized_catalog: PriceCatalog) -> None:
        expected_items = [
            PriceItem("ps4", Money(50.00, "USD"), "Amazon"),
            PriceItem("ps4", Money(25.00, "USD"), "Ebay")
        ]

        assert expected_items == serialized_catalog.items

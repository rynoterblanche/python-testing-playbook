import pytest

from core.catalog_loader import CatalogLoader
from core.model.price_catalog_aggregate.price_catalog import PriceCatalog
from core.model.price_catalog_aggregate.price_item import PriceItem
from core.model.value_objects.money import Money
from infrastructure.serializers.csv_catalog_serializer import CsvCatalogSerializer
from tests.core.fake_catalog_source import FakeCatalogSource


class TestCatalogLoaderLoad:

    @pytest.fixture(scope="class", autouse=True)
    def loaded_catalog(self):
        test_data = "ps5,100.00,USD,Amazon\n" \
                    "ps5,120.00,USD,Ebay"

        source = FakeCatalogSource(test_data)
        serializer = CsvCatalogSerializer()

        loader = CatalogLoader(source, serializer)
        catalog = loader.load()
        return catalog

    def test_catalog_loaded_correctly(self, loaded_catalog: PriceCatalog) -> None:
        expected_items = [
            PriceItem("ps5", Money(100.00, "USD"), "Amazon"),
            PriceItem("ps5", Money(120.00, "USD"), "Ebay")
        ]

        assert expected_items == loaded_catalog.items

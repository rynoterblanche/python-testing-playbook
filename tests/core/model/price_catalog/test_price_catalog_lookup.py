from src.core.model.price_catalog_aggregate.price_catalog import PriceCatalog
from src.core.model.value_objects.money import Money


class TestPriceCatalogLookup:

    def test_found_item_gets_returned(self, catalog: PriceCatalog):
        # Arrange
        catalog.add("ps5", Money(200.00, "GBP"), "Amazon")

        # Act
        item = catalog.lookup("ps5")[0]

        # Assert
        assert Money(200.00, "GBP") == item.price
        assert "Amazon" == item.seller

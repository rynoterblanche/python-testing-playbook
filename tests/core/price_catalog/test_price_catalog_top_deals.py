from src.core.model.price_catalog_aggregate.price_catalog import PriceCatalog
from src.core.model.value_objects.money import Money


class TestPriceCatalogTopDeals:

    def test_top_deal_by_currency(self, catalog: PriceCatalog):
        # Arrange
        catalog.add("ps5", Money(200.00, "GBP"), "Amazon")
        catalog.add("ps5", Money(199.90, "GBP"), "Argos")
        catalog.add("ps5", Money(90.00, "GBP"), "BlackMarket")

        # Act
        item = catalog.top_deal_by_currency("ps5", "GBP")

        # Assert
        assert 90.00 == item.price.amount
        assert "BlackMarket" == item.seller

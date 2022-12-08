import unittest

from core.model.price_catalog_aggregate.price_catalog import PriceCatalog
from core.model.value_objects.money import Money


class PriceCatalogTopDeals(unittest.TestCase):

    def setUp(self) -> None:
        """Set up fixture(s)"""
        self.catalog = PriceCatalog()

    def tearDown(self) -> None:
        """Set up fixture(s) if needed"""
        pass

    def test_top_deal_by_currency(self):
        # Arrange
        self.catalog.add("ps5", Money(200.00, "GBP"), "Amazon")
        self.catalog.add("ps5", Money(199.90, "GBP"), "Argos")
        self.catalog.add("ps5", Money(90.00, "GBP"), "BlackMarket")

        # Act
        item = self.catalog.top_deal_by_currency("ps5", "GBP")

        # Assert
        self.assertEqual(90.00, item.price.amount)
        self.assertEqual("BlackMarket", item.seller)

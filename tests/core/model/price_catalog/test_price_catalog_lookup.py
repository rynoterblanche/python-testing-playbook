import unittest

from src.core.model.price_catalog_aggregate.price_catalog import PriceCatalog
from src.core.model.value_objects.money import Money


class PriceCatalogLookup(unittest.TestCase):

    def setUp(self) -> None:
        """Set up fixture(s)"""
        self.catalog = PriceCatalog()

    def tearDown(self) -> None:
        """Set up fixture(s) if needed"""
        pass

    def test_found_item_gets_returned(self):
        # Arrange
        self.catalog.add("ps5", Money(200.00, "GBP"), "Amazon")

        # Act
        item = self.catalog.lookup("ps5")[0]

        # Assert
        self.assertEqual(Money(200.00, "GBP"), item.price)
        self.assertEqual("Amazon", item.seller)

import unittest

from core.model.price_catalog_aggregate.price_item import PriceItem
from core.model.value_objects.money import Money


class PriceItemCreation(unittest.TestCase):

    def test_to_string(self):
        test_cases = [
            ("NewB", 12.99, "USD", "Amazon", "Item: NewB, price: 12.99 USD, seller: Amazon"),
            ("XBox", 209.99, "GBP", "Ebay", "Item: XBox, price: 209.99 GBP, seller: Ebay"),
        ]

        for desc, amount, currency, seller, expected_string in test_cases:
            price_item = PriceItem(desc, Money(amount, currency), seller)
            with self.subTest(f"str({price_item}) -> {expected_string}"):
                assert str(price_item) == expected_string

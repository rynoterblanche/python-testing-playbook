import decimal

import pytest

from core.model.price_catalog_aggregate.price_item import PriceItem
from core.model.value_objects.money import Money


class TestPriceItemCreation:

    @pytest.mark.parametrize("desc, amount, currency, seller, expected_string",
                             [
                                 ("NewB", 12.99, "USD", "Amazon", "Item: NewB, price: 12.99 USD, seller: Amazon"),
                                 ("XBox", 209.99, "GBP", "Ebay", "Item: XBox, price: 209.99 GBP, seller: Ebay"),
                             ])
    def test_to_string(self, desc: str, amount: decimal, currency: str, seller: str, expected_string: str):
        price_item = PriceItem(desc, Money(amount, currency), seller)
        assert str(price_item) == expected_string

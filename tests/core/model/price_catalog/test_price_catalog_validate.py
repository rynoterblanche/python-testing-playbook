import pytest

from core.model.exceptions.item_not_found_exception import InvalidCatalogException
from core.model.price_catalog_aggregate.price_catalog import PriceCatalog
from core.model.value_objects.money import Money


class TestPriceCatalogValidate:

    def test_catalog_raises_exception_for_negative_price(self, catalog: PriceCatalog):
        # Arrange
        catalog.add("ps5", Money(-200.00, "GBP"), "Amazon")

        # Act & Assert
        with pytest.raises(InvalidCatalogException):
            catalog.validate()

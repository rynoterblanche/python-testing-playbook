import pytest

from src.core.model.exceptions.item_not_found_exception import InvalidCatalogException
from src.core.model.value_objects.money import Money


class TestPriceCatalogValidate:

    def test_catalog_raises_exception_for_negative_price(self, catalog):
        # Arrange
        catalog.add("ps5", Money(-200.00, "GBP"), "Amazon")

        # Act & Assert
        with pytest.raises(InvalidCatalogException):
            catalog.validate()

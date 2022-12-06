import pytest

from src.core.model.price_catalog_aggregate.price_catalog import PriceCatalog


@pytest.fixture(scope="module")
def catalog():
    """Provides an empty PriceCatalog"""
    return PriceCatalog()
import os

import pytest

from core.catalog_loader import CatalogLoader
from core.model.price_catalog_aggregate.price_catalog import PriceCatalog
from infrastructure.catalog_sources.file_catalog_source import FileCatalogSource
from infrastructure.serializers.csv_catalog_serializer import CsvCatalogSerializer


class TestPriceCatalogLoadsFromFile:

    @pytest.fixture(scope="class", autouse=True)
    def loaded_catalog(self):
        real_path = os.path.realpath(__file__)
        dir_path = os.path.dirname(real_path)
        data_path = os.path.join(dir_path, "fixtures", "test_data.csv")

        source = FileCatalogSource(data_path)
        serializer = CsvCatalogSerializer()

        loader = CatalogLoader(source, serializer)
        catalog = loader.load()
        return catalog

    def test_catalog_loaded(self, loaded_catalog: PriceCatalog) -> None:
        assert 12 == len(loaded_catalog.items)

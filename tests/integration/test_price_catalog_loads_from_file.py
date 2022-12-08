import os
import unittest

from core.catalog_loader import CatalogLoader
from infrastructure.catalog_sources.file_catalog_source import FileCatalogSource
from infrastructure.serializers.csv_catalog_serializer import CsvCatalogSerializer


class PriceCatalogLoadsFromFile(unittest.TestCase):

    def setUp(self) -> None:
        real_path = os.path.realpath(__file__)
        dir_path = os.path.dirname(real_path)
        data_path = os.path.join(dir_path, "fixtures", "test_data.csv")

        source = FileCatalogSource(data_path)
        serializer = CsvCatalogSerializer()

        loader = CatalogLoader(source, serializer)
        self.catalog = loader.load()

    def test_catalog_loaded(self) -> None:
        self.assertEqual(12, len(self.catalog.items))

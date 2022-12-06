from src.core.interfaces.catalog_source import CatalogSource


class FakeCatalogSource(CatalogSource):

    def __init__(self, test_data: str):
        self._test_data = test_data

    def get_catalog_from_source(self) -> str:
        return self._test_data

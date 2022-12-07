from core.interfaces.catalog_source import CatalogSource


class FileCatalogSource(CatalogSource):

    def __init__(self, filepath: str):
        self._filepath = filepath

    def get_catalog_from_source(self) -> str:
        with open(self._filepath, mode='r') as file:
            contents = file.read()
            return contents

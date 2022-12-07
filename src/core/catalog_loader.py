from core.interfaces.catalog_serializer import CatalogSerializer
from core.interfaces.catalog_source import CatalogSource
from core.model.price_catalog_aggregate.price_catalog import PriceCatalog


class CatalogLoader(object):
    def __init__(self, catalog_source: CatalogSource,
                 catalog_serializer: CatalogSerializer):
        self._catalog_source = catalog_source
        self._catalog_serializer = catalog_serializer

    def load(self) -> PriceCatalog:
        catalog_content = self._catalog_source.get_catalog_from_source()
        catalog = self._catalog_serializer.get_catalog_from_string(catalog_content)

        return catalog

from abc import ABC, abstractmethod

from core.model.price_catalog_aggregate.price_catalog import PriceCatalog


class CatalogSerializer(ABC):

    @abstractmethod
    def get_catalog_from_string(self, catalog_string: str) -> PriceCatalog:
        raise NotImplementedError

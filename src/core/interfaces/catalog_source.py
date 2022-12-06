from abc import ABC, abstractmethod


class CatalogSource(ABC):

    @abstractmethod
    def get_catalog_from_source(self) -> str:
        raise NotImplementedError

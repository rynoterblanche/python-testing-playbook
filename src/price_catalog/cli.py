import sys

from src.core.catalog_loader import CatalogLoader
from src.infrastructure.catalog_sources.file_catalog_source import FileCatalogSource
from src.infrastructure.serializers.csv_catalog_serializer import CsvCatalogSerializer


def main(filepath: str, item_desc: str, item_currency: str):
    catalog_source = FileCatalogSource(filepath)
    catalog_serializer = CsvCatalogSerializer()
    loader = CatalogLoader(catalog_source,
                           catalog_serializer)

    catalog = loader.load()
    deal = catalog.top_deal_by_currency(item_desc, item_currency)
    print(f"Best Deal: {deal}")


if __name__ == '__main__':
    filepath = sys.argv[1]
    item_desc = sys.argv[2]
    item_currency = sys.argv[3]

    main(filepath, item_desc, item_currency)

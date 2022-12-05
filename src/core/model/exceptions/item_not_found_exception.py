from typing import List

from src.core.model.exceptions.error_item import ErrorItem


class InvalidCatalogException(Exception):
    def __init__(self, error_items: List[ErrorItem]):
        self._error_items = error_items

    def __str__(self):
        error_list = [f"{err}\n" for err in self._error_items]
        return f"One or more error items found:\n {error_list}"

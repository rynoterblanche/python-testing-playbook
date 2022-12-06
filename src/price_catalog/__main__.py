import sys

from src.price_catalog import cli

filepath = sys.argv[1]
item_desc = sys.argv[2]
item_currency = sys.argv[3]

cli.main(filepath, item_desc, item_currency)

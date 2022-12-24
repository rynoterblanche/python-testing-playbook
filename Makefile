UNIT=python -m unittest discover -s ./tests/unit -t tests -v
INTEGRATION=python -m unittest discover -s ./tests/integration -t tests -v

TEST_PRODUCT=ps5
TEST_CURRENCY=GBP
TEST_PRICE_LIST=./sample_data/prices.csv

setup-env:
	pip install pipenv
	pipenv install
	pipenv shell

install:
	pipenv run python setup.py install

run:
	pipenv run python -m price_catalog $(TEST_PRICE_LIST) $(TEST_PRODUCT) $(TEST_CURRENCY)

unit-test:
	pipenv install --dev
	pipenv run $(UNIT)

integration-test:
	pipenv install --dev
	pipenv run $(INTEGRATION)

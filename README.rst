Python Testing Playbook
#######################

This project is used as a playbook for exploring testing concepts, best practices, frameworks etc.

Use the 'howto/' branches to explore further.

``howto/unit-testing-with-unittest`` is the base branch for unittest exploration.

``howto/unit-testing-with-pytest`` is the base branch for pytest exploration.

(the source code & tests in ``main`` are kept up to date with the unittest branch)


PriceCatalog
============

The example application in this project searches for price bargains - the application takes a given catalog of
items and search criteria to find relevant deals. Each catalog item provides a description, price information as
well as the seller details.

Usage:

    python setup.py install
    python -m price_catalog sample_data/prices.csv ps5 GBP

Running Unit Tests
==================

    python -m unittest discover -s tests -v

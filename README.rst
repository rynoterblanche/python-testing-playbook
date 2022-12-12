Python Testing Playbook
#######################

This project is used as a playbook for exploring testing concepts, best practices, frameworks etc.

Use the ``howto/**`` branches to explore further.

``howto/testing-with-pytest`` is the base branch for pytest exploration.

PriceCatalog
============

The example application in this project searches for price bargains - the application takes a given catalog of
items and search criteria to find relevant deals. Each catalog item provides a description, price information as
well as the seller details.

Usage:

.. code-block:: console

    python setup.py install
    python -m price_catalog sample_data/prices.csv ps5 GBP

Running Tests
=============

.. code-block:: console

    python -m pip install pytest

    # run unit tests
    pytest tests/unit

    # run integration tests
    pytest tests/integration

Using tox for testing
=====================

Installation:

Note - install tox within your global Python interpreter - see `tox installation`_.

.. code-block:: console

    python -m pip install --user tox
    python -m tox --help

Usage:

.. code-block:: console

    # run all
    python -m tox

    # run unit tests
    python -m tox -e unit
    # or
    python -m tox -- tests/unit

    # run integration
    python -m tox -e integration
    # or
    python -m tox -- tests/integration

.. _`tox installation`: https://tox.wiki/en/latest/installation.html
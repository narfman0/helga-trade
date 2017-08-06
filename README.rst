helga-trade
==============

.. image:: https://badge.fury.io/py/helga-trade.png
    :target: https://badge.fury.io/py/helga-trade

.. image:: https://travis-ci.org/narfman0/helga-trade.png?branch=master
    :target: https://travis-ci.org/narfman0/helga-trade

Stock, crypto, forex trade information plugin for helga

Installation
------------

Install via pip::

    pip install helga-trade

And add to settings!

Usage
-----

    !trade help

    !trade btc
    > btc is currently trading at 1234 USD

Development
-----------

Install all the testing requirements::

    pip install -r requirements_test.txt

Run tox to ensure everything works::

    make test

You may also invoke `tox` directly if you wish.

Release
-------

To publish your plugin to pypi, sdist and wheels are (registered,) created and uploaded with::

    make release

License
-------

Copyright (c) 2017 Jon Robison

See LICENSE for details

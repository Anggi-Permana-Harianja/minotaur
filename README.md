
minotaur-trading
=================

Up to date remote data access for pandas, works for multiple versions of pandas.

.. image:: https://img.shields.io/pypi/v/pandas-datareader.svg
    :target: https://pypi.python.org/pypi/pandas-datareader/

.. image:: [https://coveralls.io/github/Anggi-Permana-Harianja/minotaur-trading](https://coveralls.io/github/Anggi-Permana-Harianja/minotaur-trading)badge.svg?branch=master
    :target: [https://coveralls.io/github/Anggi-Permana-Harianja/minotaur-trading](https://coveralls.io/github/Anggi-Permana-Harianja/minotaur-trading)

.. image:: https://codecov.io/gh/Anggi-Permana-Harianja/minotaur-trading/branch/master/graph/badge.svg
  :target: [https://codecov.io/gh/Anggi-Permana-Harianja/minotaur-trading](https://codecov.io/gh/Anggi-Permana-Harianja/minotaur-trading)

Installation
------------

Install using ``pip``

.. code-block:: shell

   pip install minotaur-trading

Usage
-----

.. code-block:: python
  from minotaur_trading.src.simple_chart import simple_chart
  simple = Simple_chart('BBCA.JK')
  df = simple.ingest()
  df = simple.set_ma(100)
  print(df.tail())
  simple.visualize(df,['Open', 'Close'])

Documentation
-------------


Requirements
~~~~~~~~~~~~

Using pandas datareader requires the following packages:

* pandas>=0.23
* lxml
* requests>=2.19.0
* pandas

pandas-datareader

scikit-learn

beautifulsoup4

matplotlib

Building the documentation additionally requires:

* matplotlib
* ipython
* requests_cache
* sphinx
* pydata_sphinx_theme

Development and testing additionally requires:

* black
* coverage
* codecov
* coveralls
* flake8
* pytest
* pytest-cov
* wrapt

Install latest development version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   pip install git+https://github.com/pydata/pandas-datareader.git

or

.. code-block:: shell

   git clone https://github.com/pydata/pandas-datareader.git
   cd pandas-datareader
   python setup.py install

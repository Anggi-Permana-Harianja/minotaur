
minotaur-trading
=================

Up to date remote data access for pandas, works for multiple versions of pandas.

.. image:: https://img.shields.io/pypi/v/minotaur-trading.svg
    :target: https://pypi.python.org/pypi/minotaur-trading/

.. image:: https://coveralls.io/github/Anggi-Permana-Harianja/minotaur-trading/badge.svg?branch=master
    :target: https://coveralls.io/github/Anggi-Permana-Harianja/minotaur-trading
    
.. image:: https://codecov.io/gh/Anggi-Permana-Harianja/minotaur-trading/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/Anggi-Permana-Harianja/minotaur-trading
  
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

* pandas
* pandas-datareader
* scikit-learn
* beautifulsoup4
* matplotlib


Install latest development version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   pip install git+https://github.com/pydata/pandas-datareader.git

or

.. code-block:: shell

   git clone https://github.com/pydata/pandas-datareader.git
   cd pandas-datareader
   python setup.py install

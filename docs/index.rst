Base Converter
==============

Convert base-10 integers and floats to any target base.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   api

Quickstart
----------

.. code-block:: python

   from src import Converter

   converter = Converter(base=2, decimals=[0.5, 1.5, 10])
   print(converter.output())

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

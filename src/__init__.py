"""Base converter library for converting base-10 numbers to any base

Example::

    from src import Converter

    converter = Converter(base=2, decimals=[0.5, 1.5, 10])
    print(converter.output())
"""

from .conversion import Converter

__all__ = ["Converter"]

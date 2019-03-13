.. _implementations:

Implementations
======================

Libraries
------------

Currently, the following FoLiA library implementations exist. Both follow a highly
object-oriented model in which FoLiA XML elements correspond with classes.

* `FoLiApy <https://github.com/proycon/foliapy>`_ - A FoLiA library in Python.
 - `Library documentation and API reference <https://foliapy.readthedocs.io>`_
* `libfolia <https://github.com/LanguageMachines/libfolia>`_ - A FoLiA library in C++.

Both libraries are shipped as part of our `LaMachine <https://proycon.github.io/LaMachine>`_ software
distribution.

Information regarding implementation of certain elements for these two
libraries is present in the status boxes throughout this documentation. The
following table shows the level of FoLiA support in these
libraries:

The following table lists FoLiA library implementations, the last column lists the predecessor of FoLiApy, which was
part of `PyNLPl <https://github.com/proycon/pynlpl>`_.

.. csv-table:: FoLiA Library Implementations
   :file: libraries.csv
   :header-rows: 1

Tools
------------

The following tool collections are available:

* `FoLiA Tools <https://github.com/proycon/foliapy>`_ - A set of Python-based command-line tools for FoLiA processing.
  Contains a validator, convertors, and more.
 - `Tool overview and documentation <https://folia-tools.readthedocs.io>`_
* `FoLiAutils <https://github.com/LanguageMachines/foliautils>`_ - A set of command-line utilities for working with
  FoLiA, powered by libfolia.


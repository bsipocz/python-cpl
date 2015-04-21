python-cpl
==========

*Python interface for the Common Pipeline Library*

.. image:: https://pypip.in/v/python-cpl/badge.png
    :target: https://pypi.python.org/pypi/python-cpl

.. image:: https://travis-ci.org/olebole/python-cpl.png
    :target: https://travis-ci.org/olebole/python-cpl

This module can list, configure and execute 
CPL-based recipes from Python.
The input, calibration and output data can be specified as FITS files
or as [`astropy.io.fits`](http://www.astropy.org) objects in memory.

The [Common Pipeline Library](http://www.eso.org/sci/software/cpl/) (CPL)
comprises a set of ISO-C libraries that provide a comprehensive, efficient and
robust software toolkit. It forms a basis for the creation of automated
astronomical data-reduction tasks. One of the features provided by the CPL is
the ability to create data-reduction algorithms that run as plugins (dynamic
libraries). These are called "recipes" and are one of the main aspects of the
CPL data-reduction development environment.

The interface may be used to run ESO pipeline recipes linked to CPL 
versions 4.0 to 6.3.1.

Build instructions
------------------

python-cpl requires:

 * Python 2.6 or later
 * [Astropy](http://www.astropy.org) or [Pyfits](http://www.stsci.edu/institute/software_hardware/pyfits)

python-cpl uses the standard Python distutils system to build and install
itself.  From the command line run::

    python setup.py install

to install python-cpl.
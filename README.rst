********
FuncAttr
********

.. image:: https://img.shields.io/pypi/v/funcattr.svg
   :alt: Last release
   :target: https://pypi.python.org/pypi/funcattr

.. image:: https://img.shields.io/pypi/pyversions/funcattr.svg
   :alt: Python version
   :target: https://pypi.python.org/pypi/funcattr

.. image:: https://img.shields.io/readthedocs/funcattr.svg
   :alt: Documentation
   :target: https://funcattr.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/github/actions/workflow/status/kalekundert/funcattr/test.yml?branch=master
   :alt: Test status
   :target: https://github.com/kalekundert/funcattr/actions

.. image:: https://img.shields.io/coveralls/kalekundert/funcattr.svg
   :alt: Test coverage
   :target: https://coveralls.io/github/kalekundert/funcattr?branch=master

.. image:: https://img.shields.io/github/last-commit/kalekundert/funcattr?logo=github
   :alt: Last commit
   :target: https://github.com/kalekundert/funcattr

FuncAttr provides a simple decorator that assigns attributes to functions.  For 
example, if you have several different functions for analyzing the same data, 
you might use this library to give each a descriptive title to be used in 
downstream plotting routines.  Of course, it isn't difficult to assign 
attributes like these to functions without a decorator, but such assignments 
must happen after the function body and can be easy to lose track of.  A 
decorator puts these labels at the beginning of the function, and can never be 
accidentally separated from the function as the code is refactored.

Installation
============
FuncAttr is available on PyPI::

  $ pip install funcattr

Usage
=====
Here's how to use the decorator::

  from funcattr import annotate

  @annotate(title="Do Spam")
  def do_spam():
      pass

  print(do_spam.title)  # Do Spam

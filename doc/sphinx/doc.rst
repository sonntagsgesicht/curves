
.. py:module:: curves

.. module:: curves
    :noindex:

-----------------
API Documentation
-----------------

.. toctree::
    :glob:

Curve
=====

.. autoclass::  Curve

for more examples see :ref:`tutorial`


.. autofunction:: init

for more examples see :ref:`tutorial`


Plotting Curves
===============

.. autofunction:: lin

.. autofunction:: plot

for more examples see :ref:`tutorial`

.. autofunction:: plotter

for more examples see :ref:`tutorial`


Predefined Curves
=================

The *functions* subpackage provides standard function as predefined in
standard package **math**. For instance

.. autofunction:: curves.functions.exp
.. autofunction:: curves.functions.log
.. autofunction:: curves.functions.sin
.. autofunction:: curves.functions.cos
.. autofunction:: curves.functions.tan
.. autofunction:: curves.functions.gamma

for more examples see :ref:`tutorial`


and more may ...
(actually any function in **math** that may be invoked with a float value).

Mathematical constants like **pi** or **e** define constant functions.

.. autofunction:: curves.functions.e
.. autofunction:: curves.functions.pi

In addition, there is the
`ramp <https://en.wikipedia.org/wiki/Ramp_function>`_ function and
`step <https://en.wikipedia.org/wiki/Heaviside_step_function>`_ function, too.

.. autofunction:: curves.functions.ramp
.. autofunction:: curves.functions.step

for more examples see :ref:`tutorial`


Numerical Operators
===================

.. autoclass::  curves.operators.Integral

for more examples see :ref:`tutorial`


.. autoclass::  curves.operators.Derivative

for more examples see :ref:`tutorial`



Numerical Operations
====================

.. automodule::  curves.numerics

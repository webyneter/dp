=============================
dp
=============================

.. image:: https://badge.fury.io/py/dp.svg
    :target: https://badge.fury.io/py/dp

.. image:: https://travis-ci.org/webyneter/dp.svg?branch=master
    :target: https://travis-ci.org/webyneter/dp

.. image:: https://codecov.io/gh/webyneter/dp/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/webyneter/dp

dp

Documentation
-------------

The full documentation is at https://dp.readthedocs.io.

Quickstart
----------

Install dp::

    pip install dp

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dp.apps.DpConfig',
        ...
    )

Add dp's URL patterns:

.. code-block:: python

    from dp import urls as dp_urls


    urlpatterns = [
        ...
        url(r'^', include(dp_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage

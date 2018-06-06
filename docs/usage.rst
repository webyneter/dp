=====
Usage
=====

To use dp in a project, add it to your `INSTALLED_APPS`:

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

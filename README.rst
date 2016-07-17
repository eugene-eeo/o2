o2
==

.. image:: https://travis-ci.org/eugene-eeo/o2.svg?branch=master
    :target: https://travis-ci.org/eugene-eeo/o2

A dead simple Python module for checking if files have changed without
resorting to ``stat`` calls. Usage example:

.. code-block:: python

    >>> from o2 import Index
    >>> index = Index('/path/to/db.db')
    >>> open('file.txt', 'w').write('a')

    >>> index.index(['file.txt'])
    >>> open('file.txt', 'w').write('b')

    >>> index.changed
    {'file.txt'}

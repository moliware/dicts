dicts
=====

All kind of dictionaries you always think but never do. 

Check the full documentation site_

Instalation
-----------

To install dicts form Pypi: ::

  easy_install dicts

or ::

  pip install dicts

if you want to install it from source code: ::

  python setup.py install


Usage
-----

Dictionaries Features
.....................

* join:

    >>> d1 = Dict({1 : 7, 2 : [1,2], 3 : 'a'})
    >>> d1.join({1 : 2, 2 : [3], 3 : 'b'})
    {1: 9, 2: [1, 2, 3], 3: 'ab'}

* map:

    >>> d = Dict({'1' : 1, '2' : 2})
    >>> d.map(lambda x: 1/3.0)
    >>> d
    {'1': 0.3333333333333333, '2': 0.3333333333333333}

* fromrepetitions:

    >>> Dict.fromrepetitions([1,1,1,1,2])
    {1: 4, 2: 1}

* relookup:

    >>> d = Dict({'1': 1, '2' : 2, 'c' : 3})
    >>> d.relookup('\d')
    [('1', 1), ('2', 2)]

Especific dictionaries
......................

* SortedDict family

* NoCaseDict

* RegexpDict

.. _site: http://dicts.moliware.com
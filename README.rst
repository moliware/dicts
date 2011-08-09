dicts
=====

All kind of dictionaries you always think but never do.

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

- join:

    >>> d1 = Dict({1 : 7, 2 : [1,2], 3 : 'a'})
    >>> d1.join({1 : 2, 2 : [3], 3 : 'b'})
    {1: 9, 2: [1, 2, 3], 3: 'ab'}
   


Especific dictionaries
......................

- KeySortedDict:

    >>> ksd = KeySortedDict({'c' : 1, 'a' : 6, 'b' : 5})
    >>> ksd.items()
    [('a', 6), ('b', 5), ('c', 1)]
    >>> ksd.keys()
    ['a', 'b', 'c']
    >>> ksd.values()
    [6, 5, 1]

- ValueSortedDict

    >>> vsd = ValueSortedDict({'c' : 1, 'a' : 6, 'b' : 5})
    >>> vsd.items()
    [('c', 1), ('b', 5), ('a', 6)]
    >>> vsd.keys()
    ['c', 'b', 'a']
    >>> vsd.values()
    [1, 5, 6]

- SortedDict

    >>> sd = SortedDict({'c' : (1,'b'), 'a' : (6,'c'), 'b' : (5,'a')}, key=lambda x: x[1][1])
    >>> sd.items()
    [('b', (5, 'a')), ('c', (1, 'b')), ('a', (6, 'c'))]
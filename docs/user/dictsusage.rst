.. _dictsusage:

Ditionaries Usage
=================

.. module:: dicts

Dict
----

.. automethod:: Dict.join(dic)

    >>> d1 = Dict({1 : 7, 2 : [1,2], 3 : 'a'})
    >>> d1.join({1 : 2, 2 : [3], 3 : 'b'})
    {1: 9, 2: [1, 2, 3], 3: 'ab'}

.. automethod:: Dict.map(callable)

    >>> d = Dict({'1' : 1, '2' : 1})
    >>> d.map(lambda x: x/3.0)
    >>> d
    {'1': 0.3333333333333333, '2': 0.3333333333333333}

.. automethod:: Dict.fromrepetitions(iterable)

    >>> Dict.fromrepetitions([1,1,1,1,2])
    {1: 4, 2: 1}



SortedDict
----------

.. autoclass:: SortedDict

    >>> sd = SortedDict({'c' : (1,'b'), 'a' : (6,'c'), 'b' : (5,'a')}, key=lambda x: x[1][1])
    >>> sd.items()
    [('b', (5, 'a')), ('c', (1, 'b')), ('a', (6, 'c'))]



KeySortedDict
-------------

.. autoclass:: KeySortedDict

    >>> ksd = KeySortedDict({'c' : 1, 'a' : 6, 'b' : 5})
    >>> ksd.items()
    [('a', 6), ('b', 5), ('c', 1)]
    >>> ksd.keys()
    ['a', 'b', 'c']
    >>> ksd.values()
    [6, 5, 1]


ValueSortedDict
---------------

.. autoclass:: ValueSortedDict

    >>> vsd = ValueSortedDict({'c' : 1, 'a' : 6, 'b' : 5})
    >>> vsd.items()
    [('c', 1), ('b', 5), ('a', 6)]
    >>> vsd.keys()
    ['c', 'b', 'a']
    >>> vsd.values()
    [1, 5, 6]


NoCaseDict
----------

.. autoclass:: NoCaseDict

    >>> ncd = NoCaseDict({'examPLE' : 1})
    >>> 'example' in ncd
    True


Coming Soon
===========

BiDict
------

Keys and values are uniques.

RegexpDict
----------

Keys are regular expressions.

# -*- coding: utf-8 -*-

"""
 Dictiories that are sorted when they are iterated

 KeySortedDict:

 >>> ksd = KeySortedDict({'c' : 1, 'a' : 6, 'b' : 5})
 >>> ksd.items()
 [('a', 6), ('b', 5), ('c', 1)]
 >>> ksd.keys()
 ['a', 'b', 'c']
 >>> ksd.values()
 [6, 5, 1]

 ValueSortedDict

 >>> vsd = ValueSortedDict({'c' : 1, 'a' : 6, 'b' : 5})
 >>> vsd.items()
 [('c', 1), ('b', 5), ('a', 6)]
 >>> vsd.keys()
 ['c', 'b', 'a']
 >>> vsd.values()
 [1, 5, 6]

 SortedDict

 >>> sd = SortedDict({'c' : (1,'b'), 'a' : (6,'c'), 'b' : (5,'a')}, key=lambda x: x[1][1])
 >>> sd.items()
 [('b', (5, 'a')), ('c', (1, 'b')), ('a', (6, 'c'))]

 author : Miguel Olivares <miguel@moliware.com>
"""

from dict import Dict

class SortedDict(Dict):
    """ Dictionary that iterates over its elements """

    def __init__(self, data={}, cmp=None, key=None, reverse=False):
        super(SortedDict, self).__init__(data)
        self.cmp = cmp
        self.key = key
        self.reverse= reverse

    def __iter__(self):
        """ Sort and then iterate the dictionary """
        sorted_data = sorted(self.data.iteritems(), self.cmp, self.key,
                             self.reverse)
        for k,v in sorted_data:
            yield k,v

    def iteritems(self):
        for x in self.__iter__():
            yield x

    def items(self):
        return [x for x in self.iteritems()]

    def iterkeys(self):
        for k,v in self.__iter__():
            yield k

    def keys(self):
        return [k for k in self.iterkeys()]

    def itervalues(self):
        for k,v in self.__iter__():
            yield v

    def values(self):
        return [v for v in self.itervalues()]

class KeySortedDict(SortedDict):
    """ Dictionary sorted by key """
    def __init__(self, data={}, reverse=False):
        """ """
        super(KeySortedDict, self).__init__(data, reverse=reverse)

class ValueSortedDict(SortedDict):
    """ Dictionary sorted by value """
    def __init__(self, data={}, reverse=False):
        """ """
        super(ValueSortedDict, self).__init__(data, key=lambda x:x[1],
                                               reverse=reverse)
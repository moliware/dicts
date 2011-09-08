# -*- coding: utf-8 -*-
"""
    dict.sorteddict
    ~~~~~~~~~~~~~~~

    Dictionaries that are sorted when they are iterated

    :copyright: (c) 2011 by  Miguel Olivares <miguel@moliware.com>.
    :license: LGPL, see LICENSE for more details.
"""
from dict import Dict


class SortedDict(Dict):
    """ Dictionary that iterates over its elements. """

    def __init__(self, data={}, cmp=None, key=None, reverse=False):
        """
        :param data: dictionary
        :param cmp: comparison function
        :param key: function to extract comparison key
        :param reverse: reverse order
        """
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

    def __getslice__(self, i, j):
        return type(self)(self.items()[i:j])

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
        """
        :param data: dictionary
        :param reverse: reverse order
        """
        super(KeySortedDict, self).__init__(data, reverse=reverse)


class ValueSortedDict(SortedDict):
    """ Dictionary sorted by value """

    def __init__(self, data={}, reverse=False):
        """
        :param data: dictionary
        :param reverse: reverse order
        """
        super(ValueSortedDict, self).__init__(data, key=lambda x:x[1],
                                               reverse=reverse)
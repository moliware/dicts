# -*- coding: utf-8 -*-
"""
    dicts.dict
    ~~~~~~~~~~

    Extends UserDict to implement some awesome features

    :copyright: (c) 2011 by  Miguel Olivares <miguel@moliware.com>.
    :license: LGPL, see LICENSE for more details.
"""
import re
from copy import deepcopy
from UserDict import UserDict


class Dict(UserDict, object):
    """ Iterable UserDict. It is thought for being
    the base class of all specific dictionaries.
    """

    def __iter__(self):
        """ Iterable dictionary! """
        return self.data.iteritems()

    def join(self, dic):
        """ Add dic pairs to self.data """
        for k,v in dic.iteritems():
            if k in self.data:
                self[k] += dic[k]
            else:
                self[k] = deepcopy(v)
        return self

    def map(self, callable):
        """ Apply 'callable' function over all values. """
        for k,v in self.iteritems():
            self[k] = callable(v)

    @classmethod
    def fromrepetitions(cls, iterable):
        """ Create a dict whose keys are the members of the iterable and values
        are the number of times the key appears in the iterable.
        """
        d = cls()
        for key in iterable:
            d[key] = d[key] + 1 if key in d else 1
        return d

    def relookup(self, pattern):
        """ Dictionary lookup with a regular expression. Return pairs whose key 
        matches pattern.
        """
        key = re.compile(pattern)
        return filter(lambda x : key.match(x[0]), self.data.items())
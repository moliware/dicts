# -*- coding: utf-8 -*-

"""
 Extends UserDict to implement some awesome features

 iterable:

 >>> d = Dict({1 : 2, 2 : 3})
 >>> for k,v in d:
 >>>     print k,v
 1 2
 2 3

 join:

 >>> d = Dict({1 : 2})
 >>> d.join({1 : 3})
 {1: 5}

 >>> d = Dict({1 : 2})
 >>> d.join({1 : [3]})
 {1: [2, 3]}

 author : Miguel Olivares <miguel@moliware.com>
"""
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

    @classmethod
    def fromrepetitions(cls, iterable):
        """ Create a dict whose keys are the members of the iterable and values
        are the number of times the key appears in the iterable.
        """
        d = cls()
        for key in iterable:
            d[key] = d[key] + 1 if key in d else 1
        return d

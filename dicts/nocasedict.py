# -*- coding: utf-8 -*-

"""
 Keys of the dictionary are case insensitive.

 Command line Usage:

 >>> ncd = NoCaseDict({'examPLE' : 1})
 >>> 'example' in ncd
 True

 author : Miguel Olivares <miguel@moliware.com>
"""

from dict import Dict


class NoCaseDict(Dict):
    """ Keys of the dictionary are case insensitive. """

    def __init__(self, data):
        correct_keys = reduce(lambda x, y: x and isinstance(y, basestring),
                              data.iterkeys(), True)
        if not correct_keys:
            raise KeyError
        super(NoCaseDict, self).__init__(dict(map(lambda x : (x[0].lower(), x[1]), data.items())))

    def __setitem__(self, key, value):
        if not isinstance(key, basestring):
            raise KeyError
        super(NoCaseDict, self).__setitem__(key.lower(), value)

    def __contains__ (self, key):
        if not isinstance(key, basestring):
            raise KeyError
        return super(NoCaseDict, self).__contains__(key.lower())
        
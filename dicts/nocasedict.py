# -*- coding: utf-8 -*-
"""
    dicts.nocasedict
    ~~~~~~~~~~~~~~~~

    Keys of the dictionary are case insensitive.

    :copyright: (c) YEAR by  Miguel Olivares.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""
from dict import Dict


class NoCaseDict(Dict):
    """ Keys of the dictionary are case insensitive. """

    def __init__(self, data):
        """
        :param data: dictionary
        """
        correct_keys = reduce(lambda x, y: x and isinstance(y, basestring),
                              data.iterkeys(), True)
        if not correct_keys:
            raise KeyError
        lower_dict = dict(map(lambda x : (x[0].lower(), x[1]), data.items()))
        super(NoCaseDict, self).__init__(lower_dict)

    def __setitem__(self, key, value):
        if not isinstance(key, basestring):
            raise KeyError
        super(NoCaseDict, self).__setitem__(key.lower(), value)

    def __contains__ (self, key):
        if not isinstance(key, basestring):
            raise KeyError
        return super(NoCaseDict, self).__contains__(key.lower())
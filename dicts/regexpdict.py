# -*- coding: utf-8 -*-
"""
    dicts.regexpdict
    ~~~~~~~~~~~~~~~~

    Dictionary whose keys are regular expressions

    :copyright: (c) 2011 by  Miguel Olivares.
    :license: LGPL, see LICENSE for more details.
"""
from dict import Dict
import re


class RegexpDict(Dict):
    """ Keys are regular expressions. """

    def __init__(self, data={}):
        super(RegexpDict, self).__init__(data)

    def __getitem__(self, key):
        """ Returned all values that match key """
        assert(isinstance(key, basestring))
        return [v for k,v in self.iteritems() if re.match(k, key)]

    def __setitem__(self, key, value):
        assert(isinstance(key, basestring))
        return super(RegexpDict, self).__setitem__(key, value)
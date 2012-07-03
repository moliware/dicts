# -*- coding: utf-8 -*-
"""
    dicts.regexpdict
    ~~~~~~~~~~~~~~~~

    Dictionary whose keys are regular expressions

    :copyright: (c) 2011 by  Miguel Olivares.
    :license: LGPL, see LICENSE for more details.
"""
import re

from dict import Dict
from operator import or_


class RegexpDict(Dict):
    """ Keys are regular expressions. """

    def __init__(self, data={}, *flags):
        super(RegexpDict, self).__init__(data)
        self.flags = reduce(or_, flags, 0)

    def __getitem__(self, key):
        """ Returned all values that match key """
        assert(isinstance(key, basestring))
        return [v for k,v in self.iteritems() if re.match(k, key, self.flags)]

    def __setitem__(self, key, value):
        assert(isinstance(key, basestring))
        return super(RegexpDict, self).__setitem__(key, value)
# -*- coding: utf-8 -*-


import unittest
from dicts import RegexpDict


class RegexpDictTestCase(unittest.TestCase):
    """ Dict features test cases."""

    def setUp(self):
        self.d = RegexpDict({'\d+' : 1, '\w+': 2})

    def tearDown(self):
        pass

    def test_getitem(self):
        self.assertEquals(self.d['1'], [1, 2])
        self.assertEquals(self.d['abc'], [2])

if __name__ == '__main__':
    unittest.main()
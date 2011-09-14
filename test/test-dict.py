# -*- coding: utf-8 -*-


import unittest
from dicts import Dict



class DictTestCase(unittest.TestCase):
    """ Dict features test cases."""

    def setUp(self):
        self.d = Dict({1 : 7, 2 : [1,2], 3 : 'a'})

    def tearDown(self):
        pass

    def test_join(self):
        self.d.join(Dict({1 : 2, 2 : [3], 3 : 'b'}))
        self.assertEqual(self.d.items(), [(1, 9), (2, [1, 2, 3]), (3, 'ab')])

    def test_lookup(self):
        d = Dict()
        d['1'] = 10
        d['2'] = 20
        d['a'] = 30
        self.assertEqual(d.relookup('\d+'), [('1', 10), ('2', 20)])

if __name__ == '__main__':
    unittest.main()
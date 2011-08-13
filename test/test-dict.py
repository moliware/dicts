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

if __name__ == '__main__':
    unittest.main()
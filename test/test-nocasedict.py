# -*- coding: utf-8 -*-


import unittest
from dicts import NoCaseDict



class DictTestCase(unittest.TestCase):
    """ Dict features test cases."""

    def setUp(self):
        self.d = NoCaseDict({'KeY1' : 1})

    def tearDown(self):
        pass

    def test_contains(self):
        self.assertIn('key1', self.d)

if __name__ == '__main__':
    unittest.main()
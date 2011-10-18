# -*- coding: utf-8 -*-


import unittest
from dicts import SortedDict



class SortedDictTestCase(unittest.TestCase):
    """SortedDict test cases."""

    def setUp(self):
        self.sd = SortedDict({'c' : (1,'b'), 'a' : (6,'c'), 'b' : (5,'a')},
                             key=lambda x: x[1][1])

    def tearDown(self):
        pass

    def test_items(self):
        self.assertEqual(self.sd.items(),
                         [('b', (5, 'a')), ('c', (1, 'b')), ('a', (6, 'c'))])

    def test_keys(self):
        self.assertEqual(self.sd.keys(), ['b', 'c', 'a'])

    def test_values(self):
        self.assertEqual(self.sd.values(), [(5, 'a'), (1, 'b'), (6, 'c')])

    def test_iteration(self):
        d1 = dict(a=1)
        d2 = SortedDict(d1)
        self.assertEqual([x for x in d1], [x for x in d2])


if __name__ == '__main__':
    unittest.main()
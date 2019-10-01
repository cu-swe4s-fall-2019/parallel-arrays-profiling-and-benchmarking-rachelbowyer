import unittest
import plot_gtex
import string
import random
import numpy as np
import argparse
from os import path


class TestPlotGtex(unittest.TestCase):
    """tests of the plot_gtex script"""

    def test_linear_search(self):
        """test if linear search works"""
        for j in range(10):  # including rand interation
            r = []
            for i in range((10)):
                r = r + [random.choice(string.ascii_letters)]
                rset = list(dict.fromkeys(r).keys())

            aa_indx = random.randint(0, len(rset)-1)
            rset[aa_indx] = 'aa'

            rr = plot_gtex.linear_search('aa', rset)
            self.assertEqual(rr, aa_indx)

    def test_linear_search_when_not_in_list(self):
        """test if linear search returns -1 when entry not in lst"""
        for j in range(10):  # including rand interation
            r = []
            for i in range((10)):
                r = r + [random.choice(string.ascii_letters)]
                rset = list(dict.fromkeys(r).keys())

            rr = plot_gtex.linear_search('aa', rset)
            self.assertEqual(rr, -1)

    def test_binary_search(self):
        """test if binary search works"""
        for j in range(10):  # including rand interation
            D = []
            for i in range(10):
                D.append(['Thing %s' % i, i])

            index = random.randint(0, len(D)-1)
            name = 'Thing ' + str(index)
            r = plot_gtex.binary_search(name, D)
            self.assertEqual(r, index)

    def test_binary_search_when_not_in_list(self):
        """test if binary search returns -1 when entry not in lst"""
        for j in range(10):  # including rand interation
            D = []
            for i in range(10):
                D.append(['Thing %s' % i, i])

            index = len(D)
            name = 'Thing ' + str(index)
            r = plot_gtex.binary_search(name, D)
            self.assertEqual(r, -1)


if __name__ == '__main__':
    unittest.main()
    if path.exists("./ACTA2.png") is True:
        os.remove('./ACTA2.png')

# coding=utf-8
import sys
sys.path.append('../lib')
import unittest
from math_functions import *

class testMath(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(addition_fn(5,5),10)


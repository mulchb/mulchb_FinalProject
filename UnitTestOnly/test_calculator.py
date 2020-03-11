import sys
from unittest import TestCase
import random

from UnitTestOnly import calculator


class test_Multiplication(TestCase):

    def test_multiplication(self):
        self.assertEqual(calculator.Multiplication(112799, 19038), 2147467362)
        self.assertEqual(calculator.Multiplication(112799, -19038), -2147467362)
        self.assertEqual(calculator.Multiplication(-112799, 19038), -2147467362)
        self.assertEqual(calculator.Multiplication(112799, 19038), 2147467362)
        self.assertEqual(calculator.Multiplication(10 / 13, 15 / 10), 150 / 130)
        self.assertEqual(calculator.Multiplication(.00000123, 1 / 10000), .000000000123)
        self.assertEqual(calculator.Multiplication(-1, -1), 1)
        self.assertEqual(calculator.Multiplication(-1, 1), -1)
        self.assertEqual(calculator.Multiplication(1, 1), 1)

    def random_testing(self):
        random.random()
        for i in range(0, 10):
            a = random.randint(-(2 ^ 15), 2 ^ 16)
            b = random.randint(-(2 ^ 15), 2 ^ 16)
            self.assertEqual(calculator.Multiplication(a, b), (a * b))


class test_Division(TestCase):

    def test_division(self):
        self.assertEqual(calculator.Division(112799, 19038), 112799 / 19038)
        self.assertEqual(calculator.Division(112799, -19038), 112799 / -19038)
        self.assertEqual(calculator.Division(-112799, 19038), -112799 / 19038)
        self.assertEqual(calculator.Division(-112799, -19038), (-112799) / (-19038))
        self.assertEqual(calculator.Division(10 / 13, 15 / 10), 100 / (13 * 15))
        self.assertEqual(calculator.Division(.00000123, 1 / 10000), .000000000123)
        self.assertEqual(calculator.Division(-1, -1), 1)
        self.assertEqual(calculator.Division(-1, 1), -1)
        self.assertEqual(calculator.Division(1, 1), 1)
        self.assertEqual((calculator.Division(0, 100)), 0)
        self.assertEqual((calculator.Division(0, 0)), None)
        self.assertEqual((calculator.Division(1, 0)), None)

    def random_testing(self):
        random.random()
        for i in range(0, 10):
            a = random.randint(-(2 ^ 15), 2 ^ 16)
            b = random.randint(-(2 ^ 15), 2 ^ 16)
            if b != 0:
                self.assertEqual(calculator.Division(a, b), (a / b))


class test_Square_Root(TestCase):
    def constant_testing(self):
        self.assertEqual(calculator.Square_Root(2147467362), 2147467362 ** .5)
        self.assertEqual(calculator.Square_Root(150 / 130), (150 / 130) ** .5)
        self.assertEqual(calculator.Square_Root(1.01230678911), 1.01230678911 ** (1 / 2))
        self.assertEqual(calculator.Square_Root(.00000123), .00000123 ** .5)
        self.assertEqual(calculator.Square_Root(0), 0)
        self.assertEqual(calculator.Square_Root(-1), None)
        self.assertEqual(calculator.Square_Root(-0), None)
        self.assertEqual(calculator.Square_Root(-0.000010101), None)

    def random_testing(self):
        random.random()
        for i in range(0, 10):
            a = random.randint(0, 2 ^ 16)
            self.assertEqual(calculator.Square_Root(a), a ** (1 / 2))

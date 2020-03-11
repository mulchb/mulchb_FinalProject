import math
from unittest import TestCase
import random

from UnitTestOnly import calculator


class test_Multiplication(TestCase):

    def test_constant(self):
        self.assertEqual(calculator.Multiplication(112799, 19038),
                         2147467362)  # which is approximately 2^31 which is the size of 4 bytes
        self.assertEqual(calculator.Multiplication(112799, -19038), -2147467362)
        self.assertEqual(calculator.Multiplication(-112799, 19038), -2147467362)
        self.assertEqual(calculator.Multiplication(112799, 19038), 2147467362)
        self.tEqual(calculator.Multiplication(10 / 13, 15 / 10), 150 / 130)
        self.assertEqual(calculator.Multiplication(.00000123, 1 / 10000), .000000000123)
        self.assertEqual(calculator.Multiplication(-1, -1), 1)
        self.assertEqual(calculator.Multiplication(-1, 1), -1)
        self.assertEqual(calculator.Multiplication(1, 1), 1)

    def test_random_testing(self):
        random.random()
        for i in range(0, 30):
            a = random.randint(-(2 ** 15) + 1, (2 ** 16) - 1)
            # Apparently python doesnt have a MAX or MIN integer so i just did it to fit
            # inside a word
            b = random.randint(-(2 ** 15), 2 ** 16)
            self.assertEqual(calculator.Multiplication(a, b), (a * b))


class test_Division(TestCase):

    def test_division(self):
        self.assertEqual(calculator.Division(112799, 19038), 112799 / 19038)
        assertEqual(calculator.Division(112799, -19038), 112799 / -19038)
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

    def test_random_testing(self):
        random.random()
        for i in range(0, 30):
            a = random.randint(-(2 ** 15), 2 ** 16)
            b = random.randint(-(2 ** 15), 2 ** 16)
            if b != 0:
                self.assertEqual(calculator.Division(a, b), (a / b))


class test_Square_Root(TestCase):
    def test_constant_testing(self):
        self.assertEqual(calculator.Square_Root(2147467362), 2147467362 ** .5)
        self.assertEqual(calculator.Square_Root(150 / 130), (150 / 130) ** .5)
        self.assertEqual(calculator.Square_Root(1.01230678911), 1.01230678911 ** (1 / 2))
        self.assertEqual(calculator.Square_Root(.00000123), .00000123 ** .5)
        self.assertEqual(calculator.Square_Root(0), 0)
        self.assertEqual(calculator.Square_Root(-1), None)
        self.assertEqual(calculator.Square_Root(-0), None)
        self.assertEqual(calculator.Square_Root(-0.000010101), None)

    def test_test_random_testing(self):
        random.random()
        for i in range(0, 30):
            a = random.randint(0, 2 ** 16)
            self.assertEqual(calculator.Square_Root(a), a ** (1 / 2))


class test_squared(TestCase):
    def test_constant_testing(self):
        self.assertEqual(calculator.Squared(46340), 46340 ** 2)
        self.assertEqual(calculator.Squared(-46340), 46340 ** 2)
        self.assertEqual(calculator.Squared(15 / 13), (15 / 13) ** 2)
        self.assertEqual(calculator.Squared(1.012306789), 1.012306789 ** 2)
        self.assertEqual(calculator.Squared(.00000123), .00000123 ** 2)
        self.assertEqual(calculator.Squared(0), 0 ** 2)

    def test_random_testing(self):
        random.random()
        for i in range(0, 30):
            a = random.randint(-(2 ** 15), 2 ** 16)
            self.assertEqual(calculator.Squared(a), a ** (1 / 2))


class test_One_Div_X(TestCase):
    def test_constant_testing(self):
        self.assertEqual(calculator.One_Div_X(2 ** 31), (2 ** 31) ** -1)
        self.assertEqual(calculator.One_Div_X(-(2 ** 31)), -(2 ** 31) ** -1)
        self.assertEqual(calculator.One_Div_X(15 / 13), (15 / 13) ** -1)
        self.assertEqual(calculator.One_Div_X(1.012306789), 1.012306789 ** -1)
        self.assertEqual(calculator.One_Div_X(.00000123), .00000123 ** -1)
        self.assertEqual(calculator.One_Div_X(-1), -1)
        self.assertEqual(calculator.One_Div_X(0), None)

    def test_random_testing(self):
        random.random()
        for i in range(0, 30):
            a = random.randint(-(2 ** 15), 2 ** 16)
            if a != 0:  # If a = 0 answer = None != what a ** (-1) equals
                self.assertEqual(calculator.One_Div_X(a), a ** (-1))


class test_Factorial(TestCase):
    def test_constant_testing(self):
        self.assertEqual(calculator.Factorial(12), math.factorial(12))
        self.assertEqual(calculator.Factorial(11), math.factorial(11))
        self.assertEqual(calculator.Factorial(9), math.factorial(9))
        self.assertEqual(calculator.Factorial(5), math.factorial(5))
        self.assertEqual(calculator.Factorial(3), math.factorial(3))
        self.assertEqual(calculator.Factorial(1), math.factorial(1))
        self.assertEqual(calculator.Factorial(5 / 7), None)
        self.assertEqual(calculator.Factorial(-10))

    def test_random_testing(self):
        random.random()
        for i in range(0, 30):
            a = random.randint(0, 100)
            self.assertEqual(calculator.Factorial(a), math.factorial(a))


class test_Absolute_Value(TestCase):
    def test_constant_testing(self):
        self.assertEqual(calculator.Absolute_Value(2 ** 31), 2 ** 31)
        self.assertEqual(calculator.Absolute_Value(-(2 ** 31)), 2 ** 31)
        self.assertEqual(calculator.Absolute_Value(19.123456789), 19.123456789)
        self.assertEqual(calculator.Absolute_Value(-1700.321321329999), 1700.321321329999)
        self.assertEqual(calculator.Absolute_Value(.00000123), .00000123)
        self.assertEqual(calculator.Absolute_Value(-.00000123), -.00000123)
        self.assertEqual(calculator.Absolute_Value(-0), 0)
        self.assertEqual(calculator.Absolute_Value(-3 / 2), 3 / 2)
        self.assertEqual(calculator.Absolute_Value(-3 / -2), 3 / 2)
        self.assertEqual(calculator.Absolute_Value(5 / -2), 5 / 2)

    def test_random_testing(self):
        random.random()
        for i in range(0, 30):
            a = random.randint(-2 ** 15, 2 ** 16)
            self.assertEqual(calculator.Absolute_Value(a), abs(a))


class test_Sin(TestCase):
    def test_constant_testing(self):
        self.assertEqual(calculator.Sin(2 ** 31), math.sin(2 ** 31))
        self.assertEqual(calculator.Sin(-2 ** 31), math.sin(-2 ** 31))
        self.assertEqual(calculator.Sin(1.132321), math.sin(1.132321))
        self.assertEqual(calculator.Sin(-3.14), math.sin(-3.14))
        self.assertEqual(calculator.Sin(0), 0)
        self.assertEqual(calculator.Sin(-3 / -2), math.sin(-3 / -2))
        self.assertEqual(calculator.Sin(-3 / 2), math.sin(-3 / 2))
        self.assertEqual(calculator.Sin(-3 / -2), math.sin(-3 / -2))
        self.assertEqual(calculator.Sin(5 / -2), math.sin(5 / -2))
        self.assertEqual(calculator.Sin(math.pi / 2), math.sin(math.pi / 2))
        self.assertEqual(calculator.Sin(math.pi / 3), math.sin(math.pi / 3))
        self.assertEqual(calculator.Sin(math.pi), math.sin(math.pi))

    def test_random_testing(self):
        random.random()
        for i in range(0, 30):
            a = random.randint(-2 ** 15, 2 ** 16)
            self.assertEqual(calculator.Sin(a), math.sin(a))


class test_Cos(TestCase):
    def test_constant_testing(self):
        self.assertEqual(calculator.Cos(2 ** 31), math.cos(2 ** 31))
        self.assertEqual(calculator.Cos(-2 ** 31), math.cos(-2 ** 31))
        self.assertEqual(calculator.Cos(1.132321), math.cos(1.132321))
        self.assertEqual(calculator.Cos(-3.14), math.cos(-3.14))
        self.assertEqual(calculator.Cos(0), 0)
        self.assertEqual(calculator.Cos(-3 / -2), math.cos(-3 / -2))
        self.assertEqual(calculator.Cos(-3 / 2), math.cos(-3 / 2))
        self.assertEqual(calculator.Cos(-3 / -2), math.cos(-3 / -2))
        self.assertEqual(calculator.Cos(5 / -2), math.cos(5 / -2))
        self.assertEqual(calculator.Cos(math.pi / 2), math.cos(math.pi / 2))
        self.assertEqual(calculator.Cos(math.pi / 3), math.cos(math.pi / 3))
        self.assertEqual(calculator.Cos(math.pi), math.cos(math.pi))

    def test_random_testing(self):
        random.random()
        for i in range(0, 30):
            a = random.randint(-2 ** 15, 2 ** 16)
            self.assertEqual(calculator.Cos(a), math.cos(a))

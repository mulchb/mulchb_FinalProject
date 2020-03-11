import math

def Multiplication(x, y):
    return x*y


def Division(enumerator, denominator):
    if(denominator == 0):
        return None
    return enumerator / denominator


def Square_Root(x):
    if x < 0:
        return None
    return x**.5


def Squared(x):
    return x**2


def One_Div_X(x):
    return x**(-1)


def Factorial(x):
    if x < 0:
        return None
    if isinstance(x, int):
        return math.factorial(x)
    else:
        return None


def Absolute_Value(x):
    return abs(x)


def Sin(x):
    return math.sin(x)


def Cos(x):
    return math.cos(x)

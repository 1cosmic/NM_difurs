from math import log


def func(x):
    return log(x)


def funcFirstDerivative(x):
    return 1 / x


def funcSecondDerivative(x):
    return -1 / pow(x, 2)
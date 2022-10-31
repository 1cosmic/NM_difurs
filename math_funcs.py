from math import log
from random import random


def func(x):
    return log(x)


def funcFirstDerivative(x):
    return 1 / x


def funcSecondDerivative(x):
    return -1 / pow(x, 2)


def generate_randomPoints(startX, endX, step):
    countPoints = int((endX - startX) / step)
    print(countPoints)

    points = []

    for p in range(countPoints):
        points.append(random())

    print("Точки успешно сгенерированы. Всего точек: ", len(points))

    return points



def method_LeftDifference(points, dX):
    count = len(points)

    derivativesY = []

    for i in range(count - 1):
        dY = (points[i + 1] - points[i]) / dX
        derivativesY.append(dY)

    else:
        derivativesY.append(0)

    print("Алгоритм метода Левосторонней разности успешно завершён.")
    print(len(derivativesY))

    return derivativesY
import numpy as np
import itertools

arr = [_.split(":") for _ in open("input.txt", "r").read().strip().split("\n")]


def parseEquation(eqn, opr=None):
    eqnArr = eqn.lstrip().split(" ")
    tX = int(eqnArr[0])
    for idx, i in enumerate(opr):
        if i == "+":
            tX += int(eqnArr[idx+1])
        elif i == "*":
            tX *= int(eqnArr[idx + 1])
        else:
            tX = int(str(tX) + eqnArr[idx+1])
    return tX


sumTrueP1 = 0
sumIndex = []
for idz, (result, equation) in enumerate(arr):
    operators = list(itertools.product('*+', repeat=equation.lstrip().count(" ")))
    for operator in operators:
        if int(result) == parseEquation(equation, operator):
            sumTrueP1 += int(result)
            sumIndex.append(idz)
            break

print("AoC_2024_7.1:", sumTrueP1)

sumTrueP2 = 0
for idz, (result, equation) in enumerate(arr):
    if idz not in sumIndex:
        operators = list(itertools.product('*+|', repeat=equation.lstrip().count(" ")))
        for operator in operators:
            res = parseEquation(equation, operator)
            if int(result) == res:
                sumTrueP2 += int(result)
                break

print("AoC_2024_7.2:", sumTrueP1 + sumTrueP2)

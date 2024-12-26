import numpy as np
import itertools

arr = [_ for _ in open("input.txt", "r").read().strip().split("\n")]
rCount, cCount = len(arr), len(arr[0])


def getAntiNode(tA, tB):
    return tB[0] + (tB[0] - tA[0]), tB[1] + (tB[1] - tA[1])


def getAntiNodesInLine(tA, tB, rLim, cLim):
    diffX = tB[0] - tA[0]
    diffY = tB[1] - tA[1]
    inLineArr = [tB]
    c = 1
    while True:
        newAntiNode = (tB[0] + c*diffX, tB[1] + c*diffY)
        if 0 <= newAntiNode[0] < rLim and 0 <= newAntiNode[1] < cLim:
            inLineArr.append(newAntiNode)
            c += 1
        else:
            return inLineArr


d = {}
for idx, l in enumerate(arr):
    for idy, e in enumerate(l):
        if e != '.':
            if e not in d.keys():
                d[e] = [(idx, idy)]
            else:
                d[e].append((idx, idy))

antiNodeGrid = np.zeros((rCount, cCount), dtype=np.int16)
for key in d.keys():
    permutations = list(itertools.permutations(d[key], 2))
    antiNodes = [getAntiNode(*_) for _ in permutations]
    for antiNode in antiNodes:
        if 0 <= antiNode[0] < rCount and 0 <= antiNode[1] < cCount:
            antiNodeGrid[antiNode[0]][antiNode[1]] = 1

print("AoC_2024_8.1:", np.count_nonzero(antiNodeGrid))

antiNodeGrid = np.zeros((rCount, cCount), dtype=np.int16)
for key in d.keys():
    permutations = list(itertools.permutations(d[key], 2))
    antiNodeLists = [getAntiNodesInLine(*_, rCount, cCount) for _ in permutations]
    for antiNodeList in antiNodeLists:
        for antiNode in antiNodeList:
            antiNodeGrid[antiNode[0]][antiNode[1]] = 1

print("AoC_2024_8.2:", np.count_nonzero(antiNodeGrid))

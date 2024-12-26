import re
import numpy as np

diskMap = open("input.txt", "r").read().strip()
compressedMap = []
c = 0
for idx, d in enumerate(diskMap):
    d = int(d)
    if idx % 2 == 0:
        for _ in range(d):
            compressedMap.append(c)
        c += 1
    else:
        for _ in range(d):
            compressedMap.append(-1)


compressedMap = np.array(compressedMap, dtype=np.int64)
while True:
    indicesEmpty = np.argwhere(compressedMap == -1)
    indicesFull = np.argwhere(compressedMap != -1)
    idxEmpty = indicesEmpty[0][0]
    idxFull = indicesFull[-1][0]
    if idxEmpty > idxFull:
        compressedMap = compressedMap[:idxEmpty]
        break
    else:
        compressedMap[idxEmpty], compressedMap[idxFull] = compressedMap[idxFull], compressedMap[idxEmpty]

print("AoC_2024_9.1:", (compressedMap*list(range(len(compressedMap)))).sum())

compressedMap = ""
diskElements = []
c = 0
dLoc = {}
for idx, d in enumerate(diskMap):
    dInt = int(d)
    if idx % 2 == 0:
        startIndex = len(compressedMap)
        compressedMap += 'y' * dInt
        endIndex = len(compressedMap)
        diskElements.append((str(c), [startIndex, endIndex]))
        dLoc[str(c)] = [startIndex, endIndex]
        c += 1
    else:
        compressedMap += "x" * dInt

for elementStr, element in diskElements[::-1]:
    elementLength = element[1] - element[0]
    pattern = r"x{" + str(elementLength) + ",}"
    spaces = sorted([(m.start(0), m.end(0)) for m in re.finditer(pattern, compressedMap)])
    for space in spaces:
        if space[0] < element[0]:
            dLoc[elementStr] = [space[0], space[0] + elementLength]
            compressedMap = (compressedMap[:space[0]] +
                             compressedMap[element[0]:element[1]] +
                             compressedMap[space[0] + elementLength:])
            compressedMap = (compressedMap[:element[0]] +
                             'x' * elementLength +
                             compressedMap[element[1]:])
            break

result = 0
for idx in dLoc.keys():
    for idy in range(dLoc[idx][0], dLoc[idx][1]):
        result += int(idx) * idy

print("AoC_2024_9.2:", result)

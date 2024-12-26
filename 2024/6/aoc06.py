import numpy as np

arr = [_ for _ in open("input.txt", "r").read().strip().split("\n")]
mapArr = np.zeros((len(arr), len(arr[0]), 2), dtype=np.int16)

directionDict = {0: [-1, 0],
                 1: [0, 1],
                 2: [1, 0],
                 3: [0, -1]}
position, direction = None, 0
for idx, x in enumerate(arr):
    for idy, y in enumerate(x):
        if y == '#':
            mapArr[idx, idy, 0] = 1
        elif y == '^':
            mapArr[idx, idy, 1] = 1
            position = np.array([idx, idy])
        else:
            continue

mapArrC = mapArr.copy()
positionC = position.copy()
directionC = 0

while True:
    position += directionDict[direction]
    if (position[0] < 0 or position[0] >= mapArr.shape[0]) or (position[1] < 0 or position[1] >= mapArr.shape[1]):
        break
    if mapArr[position[0], position[1], 0] == 0:
        mapArr[position[0], position[1], 1] = 1
    else:
        position -= directionDict[direction]
        direction += 1
        direction %= 4

print("AoC_2024_6.1:", np.sum(mapArr[:, :, 1]))


def searchBrute(array, pos, direct, directDict):
    arrayC = array.copy()
    posC = pos.copy()
    searchCount = 0
    while True:
        posC += directionDict[direct]
        if (posC[0] < 0 or posC[0] >= arrayC.shape[0]) or (posC[1] < 0 or posC[1] >= arrayC.shape[1]):
            break
        if arrayC[posC[0], posC[1], 0] == 0:
            arrayC[posC[0], posC[1], 1] = 1
        else:
            posC -= directDict[direct]
            direct += 1
            direct %= 4
        searchCount += 1
        if searchCount % 20000 == 0:
            break
    return 1 if searchCount == 20000 else 0


obstacleCount = 0
for idx in range(mapArrC.shape[0]):
    for idy in range(mapArrC.shape[1]):
        if mapArrC[idx, idy, 0] == 0 and not (positionC[0] == idx and positionC[1] == idy):
            mapArrC[idx, idy, 0] = 1
            flag = searchBrute(mapArrC, positionC, directionC, directionDict)
            mapArrC[idx, idy, 0] = 0
            if flag:
                obstacleCount += 1

print("AoC_2024_6.2:", obstacleCount)

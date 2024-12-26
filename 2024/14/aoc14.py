import re
import numpy as np
from scipy import ndimage


def printAoCGrid(grid, dotElements):
    s = ''
    for row in grid:
        for element in row:
            if element in dotElements:
                s += '.'
            else:
                s += str(element)
        s += "\n"
    return s


class securityRobot:
    def __init__(self, roboData, gridSize):
        self.pos = [int(roboData[1]), int(roboData[0])]
        self.velocity = [int(roboData[3]), int(roboData[2])]
        self.tPositionDict = {0: self.pos.copy()}
        self.gridMaxX = gridSize[0]
        self.gridMaxY = gridSize[1]

    def getNextPosition(self):
        self.pos[0] += self.velocity[0]
        if self.pos[0] < 0:
            self.pos[0] += self.gridMaxX
        self.pos[0] %= self.gridMaxX

        self.pos[1] += self.velocity[1]
        if self.pos[1] < 0:
            self.pos[1] += self.gridMaxY
        self.pos[1] %= self.gridMaxY

    def predictPositions(self, t):
        for _ in range(t):
            self.getNextPosition()
            self.tPositionDict[_ + 1] = self.pos.copy()


arr = [re.sub(r'[pv=]', '', _).replace(" ", ",").split(",") for
       _ in open("input.txt").read().strip().split("\n")]
rowN, colN = 7, 11  # changed from 103, 101, Christmas tree not available for the example input

###############################################################################
#######################        PART 1         #################################
###############################################################################

roboLocations = []
for idx in arr:
    robo = securityRobot(idx, (rowN, colN))
    robo.predictPositions(t=100)
    roboLocations.append(robo.tPositionDict[100])

gridMap = np.zeros((rowN, colN), dtype=np.int16)
for loc in roboLocations:
    gridMap[*loc] += 1
Q1 = gridMap[0:int(rowN // 2), 0:int(colN // 2)]
Q2 = gridMap[0:int(rowN // 2), int(colN // 2) + 1:]
Q3 = gridMap[int(rowN // 2) + 1:, 0:int(colN // 2)]
Q4 = gridMap[int(rowN // 2) + 1:, int(colN // 2) + 1:]
print("AoC_2015_14.1:", np.sum(Q1) * np.sum(Q2) * np.sum(Q3) * np.sum(Q4))

###############################################################################
#######################        PART 2         #################################
###############################################################################

t = 10000
roboArr = []
for idx in arr:
    robo = securityRobot(idx, (rowN, colN))
    robo.predictPositions(t=t)
    roboArr.append(robo)

for _ in range(t):
    gridMap = np.zeros((rowN, colN), dtype=np.int16)
    for robo in roboArr:
        gridMap[*robo.tPositionDict[_]] = 1
    labelImage, labelsN = ndimage.label(gridMap)
    sizesMax = max([np.count_nonzero(labelImage[labelImage == idx]) for idx in range(labelsN + 1)])

    # Print out the Christmas tree
    if sizesMax > 100:
        with open('christmasTree.txt', 'a') as f:
            print(f"-- {_} --\n", file=f)
            print(printAoCGrid(gridMap, [0]), file=f)
            print("\n-----\n", file=f)
        print("AoC_2015_14.2:", _)
        break

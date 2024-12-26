import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

# Read the file
arr = [_ for _ in open("input.txt").read().strip().split("\n\n")]

# Read/parse the map
mapText = arr[0].split("\n")
gridMap = np.zeros((len(mapText), len(mapText[0])), dtype=np.int16)
for i, row in enumerate(mapText):
    for j, element in enumerate(row):
        if element == '#':
            gridMap[i][j] = 9
        elif element == 'O':
            gridMap[i][j] = 1
        elif element == '.':
            gridMap[i][j] = 0
        else:
            gridMap[i][j] = 2

# Read/parse the directions
directionsDict = {'<': [0, -1], '>': [0, 1], '^': [-1, 0], 'v': [1, 0]}
directionsText = ''.join(arr[1].split("\n"))
directions = [directionsDict[_] for _ in directionsText]


# Update grid map
def updateGridMap(m: np.ndarray, d: list):
    # Robo location
    roboLoc = np.argwhere(m == 2)[0]
    newRoboLoc = [roboLoc[0]+d[0], roboLoc[1]+d[1]]

    # Check valid move
    if gridMap[*newRoboLoc] == 9:
        return gridMap
    # Move empty space
    elif gridMap[*newRoboLoc] == 0:
        gridMap[*newRoboLoc], gridMap[*roboLoc] = gridMap[*roboLoc], gridMap[*newRoboLoc]
        return gridMap
    # Move boxes
    elif gridMap[*newRoboLoc] == 1:
        # Check next empty space
        boxesToMove = []
        tempBoxLoc = newRoboLoc.copy()
        while gridMap[*tempBoxLoc] == 1:
            boxesToMove.append(tempBoxLoc)
            tempBoxLoc = [tempBoxLoc[0]+d[0], tempBoxLoc[1]+d[1]]
            if gridMap[*tempBoxLoc] == 9:
                boxesToMove = []
        # If there is boxes to move
        if len(boxesToMove) > 0:
            for loc in boxesToMove[::-1]:
                replaceLoc = [loc[0]+d[0], loc[1]+d[1]]
                gridMap[*replaceLoc], gridMap[*loc] = gridMap[*loc], gridMap[*replaceLoc]
            gridMap[*newRoboLoc], gridMap[*roboLoc] = gridMap[*roboLoc], gridMap[*newRoboLoc]
            return gridMap
        else:
            return gridMap


def calculateGPS(m):
    boxLocations = np.argwhere(m == 1)
    boxLocations[:, 0] *= 100
    scoreGPS = np.sum(boxLocations, axis=1)
    return np.sum(scoreGPS)


for i in range(len(directions)):
    gridMap = updateGridMap(gridMap, directions[i])
print("AoC_2024_15.1:", calculateGPS(gridMap))

###############################################################################
#######################        PART 2         #################################
###############################################################################

# Read the file
arr = [_ for _ in open("input.txt").read().strip().split("\n\n")]

# Read/parse the map
mapText = arr[0].split("\n")
gridMap = np.zeros((len(mapText), len(mapText[0])*2), dtype=np.int16)
for i, row in enumerate(mapText):
    for j, element in enumerate(row):
        if element == '#':
            gridMap[i][(2*j)] = 9
            gridMap[i][(2*j)+1] = 9
        elif element == 'O':
            gridMap[i][(2*j)] = 7
            gridMap[i][(2*j)+1] = 8
        elif element == '.':
            gridMap[i][(2*j)] = 0
            gridMap[i][(2*j)+1] = 0
        else:
            gridMap[i][(2*j)] = 2
            gridMap[i][(2*j)+1] = 0

# Read/parse the directions
directionsDict = {'<': [0, -1], '>': [0, 1], '^': [-1, 0], 'v': [1, 0]}
directionsText = ''.join(arr[1].split("\n"))
directions = [directionsDict[_] for _ in directionsText]


# Update grid map
def updateGridMap(m: np.ndarray, d: list):
    # Robo location
    roboLoc = np.argwhere(m == 2)[0]
    newRoboLoc = [roboLoc[0]+d[0], roboLoc[1]+d[1]]

    # Check valid move
    if gridMap[*newRoboLoc] == 9:
        return gridMap
    # Move empty space
    elif gridMap[*newRoboLoc] == 0:
        gridMap[*newRoboLoc], gridMap[*roboLoc] = gridMap[*roboLoc], gridMap[*newRoboLoc]
        return gridMap
    # Move boxes
    elif gridMap[*newRoboLoc] in [7, 8]:
        boxesToMove = []
        tempBoxLoc = newRoboLoc.copy()
        if gridMap[*tempBoxLoc] == 7:
            boxesToMove.append(tempBoxLoc)
            boxesToMove.append([tempBoxLoc[0], tempBoxLoc[1]+1])
        else:
            boxesToMove.append(tempBoxLoc)
            boxesToMove.append([tempBoxLoc[0], tempBoxLoc[1]-1])

        # Check next empty space
        flag = True
        while flag:
            boxesAdded = 0
            for boxLoc in boxesToMove:
                tempBoxLoc = [boxLoc[0] + d[0], boxLoc[1] + d[1]]
                if gridMap[*tempBoxLoc] in [7, 8] and tempBoxLoc not in boxesToMove:
                    boxesAdded += 1
                    if gridMap[*tempBoxLoc] == 7:
                        boxesToMove.append(tempBoxLoc)
                        boxesToMove.append([tempBoxLoc[0], tempBoxLoc[1] + 1])
                    else:
                        boxesToMove.append(tempBoxLoc)
                        boxesToMove.append([tempBoxLoc[0], tempBoxLoc[1] - 1])
                if gridMap[*tempBoxLoc] == 9:
                    boxesToMove = []
                    break
            if boxesAdded == 0:
                break

        # If there is boxes to move
        if len(boxesToMove) > 0:
            for loc in boxesToMove[::-1]:
                replaceLoc = [loc[0]+d[0], loc[1]+d[1]]
                gridMap[*replaceLoc], gridMap[*loc] = gridMap[*loc], gridMap[*replaceLoc]
            gridMap[*newRoboLoc], gridMap[*roboLoc] = gridMap[*roboLoc], gridMap[*newRoboLoc]
            return gridMap
        else:
            return gridMap


def calculateGPS(m):
    boxLocations = np.argwhere(m == 7)
    boxLocations[:, 0] *= 100
    scoreGPS = np.sum(boxLocations, axis=1)
    return np.sum(scoreGPS)


for i in range(len(directions)):
    gridMap = updateGridMap(gridMap, directions[i])
print("AoC_2024_15.2:", calculateGPS(gridMap))

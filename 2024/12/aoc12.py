import numpy as np

file = open('input.txt').read()

# Part 1
arr = np.array([[j for j in i] for i in file.strip().split('\n')])
uniqueFlowerNames = np.unique(arr)
flowerLocationDict = {i: list(zip(*np.where(arr == i))) for i in np.unique(arr)}

flowerGardensDict = {}
flowerAreaPerimeter = {}
for key in flowerLocationDict.keys():
    flowerGardensDict[key] = {}
    flowerAreaPerimeter[key] = {}
    flowerLocations = flowerLocationDict[key].copy()
    idx = 0
    while len(flowerLocations) > 0:
        flowerStack = [flowerLocations[0]]
        flowerGardensDict[key][idx] = []
        flowerAreaPerimeter[key][idx] = [0, 0]

        while len(flowerStack) > 0:
            s = (flowerStack[0][0] + 1, flowerStack[0][1])
            n = (flowerStack[0][0] - 1, flowerStack[0][1])
            e = (flowerStack[0][0], flowerStack[0][1] + 1)
            w = (flowerStack[0][0], flowerStack[0][1] - 1)
            flowerPerimeter = 4
            flowerAreaPerimeter[key][idx][0] += 1
            for j in [s, n, e, w]:
                if j in flowerLocations or j in flowerGardensDict[key][idx] or j in flowerStack:
                    flowerPerimeter -= 1
                if j in flowerLocations:
                    flowerStack.append(j)
                    flowerLocations.remove(j)
            flowerGardensDict[key][idx].append(flowerStack[0])
            flowerAreaPerimeter[key][idx][1] += flowerPerimeter
            if (flowerStack[0][0], flowerStack[0][1]) in flowerLocations:
                flowerLocations.remove((flowerStack[0][0], flowerStack[0][1]))
            del flowerStack[0]
        idx += 1

print('AoC_2024_12_1:',
      sum([flowerAreaPerimeter[i][j][0] * flowerAreaPerimeter[i][j][1] for i in flowerAreaPerimeter.keys() for j in
           flowerAreaPerimeter[i].keys()]))

# Part 2
arr = np.array([[j for j in i] for i in file.strip().split('\n')])
uniqueFlowerNames = np.unique(arr)
flowerLocationDict = {i: list(zip(*np.where(arr == i))) for i in np.unique(arr)}

flowerGardensDict = {}
flowerAreaPerimeter = {}
for key in flowerLocationDict.keys():
    flowerGardensDict[key] = {}
    flowerAreaPerimeter[key] = {}
    flowerLocations = sorted(flowerLocationDict[key].copy())[::-1]
    idx = 0
    while len(flowerLocations) > 0:
        flowerStack = [flowerLocations[0]]
        flowerGardensDict[key][idx] = []
        flowerAreaPerimeter[key][idx] = [0, 0]
        flowerPerimeterDict = {}

        while len(flowerStack) > 0:
            s = (flowerStack[0][0] + 1, flowerStack[0][1])
            n = (flowerStack[0][0] - 1, flowerStack[0][1])
            e = (flowerStack[0][0], flowerStack[0][1] + 1)
            w = (flowerStack[0][0], flowerStack[0][1] - 1)
            flowerPerimeter = [1, 1, 1, 1]
            flowerAreaPerimeter[key][idx][0] += 1

            if n in flowerGardensDict[key][idx]:
                if flowerPerimeterDict[n][2] > 0:
                    flowerPerimeter[2] = 0.5
                if flowerPerimeterDict[n][3] > 0:
                    flowerPerimeter[3] = 0.5
            if s in flowerGardensDict[key][idx]:
                if flowerPerimeterDict[s][2] > 0:
                    flowerPerimeter[2] = 0.5
                if flowerPerimeterDict[s][3] > 0:
                    flowerPerimeter[3] = 0.5
            if w in flowerGardensDict[key][idx]:
                if flowerPerimeterDict[w][0] > 0:
                    flowerPerimeter[0] = 0.5
                if flowerPerimeterDict[w][1] > 0:
                    flowerPerimeter[1] = 0.5
            if e in flowerGardensDict[key][idx]:
                if flowerPerimeterDict[e][0] > 0:
                    flowerPerimeter[0] = 0.5
                if flowerPerimeterDict[e][1] > 0:
                    flowerPerimeter[1] = 0.5
            for idz, j in enumerate([s, n, e, w]):
                if j in flowerLocations or j in flowerGardensDict[key][idx] or j in flowerStack:
                    flowerPerimeter[idz] = 0
                if j in flowerLocations:
                    flowerStack.append(j)
                    flowerLocations.remove(j)
            flowerPerimeterDict[flowerStack[0]] = flowerPerimeter
            flowerGardensDict[key][idx].append(flowerStack[0])
            if (flowerStack[0][0], flowerStack[0][1]) in flowerLocations:
                flowerLocations.remove((flowerStack[0][0], flowerStack[0][1]))
            del flowerStack[0]
        flowerAreaPerimeter[key][idx][1] = sum([j for i in flowerPerimeterDict.keys() for
                                                j in flowerPerimeterDict[i] if j == 1])
        idx += 1

print('AoC_2024_12_2:', sum([flowerAreaPerimeter[i][j][0]*flowerAreaPerimeter[i][j][1] for
                             i in flowerAreaPerimeter.keys() for j in flowerAreaPerimeter[i].keys()]))

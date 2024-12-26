import numpy as np

arr = [_ for _ in open("input.txt", "r").read().strip().split("\n")]

searchLocations = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
searchTerm = 'MAS'
count = 0
for idx in range(len(arr)):
    for idy in range(len(arr[idx])):
        if arr[idx][idy] == 'X':
            for loc in searchLocations:
                flag = True
                for idz in range(3):
                    try:
                        idnx = idx + (loc[0] * (idz + 1))
                        idny = idy + (loc[1] * (idz + 1))
                        if 0 <= idnx < len(arr) and 0 <= idny < len(arr[idx]):
                            elem = arr[idnx][idny]
                            if elem != searchTerm[idz]:
                                flag = False
                        else:
                            flag = False
                    except IndexError:
                        flag = False
                if flag:
                    count += 1

print("AoC_2024_4.1:", count)

searchLocations = [[[-1, -1], [1, 1]],
                   [[-1, 1], [1, -1]]]

count = 0
for idx in range(len(arr)):
    for idy in range(len(arr[idx])):
        if arr[idx][idy] == 'A':
            flag = True
            for loc in searchLocations:
                idnx = idx + loc[0][0]
                idny = idy + loc[0][1]
                idnxx = idx + loc[1][0]
                idnyy = idy + loc[1][1]
                if ((0 <= idnx < len(arr) and 0 <= idny < len(arr[idx])) and
                    (0 <= idnxx < len(arr) and 0 <= idnyy < len(arr[idx]))):
                    elem1 = arr[idnx][idny]
                    elem2 = arr[idnxx][idnyy]
                    if (elem1 == 'M' and elem2 == 'S') or (elem1 == 'S' and elem2 == 'M'):
                        pass
                    else:
                        flag = False
                else:
                    flag = False
            if flag:
                count += 1
print("AoC_2024_4.2:", count)

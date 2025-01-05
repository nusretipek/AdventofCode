def getFallThroughTimes(d):
    counter, keyCounter = 0, 0
    while keyCounter != len(d):
        keyCounter = 0
        for key in d.keys():
            if (d[key][1] + int(key) + counter) % d[key][0] == 0:
                keyCounter += 1
        counter += 1
    return counter-1


discs = {1: [7, 0], 2: [13, 0], 3: [3, 2],
         4: [5, 2], 5: [17, 0], 6: [19, 7]}
print("AoC_2016_15.1:", getFallThroughTimes(discs))

discs = {1: [7, 0], 2: [13, 0], 3: [3, 2],
         4: [5, 2], 5: [17, 0], 6: [19, 7],
         7: [11, 0]}
print("AoC_2016_15.2:", getFallThroughTimes(discs))

import numpy as np

trailMap = np.array([[j for j in i] for i in open("input.txt", "r").read().strip().split("\n")],
                    dtype=np.int16)
trailHeads = list(zip(*np.where(trailMap == 0)))


def searchTrails(tMap, tHead):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    searchList = [[tHead]]
    trailPeakDict = {}
    while len(searchList) > 0:
        for direction in directions:
            r = searchList[0][-1][0] + direction[0]
            c = searchList[0][-1][1] + direction[1]
            if (0 <= r < tMap.shape[0]) and (0 <= c < tMap.shape[1]):
                val = trailMap[r][c]
                if val == 9 and len(searchList[0]) == 9:
                    if str(r)+str(c) not in trailPeakDict:
                        trailPeakDict[str(r)+str(c)] = 1
                    else:
                        trailPeakDict[str(r) + str(c)] += 1
                elif val == len(searchList[0]) and val < 9:
                    searchList.append(searchList[0]+[(r, c)])
        del searchList[0]
    return trailPeakDict


print("AoC_2024_10.1:", sum([len(searchTrails(trailMap, _)) for _ in trailHeads]))
print("AoC_2024_10.2:", sum([sum(searchTrails(trailMap, _).values()) for _ in trailHeads]))

import numpy as np

arr = [_ for _ in open("input.txt", "r").read().strip().split("\n")]

rules = []
manuals = []
flag = True
for idx in arr:
    if idx == '':
        flag = False
        continue
    if flag:
        rules.append([int(j) for j in idx.split('|')])
    else:
        manuals.append([int(j) for j in idx.split(',')])

d = {}
for rule in rules:
    if rule[1] not in d.keys():
        d[rule[1]] = [rule[0]]
    else:
        d[rule[1]].append(rule[0])

result = 0
result2 = 0
for manual in manuals:
    flag = True
    for idx, page in enumerate(manual):
        try:
            if len([value for value in manual[idx+1:] if value in d[page]]) > 0:
                flag = False
        except KeyError as e:
            continue
    if flag:
        result += manual[int(len(manual) / 2)]
    else:
        loopFlag = True
        correctOrder = manual.copy()

        while loopFlag:
            swaps = []
            for idx, page in enumerate(correctOrder):
                try:
                    for value in correctOrder[idx+1:]:
                        if page in d.keys() and value in d[page]:
                            swaps.append([page, value])
                except KeyError as e:
                    continue
            for idx, idy in swaps:
                indexIdx = correctOrder.index(idx)
                indexIdy = correctOrder.index(idy)
                correctOrder[indexIdx], correctOrder[indexIdy] = correctOrder[indexIdy], correctOrder[indexIdx]

            internalFlag = True
            for idz, page in enumerate(correctOrder):
                try:
                    if len([value for value in correctOrder[idz + 1:] if value in d[page]]) > 0:
                        internalFlag = False
                except KeyError as e:
                    continue
            if internalFlag:
                result2 += correctOrder[int(len(correctOrder) / 2)]
                loopFlag = False

print("AoC_2024_5.1:", result)
print("AoC_2024_5.2:", result2)

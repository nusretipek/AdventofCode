import numpy as np

inLines = [_.split(" ") for _ in open("input.txt", "r").read().strip().split("\n")]
inList = [np.array(_, dtype=np.int32) for _ in inLines]
safeBoolList = [len(np.unique(np.sign(np.diff(_)))) == 1 and
                np.unique(np.sign(np.diff(_)))[0] != 0 and
                np.max(np.abs(np.diff(_))) <= 3 and
                np.min(np.abs(np.diff(_))) >= 1
                for _ in inList]
print("AoC_2024_2.1:", sum(safeBoolList))

count = 0
for idx in inList:
    flag = False
    for idy in range(len(idx)):
        tempList = idx.copy()
        tempList = np.delete(tempList, idy)
        if (len(np.unique(np.sign(np.diff(tempList)))) == 1 and np.unique(np.sign(np.diff(tempList)))[0] != 0 and
           np.max(np.abs(np.diff(tempList))) <= 3 and np.min(np.abs(np.diff(tempList))) >= 1):
            flag = True
    if flag:
        count += 1
print("AoC_2024_2.2:", count)

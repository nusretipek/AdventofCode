import time
import numpy as np

t = open("input.txt").read().strip()
blinkCountP1 = 25
blinkCountP2 = 75


def blink(s):
    sArr = np.array(s.split(" "), dtype=np.int64)
    newState = ''
    for element in sArr:
        if element == 0:
            newState += '1 '
        elif len(str(element)) % 2 == 0:
            newState += str(int(str(element)[:len(str(element))//2])) + ' '
            newState += str(int(str(element)[len(str(element))//2:])) + ' '
        else:
            newState += str(int(element*2024)) + ' '
    return newState.strip()


def blinkCountPebble(d):
    dNewState = {}
    for element in d.keys():
        if element == 0:
            if 1 in dNewState.keys():
                dNewState[1] += d[element]
            else:
                dNewState[1] = d[element]
        elif len(str(element)) % 2 == 0:
            splitP1 = int(str(element)[:len(str(element)) // 2])
            splitP2 = int(str(element)[len(str(element)) // 2:])
            if splitP1 in dNewState.keys():
                dNewState[splitP1] += d[element]
            else:
                dNewState[splitP1] = d[element]
            if splitP2 in dNewState.keys():
                dNewState[splitP2] += d[element]
            else:
                dNewState[splitP2] = d[element]
        else:
            multiplyP1 = element*2024
            if multiplyP1 in dNewState.keys():
                dNewState[multiplyP1] += d[element]
            else:
                dNewState[multiplyP1] = d[element]
    return dNewState


t0 = time.time()
tP1 = t
for _ in range(blinkCountP1):
    tP1 = blink(tP1)
print('AoC_2024_11.1:', len(tP1.split(' ')), "\nTime:", time.time()-t0)


t0 = time.time()
tP2 = {}
for _ in t.split(' '):
    if int(_) in tP2.keys():
        tP2[int(_)] += 1
    else:
        tP2[int(_)] = 1

for _ in range(0, blinkCountP2):
    tP2 = blinkCountPebble(tP2)
print('\nAoC_2024_11.2:', sum(tP2.values()), "\nTime:", time.time()-t0)

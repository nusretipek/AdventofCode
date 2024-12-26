import numpy as np
import itertools

arr = [_.split("\n") for _ in open("input.txt").read().strip().split("\n\n")]


def parseSchema(s):
	isLock = 1 if all([_ == "#" for _ in s[0]]) else 0
	heights = np.zeros((len(s[0])), dtype=np.int16)
	for i in range(len(s[0])):
		for j in range(1, len(s)-1):
			if s[j][i] == "#":
				heights[i] += 1
	return isLock, heights


def checkFit(l, k):
	fitRegion = 5
	fit = l+k
	return np.all(fit <= fitRegion)


locks, keys = [], []
for i in arr:
	lock, schema = parseSchema(i)
	if lock:
		locks.append(schema)
	else:
		keys.append(schema)


fitCounter = 0
for i in locks:
	for j in keys:
		isFit = checkFit(i, j)
		if isFit:
			fitCounter += 1

print("AoC_2024_25.1:", fitCounter)

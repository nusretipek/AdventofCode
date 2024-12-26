import itertools
import numpy as np
import tqdm
import sys

arr = [_.split("-") for _ in open("input.txt").read().strip().split("\n")]
uniqueComputers = set([j for i in arr for j in i])


connectedDict = {}
for uniqueComputer in uniqueComputers:
	connectedDict[uniqueComputer] = []
	for computerX, computerY in arr:
		if computerX == uniqueComputer:
			connectedDict[uniqueComputer].append(computerY)
		elif computerY == uniqueComputer:
			connectedDict[uniqueComputer].append(computerX)
		else:
			continue

tripleTLan = set()
for key in connectedDict:
	combinations = list(itertools.combinations(connectedDict[key], r=2))
	for computerX, computerY in combinations:
		if computerX in connectedDict[computerY] and (key[0] == "t" or computerX[0] == 't' or computerY[0] == 't'):
			tripleTLan.add(tuple(sorted((key, computerX, computerY))))

print("AoC_2024_23.1:", len(tripleTLan))

largestLan = []
for key in connectedDict:
	combinations = []
	for idx in range(max(2, len(largestLan)), len(connectedDict[key])+2):
		combinations += list(itertools.combinations(connectedDict[key], r=idx))
	for combination in combinations:
		flag = True
		for computerX, computerY in list(itertools.combinations(combination, r=2)):
			#print(computerX, computerY)
			if computerX not in connectedDict[computerY]:
				flag = False
		combination = [key] + list(combination)
		if flag and len(combination) > len(largestLan):
			largestLan = combination

print("AoC_2024_23.2:", ",".join(sorted(largestLan)))

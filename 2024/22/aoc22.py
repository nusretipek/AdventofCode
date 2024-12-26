import numpy as np

arr = [int(_) for _ in open("inputP1.txt").read().strip().split("\n")]


def step1(s):
	r = s * 64
	s = s ^ r
	return s % 16777216


def step2(s):
	r = s // 32
	s = s ^ r
	return s % 16777216


def step3(s):
	r = s * 2048
	s = s ^ r
	return s % 16777216


results = []
for secretNumber in arr:
	for _ in range(2000):
		secretNumber = step1(secretNumber)
		secretNumber = step2(secretNumber)
		secretNumber = step3(secretNumber)
	results.append(secretNumber)

print("AoC_2024_22.1:", sum(results))

# Part 2
arr = [int(_) for _ in open("inputP2.txt").read().strip().split("\n")]
bananasDict = {}
for secretNumber in arr:
	bananas = [secretNumber % 10]
	for _ in range(2000):
		secretNumber = step1(secretNumber)
		secretNumber = step2(secretNumber)
		secretNumber = step3(secretNumber)
		bananas.append(secretNumber % 10)
	bananas = np.array(bananas)
	results = np.diff(bananas)
	sellerDict = {}
	for _ in range(len(results)-3):
		sequence = (results[_], results[_+1], results[_+2], results[_+3])
		if sequence not in sellerDict:
			sellerDict[sequence] = bananas[_+4]

	for _ in sellerDict.keys():
		if _ not in bananasDict:
			bananasDict[_] = sellerDict[_]
		else:
			bananasDict[_] += sellerDict[_]

print("AoC_2024_22.2:", max([_ for _ in bananasDict.values()]))

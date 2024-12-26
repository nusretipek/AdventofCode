import numpy as np
import networkx as nx
import itertools

arr = [_ for _ in open("input.txt").read().strip().split("\n")]
padDesign = [["7", "8", "9"],
             ["4", "5", "6"],
             ["1", "2", "3"],
             [" ", "0", "A"]]
keypadDesign = [[" ", "^", "A"],
                ["<", "v", ">"]]


def getShortestPathsDictionary(design):
	shortestPaths, directionDict = {}, {}
	g = nx.DiGraph()
	for node in [j for i in design for j in i if j != " "]:
		g.add_node(str(node))

	for idx in range(len(design)):
		for idy in range(len(design[0])):
			for direction in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
				neighborX = idx + direction[0]
				neighborY = idy + direction[1]
				if (0 <= neighborX < len(design) and 0 <= neighborY < len(design[0]) and
					design[neighborX][neighborY] in g.nodes and design[idx][idy] in g.nodes):
					if direction == [0, -1]:
						directionDict[(design[idx][idy], design[neighborX][neighborY])] = "<"
					elif direction == [0, 1]:
						directionDict[(design[idx][idy], design[neighborX][neighborY])] = ">"
					elif direction == [1, 0]:
						directionDict[(design[idx][idy], design[neighborX][neighborY])] = "v"
					elif direction == [-1, 0]:
						directionDict[(design[idx][idy], design[neighborX][neighborY])] = "^"
					g.add_edge(design[idx][idy], design[neighborX][neighborY], weight=1)

	buttonPermutations = list(itertools.permutations(list(g.nodes), r=2))
	for idx in g.nodes():
		shortestPaths[(idx, idx)] = [[idx, idx]]
		directionDict[(idx, idx)] = ""
	for idx in buttonPermutations:
		shortestPaths[idx] = [idy for idy in nx.all_shortest_paths(g, source=idx[0], target=idx[1])]

	return shortestPaths, directionDict


def getNumericPadInstructions(shortestPaths, directions, code="029A"):
	code = "A" + code
	pathCombinations = [""]
	for idx in range(len(code)-1):
		tempPathCombinations = []
		pair = (code[idx], code[idx+1])
		for path in shortestPaths[pair]:
			s = ""
			for idy in range(len(path) - 1):
				s += directions[(path[idy], path[idy+1])]
			s += "A"
			for knownPath in pathCombinations:
				tempPathCombinations.append(knownPath+s)
		pathCombinations = tempPathCombinations.copy()
	return pathCombinations


def calculateComplexity(code):
	shortestCodeLength = None
	padShortestPaths, padDirections = getShortestPathsDictionary(padDesign)
	keypadShortestPaths, keypadDirections = getShortestPathsDictionary(keypadDesign)
	numericPadRobotArm = getNumericPadInstructions(padShortestPaths, padDirections, code)

	for i in numericPadRobotArm:
		keypadRobot1 = getNumericPadInstructions(keypadShortestPaths, keypadDirections, i)
		minLength = min(list(map(len, keypadRobot1)))
		keypadRobot1 = [_ for _ in keypadRobot1 if len(_) == minLength]
		for j in keypadRobot1:
			keypadRobot2 = getNumericPadInstructions(keypadShortestPaths, keypadDirections, j)
			minLength2 = min(list(map(len, keypadRobot2)))
			keypadRobot2 = [_ for _ in keypadRobot2 if len(_) == minLength2]
			for z in keypadRobot2:
				if shortestCodeLength is None or shortestCodeLength > len(z):
					shortestCodeLength = len(z)
	complexity = int("".join([_ for idx, _ in enumerate(code) if _.isdigit() and not (idx == 0 and _ == "0")])) * shortestCodeLength
	return complexity


totalComplexity = 0
for c in arr:
	totalComplexity += calculateComplexity(c)
print("AoC_2024_21.1:", totalComplexity)

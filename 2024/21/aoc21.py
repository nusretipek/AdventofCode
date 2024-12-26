import itertools
import networkx as nx
from functools import lru_cache

arr = [_ for _ in open("input.txt").read().strip().split("\n")]
padDesign = [["7", "8", "9"],
             ["4", "5", "6"],
             ["1", "2", "3"],
             [" ", "0", "A"]]

keypadDesign = [[" ", "^", "A"],
                ["<", "v", ">"]]

keypadD = {'^^': 'A', 'AA': 'A', '<<': 'A', 'vv': 'A', '>>': 'A',
           '^A': '>A', '^<': 'v<A', '^v': 'vA', '^>': 'v>A',
           'A^': '<A', 'A<': 'v<<A', 'Av': '<vA', 'A>': 'vA',
           '<^': '>^A', '<A': '>>^A', '<v': '>A', '<>': '>>A',
           'v^': '^A', 'vA': '^>A', 'v<': '<A', 'v>': '>A',
           '>^': '<^A', '>A': '^A', '><': '<<A', '>v': '<A'}


def cleanCombinations(pad):
	for z in pad:
		if len(pad[z]) > 1:
			changes = []
			for x in pad[z]:
				change = 0
				for k in range(len(x) - 1):
					if x[k] != x[k + 1]:
						change += 1
				changes.append(change)
			pad[z] = pad[z][changes.index(min(changes))]
		else:
			pad[z] = pad[z][0]
	return pad


def getShortestPathsDictionary(design):
	shortestPaths, directionDict = {}, {}
	g = nx.DiGraph()
	for node in [x for z in design for x in z if x != " "]:
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

	shortestPathCombinations = {}
	for idx in shortestPaths.keys():
		paths = []
		for idy in shortestPaths[idx]:
			s = ""
			for idz in range(len(idy)-1):
				s += directionDict[idy[idz], idy[idz+1]]
			s += "A"
			paths.append(s)
		shortestPathCombinations[str(idx[0])+str(idx[1])] = paths

	shortestPathCombinations = cleanCombinations(shortestPathCombinations)
	return shortestPaths, directionDict, shortestPathCombinations


def getNumericPadInstructionsAll(shortestPaths, directions, code="029A"):
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


@lru_cache(maxsize=None)
def getKeyPadInstructionsLength(code, depth, s=0):
	if depth == 0:
		return len(code)

	code = "A" + code
	for idx in range(len(code)-1):
		s += getKeyPadInstructionsLength(keypadD[code[idx:idx+2]], depth=depth-1)
	return s


padShortestPaths, padDirections, padD = getShortestPathsDictionary(padDesign)
keypadShortestPaths, keypadDirections, _ = getShortestPathsDictionary(keypadDesign)

totalComplexityP1 = 0
totalComplexityP2 = 0
for i in arr:
	complexity = int("".join([_ for idx, _ in enumerate(i) if _.isdigit() and not (idx == 0 and _ == "0")]))
	numericPadRobotArm = getNumericPadInstructionsAll(padShortestPaths, padDirections, i)
	tempShortestP1 = []
	tempShortestP2 = []
	for j in numericPadRobotArm:
		tempShortestP1.append(getKeyPadInstructionsLength(j, 2))
		tempShortestP2.append(getKeyPadInstructionsLength(j, 25))
	totalComplexityP1 += complexity * min(tempShortestP1)
	totalComplexityP2 += complexity * min(tempShortestP2)

print("AoC_2024_21.1:", totalComplexityP1)
print("AoC_2024_21.1:", totalComplexityP2)

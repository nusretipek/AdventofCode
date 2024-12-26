import itertools
import numpy as np
import networkx as nx

arr = [_ for _ in open("input.txt").read().strip().split('\n')]
startNode, endNode = None, None
g = nx.DiGraph()

# Add nodes
for idx in range(len(arr)):
	for idy in range(len(arr[0])):
		if arr[idx][idy] != "#":
			g.add_node((idx, idy))
			if arr[idx][idy] == "S":
				startNode = (idx, idy)
			if arr[idx][idy] == "E":
				endNode = (idx, idy)

# Add edges
for node in g.nodes:
	for idx in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
		neighborNode = (node[0] + idx[0], node[1] + idx[1])
		if g.has_node(neighborNode):
			g.add_edge(node, neighborNode)


# Distance measure
def manhattanDistance(nodeX, nodeY):
	return abs(nodeX[0] - nodeY[0]) + abs(nodeX[1] - nodeY[1])


# Get the shortest path
shortestPath = nx.shortest_path(g, source=startNode, target=endNode)
shortestPaths = [_ for _ in nx.all_shortest_paths(g, source=startNode, target=endNode)]
print(f"Shortest path length is {len(shortestPath) - 1}, there are only {len(shortestPaths)} shortest paths!")


# Calculate pairwise Manhattan distance
def pairwiseDistanceGain(path, distanceThreshold, minGain, verbose=False):
	cheatCount = 0
	cheatingList = []
	indexLookup = {_: i for i, _ in enumerate(path)}
	pairs = list(itertools.combinations(path, r=2))
	for nodeX, nodeY in pairs:
		distance = manhattanDistance(nodeX, nodeY)
		distanceGain = abs(indexLookup[nodeX] - indexLookup[nodeY])
		if distance <= distanceThreshold < distanceGain and distanceGain - distance >= minGain:
			cheatingList.append(distanceGain - distance)
	for cheatingDistance in sorted(set(cheatingList)):
		if verbose:
			print(f"There are {cheatingList.count(cheatingDistance)} cheats that save {cheatingDistance} picoseconds.")
		if cheatingDistance >= minGain:
			cheatCount += cheatingList.count(cheatingDistance)
	return cheatCount


print("AoC_2024_20.1:", pairwiseDistanceGain(shortestPath, 2, 100))
print("AoC_2024_20.2:", pairwiseDistanceGain(shortestPath, 20, 100))

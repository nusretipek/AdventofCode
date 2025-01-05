import numpy as np
import networkx as nx

arr = [_ for _ in open("input.txt").read().strip().split("\n")]
grid = np.zeros((len(arr), len(arr[0])), dtype=np.int16)
startNode = None
for idx, row in enumerate(arr):
	for idy, value in enumerate(row):
		if value == "#":
			grid[idx, idy] = -1
		elif value == ".":
			grid[idx, idy] = -2
		else:
			grid[idx, idy] = int(value)
			if int(value) == 0:
				startNode = (idx, idy)

g = nx.DiGraph()
for idx in range(grid.shape[0]):
	for idy in range(grid.shape[1]):
		if grid[idx][idy] != -1:
			g.add_node((idx, idy))

for idx in range(grid.shape[0]):
	for idy in range(grid.shape[1]):
		for idz in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
			if (idx, idy) in g.nodes() and (idx + idz[0], idy + idz[1]) in g.nodes():
				g.add_edge((idx, idy), (idx + idz[0], idy + idz[1]), weight=1)


locations = list(zip(*np.where(grid >= 0)))
shortestPaths = []
wG = nx.DiGraph()
for idx in range(len(locations)):
	for idy in range(idx+1, len(locations)):
		startLocation = locations[idx]
		endLocation = locations[idy]
		if startLocation not in wG.nodes:
			wG.add_node(tuple(startLocation))
		if endLocation not in wG.nodes:
			wG.add_node(tuple(endLocation))
		shortestPathLength = nx.shortest_path_length(g, startLocation, endLocation)
		shortestPaths.append([tuple(startLocation), tuple(endLocation), shortestPathLength])
		wG.add_edge(u_of_edge=tuple(startLocation), v_of_edge=tuple(endLocation), weight=shortestPathLength)
		wG.add_edge(u_of_edge=tuple(endLocation), v_of_edge=tuple(startLocation), weight=shortestPathLength)

tsp = nx.approximation.traveling_salesman_problem(wG, nodes=locations, cycle=False,
                                                  source=startNode, method=nx.approximation.greedy_tsp)
totalDistance = 0
for idx in range(len(tsp)-1):
	for idy in shortestPaths:
		if (tsp[idx] == idy[0] and tsp[idx+1] == idy[1]) or (tsp[idx] == idy[1] and tsp[idx+1] == idy[0]):
			totalDistance += idy[2]
print("AoC_2016_24.1:", totalDistance)


tsp = nx.approximation.traveling_salesman_problem(wG, nodes=locations, cycle=True, seed=0,
                                                  source=startNode, init_cycle="greedy", method=nx.approximation.threshold_accepting_tsp)
totalDistance = 0
for idx in range(len(tsp)-1):
	for idy in shortestPaths:
		if (tsp[idx] == idy[0] and tsp[idx+1] == idy[1]) or (tsp[idx] == idy[1] and tsp[idx+1] == idy[0]):
			totalDistance += idy[2]
print("AoC_2016_24.2:", totalDistance)

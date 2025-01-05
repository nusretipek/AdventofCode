import numpy as np
import networkx as nx


designerNumber = int(open("input.txt").read().strip())
emptyGrid = np.zeros((100, 100), dtype=np.int8)
start = (1, 1)
destination = (39, 31)


def fillGrid(g, n):
	for x in range(g.shape[1]):
		for y in range(g.shape[0]):
			s = (x**2 + 3*x + 2*x*y + y + y**2) + n
			if bin(s).count("1") % 2 == 0:
				g[y, x] = 1
	return g


grid = fillGrid(emptyGrid, designerNumber)
graph = nx.Graph()

for i in range(grid.shape[0]):
	for j in range(grid.shape[1]):
		if grid[i][j] == 1:
			graph.add_node((i, j))

for node in graph.nodes():
	for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
		tempNode = (node[0]+i, node[1]+j)
		if tempNode in graph.nodes:
			graph.add_edge(node, tempNode, weight=1)

shortestPaths = nx.all_shortest_paths(graph, source=start, target=destination, weight="None", method="dijkstra")
shortestPaths = [_ for _ in shortestPaths]
shortestPathLength = nx.shortest_path_length(graph, source=start, target=destination, weight="None", method="dijkstra")
print("AoC_2016_13.1:", shortestPathLength)

reachableBy50Steps = 0
for node in graph.nodes():
	try:
		shortestPathLength = nx.shortest_path_length(graph, source=start, target=node)
		if shortestPathLength <= 50:
			reachableBy50Steps += 1
	except nx.exception.NetworkXNoPath:
		continue

print("AoC_2016_13.2:", reachableBy50Steps)



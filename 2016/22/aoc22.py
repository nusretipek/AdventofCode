import re
import numpy as np
import networkx as nx

df = [re.sub(r"\s+", " ", _).split(" ") for _ in open("input.txt").read().strip().split("\n")][2:]
size = re.findall(r"\d+", df[-1][0])
network = np.zeros((int(size[1])+1, int(size[0])+1, 2), dtype=np.int64)

# Parse df
for node in df:
	x, y = re.findall(r"\d+", node[0])
	x, y = int(x), int(y)
	network[y, x][0] = int(re.findall(r"\d+", node[2])[0])
	network[y, x][1] = int(re.findall(r"\d+", node[3])[0])

pairs = []
networkFlattened = network.reshape(-1, 2)
for idx, nodeX in enumerate(networkFlattened):
	for idy, nodeY in enumerate(networkFlattened):
		if idx != idy:
			if (0 < nodeX[0]) and (nodeX[0] <= nodeY[1]):
				pairs.append((idx, idy))
print("AoC_2016_22.1:", len(pairs))


emptyNode = (pairs[0][1] // network.shape[1], pairs[0][1] % network.shape[1])
g = nx.DiGraph()
initialStop = (0, network.shape[1]-2)
for idx in range(network.shape[0]):
	for idy in range(network.shape[1]):
		g.add_node((idx, idy))

for idx in range(network.shape[0]):
	for idy in range(network.shape[1]):
		for idz in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
			if (idx + idz[0], idy + idz[1]) in g.nodes() and np.sum(network[idx, idy]) >= network[idx + idz[0], idy + idz[1]][0]:
				g.add_edge((idx, idy), (idx + idz[0], idy + idz[1]))

shortestPathLength = nx.shortest_path_length(g, emptyNode, initialStop) + 1  # shortest path + initial swap
remainingSwaps = (network.shape[1]-2) * 5
print("AoC_2016_22.2:", shortestPathLength+remainingSwaps)





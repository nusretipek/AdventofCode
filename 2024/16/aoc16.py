import networkx as nx

# Read map and define directions
arr = [_ for _ in open("input.txt").read().strip().split("\n")]
directionDict = {"right": [0, 1], "down": [1, 0],
                 "left": [0, -1], "up": [-1, 0]}

# Create Network graph
g = nx.DiGraph()
startNode, endNode = None, None

# Parse Nodes to graph
for idx, row in enumerate(arr):
	for idy, element in enumerate(row):
		if element != '#':
			for direction in ["right", "down", "left", "up"]:
				g.add_node(((idx, idy), direction))
			if element == 'S':
				startNode = (idx, idy)
			if element == "E":
				endNode = (idx, idy)

# Parse Edges to graph
for node, direction in g.nodes:
	for d in list(directionDict.keys()):
		connectedNode = (node[0] + directionDict[d][0],
		                 node[1] + directionDict[d][1])

		if direction == d and (connectedNode, direction) in g.nodes:
			g.add_edge((node, direction), (connectedNode, direction), weight=1)
		if direction != d:
			g.add_edge((node, direction), (node, d), weight=1000)

# Add final destination
for d in directionDict.keys():
	g.add_edge((endNode, d), "endNode", weight=0)

# Find the shortest path with weights
shortestPathLength = nx.shortest_path_length(g, (startNode, "right"), "endNode", weight="weight")
print("AoC_2024_16.1:", shortestPathLength)

# Find all shortest paths
shortestPaths = nx.all_shortest_paths(g, (startNode, "right"), "endNode", weight="weight")
bestSeatNodes = set([j[0] for i in shortestPaths for j in i if j != "endNode"])
print("AoC_2024_16.2:", len(bestSeatNodes))

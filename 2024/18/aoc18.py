import numpy as np
import networkx as nx

gridSize, byteLength = 6, 12  # gridSize was 70, byteLength 1024
startNode = (0, 0)
EndNode = (gridSize, gridSize)
bytesLocations = np.array([_.split(",") for _ in open("input.txt").read().strip().split("\n")], dtype=np.int16)
arr = np.zeros((gridSize+1, gridSize+1), dtype=np.int8)

for _ in range(byteLength):
	arr[*bytesLocations[_][::-1]] = 1

g = nx.DiGraph()
for idx in range(arr.shape[0]):
	for idy in range(arr.shape[1]):
		g.add_node((idx, idy))

for idx in range(arr.shape[0]):
	for idy in range(arr.shape[1]):
		if arr[idx, idy] == 0:
			if (idy+1) < arr.shape[1] and arr[idx][idy+1] == 0:
				g.add_edge((idx, idy), (idx, idy+1))
			if (idx+1) < arr.shape[0] and arr[idx+1][idy] == 0:
				g.add_edge((idx, idy), (idx+1, idy))
			if (idy-1) >= 0 and arr[idx][idy-1] == 0:
				g.add_edge((idx, idy), (idx, idy-1))
			if (idx-1) >= 0 and arr[idx-1][idy] == 0:
				g.add_edge((idx, idy), (idx-1, idy))

print("AoC_2024_18.1:", nx.shortest_path_length(g, source=startNode, target=EndNode))

###############################################################################
#######################        PART 2         #################################
###############################################################################

gridSize, byteLength = 6, 12  # gridSize was 70, byteLength 1024
startNode = (0, 0)
EndNode = (gridSize, gridSize)
bytesLocations = np.array([_.split(",") for _ in open("input.txt").read().strip().split("\n")], dtype=np.int16)

lowestByte = 12  # lowestByte was 1024
highestByte = len(bytesLocations)
while highestByte - lowestByte > 1:
	currentByte = lowestByte + (highestByte - lowestByte) // 2
	arr = np.zeros((gridSize + 1, gridSize + 1), dtype=np.int8)
	for _ in range(currentByte):
		arr[*bytesLocations[_][::-1]] = 1

	g = nx.DiGraph()
	for idx in range(arr.shape[0]):
		for idy in range(arr.shape[1]):
			g.add_node((idx, idy))

	for idx in range(arr.shape[0]):
		for idy in range(arr.shape[1]):
			if arr[idx, idy] == 0:
				if (idy+1) < arr.shape[1] and arr[idx][idy+1] == 0:
					g.add_edge((idx, idy), (idx, idy+1))
				if (idx+1) < arr.shape[0] and arr[idx+1][idy] == 0:
					g.add_edge((idx, idy), (idx+1, idy))
				if (idy-1) >= 0 and arr[idx][idy-1] == 0:
					g.add_edge((idx, idy), (idx, idy-1))
				if (idx-1) >= 0 and arr[idx-1][idy] == 0:
					g.add_edge((idx, idy), (idx-1, idy))

	try:
		shortestPathLength = nx.shortest_path_length(g, source=startNode, target=EndNode)
		lowestByte = currentByte
	except:
		highestByte = currentByte

print("AoC_2024_18.2:", str(bytesLocations[lowestByte][0]) + "," + str(bytesLocations[lowestByte][1]))

import numpy as np
import sys

arr = [_ for _ in open("input.txt").read().strip()]
grid = np.zeros((40, len(arr)), dtype=np.int8)

# Parse initial state
for i in range(len(arr)):
	if arr[i] == "^":
		grid[0][i] = 1

# Get full grid
for i in range(1, grid.shape[0]):
	for j in range(grid.shape[1]):
		right, left = 0, 0
		center = grid[i-1][j]
		if 0 <= j-1 < grid.shape[1]:
			left = grid[i-1][j-1]
		if 0 <= j+1 < grid.shape[1]:
			right = grid[i-1][j+1]
		if ((left == 1 and center == 1 and right == 0) or
			(left == 0 and center == 1 and right == 1) or
			(left == 1 and center == 0 and right == 0) or
			(left == 0 and center == 0 and right == 1)):
			grid[i][j] = 1
	if i % 1000 == 0:
		print(i)

print("AoC_2016_18.1:", (grid.shape[0]*grid.shape[1])-np.count_nonzero(grid))


grid = np.zeros((400000, len(arr)+2), dtype=np.int8).tolist()
safeCounter = 0
for i in range(0, len(arr)):
	if arr[i] == "^":
		grid[0][i+1] = 1
	else:
		safeCounter += 1

traps = [[1, 1, 0], [0, 1, 1], [1, 0, 0], [0, 0, 1]]
for i in range(1, len(grid)):
	for j in range(1, len(grid[i])-1):
		if grid[i-1][j-1:j+2] in traps:
			grid[i][j] = 1
		else:
			safeCounter += 1

print("AoC_2016_18.2:", safeCounter)




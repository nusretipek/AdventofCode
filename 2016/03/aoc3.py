import re
import numpy as np

triangles = [sorted([int(i) for i in re.findall("\d+", _)]) for _ in open("input.txt").read().strip().split("\n")]
possibleTriangleCount = 0
for triangle in triangles:
	if triangle[0] + triangle[1] > triangle[2]:
		possibleTriangleCount += 1
print("AoC_2016_3.1:", possibleTriangleCount)

triangles = [[int(i) for i in re.findall("\d+", _)] for _ in open("input.txt").read().strip().split("\n")]
triangles = np.array(triangles)
triangles = np.transpose(triangles).reshape(-1, 3)
possibleTriangleCount = 0
for triangle in triangles:
	triangle = np.sort(triangle)
	if triangle[0] + triangle[1] > triangle[2]:
		possibleTriangleCount += 1
print("AoC_2016_3.2:", possibleTriangleCount)


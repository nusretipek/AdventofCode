directions = [[_[0], int(_[1:])] for _ in open("input.txt").read().strip().split(", ")]
directionDict = {"R": {"N": "E", "E": "S", "S": "W", "W": "N"},
                 "L": {"N": "W", "E": "N", "S": "E", "W": "S"}}

currentDirection = "N"
position = [0, 0]
visited = []
firstLocationVisitedTwice = None

for direction in directions:
	currentDirection = directionDict[direction[0]][currentDirection]
	if currentDirection == "N":
		for i in range(direction[1]):
			position[0] += 1
			if firstLocationVisitedTwice is None and tuple(position.copy()) in visited:
				firstLocationVisitedTwice = [position[0], position[1]]
			visited.append(tuple(position.copy()))
	elif currentDirection == "E":
		for i in range(direction[1]):
			position[1] += 1
			if firstLocationVisitedTwice is None and tuple(position.copy()) in visited:
				firstLocationVisitedTwice = [position[0], position[1]]
			visited.append(tuple(position.copy()))
	elif currentDirection == "S":
		for i in range(direction[1]):
			position[0] -= 1
			if firstLocationVisitedTwice is None and tuple(position.copy()) in visited:
				firstLocationVisitedTwice = [position[0], position[1]]
			visited.append(tuple(position.copy()))
	else:
		for i in range(direction[1]):
			position[1] -= 1
			if firstLocationVisitedTwice is None and tuple(position.copy()) in visited:
				firstLocationVisitedTwice = [position[0], position[1]]
			visited.append(tuple(position.copy()))

print("AoC_2016_1.1:", abs(position[0]) + abs(position[1]))
print("AoC_2016_1.2:", abs(firstLocationVisitedTwice[0]) + abs(firstLocationVisitedTwice[1]))

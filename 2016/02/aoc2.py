instructions = [_ for _ in open("input.txt").read().strip().split("\n")]

numpadDict = {1: {"R": 2, "D": 4},
              2: {"R": 3, "L": 1, "D": 5},
              3: {"L": 2, "D": 6},
              4: {"R": 5, "U": 1, "D": 7},
              5: {"R": 6, "L": 4, "U": 2, "D": 8},
              6: {"L": 5, "U": 3, "D": 9},
              7: {"R": 8, "U": 4},
              8: {"R": 9, "L": 7, "U": 5},
              9: {"L": 8, "U": 6}}

numpadDictComplex = {1: {"D": 3},
                     2: {"R": 3, "D": 6},
                     3: {"R": 4, "L": 2, "U": 1, "D": 7},
                     4: {"L": 3, "D": 8},
                     5: {"R": 6},
                     6: {"R": 7, "L": 5, "U": 2, "D": "A"},
                     7: {"R": 8, "L": 6, "U": 3, "D": "B"},
                     8: {"R": 9, "L": 7, "U": 4, "D": "C"},
                     9: {"L": 8},
                     "A": {"R": "B", "U": 6},
                     "B": {"R": "C", "L": "A", "U": 7, "D": "D"},
                     "C": {"L": "B", "U": 8},
					 "D": {"U": "B"}}


code = ""
position = 5
for instruction in instructions:
	for direction in instruction:
		if direction in numpadDict[position]:
			position = numpadDict[position][direction]
	code += str(position)
print("AoC_2016_2.1:", code)


code = ""
position = 5
for instruction in instructions:
	for direction in instruction:
		if direction in numpadDictComplex[position]:
			position = numpadDictComplex[position][direction]
	code += str(position)
print("AoC_2016_2.2:", code)

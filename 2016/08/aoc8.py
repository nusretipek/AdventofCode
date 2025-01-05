import re
import numpy as np


def parseInstructions(s):
	if "rect" in s:
		c, r, = re.findall(r"\d+", s)
		return "create", int(c), int(r)
	elif "row" in s:
		r, s, = re.findall(r"\d+", s)
		return "rowShift", int(r), int(s)
	elif "column" in s:
		c, s, = re.findall(r"\d+", s)
		return "columnShift", int(c), int(s)


instructions = [parseInstructions(_) for _ in open("input.txt").read().strip().split("\n")]
display = np.zeros((6, 50), dtype=np.int8)


for instruction in instructions:
	if instruction[0] == "create":
		display[:instruction[2], :instruction[1]] = 1
	if instruction[0] == "rowShift":
		row = display[instruction[1], :]
		for _ in range(instruction[2]):
			newRow = np.concatenate((row[-1:], row[:-1]))
			display[instruction[1], :] = newRow
	if instruction[0] == "columnShift":
		column = display[:, instruction[1]]
		for _ in range(instruction[2]):
			newColumn = np.concatenate((column[-1:], column[:-1]))
			display[:, instruction[1]] = newColumn

print("AoC_2016_8.1:", np.count_nonzero(display))

print("AoC_2016_8.2:")
for i in range(display.shape[0]):
	s = ""
	for j in range(display.shape[1]):
		if j != 0 and j % 5 == 0:
			s += " | "
		if display[i][j] == 1:
			s += "x"
		else:
			s += " "
	print(s)

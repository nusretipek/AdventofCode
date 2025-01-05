def execute(r, i, prevOut=None):
	index = 1
	if i[0] == "cpy":
		if i[1] in r.keys():
			r[i[2]] = r[i[1]]
		else:
			r[i[2]] = int(i[1])
	elif i[0] == "inc":
		r[i[1]] += 1
	elif i[0] == "dec":
		r[i[1]] -= 1
	elif i[0] == "jnz":
		if i[1] in r.keys():
			if r[i[1]] != 0:
				if i[2] in r.keys():
					index = int(r[i[2]])
				else:
					index = int(i[2])
		else:
			if int(i[1]) != 0:
				if i[2] in r.keys():
					index = int(r[i[2]])
				else:
					index = int(i[2])
	elif i[0] == "out":
		if i[1] in r.keys():
			prevOut += str(r[i[1]])
		else:
			prevOut += str(i[1])

	return r, index, prevOut


instructions = [_.split(" ") for _ in open("input.txt").read().strip().split("\n")]
idy = 0
while True:
	idx, output = 0, ""
	registers = {"a": idy, "b": 0, "c": 0, "d": 0}
	while idx < len(instructions):
		registers, indexUpdate, output = execute(registers, instructions[idx], output)
		idx += indexUpdate
		if len(output) == 10:
			break
	if output == "0101010101":
		print("AoC_2016_25.1:", idy)
		break
	idy += 1

def execute(r, i, a, currentIndex):
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
	elif i[0] == "tgl":
		if i[1] in r.keys():
			toggleIndex = currentIndex + r[i[1]]
			if 0 <= toggleIndex < len(a):
				if a[toggleIndex][0] in ["tgl", "dec"]:
					a[toggleIndex][0] = "inc"
				elif a[toggleIndex][0] == "inc":
					a[toggleIndex][0] = "dec"
				elif a[toggleIndex][0] == "jnz":
					a[toggleIndex][0] = "cpy"
				else:
					a[toggleIndex][0] = "jnz"
	return r, index, a


instructions = [_.split(" ") for _ in open("input.txt").read().strip().split("\n")]
registers = {"a": 7, "b": 0, "c": 0, "d": 0}
idx = 0
while idx < len(instructions):
	if idx == 5:
		registers["a"] += registers["b"]*registers["d"]
		idx = 10
		continue
	else:
		registers, indexUpdate, instructions = execute(registers, instructions[idx], instructions, idx)

	idx += indexUpdate
print("AoC_2016_23.1:", registers["a"])

instructions = [_.split(" ") for _ in open("input.txt").read().strip().split("\n")]
registers = {"a": 12, "b": 0, "c": 0, "d": 0}
idx = 0
while idx < len(instructions):
	if idx == 5:
		registers["a"] += registers["b"]*registers["d"]
		idx = 10
		continue
	else:
		registers, indexUpdate, instructions = execute(registers, instructions[idx], instructions, idx)

	idx += indexUpdate
print("AoC_2016_23.2:", registers["a"])

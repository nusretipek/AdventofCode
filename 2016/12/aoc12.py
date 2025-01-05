instructions = [_.split(" ") for _ in open("input.txt").read().strip().split("\n")]


def execute(r, i):
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
				index = int(i[2])
		else:
			if int(i[1]) != 0:
				index = int(i[2])
	return r, index


registers = {"a": 0, "b": 0, "c": 0, "d": 0}
idx = 0
while idx < len(instructions):
	registers, indexUpdate = execute(registers, instructions[idx])
	idx += indexUpdate
print("AoC_2016_12.1:", registers["a"])


registers = {"a": 0, "b": 0, "c": 1, "d": 0}
idx = 0
while idx < len(instructions):
	registers, indexUpdate = execute(registers, instructions[idx])
	idx += indexUpdate
print("AoC_2016_12.2:", registers["a"])

import numpy as np

arr = [_.split("\n") for _ in open("input.txt").read().strip().split("\n\n")]
states = {_.split(": ")[0]: int(_.split(": ")[1]) for _ in arr[0]}
instructions = [("states['" + _.replace(" AND ", "']&states['").replace(" OR ", "']|states['").replace(" XOR ", "']^states['")).split(" -> ")
                for _ in arr[1]]
instructions = [[_[0]+"']", _[1]]for _ in instructions]

c = 0
while len(instructions) > 0:
    if c % len(instructions) == 0:
        c = 0
    try:
        states[instructions[c][1]] = eval(instructions[c][0])
        del instructions[c]
    except KeyError:
        c += 1

sortedZ = sorted([(int(float(key[1:])), value) for key, value in states.items() if key[0] == "z"], key=lambda x: x[0])[::-1]
sortedZBits = "".join([str(_[1]) for _ in sortedZ])
print("AoC_2024_24.1:", eval("0b" + sortedZBits))

###############################################################################
#######################        PART 2         #################################
###############################################################################

arr = [_.split("\n") for _ in open("input.txt").read().strip().split("\n\n")]
states = {_.split(": ")[0]: int(_.split(": ")[1]) for _ in arr[0]}
instructions = [_.replace(" AND ", " & ").replace(" OR ", " | ").replace(" XOR ", " ^ ").split(" -> ")
                for _ in arr[1]]
instructions = [[_[0].split(" ") + [_[1]]][0] for _ in instructions]
faultyConnections = []


def matchRelay(outNode, operator):
    for instruct in instructions:
        if instruct[1] == operator and outNode in [instruct[0], instruct[1]]:
            return True
    return False


for instruction in instructions:
    flag = False
    if instruction[1] == "^":
        nodeCheck = []
        for node in [instruction[0], instruction[2], instruction[3]]:
            nodeCheck.append(node[0] not in ["x", "y", "z"])
        if all(nodeCheck):
            flag = True
        if "x00" not in [instruction[0], instruction[2]] and matchRelay(instruction[3], "|"):
            flag = True
    else:
        if instruction[3][0] == "z" and int(instruction[3][1:]) != 45:
            flag = True
    if instruction[1] == "&":
        if "x00" not in [instruction[0], instruction[2]] and  matchRelay(instruction[3], "^"):
            flag = True

    if flag:
        faultyConnections.append(instruction[3])

print("AoC_2024_24.2:", ",".join(sorted(faultyConnections)))

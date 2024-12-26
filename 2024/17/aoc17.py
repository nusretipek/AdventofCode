import numpy as np
import re


def getComboOperandValue(v, r):
    if 0 <= v <= 3:
        return v
    elif 4 <= v <= 6:
        return r[v - 4]
    else:
        return None


def performInstruction(instructionT, r):
    if instructionT[0] == 0:
        r[0] = r[0] // (2 ** getComboOperandValue(instructionT[1], r))
    elif instructionT[0] == 1:
        r[1] = r[1] ^ instructionT[1]
    elif instructionT[0] == 2:
        r[1] = getComboOperandValue(instructionT[1], r) % 8
    elif instructionT[0] == 3:
        if r[0] == 0:
            pass
        else:
            return int(instructionT[1] // 2)
    elif instructionT[0] == 4:
        r[1] = r[1] ^ r[2]
    elif instructionT[0] == 5:
        return str(getComboOperandValue(instructionT[1], r) % 8)
    elif instructionT[0] == 6:
        r[1] = r[0] // (2 ** getComboOperandValue(instructionT[1], r))
    elif instructionT[0] == 7:
        r[2] = r[0] // (2 ** getComboOperandValue(instructionT[1], r))
    else:
        pass
    return r


instructions = [re.sub(r'[^\d+,]', '', _) for _ in open("input.txt").read().strip().split("\n")]
registers = [int(instructions[0]), int(instructions[1]), int(instructions[2])]
originalInstructions = instructions[-1]
programInstructions = [(int(instructions[-1].split(",")[idx]), int((instructions[-1].split(",")[idx + 1]))) for
                       idx, element in enumerate(instructions[-1].split(",")) if idx % 2 == 0]

idx = 0
outputArr = []
while idx < len(programInstructions):
    result = performInstruction(programInstructions[idx], registers)
    if isinstance(result, list):
        registers = result
        idx += 1
    elif isinstance(result, int):
        idx = result
    elif isinstance(result, str):
        outputArr.append(result)
        idx += 1
    else:
        raise Exception("Invalid instruction!")

print("AoC_2024_17.1:", ",".join(outputArr))

###############################################################################
#######################        PART 2         #################################
###############################################################################
## Input dependent - manual reverse engineering


def getReverseSequence(p):
    p = np.array(p).flatten()
    foundSequence = [int(p[-1])]
    for operand in p[::-1]:
        tempFoundSequence = []
        for lastOperand in range(8):
            for previousOperand in foundSequence:
                registerA = 8 * previousOperand + lastOperand
                registerB = registerA % 8
                registerB = registerB ^ 1
                registerC = registerA // (2 ** registerB)
                registerB = registerB ^ 4
                registerB = registerB ^ registerC
                if registerB % 8 == operand:
                    tempFoundSequence.append(registerA)
        foundSequence = tempFoundSequence
    return sorted(foundSequence)[0]


print("AoC_2024_17.2: ", getReverseSequence(programInstructions))

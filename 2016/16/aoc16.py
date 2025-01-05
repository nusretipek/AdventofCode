import re


def dragonCurve(s):
	tempS = s[::-1]
	tempS = re.sub(r"(0)", "T", tempS)
	tempS = re.sub(r"(1)", "0", tempS)
	tempS = re.sub(r"(T)", "1", tempS)
	return s + "0" + tempS


def checkSum(s):
	checksum = s
	while len(checksum) % 2 == 0:
		newChecksum = ""
		for idx in range(0, len(checksum), 2):
			if checksum[idx] == checksum[idx+1]:
				newChecksum += "1"
			else:
				newChecksum += "0"
		checksum = newChecksum
	return checksum


state = open("input.txt").read().strip()
fillLength = 272

while len(state) < fillLength:
	state = dragonCurve(state)
print("AoC_2016_16.1:", checkSum(state[:fillLength]))

fillLength = 35651584

while len(state) < fillLength:
	state = dragonCurve(state)
print("AoC_2016_16.2:", checkSum(state[:fillLength]))

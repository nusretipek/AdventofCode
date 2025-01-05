import re


def parseInitialConditions(s):
	d = {}
	for instruction in s:
		if "value" in instruction:
			chipID, botID = re.findall(r"\d+", instruction)
			if "bot " + botID not in d:
				d["bot " + botID] = [int(chipID)]
			else:
				d["bot " + botID].append(int(chipID))
	return d


def parseGiveaways(s):
	arr = []
	for instruction in s:
		if "bot" in instruction and "value" not in instruction:
			giverBotID, lowerID, higherID = re.findall(r"(\w+)\s(\d+)", instruction)
			arr.append((" ".join(giverBotID), " ".join(lowerID), " ".join(higherID)))
	return arr


instructions = [_ for _ in open("input.txt").read().strip().split("\n")]
state = parseInitialConditions(instructions)
giveaways = parseGiveaways(instructions)


while len(giveaways) > 0:
	processed = []
	for idx, giveaway in enumerate(giveaways):
		if giveaway[0] in state and len(state[giveaway[0]]) == 2:
			if 61 in state[giveaway[0]] and 17 in state[giveaway[0]]:
				print("AoC_2016_10.1:", int(giveaway[0].split(" ")[1]))
			if giveaway[1] in state:
				state[giveaway[1]].append(min(state[giveaway[0]]))
			else:
				state[giveaway[1]] = [min(state[giveaway[0]])]
			state[giveaway[0]].remove(min(state[giveaway[0]]))
			if giveaway[2] in state:
				state[giveaway[2]].append(state[giveaway[0]][0])
			else:
				state[giveaway[2]] = [state[giveaway[0]][0]]
			state[giveaway[0]] = []
			processed.append(idx)
	giveaways = [_ for idy, _ in enumerate(giveaways) if idy not in processed]

print("AoC_2016_10.2:",  state["output 0"][0] * state["output 1"][0] * state["output 2"][0])

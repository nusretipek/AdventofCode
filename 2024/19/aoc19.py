import functools
import re

arr = [_ for _ in open("input.txt").read().strip().split("\n\n")]
patterns = tuple(arr[0].replace(" ", "").split(","))
designs = arr[1].split("\n")


@functools.lru_cache(maxsize=None)
def countPossibleCombinations(p, d):
	if len(d) == 0:
		return 1

	possibleCombinations = 0
	for pX in p:
		if len(re.findall(rf"^{pX}", d)):
			subDesign = re.sub(rf"^{pX}", "", d)
			possibleCombinations += countPossibleCombinations(p, subDesign)

	return possibleCombinations


designCombinationCounts = []
for design in designs:
	designCombinationCounts.append(countPossibleCombinations(patterns, design))

print("AoC_2024_19.1:", len(designCombinationCounts)-designCombinationCounts.count(0))
print("AoC_2024_19.2:", sum(designCombinationCounts))

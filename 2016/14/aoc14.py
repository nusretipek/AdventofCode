import hashlib
import re

salt = open("input.txt").read().strip()
searchExpressionTriplet = r"([a-z0-9])\1\1"


def getMD5(n):
	return hashlib.md5((salt + str(n)).encode()).hexdigest()


def getMD5HashToHash(h):
	return hashlib.md5(h.encode()).hexdigest()


counters, keys = [], []
i = 0
while len(keys) < 64 or len(counters) > 0:
	hashCode = getMD5(i)

	indicesToRemove = []
	removed = []
	for idx, potentialKey in enumerate(counters):
		if potentialKey[0] in hashCode:
			keys.append((potentialKey[1], potentialKey[3]))
			indicesToRemove.append(idx)
			removed.append(potentialKey[1][0])
		else:
			counters[idx][2] -= 1
		if counters[idx][2] == 0:
			indicesToRemove.append(idx)
	counters = [_ for idx, _ in enumerate(counters) if idx not in indicesToRemove]

	triplets = re.findall(searchExpressionTriplet, hashCode)

	if len(keys) < 64 and len(triplets) > 0:
		counters.append(["".join(triplets[0]*5), hashCode, 1000, i])

	i += 1
print("AoC_2016_14.1:", sorted(keys, key=lambda x: x[1])[63][1])


counters, keys = [], []
i = 0
while len(keys) < 64 or len(counters) > 0:
	hashCode = getMD5(i)
	for _ in range(2016):
		hashCode = getMD5HashToHash(hashCode)

	indicesToRemove = []
	removed = []
	for idx, potentialKey in enumerate(counters):
		if potentialKey[0] in hashCode:
			keys.append((potentialKey[1], potentialKey[3]))
			indicesToRemove.append(idx)
			removed.append(potentialKey[1][0])
		else:
			counters[idx][2] -= 1
		if counters[idx][2] == 0:
			indicesToRemove.append(idx)
	counters = [_ for idx, _ in enumerate(counters) if idx not in indicesToRemove]

	triplets = re.findall(searchExpressionTriplet, hashCode)

	if len(keys) < 64 and len(triplets) > 0:
		counters.append(["".join(triplets[0]*5), hashCode, 1000, i])

	i += 1

print("AoC_2016_14.2:", sorted(keys, key=lambda x: x[1])[63][1])

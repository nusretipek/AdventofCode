import numpy as np

arr = [_.split("-") for _ in open("input.txt").read().strip().split("\n")]
arr = np.sort(np.array(arr, dtype=np.int64), axis=0)

prevHigh = None
for idx, (low, high) in enumerate(arr):
	if prevHigh is None:
		prevHigh = high
	else:
		if low <= prevHigh+1:
			prevHigh = high
		else:
			print("AoC_2016_20.1:", prevHigh+1)
			break

allowedIPs = []
prevHigh = None
for idx, (low, high) in enumerate(arr):
	if prevHigh is None:
		prevHigh = high
	else:
		if low <= prevHigh+1:
			prevHigh = high
		else:
			for _ in range(prevHigh+1, low):
				allowedIPs.append(_)
			prevHigh = high

print("AoC_2016_20.2:", len(allowedIPs))

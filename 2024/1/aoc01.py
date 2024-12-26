import numpy as np

arr = np.array([_.split("  ") for _ in open("input.txt", "r").read().strip().split("\n")], dtype=np.int32)
arrAS0, arrAS1 = arr[:, 0].argsort(), arr[:, 1].argsort()
print("AoC_2024_1.1:", sum([abs(arr[arrAS0[idx], 0] - arr[arrAS1[idx], 1]) for idx in range(len(arrAS0))]))

counts = dict(zip(*np.unique(arr[:, 1], return_counts=True)))
print("AoC_2024_1.2:", sum([idx*counts[idx] for idx in arr[:, 0] if idx in counts.keys()]))

import functools
import numpy as np


@functools.lru_cache(maxsize=None)
def countStones(stone, blinkCount):
	if blinkCount == 0:
		return 1

	total = 0
	if stone == 0:
		total += countStones(1, blinkCount-1)
	elif len(str(stone)) % 2 == 0:
		total += countStones(int(str(stone)[:len(str(stone))//2]), blinkCount-1)
		total += countStones(int(str(stone)[len(str(stone))//2:]), blinkCount-1)
	else:
		total += countStones(int(stone*2024), blinkCount-1)

	return total


stones = np.array(open("input.txt").read().strip().split(" "), dtype=np.int64)
print('AoC_2024_11.1:', sum([countStones(_, 25) for _ in stones]))
print('AoC_2024_11.2:', sum([countStones(_, 75) for _ in stones]))

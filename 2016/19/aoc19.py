import numpy as np

elvesCount = open("input.txt").read().strip()
whiteElephantGame = np.zeros((int(elvesCount),), dtype=np.int32) + 1

while np.sort(whiteElephantGame)[-2] != 0:
	havePresentElves = np.nonzero(whiteElephantGame)[0]
	if len(havePresentElves) % 2 != 0:
		havePresentElves = np.concatenate((havePresentElves, [havePresentElves[0]]))

	for idx in range(0, len(havePresentElves), 2):
		whiteElephantGame[havePresentElves[idx]] += whiteElephantGame[havePresentElves[idx+1]]
		whiteElephantGame[havePresentElves[idx+1]] = 0
print("AoC_2016_19.1:", np.nonzero(whiteElephantGame)[0][0]+1)


whiteElephantGame = list(range(1, int(elvesCount)+1))
while len(whiteElephantGame) > 1:
	elvesLeft = len(whiteElephantGame)
	if elvesLeft % 2 == 0:
		initialIndex = int(elvesLeft // 2)
		x = []
		idy = 0
		idx = 0
		while initialIndex + idx < elvesLeft:
			x.append(whiteElephantGame[initialIndex + idx])
			idx += 3
			idy += 1
		idx = 0
		while initialIndex + idx + 1 < elvesLeft:
			x.append(whiteElephantGame[initialIndex + idx + 1])
			idx += 3
			idy += 1
		setX = set(x)
		whiteElephantGame = [_ for _ in whiteElephantGame if _ not in setX]
		whiteElephantGame = whiteElephantGame[idy:] + whiteElephantGame[:idy]
	else:
		initialIndex = int((elvesLeft-1) // 2)
		x = []
		idy = 0
		idx = 0
		while initialIndex + idx < elvesLeft:
			x.append(whiteElephantGame[initialIndex + idx])
			idx += 3
			idy += 1
		idx = 0
		while initialIndex + idx + 2 < elvesLeft:
			x.append(whiteElephantGame[initialIndex + idx + 2])
			idx += 3
			idy += 1
		setX = set(x)
		whiteElephantGame = [_ for _ in whiteElephantGame if _ not in setX]
		whiteElephantGame = whiteElephantGame[idy:] + whiteElephantGame[:idy]

print("AoC_2016_19.2:", whiteElephantGame[0])


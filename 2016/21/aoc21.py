import re

instructions = [_ for _ in open("input.txt").read().strip().split("\n")]


def parseInstruction(s, i):
	s = [_ for _ in s]

	if "swap position" in i:
		idx, idy = re.findall(r"\d+", i)
		s[int(idx)], s[int(idy)] = s[int(idy)], s[int(idx)]
		return s
	elif "swap letter" in i:
		idx, idy = [_ for idz, _ in enumerate(i.split(" ")) if idz in [2, 5]]
		for idz, e in enumerate(s):
			if e == idx:
				s[idz] = idy
			elif e == idy:
				s[idz] = idx
		return s
	elif "left" in i:
		idx = int(re.findall(r"\d+", i)[0])
		while idx > len(s):
			idx -= len(s)
			s = s[int(idx):] + s[:int(idx)]
		s = s[int(idx):] + s[:int(idx)]
		return s
	elif "right" in i:
		idx = int(re.findall(r"\d+", i)[0])
		while idx > len(s):
			idx -= len(s)
			s = s[-len(s):] + s[:-len(s)]
		s = s[-int(idx):] + s[:-int(idx)]
		return s
	elif "move" in i:
		idx, idy = re.findall(r"\d+", i)
		removedLetter = s[int(idx)]
		removedSequence = s[:int(idx)] + s[int(idx)+1:]
		s = removedSequence[:int(idy)] + [removedLetter] + removedSequence[int(idy):]
		return s
	elif "reverse" in i:
		idx, idy = re.findall(r"\d+", i)
		s = s[:int(idx)] + s[int(idx):int(idy)+1][::-1] + s[int(idy)+1:]
		return s
	elif "rotate" in i:
		indexLetter = i.split(" ")[-1]
		idx = s.index(indexLetter)
		if idx >= 4:
			idx += 1
		idx += 1
		while idx > len(s):
			idx -= len(s)
			s = s[-len(s):] + s[:-len(s)]
		s = s[-int(idx):] + s[:-int(idx)]
		return s


t = "abcdefgh"
for instruction in instructions:
	t = parseInstruction(t, instruction)
print("AoC_2016_21.1:", "".join(t))


def bruteForceUnRotater(s, i):
	s = [_ for _ in s]
	indexLetter = i.split(" ")[-1]

	sTemp = s.copy()
	powerSet = []
	for idy in range(len(s)):
		sTemp = sTemp[1:] + sTemp[:1]
		powerSet.append(sTemp)

	for e in powerSet:
		eTemp = e.copy()
		idx = e.index(indexLetter)
		if idx >= 4:
			idx += 1
		idx += 1
		while idx > len(e):
			idx -= len(e)
			e = e[-len(e):] + e[:-len(e)]
		e = e[-int(idx):] + e[:-int(idx)]
		if all([e[_] == s[_] for _ in range(len(e))]):
			return eTemp


def unparseInstruction(s, i):
	s = [_ for _ in s]

	if "swap position" in i:
		idx, idy = re.findall(r"\d+", i)
		s[int(idx)], s[int(idy)] = s[int(idy)], s[int(idx)]
		return s
	elif "swap letter" in i:
		idx, idy = [_ for idz, _ in enumerate(i.split(" ")) if idz in [2, 5]]
		for idz, e in enumerate(s):
			if e == idx:
				s[idz] = idy
			elif e == idy:
				s[idz] = idx
		return s
	elif "left" in i:
		idx = int(re.findall(r"\d+", i)[0])
		while idx > len(s):
			idx -= len(s)
			s = s[-len(s):] + s[:-len(s)]
		s = s[-int(idx):] + s[:-int(idx)]
		return s
	elif "right" in i:
		idx = int(re.findall(r"\d+", i)[0])
		while idx > len(s):
			idx -= len(s)
			s = s[int(idx):] + s[:int(idx)]
		s = s[int(idx):] + s[:int(idx)]
		return s
	elif "move" in i:
		idx, idy = re.findall(r"\d+", i)
		removedLetter = s[int(idy)]
		removedSequence = s[:int(idy)] + s[int(idy)+1:]
		s = removedSequence[:int(idx)] + [removedLetter] + removedSequence[int(idx):]
		return s
	elif "reverse" in i:
		idx, idy = re.findall(r"\d+", i)
		s = s[:int(idx)] + s[int(idx):int(idy)+1][::-1] + s[int(idy)+1:]
		return s
	elif "rotate" in i:
		return bruteForceUnRotater(s, i)


t = "fbgdceah"
for instruction in instructions[::-1]:
	t = unparseInstruction(t, instruction)
print("AoC_2016_21.2:", "".join(t))

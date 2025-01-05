compressedFile = open("input.txt").read().strip()


def decompressor(c):
	d = ""
	letterIndex = 0
	while letterIndex < len(c):
		if c[letterIndex] == "(":
			sequenceLength = ""
			repetition = ""
			switchFlag = True
			while c[letterIndex] != ")":
				letterIndex += 1
				if c[letterIndex] in ["x", ")"]:
					switchFlag = False
					continue
				else:
					if switchFlag:
						sequenceLength += c[letterIndex]
					else:
						repetition += c[letterIndex]
			letterIndex += 1
			tempSequence = c[letterIndex:letterIndex+int(sequenceLength)] * int(repetition)
			d += tempSequence
			letterIndex += int(sequenceLength)
		else:
			d += c[letterIndex]
			letterIndex += 1
	return d


decompressedFile = decompressor(compressedFile)
print("AoC_2016_9.1:", len(decompressedFile))


def decompressorV2(c):
	while True:
		d = ""
		letterIndex = 0
		while letterIndex < len(c):
			if c[letterIndex] == "(":
				sequenceLength = ""
				repetition = ""
				switchFlag = True
				while c[letterIndex] != ")":
					letterIndex += 1
					if c[letterIndex] in ["x", ")"]:
						switchFlag = False
						continue
					else:
						if switchFlag:
							sequenceLength += c[letterIndex]
						else:
							repetition += c[letterIndex]
				letterIndex += 1
				tempSequence = decompressorV2(c[letterIndex:letterIndex+int(sequenceLength)]) * int(repetition)
				d += tempSequence
				letterIndex += int(sequenceLength)
			else:
				d += c[letterIndex]
				letterIndex += 1
		if "(" not in d:
			return d
		else:
			c = d


decompressedFile = decompressorV2(compressedFile)
print("AoC_2016_9.2:", len(decompressedFile))

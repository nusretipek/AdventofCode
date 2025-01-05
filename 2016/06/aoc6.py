codes = [[j for j in _] for _ in open("input.txt").read().strip().split("\n")]

transposedCodes = ["".join(_) for _ in list(zip(*codes))]
s1, s2 = "", ""
for code in transposedCodes:
	codeSet = set(code)
	letterCounts = []
	for _ in codeSet:
		letterCounts.append((code.count(_), _))
	s1 += sorted(letterCounts)[-1][1]
	s2 += sorted(letterCounts)[0][1]

print("AoC_2016_6.1:", s1)
print("AoC_2016_6.2:", s2)

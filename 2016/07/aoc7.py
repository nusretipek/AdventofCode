ipAddresses = [_ for _ in open("input.txt").read().strip().split("\n")]

validIP = 0
for ip in ipAddresses:
	flag = True
	TLS = False
	for j in range(len(ip)-3):
		if ip[j] == '[':
			flag = False
		if ip[j] == ']':
			flag = True

		twoLetters = ip[j:j+2]
		nextTwoLetters = ip[j+2:j+4]
		if flag:
			if twoLetters == nextTwoLetters[::-1] and twoLetters != nextTwoLetters:
				TLS = True
		if not flag:
			if twoLetters == nextTwoLetters[::-1] and twoLetters != nextTwoLetters:
				TLS = False
				break
	if TLS:
		validIP += 1
print("AoC_2016_7.1:", validIP)


secretIP = 0
for ip in ipAddresses:
	flag = True
	hyperNetSequences = []
	for j in range(len(ip)-2):
		if ip[j] == '[':
			flag = False
		if ip[j] == ']':
			flag = True
		if not flag:
			threeLetters = ip[j:j+3]
			if (threeLetters[0] != threeLetters[1] and threeLetters[0] == threeLetters[2] and
				"[" not in threeLetters and "]" not in threeLetters):
				hyperNetSequences.append(threeLetters[1] + threeLetters[0] + threeLetters[1])

	flag = True
	for j in range(len(ip)-2):
		if ip[j] == '[':
			flag = False
		if ip[j] == ']':
			flag = True
		if flag:
			threeLetters = ip[j:j+3]
			if threeLetters in hyperNetSequences:
				secretIP += 1
				break
print("AoC_2016_7.2:", secretIP)

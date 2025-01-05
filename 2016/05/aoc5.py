import hashlib

code = open("input.txt").read().strip()


password, index = "", 0
while len(password) < 8:
	x = code + str(index)
	hashCode = hashlib.md5(x.encode()).hexdigest()
	if hashCode[:5] == "00000":
		password += hashCode[5]
	index += 1
print("AoC_2016_5.1:", password)


password, index = [-1] * 8, 0
while -1 in password:
	x = code + str(index)
	hashCode = hashlib.md5(x.encode()).hexdigest()
	if hashCode[:5] == "00000":
		if hashCode[5].isdigit() and 0 <= int(hashCode[5]) < 8 and password[int(hashCode[5])] == -1:
			password[int(hashCode[5])] = hashCode[6]
	index += 1
print("AoC_2016_5.2:", "".join(password))

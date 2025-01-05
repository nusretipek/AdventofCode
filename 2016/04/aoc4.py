import re

rooms = [_ for _ in open("input.txt").read().strip().split("\n")]


def parseRoomCodes(s):
	checksum = re.findall(r"(?<=\[)\w+", s)[0]
	sectorID = int(re.findall(r"\d+(?=\[)", s)[0])
	encryptedName = "".join(re.findall(r"\w+(?=-)", s))
	return encryptedName, sectorID, checksum


def checkRoom(s):
	s = parseRoomCodes(s)
	letterCounts = sorted([(letter, s[0].count(letter))for letter in set(s[0])], key=lambda x: (-x[1], x[0]))
	fiveMostCommonLetters = set([_[0] for _ in letterCounts[:5]])
	if fiveMostCommonLetters == set(s[2]):
		return s[1]
	else:
		return 0


def checkRoomWithShiftCipher(s):
	alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
	s = parseRoomCodes(s)
	shift = s[1] % 26
	x = ""
	for letter in s[0]:
		if alphabet.index(letter) != -1:
			x += alphabet[alphabet.index(letter) + shift]
	return x


total, realRooms = 0, []
for room in rooms:
	isRealRoom = checkRoom(room)
	if isRealRoom:
		total += isRealRoom
		realRooms.append(room)
print("AoC_2016_4.1:", total)

for room in realRooms:
	decryptedRoomName = checkRoomWithShiftCipher(room)
	if "northpoleobjects" in decryptedRoomName:
		print("AoC_2016_4.2:", checkRoom(room))

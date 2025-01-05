from dataclasses import dataclass
import hashlib


@dataclass
class Route:
	def __init__(self, location: str = (0, 0), salt: str = ""):
		self.location = location
		self.salt = salt


passcode = open("input.txt").read().strip()
routes = [Route()]
finalRoutes = []
flag = True

while len(routes) > 0:
	nextRoutes = []

	for route in routes:
		up, down, left, right = hashlib.md5((passcode + route.salt).encode()).hexdigest()[:4]
		if route.location == (3, 3):
			finalRoutes.append(route)
		elif route.location != (3, 3):
			if 0 <= route.location[0] - 1 < 4 and up in ["b", "c", "d", "e", "f"]:
				nextRoutes.append(Route(location=(route.location[0] - 1, route.location[1]), salt=route.salt + "U"))
			if 0 <= route.location[0] + 1 < 4 and down in ["b", "c", "d", "e", "f"]:
				nextRoutes.append(Route(location=(route.location[0] + 1, route.location[1]), salt=route.salt + "D"))
			if 0 <= route.location[1] - 1 < 4 and left in ["b", "c", "d", "e", "f"]:
				nextRoutes.append(Route(location=(route.location[0], route.location[1]-1), salt=route.salt + "L"))
			if 0 <= route.location[1] + 1 < 4 and right in ["b", "c", "d", "e", "f"]:
				nextRoutes.append(Route(location=(route.location[0], route.location[1]+1), salt=route.salt + "R"))

	finalRoutes = sorted(finalRoutes, key=lambda x: len(x.salt))
	routes = nextRoutes

finalRoutes = sorted(finalRoutes, key=lambda x: len(x.salt))
print("AoC_2016_17.1:", finalRoutes[0].salt)
print("AoC_2016_17.2:", len(finalRoutes[-1].salt))



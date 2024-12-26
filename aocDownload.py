import requests
import os

year = 2024
day = 13

cookieID = ""
cookie = dict(session=cookieID)
with requests.Session() as s:
    s.cookies.update(cookie)
    response = s.post(f"https://adventofcode.com/{year}/day/{day}/input")
    filePath = f'{year}/{day}'
    if not os.path.exists(filePath):
        os.makedirs(filePath, exist_ok=True)
    with open(filePath + "/inputP1.txt", 'w') as f:
        f.write(response.text.strip())

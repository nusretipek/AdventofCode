import numpy as np
import re

data = open("inputP1.txt", "r").read()
data = open("inputP2.txt", "r").read()

mulOperations = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)
multiples = [int(re.search(r'(\d+),(\d+)', idx).groups()[0]) *
             int(re.search(r'(\d+),(\d+)', idx).groups()[1]) for idx in mulOperations]
print("AoC_2024_3.1:", sum(multiples))

flag = True
total = 0
multiplesInstructOperations = re.findall(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", data)
multiplesInstructOperations = [idy for idx in multiplesInstructOperations for idy in idx if idy != '']
for idx in multiplesInstructOperations:
    if idx == "do()":
        flag = True
    elif idx == "don't()":
        flag = False
    else:
        if flag:
            mulGroup = re.search(r'(\d+),(\d+)', idx).groups()
            total += (int(mulGroup[0]) * int(mulGroup[1]))
print("AoC_2024_3.2:", total)

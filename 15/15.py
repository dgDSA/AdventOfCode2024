"""
Day 15: Warehouse Woes
"""

import re
from copy import deepcopy

R_ROW = re.compile(r"[#\.@O]+")
R_DIR = re.compile(r"[\^>v<]")

DIRS = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0)
}

with open("input.txt", encoding="utf-8") as f:
    contents = f.read()
    
warehouse = [list(m.group()) for m in R_ROW.finditer(contents)]
steps = [DIRS[m.group()] for m in R_DIR.finditer(contents)]

for row in warehouse:
    print("".join(row))
print()
# print(steps)

global robotPos
for y, row in enumerate(warehouse):
    for x, spot in enumerate(row):
        if spot == "@":
            robotPos = (x, y)


def pushCrate(cratePos, dir) -> bool:
#    print("pushCrate(", cratePos, dir, ")?")
    next = (cratePos[0] + dir[0], cratePos[1] + dir[1])
    target = warehouse[next[1]][next[0]]
    if target == "#":
#        print("cannot push")
        return False
    elif target == "." or (target == "O" and pushCrate(next, dir)):
        warehouse[next[1]][next[0]] = "O"
        warehouse[cratePos[1]][cratePos[0]] = "."
#        print("pushed")
        return True
    

def move(dir) -> tuple:
    next = (robotPos[0] + dir[0], robotPos[1] + dir[1])
    target = warehouse[next[1]][next[0]]
    if target == "#":
#        print("wall")
        return robotPos
    elif target == "." or (target == "O" and pushCrate(next, dir)):
        warehouse[next[1]][next[0]] = "@"
        warehouse[robotPos[1]][robotPos[0]] = "."
#        print("moved")
        return next
    return robotPos

for dir in steps:
    robotPos = move(dir)

for row in warehouse:
    print("".join(row))
    
print()

resultA = 0

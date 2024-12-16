"""
Day 15: Warehouse Woes
"""

import re
from copy import deepcopy

R_ROW = re.compile(r"[#\.@\[\]]+")
R_DIR = re.compile(r"[\^>v<]")

DIRS = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0)
}

with open("input.txt", encoding="utf-8") as f:
    contents = f.read()
    wideContents = contents.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    
warehouse = [list(m.group()) for m in R_ROW.finditer(wideContents)]
steps = [DIRS[m.group()] for m in R_DIR.finditer(wideContents)]

for row in warehouse:
    print("".join(row))
print()
# print(steps)

global robotPos
for y, row in enumerate(warehouse):
    for x, spot in enumerate(row):
        if spot == "@":
            robotPos = (x, y)


def pushCrate(crateLPos, dir) -> bool:
    """
    Pushes the crate whose [ is in the given position.
    """
    if dir == DIRS["<"]:
        return pushCrateLeft(crateLPos, dir)
    if dir == DIRS[">"]:
        return pushCrateRight(crateLPos, dir)
    return pushCrateVert(crateLPos, dir)

def pushCrateLeft(crateLPos, dir) -> bool:
    # print("pushCrateLeft(", crateLPos, dir, ")?")
    nextL = (crateLPos[0] + dir[0], crateLPos[1] + dir[1])
    targetL = warehouse[nextL[1]][nextL[0]]
    if targetL == "#":
        # print("cannot push left")
        return False
    if targetL == "." or targetL == "]" and pushCrateLeft((nextL[0] - 1, nextL[1]), dir):
        warehouse[nextL[1]][nextL[0]] = "["
        warehouse[nextL[1]][nextL[0] + 1] = "]"
        warehouse[crateLPos[1]][crateLPos[0] + 1] = "."
        # print("pushed left")
        return True
    return False

def pushCrateRight(crateLPos, dir) -> bool:
    # print("pushCrateRight(", crateLPos, dir, ")?")
    nextR = (crateLPos[0] + dir[0] + 1, crateLPos[1] + dir[1])
    targetR = warehouse[nextR[1]][nextR[0]]
    if targetR == "#":
        # print("cannot push right")
        return False
    if targetR == "." or targetR == "[" and pushCrateRight(nextR, dir):
        warehouse[crateLPos[1]][crateLPos[0] + 1] = "["
        warehouse[nextR[1]][nextR[0]] = "]"
        warehouse[crateLPos[1]][crateLPos[0]] = "."
        # print("pushed right")
        return True
    return False

        
def canPushCrateVert(crateLPos, dir) -> bool:
    # print("canPushCrateVert(", crateLPos, dir, ")?")
    nextL = (crateLPos[0] + dir[0], crateLPos[1] + dir[1])
    nextR = (nextL[0] + 1, nextL[1])
    targetL = warehouse[nextL[1]][nextL[0]]
    targetR = warehouse[nextR[1]][nextR[0]]
    if targetL == "#" or targetR == "#":
        # print("check: cannot push vertically")
        return False
    if ((targetL == "." and targetR == ".") # Simply push
        or (targetL == "[" and targetR == "]" and canPushCrateVert(nextL, dir)) # Propagate straight
        or (targetL == "]" and targetR == "." and canPushCrateVert((nextL[0] - 1, nextL[1]), dir)) # Propagate left
        or (targetL == "." and targetR == "[" and canPushCrateVert(nextR, dir)) # Propagate right
        or (targetL == "]" and targetR == "[" and canPushCrateVert((nextL[0] - 1, nextL[1]), dir) and canPushCrateVert(nextR, dir))): # Propagate both

        # print("can pushed vertically", targetL, targetR)
        return True
    return False
    #raise Exception("I'm lost on canPushCrateVert.", targetL, targetR, dir)

def pushCrateVert(crateLPos, dir) -> bool:
    # print("pushCrateVert(", crateLPos, dir, ")?")
    if not canPushCrateVert(crateLPos, dir):
        return False

    nextL = (crateLPos[0] + dir[0], crateLPos[1] + dir[1])
    nextR = (nextL[0] + 1, nextL[1])
    targetL = warehouse[nextL[1]][nextL[0]]
    targetR = warehouse[nextR[1]][nextR[0]]
    
    if targetL == "[" and targetR == "]":
        pushCrateVert(nextL, dir) # Propagate straight
    if targetL == "]":
        pushCrateVert((nextL[0] - 1, nextL[1]), dir) # Propagate left
    if targetR == "[":
        pushCrateVert(nextR, dir) # Propagate right

    warehouse[nextL[1]][nextL[0]] = "["
    warehouse[crateLPos[1]][crateLPos[0]] = "."
    warehouse[nextR[1]][nextR[0]] = "]"
    warehouse[crateLPos[1]][crateLPos[0] + 1] = "."
    
    # print("pushed vertically", targetL, targetR)
    return True
    

def move(dir) -> tuple:
    next = (robotPos[0] + dir[0], robotPos[1] + dir[1])
    target = warehouse[next[1]][next[0]]
    # print(robotPos, "=>", next)

    if target == "#":
        # print("wall")
        return robotPos
    elif target == "." or (target == "[" and pushCrate(next, dir)) or (target == "]" and pushCrate((next[0] - 1, next[1]), dir)):
        warehouse[next[1]][next[0]] = "@"
        warehouse[robotPos[1]][robotPos[0]] = "."
        # print("moved")
        return next
    return robotPos

for dir in steps:
    # print(robotPos, dir)

    robotPos = move(dir)

for row in warehouse:
    print("".join(row))
    
print()

resultB = 0
for y, row in enumerate(warehouse):
    for x, spot in enumerate(row):
        if spot == "[":
            resultB += x + 100 * y
print(resultB)


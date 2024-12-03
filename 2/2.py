import re

with open("input.txt", encoding="utf-8") as f:
    lines = [line for line in f.read().split("\n") if line]

levels = []
for line in lines:
    strList = line.split(' ')
    intList = list(map(int, strList))
    levels.append(intList)

def isAscending(level):
    for i in range(0, len(level) - 1):
        if level[i] >= level[i + 1]:
            return False
    return True

def isDescending(level):
    for i in range(0, len(level) - 1):
        if level[i] <= level[i + 1]:
            return False
    return True

def hasJumps(level):
    for i in range(0, len(level) - 1):
        if abs(level[i] - level[i + 1]) > 3:
            return True
    return False
    
def isSafe(level):
    return (isAscending(level) or isDescending(level)) and not hasJumps(level)

resultA = 0
for level in levels:
    if isSafe(level):
        resultA += 1
print(resultA)

resultB = 0
for level in levels:
    if isSafe(level):
        resultB += 1
    else:
        for i in range(0, len(level)):
            modifiedLevel = level[:i] + level[i+1:]
            if isSafe(modifiedLevel):
                resultB += 1
                print(modifiedLevel)
                break
        
print(resultB)

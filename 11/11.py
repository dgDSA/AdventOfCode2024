import math
from functools import cache
from collections import deque

with open("input.txt", encoding="utf-8") as f:
    line = f.read()

strs = line.split(' ')
stones = list(map(int, strs))

@cache
def blinkStone(stone):
    if stone == 0:
        return (1, None)
    digitsCount = int(math.log10(stone)) + 1
    if digitsCount % 2 == 0:
        div = 10 ** (digitsCount // 2)
        return (stone // div, stone % div)

    return (stone * 2024, None)
    
@cache
def countExpansionRecursive(stone, blinkTimes):
    if blinkTimes == 0:
        return 1
    
    firstStone, secondStone = blinkStone(stone)
    result = countExpansionRecursive(firstStone, blinkTimes - 1)
    if secondStone is not None:
        result += countExpansionRecursive(secondStone, blinkTimes - 1)
    
    return result
    
# deprecated - too slow, does not make full use of @cache
def countExpansionQ(startStone, startBlinkTimes):
    result = 0
    queue = deque()
    queue.append((startStone, startBlinkTimes))
    while queue:
        stone, blinkTimes = queue.pop()
        if blinkTimes == 0:
            result += 1
        else:
            firstStone, secondStone = blinkStone(stone)
            queue.appendleft((firstStone, blinkTimes - 1))
            if secondStone is not None:
                queue.appendleft((secondStone, blinkTimes - 1))

    return result
        

stonesA = list(stones)
stonesB = list(stones)

resultA = 0
for stone in stonesA:
    resultA += countExpansionRecursive(stone, 25)
print("A:", resultA)

resultB = 0
for i, stone in enumerate(stonesB):
    print(i)
    resultB += countExpansionRecursive(stone, 75)
print("B:", resultB)

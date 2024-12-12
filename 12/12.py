from copy import deepcopy

with open("input.txt", encoding="utf-8") as f:
    garden = f.read().splitlines()
HEIGHT = len(garden)
WIDTH = len(garden[0])


DELTAS = [
    (0, -1), # N
    (1, 0),  # E
    (0, 1),  # S
    (-1, 0)  # W
]

seenA = set()

def getSizeAndFenceCountA(pos, plant):
    seenA.add(pos)
    
    size = 1
    fenceCount = 0
    
    for delta in DELTAS:
        next = (pos[0] + delta[0], pos[1] + delta[1])
        if 0 <= next[0] < WIDTH and 0 <= next[1] < HEIGHT and garden[next[1]][next[0]] == plant:

            if next not in seenA:
                nextSize, nextFenceCount = getSizeAndFenceCountA(next, plant)
                size += nextSize
                fenceCount += nextFenceCount
        else:
            fenceCount += 1
    
    return size, fenceCount
            

resultA = 0
for y, line in enumerate(garden):
    for x, plant in enumerate(line):
        if (x, y) not in seenA:
            size, fenceCount = getSizeAndFenceCountA((x, y), plant)
            resultA += size * fenceCount
            #print(x, y, plant, size, fenceCount, size * fenceCount)
print(resultA)

seenB = set()

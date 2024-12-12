from copy import deepcopy

with open("input.txt", encoding="utf-8") as f:
    garden = f.read().splitlines()
HEIGHT = len(garden)
WIDTH = len(garden[0])

DIRS = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0)
}

def getSizeAndFences(pos, plant, seen):
    seen.add(pos)
    
    size = 1
    fences = [] # tuples: x position, y position, direction
    
    for dir, delta in DIRS.items():
        next = (pos[0] + delta[0], pos[1] + delta[1])
        if 0 <= next[0] < WIDTH and 0 <= next[1] < HEIGHT and garden[next[1]][next[0]] == plant:

            if next not in seen:
                nextSize, nextFences = getSizeAndFences(next, plant, seen)
                size += nextSize
                fences += nextFences
        else:
            fences.append((pos[0], pos[1], dir))
    
    return size, fences

seenA = set()
resultA = 0
for y, line in enumerate(garden):
    for x, plant in enumerate(line):
        if (x, y) not in seenA:
            size, fences = getSizeAndFences((x, y), plant, seenA)
            resultA += size * len(fences)
print(resultA)

def applyDiscounts(fences):
    fencesToBuy = []
    for fence in fences:
        # Don't pay for a fence if...
        if not any(other[2] == fence[2] # ... it's got the same direction as ...
                and ((other[0] == fence[0] and other[1] - fence[1] == 1) # ... the fence of the neighbor below or ...
                    or ((other[1] == fence[1] and other[0] - fence[0]) == 1)) for other in fences): # ... the fence of the neighbor to the right.
            fencesToBuy.append(fence)
    return fencesToBuy

seenB = set()
resultB = 0
for y, line in enumerate(garden):
    for x, plant in enumerate(line):
        if (x, y) not in seenB:
            size, fences = getSizeAndFences((x, y), plant, seenB)
            discountedFences = applyDiscounts(fences)
            resultB += size * len(discountedFences)
print(resultB)

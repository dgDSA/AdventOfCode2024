with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()
HEIGHT = len(lines)
WIDTH = len(lines[0])

hillMap = [[int(c) for c in line] for line in lines]

DELTAS = [
    (0, -1), # N
    (1, 0),  # E
    (0, 1),  # S
    (-1, 0)  # W
]

def walkUpFrom(x, y):
    currentLevel = hillMap[y][x]
    for delta in DELTAS:
        x2 = x + delta[0]
        y2 = y + delta[1]
        if 0 <= x2 < WIDTH and 0 <= y2 < HEIGHT:
            nextLevel = hillMap[y2][x2]
            if nextLevel == currentLevel + 1:
                if nextLevel == 9:
                    yield (x2, y2)
                else:
                    yield from walkUpFrom(x2, y2)

def genRoutes(x, y):
    currentLevel = hillMap[y][x]
    for delta in DELTAS:
        x2 = x + delta[0]
        y2 = y + delta[1]
        if 0 <= x2 < WIDTH and 0 <= y2 < HEIGHT:
            nextLevel = hillMap[y2][x2]
            if nextLevel == currentLevel + 1:
                if nextLevel == 9:
                    yield [(x2, y2)]
                else:
                    for subRoute in genRoutes(x2, y2):
                        yield [(x2, y2)] + subRoute

resultA = 0
resultB = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        if hillMap[y][x] == 0:
            trailsFromThisStart = set(walkUpFrom(x, y))
            resultA += len(trailsFromThisStart)
            
            routesFromThisStart = list(genRoutes(x, y))
            resultB += len(routesFromThisStart)
print(resultA)
print(resultB)

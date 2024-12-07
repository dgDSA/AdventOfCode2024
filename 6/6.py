from copy import deepcopy

DELTAS = {
    0: (0, -1), # N
    1: (1, 0),  # E
    2: (0, 1),  # S
    3: (-1, 0)  # W
}
   
with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

HEIGHT = len(lines)
WIDTH = len(lines[0])

originalObstacles = []
for y in range(HEIGHT):
    for x in range(WIDTH):
        c = lines[y][x]
        if c == '^':
            originalPos = (x, y)
        elif c == '#':
            originalObstacles.append((x, y))

class LoopException(Exception):
    pass
    
MAX_MOVES = WIDTH * HEIGHT

def movesUntilGuardLeaves(obstacles):
    ori = 0 # N
    pos = originalPos

    visited = set()
    visitedWithOri = set()
    while True:
        delta = DELTAS[ori]
        next = (pos[0] + delta[0], pos[1] + delta[1])
        if next in obstacles:
            # Turn
            ori = (ori + 1) % 4
        else:
            # Walk
            visited.add(pos)
            pos = next
            posWithOri = (pos[0], pos[1], ori)
            if posWithOri in visitedWithOri:
                raise LoopException
            else:
                visitedWithOri.add(posWithOri)

            if pos[0] < 0 or pos[0] >= WIDTH or pos[1] < 0 or pos[1] >= HEIGHT:
                return len(visited)

print('A:', movesUntilGuardLeaves(originalObstacles))
    
resultB = 0
for y in range(HEIGHT):
    print(y, "of", HEIGHT) # lol this is slow.
    for x in range(WIDTH):
        newObstacle = (x, y)
        if newObstacle not in originalObstacles:
            newObstacles = deepcopy(originalObstacles)
            newObstacles.append(newObstacle)
            try:
                _ = movesUntilGuardLeaves(newObstacles)
            except LoopException:
                resultB += 1
print('B:', resultB)
import re

R_ROBOT = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

with open("input.txt", encoding="utf-8") as f:
    contents = f.read()
    
robots = [map(int, m.groups()) for m in R_ROBOT.finditer(contents)]
      
WIDTH = 101
HEIGHT = 103

resultA = 0
quadrantNW = 0
quadrantNE = 0
quadrantSW = 0
quadrantSE = 0

midX = WIDTH // 2
midY = HEIGHT // 2

for x, y, dx, dy in robots:
    finalX = (x + (100 * dx)) % WIDTH
    finalY = (y + (100 * dy)) % HEIGHT
    
    if finalX < midX:
        if finalY < midY:
            quadrantNW += 1
        elif finalY > midY:
            quadrantSW += 1
    elif finalX > midX:
        if finalY < midY:
            quadrantNE += 1
        elif finalY > midY:
            quadrantSE += 1

resultA = quadrantNW * quadrantNE * quadrantSW * quadrantSE
print(resultA)

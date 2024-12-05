with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

width = len(lines[0])
height = len(lines)

DELTAS = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1)
]

def matches(substring, x, y, delta):
    if substring == "":
        return True

    if x < width and y < height and x >=0 and y >= 0:
        if lines[y][x] == substring[0]:
            if matches(substring[1:], x + delta[0], y + delta[1], delta):
                return True
    return False

resultA = 0
for y in range(height):
    for x in range(width):
        for delta in DELTAS:
            if matches("XMAS", x, y, delta):
                # print(x, y, delta)
                resultA += 1
print(resultA)

MAS_SAM = {"MAS", "SAM"}

def isCenterOfX(x, y):
    return (lines[y - 1][x - 1] + lines[y][x] + lines[y + 1][x + 1] in MAS_SAM
        and lines[y + 1][x - 1] + lines[y][x] + lines[y - 1][x + 1] in MAS_SAM)

resultB = 0
for y in range(1, height - 1):
    for x in range(1, width - 1):
        if isCenterOfX(x, y):
            resultB += 1
print(resultB)

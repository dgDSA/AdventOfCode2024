from collections import defaultdict

antennas = defaultdict(list)

with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()
HEIGHT = len(lines)
WIDTH = len(lines[0])

for y, line in enumerate(lines):
    for x, freq in enumerate(line):
        if freq != '.':
            antennas[freq].append((x, y))

antinodes = set()

for freq, positions in antennas.items():
    for posA in positions:
        for posB in positions:
            if posA != posB:
                dx = posB[0] - posA[0]
                dy = posB[1] - posA[1]
                antinode = (posA[0] - dx, posA[1] - dy)
                if 0 <= antinode[0] < WIDTH and 0 <= antinode[1] < HEIGHT:
                    antinodes.add(antinode)

print('A:', len(antinodes))

antinodesB = set()

for freq, positions in antennas.items():
    for posA in positions:
        for posB in positions:
            if posA != posB:
                for i in range(max(WIDTH, HEIGHT)):
                    dx = posB[0] - posA[0]
                    dy = posB[1] - posA[1]
                    antinode = (posA[0] - i * dx, posA[1] - i * dy)
                    if 0 <= antinode[0] < WIDTH and 0 <= antinode[1] < HEIGHT:
                        antinodesB.add(antinode)
                    else:
                        break

print('B:', len(antinodesB))
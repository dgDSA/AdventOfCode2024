import math
with open("input.txt", encoding="utf-8") as f:
    line = f.read()

strs = line.split(' ')
stones = list(map(int, strs))

def blink(stones):
    newStones = []
    for stone in stones:
        if stone == 0:
            newStones.append(1)
        else:
            digitsCount = int(math.log10(stone)) + 1
            if digitsCount % 2 == 0:
                div = 10 ** (digitsCount // 2)
                newStones.append(stone // div)
                newStones.append(stone % div)
            else:
                newStones.append(stone * 2024)
    
    #print(newStones)
    return newStones

stonesA = list(stones)
stonesB = list(stones)
for i in range(25):
    stonesA = blink(stonesA)
print("A:", len(stonesA))

for i in range(75):
    stonesB = blink(stonesB)
    print(i, len(stonesB))
print("B:", len(stonesB))

import re

# lines = [line for line in f.read().split("\n") if line]
# lstrs, rstrs = zip(*[re.split(" +", line) for line in lines])
# lefts = [int(lstr) for lstr in lstrs]
# rights = [int(rstr) for rstr in rstrs]

R_NUMS = re.compile(r"(\d+) +(\d+)")

lefts = []
rights = []
with open("input.txt", encoding="utf-8") as f:
    for m in R_NUMS.finditer(f.read()):
        lstr, rstr = m.groups()
        lefts.append(int(lstr))
        rights.append(int(rstr))


lefts.sort()
rights.sort()

result = 0
for le, ri in zip(lefts, rights):
    result += max(le, ri) - min(le, ri)
print(result)

resultB = 0
for le in lefts:
    c = rights.count(le)
    resultB += le * c
print(resultB)

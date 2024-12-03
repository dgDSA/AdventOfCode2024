import re

with open("input.txt", encoding="utf-8") as f:
    line = f.read()

R_MUL = re.compile(r"mul\((\d+),(\d+)\)")

resultA = 0
for m in R_MUL.finditer(line):
    le, ri = map(int, m.groups())
    resultA += le * ri
print(resultA)

R_MUL_DO_DONT = re.compile(r"(?P<mul>mul\((?P<le>\d+),(?P<ri>\d+)\))|(?P<do>do\(\))|(?P<dont>don't\(\))")
resultB = 0
enabled = True
for m in R_MUL_DO_DONT.finditer(line):
    if m.group("do"):
        enabled = True
    elif m.group("dont"):
        enabled = False
    else:
        assert m.group("mul")
        if enabled:
            le = int(m.group("le"))
            ri = int(m.group("ri"))
            resultB += le * ri
print(resultB)

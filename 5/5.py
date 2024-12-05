import functools
import re

R_RULE = re.compile(r"(\d+)\|(\d+)")
R_UPDATE = re.compile(r"(\d+)(?:,(\d+))+")
with open("input.txt", encoding="utf-8") as f:
    text = f.read()

rules = [(int(m.group(1)), int(m.group(2))) for m in R_RULE.finditer(text)]
#print(rules)

updates = [[int(s) for s in m.group().split(',')] for m in R_UPDATE.finditer(text)]
#print(updates)

def cmp(le, ri):
    for ruleLeft, ruleRight in rules:
        if le == ruleLeft and ri == ruleRight:
            return -1
        if ri == ruleLeft and le == ruleRight:
            return 1
    return 0


resultA = 0
for update in updates:
    sortedUpdate = sorted(update, key=functools.cmp_to_key(cmp))
    if update == sortedUpdate:
        resultA += update[len(update) // 2]
print(resultA)

resultB = 0
for update in updates:
    sortedUpdate = sorted(update, key=functools.cmp_to_key(cmp))
    if update != sortedUpdate:
        resultB += sortedUpdate[len(update) // 2]
print(resultB)

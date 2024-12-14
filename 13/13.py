"""
Day 13: Claw Contraption
"""

import re
from sympy import symbols, Eq, solve
from copy import deepcopy

with open("input.txt", encoding="utf-8") as f:
    contents = f.read()

R_MACHINE = re.compile(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")
machines = [list(map(int, m.groups())) for m in R_MACHINE.finditer(contents)]

def findCost(xA, yA, xB, yB, prizeX, prizeY): 
    a, b = symbols('a b', integer=True)
    eq1 = Eq(xA * a + xB * b, prizeX)
    eq2 = Eq(yA * a + yB * b, prizeY)
    
    solution = solve([eq1, eq2], (a, b))
    if solution:
        return 3 * solution[a] + solution[b]
    return 0

resultA = 0
for machine in machines:
    cost = findCost(*machine)
    resultA += cost
print(resultA)

resultB = 0
machinesB = deepcopy(machines)
for machine in machinesB:
    machine[4] += 10000000000000
    machine[5] += 10000000000000
    cost = findCost(*machine)
    resultB += cost
print(resultB)

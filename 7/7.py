import math

equations = []
with open("input.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()
    for line in lines:
        targetResult, operandsStr = line.split(': ')
        operands = list(map(int, operandsStr.split(' ')))
        equations.append((int(targetResult), operands))

def hasSolution(targetResult, operands, allowConcat, currentResult = None):
    if len(operands) == 0:
        return currentResult == targetResult
    nextOperand = operands[0]
    remainingOperands = operands[1:]
    
    if currentResult == None:
        return hasSolution(targetResult, remainingOperands, allowConcat, nextOperand)
    
    return (hasSolution(targetResult, remainingOperands, allowConcat, currentResult + nextOperand)
        or hasSolution(targetResult, remainingOperands, allowConcat, currentResult * nextOperand)
        or (allowConcat and hasSolution(targetResult, remainingOperands, allowConcat, int(str(currentResult) + str(nextOperand)))))

resultA = 0
for targetResult, operands in equations:
    if hasSolution(targetResult, operands, False):
        resultA += targetResult
print(resultA)
    
resultB = 0
for targetResult, operands in equations:
    if hasSolution(targetResult, operands, True):
        resultB += targetResult
print(resultB)

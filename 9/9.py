def readDiskMap(diskMap):
    diskMapInts = list(map(int, diskMap))

    blocks = []
    fileId = 0

    for i, diskMapInt in enumerate(diskMapInts):
        isFile = i % 2 == 0
        for j in range(diskMapInt):
            block = fileId if isFile else None
            blocks.append(block)
        if isFile:
            fileId += 1
    return blocks

def defrag(blocks):
    leftHead = 0
    rightHead = len(blocks) - 1
    while True:
        if blocks[leftHead] is None:
            while blocks[rightHead] is None:
                rightHead -= 1
            if leftHead >= rightHead:
                return

            blocks[leftHead] = blocks[rightHead]
            blocks[rightHead] = None
            rightHead -= 1
        leftHead += 1

def defragWhole(blocks):
    maxFileId = blocks[-1]
    for fileId in range(maxFileId, -1, -1):
        # print(fileId) # This is really slow. Should have used the disk-map data structure for this.
        fileStart = blocks.index(fileId)
        fileLength = 1
        while fileStart + fileLength < len(blocks) and blocks[fileStart + fileLength] == fileId:
            fileLength += 1
            
        for i in range(fileStart):
            if all(block is None for block in blocks[i:i + fileLength]):
                for j in range(fileLength):
                    blocks[i + j] = blocks[fileStart + j]
                    blocks[fileStart + j] = None
                break

def calcChecksum(blocks):
    checksum = 0
    for i, fileId in enumerate(blocks):
        if fileId is not None:
            checksum += i * fileId
    return checksum
        
with open("input.txt", encoding="utf-8") as f:
    diskMap = f.read()

blocksA = readDiskMap(diskMap)
blocksB = list(blocksA)

defrag(blocksA)
print(calcChecksum(blocksA))

defragWhole(blocksB)
#print(blocksB)
print(calcChecksum(blocksB))

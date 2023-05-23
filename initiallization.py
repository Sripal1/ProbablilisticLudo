#initialization

bases = ["G","Y","B","R"]
board=[]
for i in range(1,77):
    board.append(i)

idx=0
homeRuns = {}
offset = 6
gHomeRunIdx = 53
finishLines = {}
for i in range(len(bases)):
    board.insert(idx,bases[i])
    idx+=14
    homeRuns[bases[i]] = board[gHomeRunIdx+i*offset+i:gHomeRunIdx+i*offset+offset+i-1]
    finishLines[bases[i]] = 58+i*offset

safeSpots = {"G":(1,48),"Y":(9,14),"B":(22,27),"R":(35,40)}
path = board[:56]

print("board: "+str(board))
print("path: "+str(path))
print("homeruns: "+str(homeRuns))
print("safespots: "+str(safeSpots))
print("finishLines: "+str(finishLines))

pathG = ["G"]+[i%52 for i in range(1,52)] + [r for r in homeRuns["G"]] + [finishLines["G"]]
print(pathG)

pathY = ["Y"]
for i in range(14,14+51):
    pathY.append(i%52) if i%52 != 0 else pathY.append(52)
pathY += [r for r in homeRuns["Y"]] + [finishLines["Y"]]
print(pathY)

pathB = ["B"]
for i in range(27,27+51):
    pathB.append(i%52) if i%52 != 0 else pathB.append(52)
pathB += [r for r in homeRuns["B"]] + [finishLines["B"]]
print(pathB)

pathR = ["R"]
for i in range(40,40+51):
    pathR.append(i%52) if i%52 != 0 else pathR.append(52)
pathR += [r for r in homeRuns["R"]] + [finishLines["R"]]
print(pathR)

notInRedPath = []
for element in board:
    if element not in pathR:
        notInRedPath.append(element)
print("Not in Red's path:" + str(notInRedPath))

notInBluePath = []
for element in board:
    if element not in pathB:
        notInBluePath.append(element)
print("Not in Blue's path:" + str(notInBluePath))

notInGreenPath = []
for element in board:
    if element not in pathG:
        notInGreenPath.append(element)
print("Not in Green's path:" + str(notInGreenPath))

notInYellowPath = []
for element in board:
    if element not in pathY:
        notInYellowPath.append(element)
print("Not in Yellow's path:" + str(notInYellowPath))
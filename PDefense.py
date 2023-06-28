import initiallization
import matrixProcessing
import coinPositions

'''CALCULATING Pd'''

def getotherColorProbVector(otherColor,positionIdx):
    probMatrix = matrixProcessing.getMatrix(otherColor)
    if positionIdx == "Y":
        column = [row[3] for row in probMatrix]
    elif positionIdx == "R":
        column = [row[2] for row in probMatrix]
    elif positionIdx == "B":
        column = [row[1] for row in probMatrix]
    elif positionIdx == "G":
        column = [row[0] for row in probMatrix]
    else:
        column = [row[positionIdx+4] for row in probMatrix]
    if otherColor == "green" or otherColor == "Green": # DISCREPENCY IN GREEN LUDO MATRIX EXCEL FILE- HAS 4 REDUNDANT ROWS INSTEAD OF 2
        return column[:len(column)-4]
    # print(f"Other color probability vector : {column[:len(column)-2]}") #Eliminating last row containing column sums
    return column[:len(column)-2]

def getColorPosVector(positionIdx):
    vector = []
    for i in range(81):
        if i == positionIdx+4:
            vector.append(1)
        else:
            vector.append(0)
    # print(f"Positition vector : {vector}")
    return vector

def findGreenCoinPos(greenPosVec):
    for i in range(len(greenPosVec)):
        if greenPosVec[i] == 1:
            currGreenPos = i
            # print(f"Current green position : {currGreenPos}")
            return currGreenPos

def checkIntersection(greenPosVec,otherClrProbVec):
    currentGreenPosition = findGreenCoinPos(greenPosVec)
    PgreenCaptured = otherClrProbVec[currentGreenPosition]
    # if otherClrProbVec[currentGreenPosition] != 0:
        # print(f"Likelihood of green captured: {PgreenCaptured*100}%")
    return PgreenCaptured

# checkIntersection(getGreenPosVector(7),getotherColorProbVector("green",6))

# Create a list, Pd-green, of the likelihood of green being captured by each of the other colors [y1,y2,y3,y4,b1,b2,b3,b4,r1,r2,r3,r4]
currGreenPos = 9; # NULL spot
PDefenseGreen = {} # Dictionary of likelihood of green being captured by each of the other colors

def getPDforEachColor(otherCoins,currGreenPos,coinPositions,PDefenseGreen):
    for color in otherCoins:
        if color[0] == "Y":
            PDefenseGreen[color] = checkIntersection(getColorPosVector(currGreenPos),getotherColorProbVector("yellow",coinPositions.coinPositions[color]))
        elif color[0] == "B":
            PDefenseGreen[color] = checkIntersection(getColorPosVector(currGreenPos),getotherColorProbVector("blue",coinPositions.coinPositions[color]))
        elif color[0] == "R":
            PDefenseGreen[color] = checkIntersection(getColorPosVector(currGreenPos),getotherColorProbVector("red",coinPositions.coinPositions[color]))

# print(PDefenseGreen)
# print(checkIntersection(getGreenPosVector(9),getotherColorProbVector("yellow",9)))

PDsumByColor = {"Y":0,"B":0,"R":0}
for key,value in PDefenseGreen.items():
    if key[0] == "Y":
        PDsumByColor["Y"] += value
    elif key[0] == "B":
        PDsumByColor["B"] += value
    elif key[0] == "R":
        PDsumByColor["R"] += value

# print(PDsumByColor)

# Sum by color, and sum all values
# Track all colors in the game, including green, using the path in initialization.py and print likelihood of being struck by each color.

'''Completed Pd'''
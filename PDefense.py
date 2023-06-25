import initiallization
import matrixProcessing

'''CALCULATING Pd'''

def getotherColorProbVector(otherColor,positionIdx):
    probMatrix = matrixProcessing.getMatrix(otherColor)
    column = [row[positionIdx+4] for row in probMatrix]
    print(f"Other color probability vector : {column[:len(column)-4]}")
    return column[:len(column)-4]

def getGreenPosVector(positionIdx):
    vector = []
    for i in range(81):
        if i == positionIdx+4:
            vector.append(1)
        else:
            vector.append(0)
    print(f"Green positition vector : {vector}")
    return vector

def findGreenCoinPos(greenPosVec):
    for i in range(len(greenPosVec)):
        if greenPosVec[i] == 1:
            currGreenPos = i
            print(f"Current green position : {currGreenPos}")
            return currGreenPos

def checkIntersection(greenPosVec,otherClrProbVec):
    currentGreenPosition = findGreenCoinPos(greenPosVec)
    PgreenCaptured = otherClrProbVec[currentGreenPosition]
    if otherClrProbVec[currentGreenPosition] != 0:
        print(f"Likelihood of green captured: {PgreenCaptured*100}%")
    return PgreenCaptured

# checkIntersection(getGreenPosVector(7),getotherColorProbVector("green",6))

# Create a list, Pd-green, of the likelihood of green being captured by each of the other colors [y1,y2,y3,y4,b1,b2,b3,b4,r1,r2,r3,r4]
currGreenPos = 9; # NULL spot
otherCoins = ["Y1","Y2","Y3","Y4","B1","B2","B3","B4","R1","R2","R3","R4"] # List of other colors
coinPositions = {"Y1":7,"Y2":8,"Y3":9,"Y4":10,"B1":5,"B2":4,"B3":3,"B4":2,"R1":1,"R2":34,"R3":35,"R4":36,"G1":4,"G2":5,"G3":6,"G4":7} # Dictionary of other colors' coin positions
PDefenseGreen = {} # Dictionary of likelihood of green being captured by each of the other colors

def getPDforEachColor(otherCoins,currGreenPos,coinPositions,PDefenseGreen):
    for color in otherCoins:
        if color[0] == "Y":
            PDefenseGreen[color] = checkIntersection(getGreenPosVector(currGreenPos),getotherColorProbVector("yellow",coinPositions[color]))
        elif color[0] == "B":
            PDefenseGreen[color] = checkIntersection(getGreenPosVector(currGreenPos),getotherColorProbVector("blue",coinPositions[color]))
        elif color[0] == "R":
            PDefenseGreen[color] = checkIntersection(getGreenPosVector(currGreenPos),getotherColorProbVector("red",coinPositions[color]))

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

def updatePos(coin, dieRollVal):
    if dieRollVal >= 1 and dieRollVal <= 6:
        currPos = coinPositions[coin]

        color = "UNKNOWN"
        path = "UNKNOWN"
        if coin[0] == "G":
            color = "green"
            path = initiallization.pathG
        elif coin[0] == "Y":
            color = "yellow"
            path = initiallization.pathY

        elif coin[0] == "B":
            color = "blue"
            path = initiallization.pathB

        elif coin[0] == "R":
            color = "red"
            path = initiallization.pathR

        if (currPos + dieRollVal) in path:
            coinPositions[coin] = currPos + dieRollVal
            print("New position: "+ str(coinPositions[coin]))
updatePos("G1",6)



# Sum by color, and sum all values
# Track all colors in the game, including green, using the path in initialization.py and print likelihood of being struck by each color.

'''Completed Pd'''
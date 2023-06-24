import initiallization
import matrixProcessing

'''CALCULATING Pd'''

def getotherColorProbVector(positionIdx,probMatrix):
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

currGreenPos = 4; # NULL spot
PgreenCaptured = None

def findGreenCoinPos(greenPosVec):
    for i in range(len(greenPosVec)):
        if greenPosVec[i] == 1:
            currGreenPos = i
            print(f"Current green position : {currGreenPos}")
            return currGreenPos

def checkIntersection(greenPosVec,otherClrProbVec):
    currentGreenPosition = findGreenCoinPos(greenPosVec)
    PgreenCaptured = otherClrProbVec[currentGreenPosition+1]
    if otherClrProbVec[currentGreenPosition] != 0:
        print(f"Likelihood of green captured: {PgreenCaptured*100}%")

checkIntersection(getGreenPosVector(7),getotherColorProbVector(6,matrixProcessing.getMatrix("green")))

# Create a list, Pd-green, of the likelihood of green being captured by each of the other colors [y1,y2,y3,y4,b1,b2,b3,b4,r1,r2,r3,r4]
# Sum by color, and summ all values
# Track all colors in the game, including green, using the path in initialization.py and print likelihood of being struck by each color.

'''Completed Pd'''
import matrixProcessing
import PDefense
import coinPositions
import time

def getAllPosofColor(colorName):
    """
    Returns a list of all positions on the board of the given color.
    """
    allPositionsOfColor = {}
    positionsDict = coinPositions.coinPositionsJSON
    if colorName == "Yellow" or colorName == "yellow":
        for key,value in positionsDict.items():
            if key[0] == "Y":
                allPositionsOfColor[key] = value
    elif colorName == "Blue" or colorName == "blue":
        for key,value in positionsDict.items():
            if key[0] == "B":
                allPositionsOfColor[key] = value
    elif colorName == "Red" or colorName == "red":
        for key,value in positionsDict.items():
            if key[0] == "R":
                allPositionsOfColor[key] = value
    elif colorName == "Green" or colorName == "green":
        for key,value in positionsDict.items():
            if key[0] == "G":
                allPositionsOfColor[key] = value
    
    return allPositionsOfColor

# print(getAllPosofColor("yellow"))

def getCoinPosVector(allPositionsOfColor):
    allProbVectorsOfColor = {}
    colorIdentifier = list(allPositionsOfColor.keys())[0][0]

    if colorIdentifier == "Y":
        color = "yellow"
    elif colorIdentifier == "B":
        color = "blue"
    elif colorIdentifier == "R":
        color = "red"
    elif colorIdentifier == "G":
        color = "green"

    for key,value in allPositionsOfColor.items():
        if type(value) == int:
            allProbVectorsOfColor[key] = PDefense.getotherColorProbVector(color,value)
        else:
            print("Error: Key is not an integer. Still in homebase")
    
    return allProbVectorsOfColor

print(coinPositions.coinPositionsJSON)
coinPositions.initialize_positions()
print(coinPositions.coinPositionsJSON)
coinPositions.updatePos("Y1",6)
print(coinPositions.coinPositionsJSON)
coinPositions.updatePos("Y2",5)
print(coinPositions.coinPositionsJSON)
coinPositions.updatePos("Y3",4)
coinPositions.updatePos("Y4",3)
print(getAllPosofColor("yellow"))
print(getCoinPosVector(getAllPosofColor("yellow")))
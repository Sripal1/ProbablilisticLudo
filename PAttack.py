import matrixProcessing
import PDefense
import coinPositions
import time
import numpy as np
import copy

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

# print(getAllPosofColor("red"))

def getAllCoinProbVector(allPositionsOfColor):
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
        allProbVectorsOfColor[key] = PDefense.getotherColorProbVector(color,value)
        # if type(value) == int:
        #     allProbVectorsOfColor[key] = PDefense.getotherColorProbVector(color,value)
        # else:
        #     # WHAT DO I DO IF THE COIN IS STILL IN BASE?
        #     # Index into the home base vector
        #     print("Error: Key is not an integer. Still in homebase")
        
    return allProbVectorsOfColor
# print(getAllCoinProbVector(getAllPosofColor("red")))

def getAllForecastedProbVector(allProbVectorsOfColor,allPositionsOfColor):
    allForecastedProbVectorsOfColor = {}

    currentVec = [0 for i in range(81)]
    currentVec = np.array(currentVec)
    for key,value in allPositionsOfColor.items():
        currentVec += np.array(PDefense.getColorPosVector(value))
    # print("Current vector: "+str(currentVec))

    for coin,pos in allPositionsOfColor.items():
        tempCurrVector = copy.deepcopy(currentVec)
        tempCurrVector[pos+4] = 0
        # print("Current vector: " + str(tempCurrVector))

        if coin in allProbVectorsOfColor.keys():
            currProbVector = allProbVectorsOfColor[coin]
            summedVector = tempCurrVector + currProbVector
            allForecastedProbVectorsOfColor[coin] = summedVector.tolist()
    
    return allForecastedProbVectorsOfColor

# print(getAllForecastedProbVector(getAllCoinProbVector(getAllPosofColor("Yellow")),getAllPosofColor("Yellow")))

def PAoneColor(otherColor,currGreenPos):
    dictOtherColor = getAllForecastedProbVector(getAllCoinProbVector(getAllPosofColor(otherColor)),getAllPosofColor(otherColor))
    greenCoinProbVector = PDefense.getotherColorProbVector("green",currGreenPos)
    result = {}
    for otherColorCoin,forecastedProbVector in dictOtherColor.items():
        # print(forecastedProbVector)
        # print(greenCoinProbVector)
        result[otherColorCoin] = round(np.dot(forecastedProbVector, greenCoinProbVector),5)
        # print("RESULT" + str(result))
    return result

# print(PAoneColor("blue",12))

def getAllPAttack(greenCoinPos):
    
    # blueDict = PAoneColor("blue",greenCoinPos)
    # redDict = PAoneColor("red",greenCoinPos)
    yellowDict = PAoneColor("yellow",greenCoinPos)
    summedPAttackDict = {"Yellow":0,"Blue":0,"Red":0}

    for value in yellowDict.values():
        summedPAttackDict["Yellow"]+=value
    # for value in blueDict.values():
    #     summedPAttackDict["Blue"]+=value
    # for value in redDict.values():
    #     summedPAttackDict["Red"]+=value
    
    return summedPAttackDict

print(getAllPAttack(12))

# print(getAllForecastedProbVector(getAllCoinProbVector(getAllPosofColor("yellow")),getAllPosofColor("yellow")))
# print(coinPositions.coinPositionsJSON)
# coinPositions.initialize_positions()
# print(coinPositions.coinPositionsJSON)
# coinPositions.updatePos("Y1",6)
# print(coinPositions.coinPositionsJSON)
# coinPositions.updatePos("Y2",5)
# print(coinPositions.coinPositionsJSON)
# coinPositions.updatePos("Y3",4)
# coinPositions.updatePos("Y4",3)
# print(getAllPosofColor("yellow"))
# print(getCoinPosVector(getAllPosofColor("yellow")))
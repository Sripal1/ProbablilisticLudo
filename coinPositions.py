import initiallization
import time
import json

otherCoins = ["Y1","Y2","Y3","Y4","B1","B2","B3","B4","R1","R2","R3","R4"] # List of other colors

# Path to the file where the positions will be stored
positions_file = "coin_positions.json"

# Load the initial positions from the file or create a new dictionary if the file doesn't exist
try:
    with open(positions_file, "r") as file:
        coinPositionsJSON = json.load(file)

except FileNotFoundError:
    coinPositionsJSON = {"Y1":initiallization.pathY[0],"Y2":initiallization.pathY[0],"Y3":initiallization.pathY[0],"Y4":initiallization.pathY[0],
                    "B1":initiallization.pathB[0],"B2":initiallization.pathB[0],"B3":initiallization.pathB[0],"B4":initiallization.pathB[0],
                    "R1":initiallization.pathR[0],"R2":initiallization.pathR[0],"R3":initiallization.pathR[0],"R4":initiallization.pathR[0],
                    "G1":initiallization.pathG[0],"G2":initiallization.pathG[0],"G3":initiallization.pathG[0],"G4":initiallization.pathG[0]}


def save_positions_to_file():
    with open(positions_file, "w") as file:
        json.dump(coinPositionsJSON, file)

def updatePos(coin, dieRollVal):
    if dieRollVal >= 1 and dieRollVal <= 6:

        currPos = coinPositionsJSON[coin]

        path = "UNKNOWN"
        if coin[0] == "G":
            path = initiallization.pathG
        elif coin[0] == "Y":
            path = initiallization.pathY
        elif coin[0] == "B":
            path = initiallization.pathB
        elif coin[0] == "R":
            path = initiallization.pathR

        idxOldPos = path.index(currPos)
        idxNewPos = idxOldPos + dieRollVal
        if idxNewPos < len(path):
            coinPositionsJSON[coin] = path[idxNewPos]
            save_positions_to_file()
            print("New position: " + str(coinPositionsJSON[coin]))


def initialize_positions():
    with open(positions_file, "w") as file:
        global coinPositionsJSON
        coinPositionsJSON = {"Y1":initiallization.pathY[0],"Y2":initiallization.pathY[0],"Y3":initiallization.pathY[0],"Y4":initiallization.pathY[0],
                     "B1":initiallization.pathB[0],"B2":initiallization.pathB[0],"B3":initiallization.pathB[0],"B4":initiallization.pathB[0],
                     "R1":initiallization.pathR[0],"R2":initiallization.pathR[0],"R3":initiallization.pathR[0],"R4":initiallization.pathR[0],
                     "G1":initiallization.pathG[0],"G2":initiallization.pathG[0],"G3":initiallization.pathG[0],"G4":initiallization.pathG[0]}
        json.dump(coinPositionsJSON, file)

# Example usage:
# updatePos("Y1", 4)  # Update the position of Y1 with a die roll value of 3
# updatePos("B1", 6)  # Update the position of B1 with a die roll value of 6")
# updatePos("B1",6)
# updatePos("B1",6)
# updatePos("B1",6)
# updatePos("B1",6)
# updatePos("B1",6)
# initialize_positions()
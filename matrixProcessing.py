import os
import numpy as np
import pandas as pd
import math

# Function that takes in color's excel file and returns a 2D array of the file contents

def getMatrix(color):
    folder_name = "resultMatrices"
    if color == ("Yellow") or ("yellow"):
        file_path = os.path.join(folder_name, "Yellow Ludo Matrix 2.xlsx")
    elif color == ("Blue") or ("blue"):
        file_path = os.path.join(folder_name, "Blue Ludo Matrix 2.xlsx")
    elif color == ("Red") or ("red"):
        file_path = os.path.join(folder_name, "Red Ludo Matrix 2.xlsx")
    elif color == ("Green") or ("green"):
        file_path = os.path.join(folder_name, "Green Ludo Matrix-2.xlsx")
    else:
        print(f"{color} not a valid color name. Retry!")
    
    data_frame = pd.read_excel(file_path)
    matrixA = data_frame.to_numpy()
    matrixA = np.array(matrixA)
    matrixA = matrixA.tolist()
    modified_array = [subarray[1:] for subarray in matrixA] # remove first column
    finalArr = []
    for line in modified_array:
        line = [0 if math.isnan(x) else x for x in line] # replace NaN with 0
        line = [round(x,5) for x in line] # round to 5 decimal places
        finalArr.append(line)

    return finalArr

print(getMatrix("yellow"))
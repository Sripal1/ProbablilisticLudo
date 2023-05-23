import pandas as pd
import numpy as np

#Adjusting printing options to display the full mmatrix
np.set_printoptions(threshold=np.inf)
colors = ["yellow","blue","red","green"]
for color in colors:
    matrixName = color + "Matrix.csv"
    df = pd.read_csv(matrixName)
    df_filled = df.fillna(0.0)
    matrix = df_filled.values
    result_matrix = [[float(eval(entry.strip())) if isinstance(entry, str) else entry for entry in row] for row in matrix]
    print(matrixName)
    print(result_matrix)
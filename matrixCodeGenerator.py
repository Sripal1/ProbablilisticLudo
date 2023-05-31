import os
import pandas as pd
import numpy as np

# Adjusting printing options to display the full matrix
np.set_printoptions(threshold=np.inf)

folder_name = "CSV matrix files"
colors = ["yellow", "blue", "red", "green"]
for color in colors:
    matrixName = os.path.join(folder_name, color + "Matrix.csv")
    df = pd.read_csv(matrixName)
    df_filled = df.fillna(0.0)
    matrix = df_filled.values
    result_matrix = [[float(eval(entry.strip())) if isinstance(entry, str) else entry for entry in row] for row in matrix]
    print(matrixName)
    print(result_matrix)

# Define the folder path
folder_path = "/Users/sriranganathanpalaniappan/Desktop/Projects/ProbablilisticLudo/resultMatrices"

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Save the matrix to the new folder
np.save(os.path.join(folder_path, "green_result_matrix.npy"), result_matrix)

np.save("green_result_matrix.npy", result_matrix)
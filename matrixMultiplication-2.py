import pandas as pd
import numpy as np
import os
import math
import subprocess
import openpyxl

# Adjusting printing options to display the full matrix
np.set_printoptions(threshold=np.inf)

folder_name = "resultMatrices"
file_path = os.path.join(folder_name, "Green Ludo Matrix-2.xlsx")

# Read the Excel file using pandas
data_frame = pd.read_excel(file_path)

# Convert the data frame to a NumPy array
matrixA = data_frame.to_numpy()

# print(matrixA)
# print(matrixA[0][1])

matrixA = np.array(matrixA)
matrixA = matrixA.tolist()

modified_array = [subarray[1:] for subarray in matrixA]

finalArr = []
for line in modified_array:
    line = [0 if math.isnan(x) else x for x in line]
    line = [round(x,3) for x in line]
    # print(line)
    # print("\n\n")
    finalArr.append(line)

print(finalArr)
print(f"Number of rows {len(finalArr)}")
print(f"Number of columns {len(finalArr[0])}")

finalArr = np.array(finalArr)
multiplier = np.array(finalArr)
result = finalArr * multiplier
print(result)

df = pd.DataFrame(result)
output_file = 'output.xlsx'
df.to_excel(output_file, index=False)
# subprocess.call(['open', outputA_file])

subprocess.call(['open', output_file])
# Open the Excel file
excel_file = openpyxl.load_workbook(output_file) 
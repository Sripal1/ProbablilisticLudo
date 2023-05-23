import pandas as pd
import numpy as np

#Adjusting printing options to display the full mmatrix
np.set_printoptions(threshold=np.inf)

# df = pd.read_excel("testMatrix1.xlsx", sheet_name=0)
df = pd.read_csv('testMatrix1.csv')
# a = df.as_matrix()
df_filled = df.fillna(0.0)

# # Remove single quotes and convert to float
# df_cleaned = df_filled.apply(lambda x: pd.to_numeric(x, errors='coerce').fillna(x))
# df_cleaned = df.astype(float)
matrix = df_filled.values
# # print(df)
# print(matrix)

result_matrix = [[float(eval(entry.strip())) if isinstance(entry, str) else entry for entry in row] for row in matrix]

# Print the resulting matrix
# for row in result_matrix:
#     print(row)

print(result_matrix)

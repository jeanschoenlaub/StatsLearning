import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import pandas as pd

data = pd.read_csv("Auto.csv", na_values=['?'])

# Removing Na's
data_nulls = data[data.isnull().any(axis=1)]
data_cleaned = data.dropna()

#################### 9.a ####################

# Checking the columns
print(data_cleaned.columns)
print(data_cleaned.iloc[0])
print(data_cleaned.iloc[:,6])
# qualitative = name and origin

#################### 9.b, 9.c ####################

for column in data_cleaned.columns:
    column_data = data_cleaned[column]
    if (column != "name" and column != "origin"):
        mean_value = np.mean(column_data)
        std = np.std(column_data)
        max_value = np.max(column_data)
        min_value = np.min(column_data)
        print ("Column name "+column)
        print("Range: ["+ str(min_value)+ ", "+ str(max_value)+"]" )
        print("Mean: "+ str(mean_value)+ ", STD: "+ str(std) )

#################### 9.d####################

# data_filtered = pd.concat([data_cleaned.iloc[0:10], data_cleaned.iloc[85:]])

# for column in data_filtered.columns:
#     column_data = data_filtered[column]
#     if (column != "name" and column != "origin"):
#         mean_value = np.mean(column_data)
#         std = np.std(column_data)
#         max_value = np.max(column_data)
#         min_value = np.min(column_data)
#         print ("Column name "+column)
#         print("Range: ["+ str(min_value)+ ", "+ str(max_value)+"]" )
#         print("Mean: "+ str(mean_value)+ ", STD: "+ str(std) )

################### 9.d####################
print(data_cleaned.columns)
print(data.columns)
# Plotting removing the qualitative originin column
pd.plotting.scatter_matrix(data_cleaned.iloc[:,:6])
plt.show()



# Findings:
# Step function for horsepower  / cylinder
# Linear relationships : Displacement / weight & horsepower, accel / displacement and horsepower


# All othet predictors seme to be good for estimating mpg
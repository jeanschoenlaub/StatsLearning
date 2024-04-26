import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import pandas as pd

data = pd.read_csv("Boston.csv", index_col=[0], na_values=['NaN'])
print(data.describe())


#################### 9.a ####################
# pd.plotting.scatter_matrix(data.iloc[:,0:6])
# plt.show()

# Linear realationship indust zone and nox polltuion

# exp realationship age and l status income

#################### 9.b ####################
# columns_to_plot = pd.concat([data.iloc[:, 0], data.iloc[:, 6:]], axis=1)

# # Now plot the scatter matrix
# scatter_matrix = pd.plotting.scatter_matrix(columns_to_plot, alpha=0.2, figsize=(12, 12), diagonal='hist')
# plt.show()
# Crime and pollution / indus szone
# Crime and age, crime and dis
# but overall weak relationships 

#################### 9.c ####################
columns_to_plot = pd.concat([data["zn"], data["ptratio"],data["tax"], data["crim"]], axis=1)

# Now plot the scatter matrix
# scatter_matrix = pd.plotting.scatter_matrix(columns_to_plot, alpha=0.2, figsize=(12, 12), diagonal='hist')
# plt.show()
# No relatiosship zoning crime rate (except zone 0)
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# Exploring crime rate data 

# filtered_crim = data[data['crim'] > 1]['crim']
# filtered_crim_by_zn = data[data['crim'] > 1][['crim','zn','ptratio','tax']]
# filtered_crim_by_pt = data[data['crim'] > 1][['crim','ptratio']]
# filtered_crim_by_tax = data[data['crim'] > 1][['crim','tax']]


# axes[0,0].hist(filtered_crim, bins=25, edgecolor='black')
# axes[0,0].set_title('Histogram of CRIM > 1')
# axes[0,0].set_xlabel('CRIM Rate')
# axes[0,0].set_ylabel('Frequency')

# axes[0,1].hist(filtered_crim_by_tax)
# axes[0,1].set_title('Hist crime and tax')
# axes[0,1].set_xlabel('CRIM Rate')
# axes[0,1].set_ylabel('Zone')

# axes[1,0].hist(filtered_crim_by_pt)
# axes[1,0].set_title('Hist crime and pt')
# axes[1,0].set_xlabel('CRIM Rate')
# axes[1,0].set_ylabel('pt ratio')

# axes[1,1].scatter(filtered_crim_by_zn['crim'], filtered_crim_by_zn['tax'])
# axes[1,1].set_title('Scatter crime and tax')
# axes[1,1].set_xlabel('CRIM Rate')
# axes[1,1].set_ylabel('Tax')

# plt.show()

#################### 9.d ####################
# bound_to_charles = data[data["chas"] ==1]
# print(bound_to_charles.count())

# 35 near charles river

# #################### 9.e ####################
# print(np.median(data["ptratio"]))

# 35 near charles river
# median is 19.05

#################### 9.f ####################
print(np.min(data["medv"]))
# suburb 5 lowest value
index = data.index[data["medv"] == np.min(data["medv"])]
print(data.iloc[398,:])

# Crime is much hifgher then average (10x), indus a bit higher, tax higher
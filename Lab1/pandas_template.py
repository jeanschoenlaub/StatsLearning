import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

Auto = pd.read_csv('Auto.csv', na_values=['?'])
# Can also set the index for better vis
Auto_re = Auto.set_index('name')

# Checking data
# unique = np.unique(Auto['horsepower'])
# print(unique)
# Auto_re = Auto.set_index('name')
# print(Auto_re)
# rows = ['amc rebel sst', 'ford torino'] 
# Auto_re.loc[rows]

# Removing empties
# Auto_no_empty = Auto.dropna()
# print(Auto_no_empty)

#Filtering 
# idx_80 = Auto['year'] > 80 
# print(Auto[idx_80])


# Selecting rows and columns
# Can access by index using iloc
# print(Auto.iloc[:,1])
#  1st, 3rd and and 4th columns 
# print(Auto.iloc[:,[0,2,3]])
# Or by name using loc
# print(Auto_re.loc[lambda df: df['year'] > 80, ['weight', 'origin']])
# print(Auto_re.loc[lambda df: (df['displacement'] < 300)
# & (df.index.str.contains('ford')
# | df.index.str.contains('datsun')), ['weight', 'origin']
# ])


# Looping tuples with zip
# total = 0
# for value, weight in zip([2,3,19], [0.2,0.3,0.5]): 
#     total += weight * value
# print('Weighted total is: {0}'.format(total))

# And formating
# rng = np.random.default_rng(1)
# A = rng.standard_normal((127, 5))
# M = rng.choice([0, np.nan], p=[0.8,0.2], size=A.shape) 
# A += M
# D = pd.DataFrame(A, columns=['food', 'bar', 'pickle', 'snack', 'popcorn'])

# for col in D.columns:
#     template = 'Column "{0}" has "{1:.2%}" missing values' 
#     print(template.format(col,np.isnan(D[col]).mean()))


# Ploting from dataframes
# We can use subplots again accessing columns by names
# fig, ax = plt.subplots(figsize=(8, 8))
# ax.plot(Auto['horsepower'], Auto['mpg'], '+')
# ax.set_xlabel("Horsepower")
# ax.set_ylabel("mpg")
# plt.show()


# #Or using Data frame plot
# ax = Auto.plot.scatter('horsepower', 'mpg')
# ax.set_title('Horsepower vs. MPG')
# plt.show()


# Changing quant > qualitative data and box plotting
# Auto.cylinders = pd.Series(Auto.cylinders, dtype='category') 
# Auto.cylinders.dtype
# fig, ax = plt.subplots(figsize=(8, 8)) 
# Auto.boxplot('mpg', by='cylinders', ax=ax)
# # Or histogram
# Auto.hist('mpg', color='green', bins=12, ax=ax)
# plt.show()

pd.plotting.scatter_matrix(Auto[['mpg', 'displacement','weight']])
plt.show()
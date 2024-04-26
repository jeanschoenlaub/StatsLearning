import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import pandas as pd

data = pd.read_csv("College.csv", index_col=0)

#################### 8.c ####################

print(data.describe())

#################### 8.d ####################

# scatter_plot_data = data[['Top10perc', 'Apps','Enroll']]
# pd.plotting.scatter_matrix(scatter_plot_data)


#################### 9.e ####################

# data_private_schools = data[data['Private'] == 'Yes']
# data_public_schools = data[data['Private'] == 'No']

# fig, axes = plt.subplots(figsize=(10, 6),  ncols=2)  # Setting figure size for better visibility
# # Plotting the boxplot on the first subplot
# data_private_schools.boxplot(column='Outstate', by='Private', ax=axes[0])
# axes[0].set_title('Outstate Tuition for Private schools')  # Setting title of the plot
# axes[0].set_xlabel('Private')  # Labeling the x-axis
# axes[0].set_ylabel('Outstate Tuition Fees')  # Labeling the y-axis

# data_public_schools.boxplot(column='Outstate', by='Private', ax=axes[1])
# axes[1].set_title('Outstate Tuition for Public schools')  # Setting title of the plot
# axes[1].set_xlabel('Private')  # Labeling the x-axis
# axes[1].set_ylabel('Outstate Tuition Fees')  # Labeling the y-axis
# plt.show()

#################### 8.f ####################

# data['Elite'] = pd.cut(data['Top10perc'], [0,50,100], labels=['No', 'Yes'])

# elite_schools = data[data['Elite'] == "Yes"]
# non_elite_schools = data[data['Elite'] == "No"]

# print(data['Elite'].value_counts())
# fig, ax = plt.subplots(figsize=(10, 6))  # Setting figure size for better visibility
# # Plotting the boxplot on the first subplot
# data.boxplot(column='Outstate', by='Elite', ax=ax)

# ax.set_title('Outstate Tuition by Elite schools')  # Setting title of the plot
# ax.set_xlabel('Elite')  # Labeling the x-axis
# ax.set_ylabel('Outstate Tuition Fees')  # Labeling the y-axis


#################### 8.g ####################
fig, axes = plt.subplots(figsize=(10, 6),  ncols=2, nrows =2)  # Setting figure size for better visibility
# Plotting the boxplot on the first subplot

data['Elite'] = pd.cut(data['Top10perc'], [0,50,100], labels=['No', 'Yes'])

data.boxplot(column='Outstate', by='Elite', ax=axes[0,0])
axes[0,0].set_title('Outstate tuition fee by Elite school status')  # Setting title of the plot
axes[0,0].set_xlabel('Private')  # Labeling the x-axis
axes[0,0].set_ylabel('Outstate Tuition Fees')  # Labeling the y-axis


data['AcceptRate'] = data['Accept'] / data['Apps']
data['NotPicky'] = pd.cut(data['AcceptRate'], [0,0.5,1], labels=['No', 'Yes'])

print(data[['AcceptRate','NotPicky']])

data.boxplot(column='Top10perc', by='NotPicky', ax=axes[0,1])
axes[0,1].set_title('School talent by pickiness')  # Setting title of the plot
axes[0,1].set_xlabel('Accept rate > 50%')  # Labeling the x-axis
axes[0,1].set_ylabel('School talent')  # Labeling the y-axis

plt.tight_layout()
plt.tight_layout()
plt.show()
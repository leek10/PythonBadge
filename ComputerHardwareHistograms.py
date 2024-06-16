# Using Panda to manipulate data into a binnable form to make histograms of the dataset

import pandas as pd 
import matplotlib.pyplot as plt

dataFrame = pd.read_excel('C:/Users/leeka/Downloads/PythonBadge/ComputerSurveyData.xlsx')
print(dataFrame.head())

column_to_bin = 'CPU Cycle Rate (in GHz)'
bins = [0, 1.8, 2.8, 3.5, 4.05, 4.7]

# Creating histogram
plt.figure(figsize = (8, 6))
plt.hist(dataFrame['CPU Cycle Rate (in GHz)'], bins = bins)
plt.xlabel('CPU Cycle Rate (GHz)')
plt.ylabel('Number of CPUs')
plt.title('CPU Cycle Rates')
plt.grid(True)
plt.show()

# Program outputs a summary of each varaible to a single text file
# Saves a histogram of each variable to png files, and
# Outputs a scatter plot of each pair of variables.
# Author: Clare Tubridy

import pandas as pd
import matplotlib.pyplot as plt

# Loads the Iris dataset from a CSV file
iris_data = pd.read_csv('iris.csv')

# Summary of each variable to a single text file
with open('iris_summary.txt', 'w') as f:
    f.write(iris_data.describe().to_string())

# Histogram pf each variable to PNG files
for col in iris_data.columns[:-1]:
    plt.hist(iris_data[col], bins = 10)
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.savefig(f'{col}_histogram.png')
    plt.clf()                            # Clears figure for the next plot
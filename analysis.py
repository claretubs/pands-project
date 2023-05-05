# Program outputs a summary of each varaible to a single text file
# Saves a histogram of each variable to png files, and
# Outputs a scatter plot of each pair of variables.
# Author: Clare Tubridy

import pandas as pd
import matplotlib.pyplot as plt

# Loads the Iris dataset from a CSV file
iris_data = pd.read_csv('iris.csv')

# Summary of each variable to a single text file
with open('iris_summary.txt', 'w') as f:            # Opens files without having to use the close() function
    f.write(iris_data.describe().to_string())       # Converts summary data to a string and writes it to a .txt file

# Histogram pf each variable to PNG files
for col in iris_data.columns[:-1]:                  # Iterates over each column in the dataframe except the last one
    plt.hist(iris_data[col], bins = 8, color = 'green', edgecolor = 'black')   # Creates a histogram, with 10 bins, for each column
    plt.xlabel(col)                                 # X label
    plt.ylabel('Frequency')                         # Y label
    plt.savefig(f'{col}_histogram.png')             # Saves histogram as a PNG file
    plt.clf()                                       # Clears figure for the next plot
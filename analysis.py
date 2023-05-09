# Program outputs a summary of each varaible to a single text file
# Saves a histogram of each variable to png files, and
# Outputs a scatter plot of each pair of variables.
# Author: Clare Tubridy

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loads the Iris dataset from a CSV file
iris_data = pd.read_csv('iris.csv')

# Summary of each variable to a single text file
with open('iris_summary.txt', 'w') as f:                # Opens files without having to use the close() function
    f.write(iris_data.describe().to_string())           # Converts summary data to a string and writes it to a .txt file

# Histogram of each variable to PNG files
for col in iris_data.columns[:-1]:                      # Iterates over each column in the dataframe except the last one
    plt.hist(iris_data[col], bins = 8, color = 'green', edgecolor = 'black')   # Creates a histogram, with 10 bins, for each column
    plt.xlabel(col)                                     # X label
    plt.ylabel('Frequency')                             # Y label
    plt.savefig(f'{col}_histogram.png')                 # Saves histogram as a PNG file
    plt.clf()                                           # Clears figure for the next plot

# Scatter plot of each pair of variables
fig, axes = plt.subplots(1,2,figsize = (10,4))         # Create a figure with a 1x2 grid of subplots

# Plot the Sepal scatterplot in the first subplot
sns.scatterplot(x = 'SepalLength', y = 'SepalWidth',   # Creates a scatter plot with x being the x-axis and y being the y-axis
                hue = 'Species', data = iris_data, ax = axes[0])    # Seperates the 3 different species (grouping varaible)
axes[0].legend(bbox_to_anchor = (1,1), loc = 'upper left')          # Lengend made at specidied location
axes[0].set_title('Sepal Scatter Plot')                # Title of scatter plot

# Plot the Petal scatterplot in the second subplot
# Same method carried out as for the first scatter plot
# Differences are the x and y axis, title and,
# 'axes[1]' places this subplot beside the first subplot
sns.scatterplot(x = 'PetalLength', y = 'PetalWidth', 
                hue = 'Species', data = iris_data, ax = axes[1])
axes[1].legend(bbox_to_anchor = (1,1), loc = 'upper left')
axes[1].set_title('Petal Scatter Plot')

plt.tight_layout()                                      # Adjust the spacing between subplots
plt.savefig('Scatter_Plots')                            # Saves scatterplot as a PNG file

# Box Plot of variables
fig2, ax2 = plt.subplots(figsize=(8, 6))                # Create a new figure with a specified size
iris_data.boxplot(ax=ax2)                               # Create the boxplot on the specified figure
ax2.set_title('Box plot of the Fisher\'s Iris dataset') # Set title
ax2.set_ylabel('Value')                                 # Set y axis
plt.savefig('Box_Plot')                                 # Saves box plot as a PNG file
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv("your_file.csv")

# Create the scatter plot
plt.scatter(data['ElapsedRaw'], data['Partition'], c=data['Partition'].map({'defq': 'blue', 'gpu': 'red', 'ice4hpc': 'green'}))

# Set the labels and title
plt.xlabel("ElapsedRaw")
plt.ylabel("Partition")
plt.title("Scatter Plot of ElapsedRaw vs. Partition")

# Show the plot
plt.show()

import matplotlib.pyplot as plt

def read_data(filename):
  """
  Reads data from a file with specific format and returns lists of dates, CPU, and GPU usage.

  Args:
      filename: The name of the file to read.

  Returns:
      A tuple containing three lists: dates, cpu_usage, and gpu_usage.
  """
  dates, cpu_usage, gpu_usage = [], [], []
  with open(filename, 'r') as file:
    for line in file:
      data = line.strip().split()  # Split line by whitespace, removing leading/trailing spaces
      dates.append(data[0])
      cpu_usage.append(float(data[1].replace('%', '')))  # Convert percentage string to float
      gpu_usage.append(float(data[2].replace('%', '')))
  return dates, cpu_usage, gpu_usage

# Replace 'data.txt' with your actual filename
dates, cpu_usage, gpu_usage = read_data('data.txt')

# Create the histogram with separate bars
plt.figure(figsize=(10, 6))  # Set figure size (optional)
plt.bar(dates, cpu_usage, label='tot CPU Usage', width=0.4, align='center', color='skyblue')
plt.bar([x for x in dates], gpu_usage, label='tot GPU Usage', width=0.4, align='edge', color='royalblue')  # Adjust x positions for separate bars
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability (optional)
plt.xlabel('Date')
plt.ylabel('Percentage Usage (%)')
plt.title('Total CPU and GPU Usage Over Time (source:SLURM Database)')
plt.legend()
plt.tight_layout()
plt.show()



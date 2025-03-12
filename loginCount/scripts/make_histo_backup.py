import matplotlib.pyplot as plt
import numpy as np


def read_data(filename):
  """
  Reads data from a two-column text file.

  Args:
      filename: The path to the text file.

  Returns:
      A tuple containing two lists: dates and login_counts.
  """
  dates = []
  login_counts = []
  with open(filename, 'r') as f:
    for line in f:
      date, count = line.strip().split()
      dates.append(date)
      login_counts.append(int(count))
      print(dates)
  return dates, login_counts


def plot_histogram(dates, login_counts):
  """
  Creates a histogram plot with login counts on top of bars.

  Args:
      dates: A list of dates (strings).
      login_counts: A list of login counts (integers).
  """
  plt.bar(dates, login_counts)
  plt.xlabel("Date")
  plt.ylabel("Number of Logins")
  plt.title("Login Distribution")

  # Add login counts on top of bars
  for i, v in enumerate(login_counts):
    plt.text(i, v + 0.1, str(v), ha='center', va='bottom')

  plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
  plt.tight_layout()
  #plt.show()
  fig1 = plt.gcf()
  plt.show()
  plt.draw()
  fig1.savefig('logins_histo.png', dpi=100)  

if __name__ == "__main__":
  filename = "data.txt"  # Replace with your actual filename
  dates, login_counts = read_data(filename)
  plot_histogram(dates, login_counts)



import pandas as pd
import sys
import numpy as np

basePath=sys.argv[1]

def read_wtmp_file(filename):
  """
  Reads a wtmp file, removes the last two lines, parses the data,
  and returns a DataFrame with specific columns.

  Args:
      filename: The path to the wtmp file.

  Returns:
      A pandas DataFrame containing user information.
  """
  with open(filename, 'r') as f:
    # Read all lines except the last two
    lines = f.readlines()[:-2]
  #print(lines)
  
  print(line.split("T")[0].strip().split() for line in lines)

  # Split each line by whitespace
  #data = [line.split("T")[0].strip().split() for line in lines]
  data = [line.split("T")[0].strip().split() for line in lines if "reboot" not in line]

  # Create a DataFrame with specific columns
  df = pd.DataFrame(np.vstack((data)), columns=["user", "unused1", "IP", "date"])
  df=df[['user', 'date']]
  from tabulate import tabulate
  with open(basePath+'table_1.txt', 'w') as f:
    f.write(tabulate(df, headers='keys', tablefmt='psql'))
  

# Example usage
filename = basePath+"last_timeformat_iso_today.txt"  # Replace with your actual filename
df = read_wtmp_file(filename)




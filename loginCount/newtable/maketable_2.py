import pandas as pd
import sys

basePath=sys.argv[1]

def read_wtmp_file(filename, output_file=basePath+"table_2.txt"):
  """
  Reads a wtmp file, removes the last two lines, parses the data,
  and returns a DataFrame with specific columns.

  Args:
      filename: The path to the wtmp file.
      output_file: The path to the output file (default: "table_2.txt").

  Returns:
      A pandas DataFrame containing user information.
  """

  with open(filename, 'r') as f:
    # Read all lines except the last two
      lines = f.readlines()[:-2]
      lines = [line for line in lines if "reboot" not in line] 

  # Split each line by whitespace
  data = [line.split("T")[0].strip().split() for line in lines if not line.lower().startswith("reboot")]

  # Create a DataFrame with specific columns
  df = pd.DataFrame(data, columns=["user", "unused1", "IP", "date"]) #, "time1", "time2", "duration"])

  df.drop(columns=["unused1", "IP"], inplace=True)

  # Instead of printing, write the DataFrame to a file
  with open(output_file, 'w') as f:
      df.to_csv(f, index=False)  # Save as CSV to "table_2.txt"

  # Rest of the code remains the same (dropping duplicates, date conversion, etc.)

# Example usage
filename = basePath+"last_timeformat_iso_today.txt"  # Replace with your actual filename
df = read_wtmp_file(filename)


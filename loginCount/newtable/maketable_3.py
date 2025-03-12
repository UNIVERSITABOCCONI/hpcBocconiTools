import pandas as pd
import sys

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
    lines = [line for line in lines if "reboot" not in line]

  # Split each line by whitespace
  data = [line.split("T")[0].strip().split() for line in lines if not line.lower().startswith("reboot")]

  # Create a DataFrame with specific columns
  df = pd.DataFrame(data, columns=["user", "unused1", "IP", "date"]) #, "time1", "time2", "duration"])

  df.drop(columns=["unused1", "IP"], inplace=True)

  df.drop_duplicates(inplace=True)

  # Convert the 'date' column to datetime format
  df['date'] = pd.to_datetime(df['date'])

  # Merge date and user columns into a single string
  df['date_user'] = df['date'].dt.strftime('%Y-%m-%d') + ' ' + df['user']

  # Sort by date_user
  df = df.sort_values(by='date_user')

  # Count user occurrences
  user_counts = df['user'].value_counts()

  # Print results in desired format to a file (table_3.txt)
  with open(basePath+"table_3.txt", "w") as output_file:
    for user, count in user_counts.items():
      output_file.write(f"{user} {count}\n")

# Example usage
filename = basePath+"last_timeformat_iso_today.txt"  # Replace with your actual filename
read_wtmp_file(filename)

#print("User counts written to table_3.txt")  # Optional confirmation message


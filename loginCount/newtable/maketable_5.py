from prettytable import PrettyTable
import sys

basePath=sys.argv[1]

def count_labels(input_filename, output_filename):
  """
  Reads a file with label information, counts occurrences of each label,
  and writes the results to a new file in a pretty table format using PrettyTable.

  Args:
    input_filename: The name of the input file.
    output_filename: The name of the output file.
  """
  label_counts = {}
  with open(input_filename, 'r') as input_file:
    # Skip the header line (assuming there is one)
    next(input_file)
    for line in input_file:
      _, _, label = line.strip().split()
      if label in label_counts:
        label_counts[label] += 1
      else:
        label_counts[label] = 1

  # Get the number of HPC cluster users from bash command
  import subprocess

  # Define the bash command
  command = "getent group -s sss | grep grp_hpcclusterbocconiusers "

  # Execute the command and capture the output and exit code
  process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
  output, _ = process.communicate()
  exit_code = process.returncode
  #print(output)

  user_string=str(output)

  # Count the number of commas
  num_commas = user_string.count(',')
  num_users = num_commas + 6

  # Create a PrettyTable object
  table = PrettyTable(["Label", "Count"])

  my_count=0
  # Add data to the table
  for label, count in label_counts.items():
    table.add_row([label, count])
    my_count += count
  #print(my_count)

  # Add a custom row with "never" and number of users
  table.add_row(["never", (num_users-my_count)])

  # Get the CSV string
  csv_string = table.get_csv_string()

  # Write the CSV string to a file
  with open(output_filename, "w") as f:
      f.write(csv_string)

  

# Example usage
count_labels(basePath+"table_4.txt", basePath+"table_5.csv")  # Replace with your actual file names


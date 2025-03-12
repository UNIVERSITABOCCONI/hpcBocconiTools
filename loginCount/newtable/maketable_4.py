import sys

basePath=sys.argv[1]

def process_file(input_filename, output_filename):
  """
  Reads a file without a header, adds a label column based on the second 
  column's value, and writes the results to a new file.

  Args:
    input_filename: The name of the input file.
    output_filename: The name of the output file.
  """
  with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
    output_file.write("name score Label\n")  # Add header for the output file

    for line in input_file:
      name, score = line.strip().split()
      score = int(score)
      label = "10+" if score >= 10 else ("5" if 5 <= score <= 9 else "1")
      output_file.write(f"{name} {score} {label}\n")

# Example usage
process_file(basePath+"table_3.txt", basePath+"table_4.txt")  # Replace with your actual file names


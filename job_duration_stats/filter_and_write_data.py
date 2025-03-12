def filter_and_write_data(input_file, output_file, threshold=15):
  """
  Reads a file with 2 columns, filters data where 1st column is less than threshold,
  and writes the filtered data to a new file.

  Args:
      input_file (str): Path to the input file.
      output_file (str): Path to the output file.
      threshold (int, optional): The value to compare the first column data with. Defaults to 15.
  """

  with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Skip the header line (optional, modify if your file doesn't have a header)
    next(infile)  # Assuming the first line is a header

    for line in infile:
      data = line.strip().split(',')  # Split by comma (modify for different delimiter)
      if len(data) == 2:  # Check if there are exactly 2 columns
        try:
          first_column_value = float(data[0])  # Convert the first column to a number
          if first_column_value < threshold:
            outfile.write(','.join(data) + '\n')  # Write the line to the output file
        except ValueError:
          # Handle lines with non-numeric values in the first column (optional)
          pass  # You can print a warning message or skip the line here

if __name__ == '__main__':
  input_file = '2NNodes_20may_20june'  # Replace with your actual input file path
  output_file = 'filtered_data.txt'  # Replace with your desired output file path
  filter_and_write_data(input_file, output_file)
  print(f'Data filtered and written to "{output_file}".')

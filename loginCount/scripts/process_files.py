import os
current_dir="/root/utilities/hpcBocconiTools/loginCount/scripts/"

def get_last_part_of_filename(filename):
  """
  Extracts the last part of a filename after the underscore.

  Args:
      filename: The filename string.

  Returns:
      The last part of the filename after the underscore, or an empty string
      if no underscore is found.
  """
  parts = filename.split("_")
  if len(parts) > 1:
    return parts[-1]
  else:
    return ""

def process_file(filename):
  """
  This function reads a text file, extracts the last word from each line without the ending dot,
  and counts the occurrences of these words without repetition.

  Args:
      filename: The path to the text file.

  Returns:
      A dictionary where the keys are the unique last words and the values are their counts.
  """

  # Initialize an empty dictionary to store word counts
  word_counts = {}

  # Open the file in read mode
  with open(filename, 'r') as f:
    # Read all lines at once
    lines = f.readlines()

    # Iterate over each line
    for line in lines:
      # Extract the last word (assuming there are spaces)
      last_word = line.strip().split()[-1]

      # Remove the dot from the end of the word (if it exists)
      last_word = last_word.rstrip(".")

      # Convert to lowercase for case-insensitive counting (optional)
      # last_word = last_word.lower()  # Uncomment for case-insensitive counting

      # Update the word count dictionary
      if last_word in word_counts:
        word_counts[last_word] += 1
      else:
        word_counts[last_word] = 1

  return len(word_counts)

def process_login_files(directory):
  """
  Processes all files named like logins_YYYY-MM-DD in a directory.

  Args:
      directory: The directory path to process.
  """
  for filename in os.listdir(directory):
    if filename.startswith("logins_") and len(filename.split("_")) == 2:
      last_part = get_last_part_of_filename(filename)
      #print(f"File: {filename}, Last Part: {last_part}")
      count = process_file(current_dir+filename)
      print(last_part + " " + str(count))

# Example usage:

directory=current_dir
#directory = "."  # current directory otherwise it won't work
process_login_files(directory)


def extract_hpc_logins(filename):
  """Extracts HPC logins from a file with the specified format.

  Args:
    filename: The name of the file to read.

  Returns:
    A list of strings, each containing an HPC login.
  """

  hpc_logins = []
  with open(filename, 'r') as file:
    for line in file:
      if line.startswith("      hpc"):
        login = line.split()[1]
        hpc_logins.append(login)
  return hpc_logins

# Example usage:
filename = "topCPU_users_MONTHbyMONTH_2024"  # Replace with your actual filename
logins = extract_hpc_logins(filename)
unique_logins = set(logins)

'''
print(logins)
print(" ")
print("top users that appear at least once")
print(" ")
print(unique_logins)
print(len(unique_logins))
'''

for element in unique_logins:
  print(f"{element} ")


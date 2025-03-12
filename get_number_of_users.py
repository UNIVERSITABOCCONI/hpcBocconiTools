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

# Print the result
#print(f"Number of commas: {num_commas}")
#print(f"Number of hpc bocconi users (including 5 admins): {num_users}")
print(f"Number of hpc bocconi users: {num_users}")


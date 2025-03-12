import subprocess
import pandas as pd
import sys
from prettytable import PrettyTable

# Check for required arguments
if len(sys.argv) < 4:
        print("Usage: python reportCostPerAccount.py <users> | <admins> <from_date> <to_date>")
        print("Example: python reportCostPerAccount.py admins 2024-11-25 2024-11-26")
        sys.exit(1)


if(sys.argv[1] == "users"):
  group_name = "grp_hpcclusterbocconiusers"
elif(sys.argv[1] == "admins"):
  group_name = "grp_hpcclusterbocconiadmins"
else:
  print("wrong parameter passed to script!")

# Get start and end dates from arguments
start_date = sys.argv[2]
end_date = sys.argv[3]

def validate_date_format(date_str):
  """
  This function validates if the input string is in YYYY-MM-DD format.
  """
  from datetime import datetime
  try:
    datetime.strptime(date_str, "%Y-%m-%d")
    return True
  except ValueError:
    return False


def get_users_from_group(group_name):
  """Gets a list of users from a specified group.

  Args:
    group_name: The name of the group to query.

  Returns:
    A list of usernames in the group.
  """

  result = subprocess.run(['getent', 'group', '-s', 'sss', group_name], capture_output=True, text=True)
  if result.returncode != 0:
    raise RuntimeError(f"Failed to get group information: {result.stderr}")

  user_list = result.stdout.strip().split(':')[3].split(',')
  return user_list

def get_user_resource_usage(user):
    command = f"sreport --noheader cluster UserUtilizationByAccount user {user} -T mem,cpu,gres/gpu Start=10/01 End=11/01"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        lines = result.stdout.strip().split('\n')
        data = []
        #print("lines", lines)
        if(len(lines)<=1): # user usage is 0 as command return empty result
          data = {
                'hpc': ['-'],
                'user': [user],
                'last': ['-'],
                'account': ['-'],
                'resource': ['-'],
                'usage': [0]
                }
          #print(f"User {user} as no usage")
          return pd.DataFrame(data, columns=['hpc', 'user', 'last', 'account', 'resource', 'usage'])
        else:
          for line in lines:
              fields = line.split()
              data.append(fields)
        return pd.DataFrame(data, columns=['hpc', 'user', 'last', 'account', 'resource', 'usage'])
    else:
        print(f"Command failed for user {user}: {result.stderr}")
        return None

def export_to_csv(df, output_file_path):
    """Exports the DataFrame to a CSV file.

    Args:
        df (pandas.DataFrame): The DataFrame to export.
        output_file_path (str): The path to the output CSV file.
    """

    df.to_csv(output_file_path, index=False)

user_list = get_users_from_group(group_name)

df = pd.DataFrame(columns=['hpc', 'user', 'last', 'account',  'resource', 'usage'])
for user in user_list:
    user_df = get_user_resource_usage(user)
    if user_df is not None:
        df = pd.concat([df, user_df], ignore_index=True)

# Create a PrettyTable instance
table = PrettyTable(["hpc", "user", "last", "account", "resource", "usage"])

# Add data from DataFrame to PrettyTable
for index, row in df.iterrows():
    table.add_row(row.tolist())

# Print the table
#print(table)


export_to_csv(df,"/root/utilities/hpcBocconiTools/dataToReport/usageByAccountData/UsagePerAccount_"+start_date+"_"+end_date+".csv")

# Save the table to a file (optional)
with open("UsagePerAccount_"+start_date+"_"+end_date, 'w') as f:
    f.write(table.get_string())


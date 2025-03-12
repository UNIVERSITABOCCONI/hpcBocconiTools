import subprocess
import pandas as pd
import sys 

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

user_list = get_users_from_group(group_name)

df = pd.DataFrame(columns=['hpc', 'user', 'last', 'account',  'resource', 'usage'])
for user in user_list:
    user_df = get_user_resource_usage(user)
    if user_df is not None:
        df = pd.concat([df, user_df], ignore_index=True)

#print(df.dtypes)

# Convert 'usage' column to numeric
df['usage'] = pd.to_numeric(df['usage'], errors='coerce')

# Handle missing values (optional)
df['usage'].fillna(0, inplace=True)

# Define factors
c1 = 0.0 ## 25 euro per TB per mese darebbe questo coeff. -> c1 = 0.000025
c2 = 0.00017
c3 = 0.034

# Create a new column based on conditions
df['cost'] = df.apply(lambda row: 
                                row['usage'] * c1 if row['resource'] == 'mem' else
                                row['usage'] * c2 if row['resource'] == 'cpu' else
                                row['usage'] * c3 if row['resource'] == 'gres/gpu' else
                                0, axis=1)

#df['total_cpu_gres_gpu_usage'] = df.groupby('user')['usage'].transform(lambda x: x[(x.index == 'cpu') | (x.index == 'gres/gpu')].sum())
# Filter the DataFrame for relevant rows
filtered_df = df[(df['resource'] == 'cpu') | (df['resource'] == 'gres/gpu')]

# Group by 'user' and sum the 'usage' column
#grouped_df = filtered_df.groupby('user')['usage'].sum()
# Merge the grouped DataFrame back to the original DataFrame
#df = df.merge(grouped_df, on='user', how='left')

grouped_df = df.groupby(df.iloc[:, 0])['cost'].sum().reset_index()


# Rename the merged column
#df.rename(columns={'usage_y': 'total_cpu_gres_gpu_usage'}, inplace=True)
df.fillna(0)

#print(df.to_string())   

# Group by 'user' and sum the 'usage' column
#grouped_df = filtered_df.groupby('user')['cost'].sum().reset_index()
grouped_df = filtered_df.groupby('user').agg({'account': 'first', 'cost': 'sum'}).reset_index()


# Rename the column
grouped_df.rename(columns={'usage': 'total_cpu_gres_gpu_usage'}, inplace=True)

grouped_df=grouped_df.round(2)

grouped_df = grouped_df.sort_values(by='cost', ascending=False)
#print(grouped_df.to_string())

#print('total cost for this month:')
#print(grouped_df['cost'].sum().round(0))

from tabulate import tabulate
print(tabulate(grouped_df, headers='keys', tablefmt='psql'))
t=tabulate(grouped_df, headers='keys', tablefmt='psql')

#from tabulate import tabulate
with open("REPORTS/report_cost_start_"+start_date+"_end_"+end_date+".txt", 'w') as f:
    print(t, file=f)
    print('total cost for this period:')
    print(grouped_df['cost'].sum().round(0))

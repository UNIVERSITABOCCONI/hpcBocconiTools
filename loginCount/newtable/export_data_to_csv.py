import pandas as pd

file_path_base = "/root/utilities/hpcBocconiTools/loginCount/newtable/"

def extract_table_data(file_path):
    """Extracts data from a table-like file.

    Args:
        file_path (str): Path to the file.

    Returns:
        pandas.DataFrame: A DataFrame containing the extracted data.
    """

    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Identify the header row and data rows
    header_row = 0
    data_rows = []
    for i, line in enumerate(lines):
        if 'Label' in line and 'Count' in line:
            header_row = i
            break

    for line in lines[header_row+1:]:
        if '---' not in line: 
            label, count = line.strip().split('|')
            label = label.strip()
            count = count.strip()
            data_rows.append([label, count])

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data_rows, columns=['Label', 'Count'])

    return df

# Example usage:
file_path = file_path_base+'table_5.txt' 
print(file_path) 
df = extract_table_data(file_path)

import datetime
# Get today's date
today = datetime.date.today()
# Format the date as a string
formatted_date = today.strftime("%Y-%m-%d")

# Save the DataFrame to a CSV file
df.to_csv('/root/utilities/hpcBocconiTools/dataToReport/userActivityData/usersActivity'+formatted_date+'.csv', index=False)

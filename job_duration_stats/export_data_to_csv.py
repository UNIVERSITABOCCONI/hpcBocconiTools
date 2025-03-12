import os
import pandas as pd
import sys

def read_file_to_dataframe(file_path):
    """Reads a file with the specified format into a Pandas DataFrame.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        pandas.DataFrame: The DataFrame containing the data from the file.
    """

    # Read the file, specifying the delimiter as a tab (\t)
    df = pd.read_csv(file_path, sep='\t', header=0)

    # Assign column names
    df.columns = ['JobDuration']

    df['JobDuration'] = df['JobDuration'].str.strip()
    df = df.drop(0)

    return df

def export_to_csv(df, output_file_path):
    """Exports the DataFrame to a CSV file.

    Args:
        df (pandas.DataFrame): The DataFrame to export.
        output_file_path (str): The path to the output CSV file.
    """

    df.to_csv(output_file_path, index=False)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    import datetime
    # Get today's date
    today = datetime.date.today()
    # Format the date as a string
    formatted_date = today.strftime("%Y-%m-%d")

    input_file = os.path.basename(sys.argv[1])
    new_filename = str(input_file).replace(".txt", formatted_date)
    #new_input_file = input_file.replace("/root/utilities/hpcBocconiTools/job_duration_stats/", "")
    output_file = "/root/utilities/hpcBocconiTools/dataToReport/jobDurationData/"+new_filename+".csv"
    print(output_file)

    df = read_file_to_dataframe(sys.argv[1])
    export_to_csv(df, output_file)

    print("Data exported to CSV successfully!")

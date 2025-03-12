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
    df = pd.read_csv(file_path, sep=r'\s+', header=None)

    # Assign column names
    df.columns = ['JobID', 'JobState', 'User', 'Partition', 'ElapsedTime', 'SubmitTime', 'StartTime']

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

    input_file = str(sys.argv[1])
    new_input_file = input_file.replace("/root/utilities/hpcBocconiTools/waiting_job_stats/", "").replace(".txt","")
    output_file = "/root/utilities/hpcBocconiTools/dataToReport/waitingTimeData/"+new_input_file+".csv"

    df = read_file_to_dataframe(input_file)
    export_to_csv(df, output_file)

    print("Data exported to CSV successfully!")

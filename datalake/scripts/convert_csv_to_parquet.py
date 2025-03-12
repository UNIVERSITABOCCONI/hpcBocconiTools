import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

import datetime
yesterday = datetime.date.today() - datetime.timedelta(days=1)

def csv_to_parquet(csv_file, parquet_file):
    """
    Reads a CSV file, converts it to a Pandas DataFrame, and writes it as a Parquet file.

    Args:
        csv_file (str): Path to the input CSV file.
        parquet_file (str): Path to the output Parquet file.
    """
    try:
        df = pd.read_csv(csv_file, sep='|')
        table = pa.Table.from_pandas(df)
        pq.write_table(table, parquet_file)
        print(f"Converted {csv_file} to {parquet_file}")
    except Exception as e:
        print(f"Error processing {csv_file}: {e}")

def main():
    """
    Iterates through CSV files in a directory, converts them to Parquet, and renames the source CSV files.
    """
    yesterday_str = yesterday.strftime("%Y%m%d")
    directory = '/root/utilities/hpcBocconiTools/datalake/data/'+yesterday_str  # Replace with the actual directory path
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            csv_path = os.path.join(directory, filename)
            parquet_path = os.path.join(directory, filename.replace(".csv", ".parquet"))
            csv_to_parquet(csv_path, parquet_path)
            os.rename(csv_path, csv_path + ".done")

if __name__ == "__main__":
    main()

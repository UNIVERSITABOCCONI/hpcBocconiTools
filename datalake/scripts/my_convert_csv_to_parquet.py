import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import glob  # For easier subdirectory handling

directory = '/root/utilities/hpcBocconiTools/datalake/data_post_generated/'  # Replace with the actual directory path


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
    # Use glob to recursively find all CSV files in subdirectories
    for csv_path in glob.glob(os.path.join(directory, "**/*.csv")):  # **/* finds files in subdirectories
        filename = os.path.basename(csv_path)  # Get the filename from the full path
        subdirectory = os.path.dirname(csv_path)  # Get the subdirectory path
        parquet_filename = filename.replace(".csv", ".parquet")
        parquet_path = os.path.join(subdirectory, parquet_filename)

        csv_to_parquet(csv_path, parquet_path)

        done_path = csv_path + ".done"
        try:
            os.rename(csv_path, done_path) # Try renaming
            print(f"Renamed {csv_path} to {done_path}")
        except OSError as e: # Handle potential errors
            print(f"Error renaming {csv_path}: {e}")

if __name__ == "__main__":
    main()

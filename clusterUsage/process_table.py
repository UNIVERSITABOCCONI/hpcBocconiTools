import sys
import csv

def process_table(start_date, end_date):
    """
    Reads a table from an input file, removes the fourth column, and writes the modified table to an output file with a header.

    Args:
        start_date (str): Start date in YYYY-MM-DD format.
        end_date (str): End date in YYYY-MM-DD format.
    """

    input_filename = f"/root/utilities/hpcBocconiTools/clusterUsage/{start_date}_{end_date}_gpu_cpu_usage"
    output_filename = f"/root/utilities/hpcBocconiTools/clusterUsage/{start_date}_{end_date}_gpu_cpu_usage.csv"

    with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=' ')
        writer = csv.writer(outfile, delimiter=' ')

        # Write the header row
        writer.writerow(['date', 'gpu', 'cpu'])

        # Iterate over the rows and write the desired columns
        for row in reader:
            writer.writerow(row[:7])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <start_date> <end_date>")
        sys.exit(1)

    start_date = sys.argv[1]
    end_date = sys.argv[2]

    process_table(start_date, end_date)

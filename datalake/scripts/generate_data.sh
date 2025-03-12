#!/bin/bash

# Function to check if a date is valid (YYYY-MM-DD format)
is_valid_date() {
  date -d "$1" > /dev/null 2>&1
  return $?
}

# Function to increment a date by one day
increment_date() {
  date -d "$1 + 1 day" +%Y%m%d
}

# Get the start and end dates from the user
read -p "Enter the start date (YYYYMMDD): " start_date
read -p "Enter the end date (YYYYMMDD): " end_date

# Validate the dates
if ! is_valid_date "$start_date"; then
  echo "Invalid start date. Please use YYYYMMDD format."
  exit 1
fi

if ! is_valid_date "$end_date"; then
  echo "Invalid end date. Please use YYYYMMDD format."
  exit 1
fi

# Check if the start date is before the end date
if [[ "$start_date" > "$end_date" ]]; then
  echo "Start date must be before the end date."
  exit 1
fi

current_date="$start_date"

# Loop through the dates and print each one.  Use date comparison.
while [[ $(date -d "$current_date" +%s) -le $(date -d "$end_date" +%s) ]]; do
  echo "$current_date"
  /root/utilities/hpcBocconiTools/datalake/scripts/my_report_all_users_account_data.sh $current_date
  #/root/utilities/hpcBocconiTools/datalake/scripts/my_report_gpu_cpu_ram_daily_data.sh $current_date

  #/software/miniconda3/bin/python /root/utilities/hpcBocconiTools/datalake/scripts/convert_csv_to_parquet.py 
  #/software/miniconda3/bin/python /root/utilities/hpcBocconiTools/datalake/scripts/transfer_file_to_datalake.py 

  current_date=$(increment_date "$current_date")
done

exit 0


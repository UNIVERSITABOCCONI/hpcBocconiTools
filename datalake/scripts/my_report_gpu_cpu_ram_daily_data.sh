#!/bin/bash

current_date_yyyymmdd=$1
year="${current_date_yyyymmdd:0:4}"
month="${current_date_yyyymmdd:4:2}"
day="${current_date_yyyymmdd:6:2}"
current_date="${year}-${month}-${day}"

# Define the absolute path to the directory
base_path="/root/utilities/hpcBocconiTools/datalake/data_post_generated"

# Create the full path including yesterday's today
full_path="$base_path/$current_date"

# Create the directory. -p handles parent dirs and existing dirs.
mkdir -p "$full_path"
###

sreport cluster Utilization --tres=gres/gpu,cpu,mem -t Percent start=$current_date end=$current_date | awk '/hpc/ {if (i==0) {printf "gpu | cpu | mem |\n%s | ", $3} else if (i==1) {printf "%s | ", $3} else if (i==2) {printf "%s |\n", $3}; i++}' >> /root/utilities/hpcBocconiTools/datalake/data_post_generated/${current_date}/resources_usage.csv


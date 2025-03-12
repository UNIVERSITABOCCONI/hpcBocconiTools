
today=$(date +%F)
yesterday=$(date -d yesterday +%F)

###
yesterday_2=$(date -d yesterday +%Y%m%d)

# Define the absolute path to the directory
base_path="/root/utilities/hpcBocconiTools/datalake/data"

# Create the full path including yesterday's date
full_path="$base_path/$yesterday_2"

# Create the directory. -p handles parent dirs and existing dirs.
mkdir -p "$full_path"
###

#sreport cluster Utilization --tres=gres/gpu,cpu,mem -t Percent start=$(date -d yesterday +%F) end=$(date +%F) | awk '/hpc/ {if (i==0) printf "%s | %s |\n", "gpu", $3; else if (i==1) printf "%s | %s |\n", "cpu", $3; else if (i==2) printf "%s | %s |\n", "mem", $3; i++}' >> /root/utilities/hpcBocconiTools/datalake/data/${yesterday_2}/resources_usage.csv

sreport cluster Utilization --tres=gres/gpu,cpu,mem -t Percent start=$(date -d yesterday +%F) end=$(date +%F) | awk '/hpc/ {if (i==0) {printf "gpu | cpu | mem |\n%s | ", $3} else if (i==1) {printf "%s | ", $3} else if (i==2) {printf "%s |\n", $3}; i++}' >> /root/utilities/hpcBocconiTools/datalake/data/${yesterday_2}/resources_usage.csv
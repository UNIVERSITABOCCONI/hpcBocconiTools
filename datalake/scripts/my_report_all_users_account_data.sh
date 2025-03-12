#!/bin/bash

current_date_yyyymmdd=$1
year="${current_date_yyyymmdd:0:4}"
month="${current_date_yyyymmdd:4:2}"
day="${current_date_yyyymmdd:6:2}"
current_date="${year}-${month}-${day}"

# Define the absolute path to the directory
base_path="/root/utilities/hpcBocconiTools/datalake/data_post_generated"

# Create the full path including yesterday's my_date
full_path="$base_path/$current_date"

# Create the directory. -p handles parent dirs and existing dirs.
mkdir -p "$full_path"
###

userListAsString=`getent group -s sss| grep grp_hpcclusterbocconiusers | cut -f 4 -d :`

#check output
#echo $userListAsString
#echo "-----------------  --------------"

# Set the IFS (Internal Field Separator) to space
# Use read to bash convert string to array
IFS=',' read -ra userListAsArray <<< "$userListAsString"

for username in "${userListAsArray[@]}";
do
	sacct -a -L --noconvert --user $username -p -S $current_date -E $current_date -o JobID,JobName,Account,User,AllocCPUS,AllocNodes,AllocTRES,Cluster,ElapsedRaw,End,NNodes,Partition,Start,State,Submit | grep -v ".batch" >> /root/utilities/hpcBocconiTools/datalake/data_post_generated/${current_date}/users_accounts.csv

done




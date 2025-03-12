
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

userListAsString=`getent group -s sss| grep grp_hpcclusterbocconiusers | cut -f 4 -d :`

#check output
#echo $userListAsString
#echo "-----------------  --------------"

# Set the IFS (Internal Field Separator) to space
# Use read to bash convert string to array
IFS=',' read -ra userListAsArray <<< "$userListAsString"

sacct -a -L --noconvert --user piunno -p -o JobID,JobName,Account,User,AllocCPUS,AllocNodes,AllocTRES,Cluster,ElapsedRaw,End,NNodes,Partition,Start,State,Submit >> /root/utilities/hpcBocconiTools/datalake/data/${yesterday_2}/users_accounts.csv

for username in "${userListAsArray[@]}";
do
	sacct -a -L --noconvert --noheader --user $username -p -S $yesterday -E $today -o JobID,JobName,Account,User,AllocCPUS,AllocNodes,AllocTRES,Cluster,ElapsedRaw,End,NNodes,Partition,Start,State,Submit | grep -v ".batch" | grep -v -i doit >> /root/utilities/hpcBocconiTools/datalake/data/${yesterday_2}/users_accounts.csv

done




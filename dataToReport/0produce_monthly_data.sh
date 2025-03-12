#############################
# cluster usage CPU GPU
# TODO: add RAM
#############################

#start=$(date +\%Y)-$(date --date "-1 month" +\%m)-$(date +\%d)
#end=$(date +\%Y)-$(date +\%m)-$(date --date "-1 days" +\%d)

# Function to get the previous month, considering year rollover
get_prev_month() {
  local current_month=$(date +"%m")
  local current_year=$(date +"%Y")

  if [ "$current_month" = "01" ]; then
    prev_month="12"
    prev_year=$((current_year - 1))
  else
    prev_month=$(date --date "-1 month" +"%m")
    prev_year=$current_year
  fi

  echo "$prev_year-$prev_month"
}

# Get the start and end dates
start=$(get_prev_month)-$(date +"%d")
end=$(date +"%Y-%m-%d")

echo "start" $start
echo "end" $end

basePath='/root/utilities/hpcBocconiTools/clusterUsage/'
python_code='report_GPU_CPU_Usage_StartEnd.py'
/software/miniconda3/bin/python $basePath$python_code $start $end > "${basePath}${start}_${end}_gpu_cpu_usage"

python_export_to_csv='export_data_to_csv.py'
/software/miniconda3/bin/python $basePath$python_export_to_csv ${basePath}${start}_${end}_gpu_cpu_usage

echo "CPU GPU USAGE"
echo "cpu gpu usage in /root/utilities/hpcBocconiTools/dataToReport/clusterUsageData/ "

################################
# job duration
################################

basePath="/root/utilities/hpcBocconiTools/job_duration_stats/"

# clean previous files duration
#mv ${basePath}duration.txt ${basePath}archive/duration${start}.txt

sacct -aX --starttime ${start}T00:00:00 --endtime ${end}T00:00:00 --format=ElapsedRaw > ${basePath}duration.txt

/software/miniconda3/bin/python $basePath$python_export_to_csv ${basePath}duration.txt

echo "JOB STATS"
echo "job stats in /root/utilities/hpcBocconiTools/dataToReport/jobDurationData/"

######################
# waiting times
######################
#start=$(date +\%Y)-$(date --date "-1 month" +\%m)-$(date +\%d)
basePath="/root/utilities/hpcBocconiTools/waiting_job_stats/"
#SLURM command to genrate file with data 
echo $start
sacct -Xa --starttime ${start}T00:00:00 --endtime ${end}T00:00:00 -o jobid,state,user,partition,elapsed,submit,start  | grep gpu | egrep "COMPLETED | RUNNING" > ${basePath}waiting_time_gpu_${start}.txt
sacct -Xa --starttime ${start}T00:00:00 --endtime ${end}T00:00:00 -o jobid,state,user,partition,elapsed,submit,start | grep -v gpu | egrep "COMPLETED | RUNNING" > ${basePath}waiting_time_cpu_${start}.txt

cp ${basePath}waiting_time_cpu_${start}.txt /root/utilities/hpcBocconiTools/dataToReport/waitingTimeData/waiting_time_cpu_${start}_${end}.csv
cp ${basePath}waiting_time_gpu_${start}.txt /root/utilities/hpcBocconiTools/dataToReport/waitingTimeData/waiting_time_gpu_${start}_${end}.csv

/software/miniconda3/bin/python $basePath$python_export_to_csv ${basePath}waiting_time_gpu_${start}.txt
/software/miniconda3/bin/python $basePath$python_export_to_csv ${basePath}waiting_time_cpu_${start}.txt

echo "WAITING TIMES"
echo "waiting times in /root/utilities/hpcBocconiTools/dataToReport/waitingTimeData/"


###############################
# users activity
###############################

basePath="/root/utilities/hpcBocconiTools/loginCount/newtable/"
rm -rf ${basePath}remove/*
mv ${basePath}table_* ${basePath}last* ${basePath}remove/ 

userActivityPath="/root/utilities/hpcBocconiTools/dataToReport/userActivityData/"
cat /var/log/{wtmp-*,wtmp} > ${userActivityPath}wtmp 

/bin/last -s ${start} -f ${userActivityPath}wtmp --time-format iso > ${basePath}last_timeformat_iso_today.txt

/software/miniconda3/bin/python ${basePath}maketable_1.py $basePath
/software/miniconda3/bin/python ${basePath}maketable_2.py $basePath
/software/miniconda3/bin/python ${basePath}maketable_3.py $basePath
/software/miniconda3/bin/python ${basePath}maketable_4.py $basePath
/software/miniconda3/bin/python ${basePath}maketable_5.py $basePath

cp ${basePath}table_5.csv /root/utilities/hpcBocconiTools/dataToReport/userActivityData/${start}_${end}_usersActivity.csv

echo "USERS ACTIVITY"
echo "users activity in /root/utilities/hpcBocconiTools/dataToReport/userActivityData/"


##########################
# report usage by account
##########################
basePath="/root/utilities/hpcBocconiTools/usageByAccount/"

/software/miniconda3/bin/python ${basePath}reportUsagePerAccount.py users ${start} ${end} > ${basePath}UsagePerAccount_${start}_${end}_users
#cp ${basePath}UsagePerAccount_${start}_${end}_users /root/utilities/hpcBocconiTools/dataToReport/usageByAccountData/UsagePerAccount_${start}_${end}

#/software/miniconda3/bin/python ${basePath}reportUsagePerAccount.py admins ${start} ${end} > ${basePath}UsagePerAccount_${start}_${end}_admins
#cat ${basePath}UsagePerAccount_${start}_${end}_admins >> /root/utilities/hpcBocconiTools/dataToReport/usageByAccountData/UsagePerAccount_${start}_${end}


echo "USAGE BY ACCOUNT"
echo "usage by account in /root/utilities/hpcBocconiTools/dataToReport/usageByAccountData/"

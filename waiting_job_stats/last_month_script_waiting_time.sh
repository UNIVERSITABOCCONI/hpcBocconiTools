# the script produces a histograms with the wating times (how long are pending the jobs)

# clean previous files histograms
#mv /root/utilities/hpcBocconiTools/waiting_job_stats/figures/2024/histogram_* /root/utilities/hpcBocconiTools/waiting_job_stats/figures/2024/archive/

basePath="/root/utilities/hpcBocconiTools/waiting_job_stats/"

###start=$(date --date "-1 year" +\%Y)-$(date +\%m)-$(date +\%d)

start=$(date +\%Y)-$(date --date "-1 month" +\%m)-$(date --date "-1 day" +\%d)
end=$(date +\%Y)-$(date +\%m)-$(date --date "-1 days" +\%d)

#SLURM command to genrate file with data 
#sacct -Xa --starttime ${start}T00:00:00 --endtime ${end}T00:00:00 -o jobid,state,user,partition,elapsed,submit,start  | grep gpu > waiting_time_gpu_${start}_${end}.txt

sacct --noheader -Xa --starttime ${start}T00:00:00 --endtime ${end}T00:00:00 -o jobid,state,user,partition,elapsed,submit,start | grep -v gpu |grep -v None > waiting_time_cpu_${start}_${end}.txt






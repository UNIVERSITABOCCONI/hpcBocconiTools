# the script produces a histograms with the wating times (how long are pending the jobs)

# clean previous files histograms
#mv /root/utilities/hpcBocconiTools/waiting_job_stats/figures/2024/histogram_* /root/utilities/hpcBocconiTools/waiting_job_stats/figures/2024/archive/

basePath="/root/utilities/hpcBocconiTools/waiting_job_stats/"

start=$(date --date "-1 year" +\%Y)-$(date +\%m)-$(date +\%d)
end=$(date +\%Y)-$(date +\%m)-$(date --date "-1 days" +\%d)

#SLURM command to genrate file with data 
sacct -Xa --starttime ${start}T00:00:00 --endtime ${end}T00:00:00 -o jobid,state,user,partition,elapsed,submit,start  | grep gpu | egrep "COMPLETED | RUNNING" > waiting_time_gpu_${start}.txt

sacct -Xa --starttime ${start}T00:00:00 --endtime ${end}T00:00:00 -o jobid,state,user,partition,elapsed,submit,start | grep -v gpu | egrep "COMPLETED | RUNNING" > waiting_time_cpu_${start}.txt







# the script produces 3 histograms with the job durations

# clean previous files histograms
mv /root/utilities/hpcBocconiTools/job_duration_stats/figures/2024/histogram_* /root/utilities/hpcBocconiTools/job_duration_stats/figures/2024/archive/

basePath="/root/utilities/hpcBocconiTools/job_duration_stats/"

###start=$(date +\%Y)-$(date --date "-1 month" +\%m)-$(date +\%d)

start=$(date --date "-1 year" +\%Y)-$(date --date "-1 month" +\%m)-$(date --date "-27 day" +\%d)
end=$(date +\%Y)-$(date +\%m)-$(date --date "-1 days" +\%d)

# clean previous files duration
mv /root/utilities/hpcBocconiTools/job_duration_stats/duration.txt /root/utilities/hpcBocconiTools/job_duration_stats/archive/duration${start}.txt

sacct --noheader -aX --starttime ${start}T00:00:00 --endtime ${end}T00:00:00 --format=ElapsedRaw > ${basePath}duration.txt

/software/miniconda3/bin/python ${basePath}histo_T_maj_1h_NI.py
/software/miniconda3/bin/python ${basePath}histo_T_min_1h_NI.py
/software/miniconda3/bin/python ${basePath}histo_T_min_15sec_NI.py



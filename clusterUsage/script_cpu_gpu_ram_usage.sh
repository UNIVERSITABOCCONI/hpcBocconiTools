

basePath='/root/utilities/hpcBocconiTools/clusterUsage/'
python_code='report_GPU_CPU_RAM_Usage_StartEnd.py'

start_day=$(date +\%Y)-$(date --date "-1 month" +\%m)-$(date --date "-7 day" +\%d)
end_day=$(date +\%Y)-$(date +\%m)-$(date --date "-1 days" +\%d)

/software/miniconda3/bin/python $basePath$python_code $start_day $end_day > "${basePath}${start_day}_${end_day}_gpu_cpu_ram_usage_lastweek"

##/software/miniconda3/bin/python ${basePath}make_histo.py



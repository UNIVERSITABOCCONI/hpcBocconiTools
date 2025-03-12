basePath='/root/utilities/hpcBocconiTools/usageByAccount/'
python_code='reportCostPerAccount.py'

start_day=$(date +\%Y)-$(date --date "-1 month" +\%m)-$(date +\%d)
end_day=$(date +\%Y)-$(date +\%m)-$(date --date "-1 days" +\%d)
#group="users"
group="admins"

/software/miniconda3/bin/python $basePath$python_code $group $start_day $end_day 



import sys
import subprocess 
import datetime
import re

#TODO insert wanring to insert argv1,2
if (len(sys.argv) < 2 and len(sys.argv) < 3):
        print("Usage: python reportUsageStartEnd.py start_date end_date")
        print(" date format YYYY-MM-DD (ex. 2023-11-22)")
        sys.exit(0)

start_date_str = sys.argv[1]
end_date_str = sys.argv[2]

date_format = '%Y-%m-%d'
start_date = datetime.datetime.strptime(start_date_str, date_format)
end_date = datetime.datetime.strptime(end_date_str, date_format)
# delta time
delta = datetime.timedelta(days=1)

# iterate over range of dates
while (start_date <= end_date):
        
	proc = subprocess.Popen(["sreport cluster Utilization --tres=\'gres/gpu,cpu\' -t Percent start=" + start_date.strftime(date_format) + " end=" + (start_date+delta).strftime(date_format) + " -n | awk '{ print $3 }'"], stdout=subprocess.PIPE, shell=True)
	
	(out, err) = proc.communicate()
	#print(re.sub(r'[^0-9.%]', '', str(out)))  
	print(start_date.strftime('%Y-%m-%d'), re.sub(r'[^0-9.%]', ' ', str(out)))
	start_date += delta

# This code generates an histogram of the waiting times for jobs
# taking as input a file waiting_time.txt

import matplotlib.pyplot as plt
import datetime

# Get the current date
today = datetime.date.today()

# Calculate one month ago
one_month_ago = today - datetime.timedelta(days=29)

# Convert dates to strings
current_date_str = today.strftime("%Y-%m-%d")
one_month_ago_str = one_month_ago.strftime("%Y-%m-%d")

filename = "/root/utilities/hpcBocconiTools/waiting_job_stats/waiting_time.txt"
my_string = one_month_ago_str


lines=[]
with open(filename) as f:
    next(f) # skip header line
    next(f) # skip header line
    for line in f:
        lines.append(int(line.replace("\n", "").replace(",", "")))

lines.remove(max(lines))

# from seconds to hours
lines = [x * 0.000277778 for x in lines]
# selecting by duration (more than 1 h)
lines_more_1h = [x for x in lines if (x > 1)]
lines_between_15s_and_1h = [x for x in lines if (x >0.004 and x <1.0)]
lines_less_15s = [x for x in lines if (x <16)]
#print(lines)
#print(int(max(lines)), int(min(lines)), int(sum(lines)/len(lines)), len(lines) )

# the histogram of the data (more than 1 h)
label_size=30
fig, ax = plt.subplots(figsize=(16, 10))
ax.hist(lines, density=False)
ax.set_title('Statistics of Pending Jobs in hours from ' +my_string+' \n T > 1 h', fontsize=label_size)
ax.set_xlabel('SLURM Pending Jobs in hours', fontsize=label_size)
ax.set_ylabel('Number of occurrences', fontsize=label_size)
ax.tick_params(axis='both', which='major', labelsize=label_size)
ax.tick_params(axis='both', which='major', labelsize=label_size)
plt.text(.99, .99, 'tot occurrences = %s'%len(lines), ha='right', va='top', transform=ax.transAxes, color='blue', style='italic', fontsize=label_size)
for rect in ax.patches:
    height = rect.get_height()
    ax.annotate(f'{int(height)}', xy=(rect.get_x()+rect.get_width()/2, height),
                xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=label_size)
plt.show()
fig.tight_layout()
fig.savefig('/root/utilities/hpcBocconiTools/waiting_job_stats/figures/2024/histogram_'+my_string+'T_ma_1h.png')

# the histogram of the data (x >0.004 and x <1.0)
label_size=30
fig, ax = plt.subplots(figsize=(16, 10))
ax.hist(lines, density=False)
ax.set_title('Statistics of Pending Jobs in hours from ' +my_string+'\n T < 1 h', fontsize=label_size)
ax.set_xlabel('SLURM Pending Jobs in hours', fontsize=label_size)
ax.set_ylabel('Number of occurrences', fontsize=label_size)
ax.tick_params(axis='both', which='major', labelsize=label_size)
ax.tick_params(axis='both', which='major', labelsize=label_size)
plt.text(.99, .99, 'tot occurrences = %s'%len(lines), ha='right', va='top', transform=ax.transAxes, color='blue', style='italic', fontsize=label_size)
for rect in ax.patches:
    height = rect.get_height()
    ax.annotate(f'{int(height)}', xy=(rect.get_x()+rect.get_width()/2, height),
                xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=label_size)

plt.show()
fig.tight_layout()
fig.savefig('/root/utilities/hpcBocconiTools/waiting_job_stats/figures/2024/histogram_'+my_string+'T_min_1h.png')

# the histogram of the data x < 16s
label_size=28
fig, ax = plt.subplots(figsize=(16, 10))
ax.hist(lines, density=False)
ax.set_title('Statistics of Pending Jobs in seconds from ' +my_string+'\n T < 15 sec', fontsize=label_size)
ax.set_xlabel('SLURM Pending Jobs in seconds', fontsize=label_size)
ax.set_ylabel('Number of occurrences', fontsize=label_size)
ax.tick_params(axis='both', which='major', labelsize=label_size)
plt.text(.99, .99, 'tot occurrences = %s'%len(lines), ha='right', va='top', transform=ax.transAxes, color='blue', style='italic', fontsize=label_size)
for rect in ax.patches:
    height = rect.get_height()
    ax.annotate(f'{int(height)}', xy=(rect.get_x()+rect.get_width()/2, height),
                xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=label_size)
plt.show()
fig.tight_layout()
fig.savefig('/root/utilities/hpcBocconiTools/waiting_job_stats/figures/2024/histogram_'+my_string+'T_min_15sec.png')

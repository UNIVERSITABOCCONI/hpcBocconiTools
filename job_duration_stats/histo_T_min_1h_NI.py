import matplotlib.pyplot as plt
import datetime

# Get the current date
today = datetime.date.today()

# Calculate one month ago
one_month_ago = today - datetime.timedelta(days=29)

# Convert dates to strings
current_date_str = today.strftime("%Y-%m-%d")
one_month_ago_str = one_month_ago.strftime("%Y-%m-%d")

filename = "/root/utilities/hpcBocconiTools/job_duration_stats/duration.txt"
my_string = one_month_ago_str

my_string
lines=[]
with open(filename) as f:
    next(f) # skip header line
    next(f) # skip header line
    for line in f:
        lines.append(int(line.replace("\n", "").replace(",", "")))

# from seconds to hours
lines = [x * 0.000277778 for x in lines]
# selecting by duration
lines = [x for x in lines if (x >0.004 and x <1.0)]
#print(lines)
#print(int(max(lines)), int(min(lines)), int(sum(lines)/len(lines)), len(lines) )

# the histogram of the data
label_size=30
fig, ax = plt.subplots(figsize=(16, 10))
ax.hist(lines, density=False)
ax.set_title('Statistics of Job duration in hours from ' +my_string+'\n T < 1 h', fontsize=label_size)
ax.set_xlabel('SLURM Job duration in hours', fontsize=label_size)
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
fig.savefig('/root/utilities/hpcBocconiTools/job_duration_stats/figures/2025/histogram_'+my_string+'T_min_1h.png')

import matplotlib.pyplot as plt
import numpy as np

filename = input("Enter the filename: ")
my_string = input("Enter a one-word string with date (example 'feb28_2024'): ")

lines=[]
with open(filename) as f:
    next(f) # skip header line
    next(f) # skip header line
    for line in f:
        lines.append(int(line.replace("\n", "").replace(",", "")))



# from seconds to hours
#lines = [x * 0.000277778 for x in lines]
#from seconds to minutes
#lines = [x * 0.0166667 for x in lines]
lines = [x for x in lines if (x <16)]
print(lines)
print(int(max(lines)), int(min(lines)), int(sum(lines)/len(lines)), len(lines) )

# the histogram of the data
label_size=28
fig, ax = plt.subplots(figsize=(16, 10))
ax.hist(lines, density=False)
ax.set_title('Statistics of Job duration in seconds from ' +my_string+'\n T < 15 sec', fontsize=label_size)
ax.set_xlabel('SLURM Job duration in seconds', fontsize=label_size)
ax.set_ylabel('Number of occurrences', fontsize=label_size)
ax.tick_params(axis='both', which='major', labelsize=label_size)


plt.text(.99, .99, 'tot occurrences = %s'%len(lines), ha='right', va='top', transform=ax.transAxes, color='blue', style='italic', fontsize=label_size)

for rect in ax.patches:
    height = rect.get_height()
    ax.annotate(f'{int(height)}', xy=(rect.get_x()+rect.get_width()/2, height),
                xytext=(0, 5), textcoords='offset points', ha='center', va='bottom', fontsize=label_size)

plt.show()
fig.tight_layout()
fig.savefig('/root/utilities/hpcBocconiTools/job_duration_stats/figures/2024/histogram_'+my_string+'T_min_15sec.png')

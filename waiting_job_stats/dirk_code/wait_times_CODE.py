import pandas as pd
import matplotlib.pyplot as plt

df_cpu_wait = pd.read_csv("data/waiting_time_cpu_2025-02-03_2025-03-03.txt", sep='\s+', names=['JobID', 'JobState', 'User', 'Partition', 'ElapsedTime', 'SubmitTime', 'StartTime'], date_format='Y-M-D')


df_cpu_wait['StartTime'] = pd.DatetimeIndex(df_cpu_wait['StartTime'])
df_cpu_wait['SubmitTime'] = pd.DatetimeIndex(df_cpu_wait['SubmitTime'])
df_cpu_wait['ElapsedTime'] = pd.to_timedelta(df_cpu_wait.ElapsedTime)
df_cpu_wait['wait'] = df_cpu_wait.StartTime - df_cpu_wait.SubmitTime

df_gpu_wait = pd.read_csv("data/waiting_time_gpu_2025-02-02_2025-03-02.txt", sep='\s+', names=['JobID', 'JobState', 'User', 'Partition', 'ElapsedTime', 'SubmitTime', 'StartTime'], date_format='Y-M-D')
df_gpu_wait['StartTime'] = pd.DatetimeIndex(df_gpu_wait['StartTime'])
df_gpu_wait['SubmitTime'] = pd.DatetimeIndex(df_gpu_wait['SubmitTime'])
df_gpu_wait['ElapsedTime'] = pd.to_timedelta(df_gpu_wait.ElapsedTime)
df_gpu_wait['wait'] = df_gpu_wait.StartTime - df_gpu_wait.SubmitTime

print("CPU stats")
print(df_cpu_wait.wait.describe())
print(df_cpu_wait.wait.median())

print("GPU stats")
print("---------------------")
print(df_gpu_wait.wait.describe())
print(df_gpu_wait.wait.median())

fig, ax = plt.subplots(figsize=(20,10))
(df_cpu_wait.wait.dt.seconds/3600).hist()
#fig.savefig('cpu_wait.png')

fig, ax = plt.subplots(figsize=(20,10))
(df_gpu_wait.wait.dt.seconds/3600).hist()
#fig.savefig('gpu_wait.png')

## check only jobs that wait longer than they run and did not start immediately
too_long_cpu = df_cpu_wait[(df_cpu_wait.ElapsedTime.dt.seconds < df_cpu_wait.wait.dt.seconds) & (df_cpu_wait.wait.dt.seconds > 0)]
too_long_gpu = df_gpu_wait[(df_gpu_wait.ElapsedTime.dt.seconds < df_gpu_wait.wait.dt.seconds) & (df_gpu_wait.wait.dt.seconds > 0)]

# get difference between wait time and runtime in hours
too_long_cpu['Diff'] = ((too_long_cpu.wait.dt.seconds - too_long_cpu.ElapsedTime.dt.seconds)/3600)
# get wait to run ratio
too_long_cpu['Ratio'] = ((too_long_cpu.wait.dt.seconds / too_long_cpu.ElapsedTime.dt.seconds))
too_long_gpu['Diff'] = ((too_long_gpu.wait.dt.seconds - too_long_gpu.ElapsedTime.dt.seconds)/3600)
too_long_gpu['Ratio'] = ((too_long_gpu.wait.dt.seconds / too_long_gpu.ElapsedTime.dt.seconds))

print("CPU jobs that wait longer than they run")
print(len(too_long_cpu)/len(df_cpu_wait)) # % of jobs waiting longer than they run
print(too_long_cpu['Diff'].describe())
#too_long_cpu['Diff'].plot.hist(bins=24)
#fig.savefig('cpu_wait_toolong.png')

print("GPU jobs that wait longer than they run")
print("---------------------")
print(len(too_long_gpu)/len(df_gpu_wait))
print(too_long_gpu['Diff'].describe())
#too_long_gpu['Diff'].plot.hist(bins=24)
#fig.savefig('gpu_wait_toolong.png')

print("number of CPU users")
print(df_cpu_wait['User'].nunique())
print("total jobs")
print(df_cpu_wait['User'].count())
print("number of GPU users")
print(df_gpu_wait['User'].nunique())
print("total jobs")
print(df_gpu_wait['User'].count())

print("accounts CPU jobs")
print(df_cpu_wait['User'].unique())
print("accounts GPU jobs")
print(df_gpu_wait['User'].unique())


cpu_users = set(df_cpu_wait['User'].unique())
gpu_users = set(df_gpu_wait['User'].unique())

intersection = cpu_users.intersection(gpu_users)


if intersection:
    print("There are intersections between the two groups.")
    print("Intersecting users:", intersection)
else:
    print("There are no intersections between the two groups.")

print("active users (running jobs) over one month")
print(len(cpu_users) + len(gpu_users) - len(intersection))

cpu_users = cpu_users - intersection
gpu_users = gpu_users - intersection

print("GPU only")
print(len(gpu_users))
print("CPU only")
print(len(cpu_users))
print("GPU & CPU")
print(len(intersection))
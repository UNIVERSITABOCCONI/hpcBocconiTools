import pandas as pd
import matplotlib.pyplot as plt

df_gpu_wait = pd.read_csv("data/waiting_time_cpu_2024-01-01_2025-03-02.txt", sep='\s+', names=['JobID', 'JobState', 'User', 'Partition', 'ElapsedTime', 'SubmitTime', 'StartTime'], date_format='Y-M-D')
df_gpu_wait['StartTime'] = pd.DatetimeIndex(df_gpu_wait['StartTime'])
df_gpu_wait['SubmitTime'] = pd.DatetimeIndex(df_gpu_wait['SubmitTime'])
df_gpu_wait['ElapsedTime'] = pd.to_timedelta(df_gpu_wait.ElapsedTime)
df_gpu_wait['wait'] = df_gpu_wait.StartTime - df_gpu_wait.SubmitTime

print("GPU stats")
print("---------------------")
print(df_gpu_wait.wait.describe())
print(df_gpu_wait.wait.median())

fig, ax = plt.subplots(figsize=(20,10))
(df_gpu_wait.wait.dt.seconds/3600).hist()
#fig.savefig('gpu_wait.png')

## check only jobs that wait longer than they run and did not start immediately
too_long_gpu = df_gpu_wait[(df_gpu_wait.ElapsedTime.dt.seconds < df_gpu_wait.wait.dt.seconds) & (df_gpu_wait.wait.dt.seconds > 0)]

# get difference between wait time and runtime in hours
# get wait to run ratio
too_long_gpu['Diff'] = ((too_long_gpu.wait.dt.seconds - too_long_gpu.ElapsedTime.dt.seconds)/3600)
too_long_gpu['Ratio'] = ((too_long_gpu.wait.dt.seconds / too_long_gpu.ElapsedTime.dt.seconds))


print("GPU jobs that wait longer than they run")
print("---------------------")
print(len(too_long_gpu)/len(df_gpu_wait))
print(too_long_gpu['Diff'].describe())
#too_long_gpu['Diff'].plot.hist(bins=24)
#fig.savefig('gpu_wait_toolong.png')

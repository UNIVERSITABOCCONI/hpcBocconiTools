import pandas as pd
import matplotlib.pyplot as plt

df_cpu_wait = pd.read_csv("waiting_time_cpu_2024-12-20_1month.txt", sep='\s+', names=['JobID', 'JobState', 'User', 'Partition', 'ElapsedTime', 'SubmitTime', 'StartTime'], date_format='Y-M-D')


df_cpu_wait['StartTime'] = pd.DatetimeIndex(df_cpu_wait['StartTime'])
df_cpu_wait['SubmitTime'] = pd.DatetimeIndex(df_cpu_wait['SubmitTime'])
df_cpu_wait['ElapsedTime'] = pd.to_timedelta(df_cpu_wait.ElapsedTime)
df_cpu_wait['wait'] = df_cpu_wait.StartTime - df_cpu_wait.SubmitTime


df_gpu_wait = pd.read_csv("waiting_time_gpu_2024-01-13_2025-01-12.txt", sep='\s+', names=['JobID', 'JobState', 'User', 'Partition', 'ElapsedTime', 'SubmitTime', 'StartTime'], date_format='Y-M-D')
df_gpu_wait['StartTime'] = pd.DatetimeIndex(df_gpu_wait['StartTime'])
df_gpu_wait['SubmitTime'] = pd.DatetimeIndex(df_gpu_wait['SubmitTime'])
df_gpu_wait['ElapsedTime'] = pd.to_timedelta(df_gpu_wait.ElapsedTime)
df_gpu_wait['wait'] = df_gpu_wait.StartTime - df_gpu_wait.SubmitTime


import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("2023-11-16_2024-11-10_gpu_cpu_usage", sep='\s+', names=['Dates', 'GPU_usage', 'CPU_usage'], date_format='Y-M-D')
for col in ['GPU_usage', 'CPU_usage']:
    df1[col] = df1[col].str.rstrip('%').astype('float')
    df1['{}_MA_week'.format(col)] = df1[col].rolling(window=7).mean()
    df1['{}_MA_month'.format(col)] = df1[col].rolling(window=30).mean()

fig, ax = plt.subplots(figsize=(20,10))
df1[['Dates', 'GPU_usage_MA_month', 'CPU_usage_MA_month']].plot.line(x='Dates', ax=ax)
fig.savefig('monthly_usage.png')



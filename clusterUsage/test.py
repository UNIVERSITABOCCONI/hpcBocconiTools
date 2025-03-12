# Load data from string
df = pd.read_csv(io.StringIO(data), sep='\t', header=None, names=['Date', 'Value1', 'Value2'])

# Clean and convert data
df['Date'] = pd.to_datetime(df['Date'])
df['Value1'] = df['Value1'].str.rstrip('%').astype('float') / 100.0
df['Value2'] = df['Value2'].str.rstrip('%').astype('float') / 100.0

# Calculate week start
df['Week_Start'] = df['Date'] - pd.to_timedelta(df['Date'].dt.dayofweek, unit='d')

# Calculate weekly means and standard deviations
weekly_stats = df.groupby('Week_Start').agg(
    Value1_mean=('Value1', 'mean'),
    Value2_mean=('Value2', 'mean'),
    Value1_std=('Value1', 'std'),
    Value2_std=('Value2', 'std')
).reset_index()

# Print the result
print(weekly_stats)

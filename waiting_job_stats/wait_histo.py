import matplotlib.pyplot as plt
import pandas as pd
import datetime
import matplotlib.dates as mdates
import time

# Function to convert duration string to seconds
def convert_duration_to_seconds(duration_str):
    parts = duration_str.split('-')
    days = 0
    if len(parts) == 2:
        days = int(parts[0])
    time_str = parts[-1]
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds
    return total_seconds


def plot_data(filename):
    """Plots a histogram of job completion times from the given file.

    Args:
        filename: The name of the input file.
    """

    # Read the data from the file
    df = pd.read_csv(filename, delim_whitespace=True, header=None)
    print(df)

    # Extract the relevant columns
    df.columns = ['JobID', 'User', 'SubmitTime', 'EndTime', 'State', 'PlannedTime', 'Partition']
    print(df)

    df = df[['SubmitTime', 'PlannedTime']]
    #print(df)

    # Extract date from the first part of the first column
    df['Date'] = pd.to_datetime(df['SubmitTime'].str.split('T').str[0])


    # Extract duration from the second column
    #df['Duration'] = df['PlannedTime'].str.replace('-', '')
    #df['Duration'] = df['Duration'].apply(lambda x: datetime.timedelta(days=int(x[:2]), hours=int(x[2:5]), minutes=int(x[5:8]), seconds=int(x[8:])))

    #print(df)


    # Sample data (replace with your own)
    dates = df['Date'].values
    durations = df['PlannedTime']

    # Convert durations to seconds
    durations_seconds = [convert_duration_to_seconds(duration) for duration in durations]
    #dates = [dates for date in dates
    print("======================")
    print(durations_seconds)
    print(dates)
    print("======================")

    # Create the plot
    plt.figure(figsize=(10, 6))
    #plt.plot(dates, durations_seconds, marker='o', linestyle='-', color='blue')
    plt.scatter(dates, durations_seconds, color='blue')#, width=0.5)

    # Set labels and title
    plt.title('Daily Duration Over Time')
    plt.xlabel('Date')
    plt.ylabel('Waiting time (seconds)')
    # Format the x-axis dates
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.xticks(rotation=45)
    # Show the plot
    plt.tight_layout()
    plt.show()
    plt.savefig(gpu_2024_01_13_2025_01_12.pdf)


# Example usage
filename = 'waiting_time_gpu_2024-01-13_2025-01-12.txt'  # Replace with the actual filename
plot_data(filename)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Your original data with timestamps
# data = [(0, -450, timestamp1), (1, -440, timestamp2), ... , (806, 410, timestampN)]
data = out_dict['traj_record'][0]

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data, columns=['x', 'y'])

df['timestamp'] = out_dict['traj_timestamp'][0]
# Convert the 'timestamp' column to datetime type
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')  # Assuming timestamps are in seconds

# Set the 'timestamp' column as the index
df.set_index('timestamp', inplace=True)

# Define the downsampling time interval (e.g., 5 milliseconds)
downsampling_interval = '25L'

# Resample using asfreq to keep the original values at the specified interval
#downsampled_df = df.asfreq(downsampling_interval, method='pad')
downsampled_df = df.resample(downsampling_interval).mean().dropna()
# Create a new column with tuples of downsampled x and y values
downsampled_df['downsampled_coordinates'] = list(zip(downsampled_df['x'], downsampled_df['y']))

# Create a new figure
plt.figure(figsize=(8, 6))

# Plot the downsampled mouse trajectory
#plt.plot(downsampled_df['x'], downsampled_df['y'], label='Downsampled Mouse Trajectory', color='blue')
plt.scatter(downsampled_df['x'], downsampled_df['y'], color='red', s=3, label='Downsampled Mouse Positions')
plt.hlines(-108, xmin=-800, xmax=800, colors='orange')

# Add labels and title
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Downsampled Mouse Trajectory')

# Set x-axis limits to show the left side of the screen
plt.xlim(-840, 840)
plt.ylim(-500, 500)  # Assuming max(downsampled_df['x']) is the rightmost position

# Add legend
plt.legend()

# Show the plot
plt.show()

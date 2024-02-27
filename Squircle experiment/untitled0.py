# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:50:23 2024

@author: veoni
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:11:14 2024

@author: veoni
"""
import pandas as pd
import glob
import warnings

warnings.filterwarnings('ignore')
data_files = glob.glob(r'../Squircle experiment/data/*.json')
# Load the dataset
df = pd.DataFrame()
for i in range(len(data_files)):
    temp_df = pd.read_json(data_files[i])
    temp_df['previous_response'] = temp_df['choice'].shift(fill_value=None)
    df = pd.concat([df, temp_df])
df = df.drop(df.columns[df.columns.str.contains('Unnamed', case=False)], axis=1)
# select only the main task
df = df[(df['block_number'] != 'Training') & (df['acc'] != 'NAN')]

# extracting sample size
n = len(set(df.pt_num))

df_acc = df[(df['difficulty'] != 'Control') & (df['acc'] != 'Control') & (df['acc'] != 'NAN')]

# Convert 'acc' column to 1 for True and 0 for False
df_acc['acc'] = df_acc['acc'].astype(int)

# Assuming df is your original DataFrame with 'traj_record' and 'traj_timestamp' columns

# Define the downsampling time interval (e.g., 25 milliseconds)
downsampling_interval = '10L'

# Create empty lists to store the downsampled coordinates and timestamps
downsampled_coordinates_list = []
new_timestamps_list = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Extract data for the current trial
    data = row['traj_record']

    # Convert the data to a pandas DataFrame
    df_trial = pd.DataFrame(data, columns=['x', 'y'])

    df_trial['timestamp'] = row['traj_timestamp']
    # Convert the 'timestamp' column to datetime type
    df_trial['timestamp'] = pd.to_datetime(df_trial['timestamp'], unit='s')  # Assuming timestamps are in seconds

    # Set the 'timestamp' column as the index
    df_trial.set_index('timestamp', inplace=True)

    # Resample using asfreq to keep the original values at the specified interval
    downsampled_df = df_trial.resample(downsampling_interval).mean().dropna()

    # Create a new column with tuples of downsampled x and y values
    downsampled_df['downsampled_coordinates'] = list(zip(downsampled_df['x'], downsampled_df['y']))

    # Append downsampled coordinates and timestamps to the lists
    downsampled_coordinates_list.append(downsampled_df['downsampled_coordinates'].tolist())
    new_timestamps_list.append(downsampled_df.index.tolist())

# Add new columns to the original DataFrame
df['downsampled_traj'] = downsampled_coordinates_list
df['timestamps'] = new_timestamps_list
df.reset_index(inplace=True)
df.to_json('DF_clean.json')
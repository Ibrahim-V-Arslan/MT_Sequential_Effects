# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:13:08 2023

@author: veoni
"""

import os
import math
from psychopy import visual, core, event
from experiment_prerequisite import experiment_df, training_df, training_trial, max_trial
import pandas as pd

# Constants
WIDTH = 1920
HEIGHT = 1080
MOVEMENT_RADIUS = 150
N_CIRCLES = 8


# Psychopy Window
win = visual.Window(size=(WIDTH, HEIGHT), units='pix', fullscr=False, allowGUI=True, color=(100, 100, 100), colorSpace='rgb255')
win.mouseVisible = True

# Function to display stimuli
def display_stimuli(condition):
    # Filter the dataframe for the given condition and stimulus color Blue
    filtered_df = experiment_df[(experiment_df['Condition'] == condition) & (experiment_df['Stimulus Color'] == 'Blue')]

    if filtered_df.empty:
        return

    # Move the stimuli upwards and make them smaller 
    start_y = 320
    angles = [(i * (360 / N_CIRCLES)) for i in range(N_CIRCLES)]
    positions = [(MOVEMENT_RADIUS * math.cos(math.radians(angle)),
                  MOVEMENT_RADIUS * math.sin(math.radians(angle)) + start_y) for angle in angles]

    # Create circles
    circles = [visual.Circle(win, units="pix", size=60, colorSpace="rgb255", pos=pos, fillColor=filtered_df[f'RGB_{i}'].iloc[0])
               for i, pos in enumerate(positions, start=1)]

    # Create fixation cross
    fixation = visual.TextStim(win, text="+", height=52, color="black", pos=(0, 320))

    # Draw stimuli and fixation cross
    fixation.draw()
    for circle in circles:
        circle.draw()

    # Display window
    win.flip()

    # Wait for a key press to close
    event.waitKeys(keyList=['space'])

# Display stimuli for each condition
for condition in ['Easy', 'Medium', 'Hard']:
    display_stimuli(condition)

# Close window
win.close()
core.quit()

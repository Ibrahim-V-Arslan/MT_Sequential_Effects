# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:04:29 2023

@author: veoni
"""

import os
# Set the directory of the current script as the working directory
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)
import sys
from psychopy import visual, core, event, gui
import pandas as pd
from psychopy.event import Mouse
from experiment_prerequisite import experiment_df, training_df, training_trial, max_trial
import math


# Constants
WIDTH = 1920
HEIGHT = 1080
onset_point = -108
stim_duration = 0.2
MOVEMENT_RADIUS = 150
N_CIRCLES = 8
  
# Clocks
clock = core.Clock()
overall_time = core.Clock()

# Variables
variables = [
    'pt_num', 'Age', 'Gender', 'Handedness', 'trial_nbr', 'block_number',
    'traj_record', 'traj_timestamp', 'stim_traj', 'rt', 'acc', 'choice', 'true_value', 'difficulty', 'c_value', 'Experiment Duration',
]

# Create an empty dictionary for output
out_dict = {variable: [] for variable in variables}

# GUI screen to collect participant number
myDlg = gui.Dlg(title="Squircle Task")
myDlg.addField('Participant Number')
myDlg.addField('Age:')
myDlg.addField('Gender:', choices=["Male", "Female", "Other"])
myDlg.addField('Preferred Hand', choices=["Right", "Left"])
pt_num = myDlg.show()

if not myDlg.OK or not pt_num[0].isdigit():
    print("ERROR!!! Participant number is not a digit.")
    sys.exit()
    
# Psychopy Window
win = visual.Window(size=(WIDTH, HEIGHT), units='pix', fullscr=True,allowGUI=True, color=(100, 100, 100), colorSpace='rgb255')
win.mouseVisible = True

# Stimuli
fixation = visual.TextStim(win, text="+", height=52, color="black", pos=(0, 320))
correct_answer = visual.TextStim(win, text="Good", color=(-1, 1, -1), colorSpace='rgb', bold=True, height=26)
incorrect_answer = visual.TextStim(win, text="Wrong", color=(1.0, -1, -1), colorSpace='rgb', bold=True, height=26)
control_answer = visual.TextStim(win, text="Control", color="yellow", colorSpace='rgb', bold=True, height=26)
return_square = visual.Rect(win, width=30, height=30, lineColor='green', fillColor = "white",  pos=(0, -450), colorSpace="rgb255")


# Move the stimuli upwards and make them smaller 
start_y = 320
angles = [(i * (360 / N_CIRCLES)) for i in range(N_CIRCLES)]
positions = [(MOVEMENT_RADIUS * math.cos(math.radians(angle)),
              MOVEMENT_RADIUS * math.sin(math.radians(angle)) + start_y) for angle in angles]

# Create circles
circles = [visual.Circle(win, units="pix", size=60, colorSpace="rgb255", pos=pos, fillColor=training_df[f'RGB_{i}'].iloc[0])
           for i, pos in enumerate(positions, start=1)]

# Option Boxes
red_pill = visual.Rect(win, width=150, height=150, fillColor="red", pos=(885, 465), autoDraw=False)
blue_pill = visual.Rect(win, width=150, height=150, fillColor="blue", pos=(-885, 465), autoDraw=False)

# Training Lines
horizon = visual.Line(win, start=(-960, onset_point), end=(960, onset_point), lineColor='black', autoDraw=False)
win.flip()

# Mouse
mouse = Mouse()
mouse.setVisible(True)

# Instructions
instr_1 = visual.ImageStim(win, image="./instructions/instruction1.png")
instr_2 = visual.ImageStim(win, image="./instructions/instruction2.png")
instr_3 = visual.MovieStim(win, filename = "./instructions/Instruction3.mp4", pos = (0,0), noAudio = True, autoStart = True, loop = False, size = (1920,1080), flipVert=False, flipHoriz=False)
instr_trn_to_exp = visual.ImageStim(win, image="./instructions/trn_to_exp.png")
instr_4 = visual.ImageStim(win, image="./instructions/instruction4.png")
instr_mid = visual.ImageStim(win, image="./instructions/instruction_mid.png")
instr_end = visual.ImageStim(win, image="./instructions/instruction_end.png")


instr_1.draw()
win.flip()
event.waitKeys(keyList=['space'])#if pt presses space --> start exp
win.flip()
instr_2.draw()
win.flip()
event.waitKeys(keyList=['space'])#if pt presses space --> start exp
win.flip()
instr_3.play()
instr_timer = core.Clock()
while instr_timer.getTime() < 16:
    instr_3.draw()
    win.flip()
    if event.getKeys(keyList=['space']):
        break
# Stop the movie playback
instr_3.stop()
#if pt presses space --> start exp
win.flip()
instr_4.draw()
win.flip()
event.waitKeys(keyList=['space'])#if pt presses space --> start exp
horizon.autoDraw = True
red_pill.autoDraw = True
blue_pill.autoDraw = True
    

training = True

# Training block loop
for i in range(training_trial):
    out_dict['pt_num'].append(int(pt_num[0]))
    out_dict['Age'].append(pt_num[1])
    out_dict['Gender'].append(pt_num[2])
    out_dict['Handedness'].append(pt_num[3])
    out_dict['trial_nbr'].append(i + 1)
    out_dict['block_number'].append("Training")
    out_dict['c_value'].append(round(training_df['c_value'].iloc[i],3))
    mouse_positions = []
    trajectory_timestamp = []
    traj_stim_on = []
    shown = False

    # Reset the mouse position and variables for each trial
    core.wait(0.1)
    fixation.draw()
    mouse.setPos((0, -450))
    win.flip()
    trial_timing = core.Clock()
    while -1:
        if event.getKeys(keyList=["escape"]):
            win.close()
            core.quit()    
        x, y = mouse.getPos()
        mouse_positions.append((int(mouse.getPos()[0]),int(mouse.getPos()[1])))
        trajectory_timestamp.append(trial_timing.getTime())
        core.wait(0.001)

        if y > onset_point and not shown:
            fixation.draw()
            for j, circle in enumerate(circles, start=1):
                circle.color = training_df[f'RGB_{j}'].iloc[i]
                circle.draw(win)
            win.flip()
            rt = core.Clock()
            start_time = core.Clock()
            while start_time.getTime() < stim_duration: # Record start time of the loop
                core.wait(0.001)
                mouse_positions.append((int(mouse.getPos()[0]),int(mouse.getPos()[1])))
                trajectory_timestamp.append(trial_timing.getTime())
                traj_stim_on.append(mouse_positions[-1])
                
            win.flip()
            shown = True
            #rt = core.Clock() was here before
            if shown == True:
                trial_duration = core.Clock()
                
        if shown == True:
            if trial_duration.getTime() >= 5:
                out_dict['rt'].append("NAN")
                choice = "NAN"
                out_dict["choice"].append('NAN')
                out_dict['true_value'].append(training_df["Stimulus Color"].iloc[i])
                out_dict["difficulty"].append(training_df["Condition"].iloc[i])
                out_dict['acc'].append('NAN')
                out_dict['traj_record'].append(mouse_positions)
                out_dict['traj_timestamp'].append(trajectory_timestamp)
                out_dict['stim_traj'].append(traj_stim_on)
                break
        # Stop the trial when red pill boundary is reached
        
        if y >= 390 and x >= 810:
            out_dict['rt'].append(rt.getTime())
            choice = "Red"
            out_dict["choice"].append('Red')
            out_dict['true_value'].append(training_df["Stimulus Color"].iloc[i])
            out_dict["difficulty"].append(training_df["Condition"].iloc[i])
            out_dict['traj_timestamp'].append(trajectory_timestamp)
            out_dict['stim_traj'].append(traj_stim_on)

            if training_df["Stimulus Color"].iloc[i] == choice:
                out_dict['acc'].append(True)
            else:
                out_dict['acc'].append(False)

            out_dict["traj_record"].append(mouse_positions)

            if training:
                feedback_text = correct_answer if choice == training_df["Stimulus Color"].iloc[i] else incorrect_answer
                win.flip()
                feedback_text.draw(win)
                win.flip()
                core.wait(0.5)

            shown = False
            returned = False
            while not returned:
                return_square.draw()
                win.flip()
                x, y = mouse.getPos()
                if -15 <= x <= 15 and -465 <= y <= -435:
                    returned = True
            break

        # Stop the trial when blue pill boundary is reached
        elif y >= 390 and x <= -810:
            out_dict['rt'].append(rt.getTime())
            choice = "Blue"
            out_dict["choice"].append("Blue")
            out_dict['true_value'].append(training_df["Stimulus Color"].iloc[i])
            out_dict["difficulty"].append(training_df["Condition"].iloc[i])
            out_dict['traj_timestamp'].append(trajectory_timestamp)
            out_dict['stim_traj'].append(traj_stim_on)

            if training_df["Stimulus Color"].iloc[i] == choice:
                out_dict['acc'].append(True)
            else:
                out_dict['acc'].append(False)

            out_dict["traj_record"].append(mouse_positions)
        
            if training:
                feedback_text = correct_answer if choice == training_df["Stimulus Color"].iloc[i] else incorrect_answer
                win.flip()
                feedback_text.draw(win)
                win.flip()
                core.wait(0.5)
            shown = False
            returned = False
            while not returned:
                return_square.draw()
                win.flip()
                x, y = mouse.getPos()
                if -15 <= x <= 15 and -465 <= y <= -435:
                    returned = True
            break
    out_dict['Experiment Duration'].append(overall_time.getTime()) 
    
horizon.autoDraw = False
training = False
if training == False:
    instr_trn_to_exp.draw()
    block_RT = round((sum(out_dict['rt']) / len(out_dict['rt'])),2)
    block_acc = round((out_dict['acc'].count(True) / (len(out_dict['acc']) - out_dict['acc'].count('Control') - out_dict['acc'].count('NAN'))),2)
    b_rt = visual.TextStim(win, text = str(block_RT), pos = (0, -200), color= (0,0,0), colorSpace='rgb255')
    b_acc = visual.TextStim(win, text = str(block_acc), pos = (0, -80), color= (0,0,0), colorSpace='rgb255')
    b_rt.setSize(42)
    b_acc.setSize(42)
    b_rt.draw()
    b_acc.draw()
    win.flip()
    event.waitKeys(keyList=["escape", 'space'])
    
# Main experiment loop
for i in range(max_trial):
    out_dict['pt_num'].append(int(pt_num[0]))
    out_dict['Age'].append(pt_num[1])
    out_dict['Gender'].append(pt_num[2])
    out_dict['Handedness'].append(pt_num[3])
    out_dict['c_value'].append(round(experiment_df['c_value'].iloc[i],3))

    if event.getKeys(keyList=["escape"]):
        win.close()
        core.quit()

    # Determine block number
    block_percentage = (i + 1) / max_trial
    block_number = f"Block {math.ceil(block_percentage * 10)}"
    out_dict['block_number'].append(block_number)

    # Display block number
    b_num = visual.TextStim(win, text=str(math.ceil(block_percentage * 10)), pos=(100, 165), color=(0, 0, 0), colorSpace='rgb255', bold=True)
    b_num.setSize(42)

    if math.isclose(block_percentage, 0.1) or math.isclose(block_percentage, 0.2) or math.isclose(block_percentage, 0.3) \
            or math.isclose(block_percentage, 0.4) or math.isclose(block_percentage, 0.5) \
            or math.isclose(block_percentage, 0.6) or math.isclose(block_percentage, 0.7) \
            or math.isclose(block_percentage, 0.8) or math.isclose(block_percentage, 0.9):
        instr_mid.draw()
        block_RT = round((sum(out_dict['rt']) / len(out_dict['rt'])), 2)
        block_acc = round((out_dict['acc'].count(True) / (len(out_dict['acc']) - out_dict['acc'].count('Control') - out_dict['acc'].count('NAN'))),2)
        b_rt = visual.TextStim(win, text=str(block_RT), pos=(0, -250), color=(0, 0, 0), colorSpace='rgb255')
        b_acc = visual.TextStim(win, text=str(block_acc), pos=(0, -90), color=(0, 0, 0), colorSpace='rgb255')
        b_rt.setSize(42)
        b_acc.setSize(42)
        b_num.setSize(42)
        b_num.draw()
        b_rt.draw()
        b_acc.draw()
        win.flip()
        event.waitKeys(keyList=["escape", 'space'])

    # Set up trial
    out_dict['trial_nbr'].append(i + 1)
    mouse_positions = []
    traj_stim_on = []
    trajectory_timestamp = []
    shown = False

    # Reset the mouse position and variables for each trial
    core.wait(0.1)
    fixation.draw()
    mouse.setPos((0, -450))
    win.flip()

    while -1:
        if event.getKeys(keyList=["escape"]):
            win.close()
            core.quit()

        x, y = mouse.getPos()
        mouse_positions.append((int(mouse.getPos()[0]),int(mouse.getPos()[1])))
        trajectory_timestamp.append(trial_timing.getTime())
        core.wait(0.001)

        if y > onset_point and not shown:
            fixation.draw()
            for j, circle in enumerate(circles, start=1):
                circle.color = experiment_df[f'RGB_{j}'].iloc[i]
                circle.draw(win)
            win.flip()

            start_time = core.Clock()
            while start_time.getTime() < stim_duration:
                core.wait(0.001)
                mouse_positions.append((int(mouse.getPos()[0]),int(mouse.getPos()[1])))
                trajectory_timestamp.append(trial_timing.getTime())
                traj_stim_on.append(mouse_positions[-1])
            win.flip()
            shown = True
            rt = core.Clock()
            if shown == True:
                trial_duration = core.Clock()
                
        if shown == True:
            if trial_duration.getTime() >= 5:
                out_dict['rt'].append("NAN")
                choice = "NAN"
                out_dict["choice"].append('NAN')
                out_dict['true_value'].append(experiment_df["Stimulus Color"].iloc[i])
                out_dict["difficulty"].append(experiment_df["Condition"].iloc[i])
                out_dict['acc'].append('NAN')
                out_dict['traj_record'].append(mouse_positions)
                out_dict['traj_timestamp'].append(trajectory_timestamp)
                out_dict['stim_traj'].append(traj_stim_on)
                break
        # Stop the trial when red pill boundary is reached
        if y >= 390 and x >= 810:
            out_dict['rt'].append(rt.getTime())
            choice = "Red"
            out_dict["choice"].append('Red')
            out_dict['true_value'].append(experiment_df["Stimulus Color"].iloc[i])
            out_dict["difficulty"].append(experiment_df["Condition"].iloc[i])
            out_dict['traj_timestamp'].append(trajectory_timestamp)
            out_dict['stim_traj'].append(traj_stim_on)

            if experiment_df["Stimulus Color"].iloc[i] == choice:
                out_dict['acc'].append(True)
            elif experiment_df["Stimulus Color"].iloc[i] == "Control":
                out_dict['acc'].append("Control")
            else:
                out_dict['acc'].append(False)

            out_dict["traj_record"].append(mouse_positions)

            shown = False
            returned = False
            while not returned:
                return_square.draw()
                win.flip()
                x, y = mouse.getPos()
                if -15 <= x <= 15 and -465 <= y <= -435:
                    returned = True
            break

        # Stop the trial when blue pill boundary is reached
        elif y >= 390 and x <= -810:
            out_dict['rt'].append(rt.getTime())
            choice = "Blue"
            out_dict["choice"].append("Blue")
            out_dict['true_value'].append(experiment_df["Stimulus Color"].iloc[i])
            out_dict["difficulty"].append(experiment_df["Condition"].iloc[i])
            out_dict['traj_timestamp'].append(trajectory_timestamp)
            out_dict['stim_traj'].append(traj_stim_on)

            if experiment_df["Stimulus Color"].iloc[i] == choice:
                out_dict['acc'].append(True)
            elif experiment_df["Stimulus Color"].iloc[i] == "Control":
                out_dict['acc'].append("Control")
            else:
                out_dict['acc'].append(False)

            out_dict["traj_record"].append(mouse_positions)

            shown = False
            returned = False
            while not returned:
                return_square.draw()
                win.flip()
                x, y = mouse.getPos()
                if -15 <= x <= 15 and -465 <= y <= -435:
                    returned = True
            break

    out_dict['Experiment Duration'].append(overall_time.getTime())

instr_end.draw(win)
win.flip()
event.waitKeys(keyList=['space'])
win.close()

# Data Output
out_df = pd.DataFrame.from_dict(out_dict)
out_df.to_excel(f'./data/results_{pt_num[0]}.xlsx', index=False)
experiment_df.to_excel(f'./data/input_dataset_{pt_num[0]}.xlsx')

# Quit
core.quit()

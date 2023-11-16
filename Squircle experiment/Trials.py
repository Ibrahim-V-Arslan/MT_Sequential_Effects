# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:12:02 2023

@author: veoni
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:00:20 2023

@author: veoni
"""
import os, sys, webbrowser
set_wd = os.chdir("C://Users//veoni//Desktop//DesenderLab//Mouse Tracking//Squircle experiment//")
import random
import numpy as np
from psychopy import visual, core, event, gui
import pandas as pd
from psychopy.event import Mouse
from Pseudorand import m_range
from csv_creator import experiment_df, training_df, training_trial, max_trial
import math


WIDTH = 1920
HEIGHT  = 1080
onset_point = -108
#max_trial = 500
clock = core.Clock()
stim_duration = 0.2
overall_time = core.Clock()
variables = [
    'pt_num', # participant number
    'Age', # Age of the participant
    'Gender', # Gender
    'Handedness', #Preferred Hand
    'trial_nbr', # trial number
    'block_number', # Block Number
    'traj_record', # trajectory of the mouse
    'rt', # reaction time
    'acc', # accuracy
    'choice', #what is chosen 
    'true_value',# what is true value
    'difficulty', # level of manipulation (easy/medium/hard)
    'Experiment Duration', # overall duration
]



# create an empty dict for output
out_dict = {}
for variable in variables:
    out_dict[variable] = []

win = visual.Window(size = (WIDTH,HEIGHT), units = ('pix'), fullscr = False, color = (100,100,100), colorSpace='rgb255')
win.mouseVisible = True
#create fixation cross
fixation = visual.TextStim(win, text = "+", height=(52), color ="black", pos = (0,270))

#instr_mid = visual.ImageStim(win, image = "./instructions/mid.png")
#instr_end = visual.ImageStim(win, image= "./instructions/End.png")

correct_answer = visual.TextStim(win, text="Good", color = (-1, 1, -1), colorSpace = 'rgb', bold = True, height = 26)
incorrect_answer = visual.TextStim(win, text="Wrong", color = (1.0, -1, -1), colorSpace = 'rgb', bold = True, height = 26)
control_answer = visual.TextStim(win, text="Control", color = "yellow", colorSpace = 'rgb', bold = True, height = 26)

choice = "" # it is for recording the current selection and compare it with the stimuli
#GUI screen to collect participant number  
# myDlg = gui.Dlg(title="Object Recognition Task")
# myDlg.addField('Participant Number')
# myDlg.addField('Age:')
# myDlg.addField('Gender:',choices=["Male", "Female", "Other"])
# myDlg.addField('Preferred Hand', choices = ["Right", "Left"])
# pt_num = myDlg.show()  # show dialog and wait for OK or Cancel
# if myDlg.OK:  # if ok_data is not None
#     if pt_num[0].isdigit():
#         print(pt_num)
#     else: #error + close system if pt number is not a digit
#         print("ERROR!!! this is not a digit\n")
#         sys.exit()
# else:
#     sys.exit()

#move the stimuli upwards and make it smaller

MOVEMENT_RADIUS = 150
N_CIRCLES = 8

# Set the starting y-coordinate to 270
start_y = 320

angles = [(i * (360 / N_CIRCLES)) for i in range(N_CIRCLES)]  # get list of angles

# Adjust the initial y-coordinate for each circle
positions = [(MOVEMENT_RADIUS * math.cos(math.radians(angle)),
               MOVEMENT_RADIUS * math.sin(math.radians(angle)) + start_y) for angle in angles]


c1 = visual.Circle(win, units = "pix", size = (60), colorSpace = "rgb255", pos = positions[0], fillColor = training_df['RGB_1'].iloc[0])
c2 = visual.Circle(win, units = "pix", size = (60), colorSpace = "rgb255", pos = positions[1], fillColor = training_df['RGB_2'].iloc[0])
c3 = visual.Circle(win, units = "pix", size = (60), colorSpace = "rgb255", pos = positions[2], fillColor = training_df['RGB_3'].iloc[0])
c4 = visual.Circle(win, units = "pix", size = (60), colorSpace = "rgb255", pos = positions[3], fillColor = training_df['RGB_4'].iloc[0])
c5 = visual.Circle(win, units = "pix", size = (60), colorSpace = "rgb255", pos = positions[4], fillColor = training_df['RGB_5'].iloc[0])
c6 = visual.Circle(win, units = "pix", size = (60), colorSpace = "rgb255", pos = positions[5], fillColor = training_df['RGB_6'].iloc[0])
c7 = visual.Circle(win, units = "pix", size = (60), colorSpace = "rgb255", pos = positions[6], fillColor = training_df['RGB_7'].iloc[0])
c8 = visual.Circle(win, units = "pix", size = (60), colorSpace = "rgb255", pos = positions[7], fillColor = training_df['RGB_8'].iloc[0])
#find alternative for pixel coding
#Option Boxes they should be bigger
red_pill = visual.Rect(win, width= 150, height=150, fillColor ="red", pos = (885,465), autoDraw = False)
blue_pill = visual.Rect(win, width= 150, height=150, fillColor ="blue", pos = (-885,465), autoDraw = False)
#training Lines
horizon = visual.Line(win,start = (-960,-108), end = (960,-108), lineColor = 'black', autoDraw = False)
win.flip()


mouse = Mouse()

lower_limit = -108
mouse.setVisible(True)

instr_1 = visual.ImageStim(win, image= "./instructions/Instruction1.png")
instr_2 = visual.ImageStim(win, image = "./instructions/Instruction2.png")


instr_1.draw()
win.flip()
if event.waitKeys(keyList=['space']):#if pt presses space --> start exp
    win.flip()
    instr_2.draw()
    win.flip()
    
if event.waitKeys(keyList=['space']):#if pt presses space --> start exp
    win.flip()
    horizon.autoDraw = True
    red_pill.autoDraw = True
    blue_pill.autoDraw = True
    

training = True

# Main experiment loop
#n trials
for i in range(training_trial):
    out_dict['trial_nbr'].append(i+1)
    mouse_positions = []
    shown = False
    # Reset the mouse position and variables for each trial
    #almost all numeric values to variable names
    core.wait(0.2)
    fixation.draw()
    mouse.setPos((0, -450))
    win.flip()
    while -1:
        
        if event.getKeys(keyList=["escape"]):
                win.close()
                core.quit()
        x,y = mouse.getPos()
        
        mouse_positions.append(mouse.getPos())
        core.wait(0.001)
        
        if y > -108 and shown == False:
            fixation.draw()
            c1.color = (training_df['RGB_1'].iloc[i])
            c1.draw(win)
            
            c2.color = (training_df['RGB_2'].iloc[i])
            c2.draw(win)
            
            c3.color = (training_df['RGB_3'].iloc[i])
            c3.draw(win)
            
            c4.color = (training_df['RGB_4'].iloc[i])
            c4.draw(win)
            
            c5.color = (training_df['RGB_5'].iloc[i])
            c5.draw(win)
            
            c6.color = (training_df['RGB_6'].iloc[i])
            c6.draw(win)
            
            c7.color = (training_df['RGB_7'].iloc[i])
            c7.draw(win)
            
            c8.color = (training_df['RGB_8'].iloc[i])
            c8.draw(win)
            
            win.flip()

            start_time = core.Clock()
            while start_time.getTime() < .2:
                core.wait(0.001)
                mouse_positions.append(mouse.getPos())
            win.flip()
            shown = True
            rt = core.Clock()
        # Stop the experiment when red pill boundary is reached
        if y >= 390 and x >= 810:
            out_dict['rt'].append(rt.getTime())
            choice = "Red"
            out_dict["choice"].append('Red')
            out_dict['true_value'].append(training_df["Stimulus Color"].iloc[i])
            out_dict["traj_record"].append(mouse_positions)
            out_dict["block_number"].append("Training")
            if training == True:
                
                if choice == training_df["Stimulus Color"].iloc[i]:
                    win.flip()
                    correct_answer.draw(win) #draw the feedback 
                    win.flip()
                    core.wait(0.5)
                elif choice != training_df["Stimulus Color"].iloc[i]:
                    win.flip()
                    incorrect_answer.draw(win) #draw the feedback 
                    win.flip()
                    core.wait(0.5)
                out_dict["difficulty"].append(training_df["Condition"].iloc[i])
            shown = False
            break
        
        # Stop the experiment when blue pill boundary is reached
        elif y >= 390 and x <= -810:
            out_dict['rt'].append(rt.getTime())
            choice = "Blue"
            out_dict["choice"].append("Blue")
            out_dict['true_value'].append(training_df["Stimulus Color"].iloc[i])
            out_dict["traj_record"].append(mouse_positions)
            out_dict["block_number"].append("Training")
            if training == True:
                
                if choice == training_df["Stimulus Color"].iloc[i]:
                    win.flip()
                    correct_answer.draw(win) #draw the feedback 
                    win.flip()
                    core.wait(0.5)
                elif choice != training_df["Stimulus Color"].iloc[i]:
                    win.flip()
                    incorrect_answer.draw(win) #draw the feedback 
                    win.flip()
                    core.wait(0.5)
                out_dict["difficulty"].append(training_df["Condition"].iloc[i])
                    
            shown = False
            break
        
        
    out_dict['Experiment Duration'].append(overall_time.getTime())

#NOW THE EXPERIMENT
for i in range(max_trial):
    out_dict['trial_nbr'].append(i+1)
    mouse_positions = []
    shown = False
    # Reset the mouse position and variables for each trial
    #almost all numeric values to variable names
    core.wait(0.2)
    fixation.draw()
    mouse.setPos((0, -450))
    win.flip()
    while -1:
        
        if event.getKeys(keyList=["escape"]):
                win.close()
                core.quit()
        x,y = mouse.getPos()
        
        mouse_positions.append(mouse.getPos())
        core.wait(0.001)
        
        if y > -108 and shown == False:
            fixation.draw()
            c1.color = (training_df['RGB_1'].iloc[i])
            c1.draw(win)
            
            c2.color = (training_df['RGB_2'].iloc[i])
            c2.draw(win)
            
            c3.color = (training_df['RGB_3'].iloc[i])
            c3.draw(win)
            
            c4.color = (training_df['RGB_4'].iloc[i])
            c4.draw(win)
            
            c5.color = (training_df['RGB_5'].iloc[i])
            c5.draw(win)
            
            c6.color = (training_df['RGB_6'].iloc[i])
            c6.draw(win)
            
            c7.color = (training_df['RGB_7'].iloc[i])
            c7.draw(win)
            
            c8.color = (training_df['RGB_8'].iloc[i])
            c8.draw(win)
            
            win.flip()

            start_time = core.Clock()
            while start_time.getTime() < .2:
                core.wait(0.001)
                mouse_positions.append(mouse.getPos())
            win.flip()
            shown = True
            rt = core.Clock()
        # Stop the experiment when red pill boundary is reached
        if y >= 390 and x >= 810:
            out_dict['rt'].append(rt.getTime())
            choice = "Red"
            out_dict["choice"].append('Red')
            out_dict['true_value'].append(training_df["Stimulus Color"].iloc[i])
            out_dict["traj_record"].append(mouse_positions)
            out_dict["block_number"].append("Training")
            if training == True:
                
                if choice == training_df["Stimulus Color"].iloc[i]:
                    win.flip()
                    correct_answer.draw(win) #draw the feedback 
                    win.flip()
                    core.wait(0.5)
                elif choice != training_df["Stimulus Color"].iloc[i]:
                    win.flip()
                    incorrect_answer.draw(win) #draw the feedback 
                    win.flip()
                    core.wait(0.5)
                out_dict["difficulty"].append(training_df["Condition"].iloc[i])
            shown = False
            break
        
        # Stop the experiment when blue pill boundary is reached
        elif y >= 390 and x <= -810:
            out_dict['rt'].append(rt.getTime())
            choice = "Blue"
            out_dict["choice"].append("Blue")
            out_dict['true_value'].append(training_df["Stimulus Color"].iloc[i])
            out_dict["traj_record"].append(mouse_positions)
            out_dict["block_number"].append("Training")
            if training == True:
                
                if choice == training_df["Stimulus Color"].iloc[i]:
                    win.flip()
                    correct_answer.draw(win) #draw the feedback 
                    win.flip()
                    core.wait(0.5)
                elif choice != training_df["Stimulus Color"].iloc[i]:
                    win.flip()
                    incorrect_answer.draw(win) #draw the feedback 
                    win.flip()
                    core.wait(0.5)
                out_dict["difficulty"].append(training_df["Condition"].iloc[i])
                    
            shown = False
            break
        
        
    out_dict['Experiment Duration'].append(overall_time.getTime())

# Close the window
win.close()

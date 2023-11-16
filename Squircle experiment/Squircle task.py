# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:00:20 2023

@author: veoni
"""

import random
import numpy as np
from psychopy import visual, core, event, gui
import os, sys, webbrowser
import pandas as pd
from psychopy.event import Mouse


WIDTH = 1920
HEIGHT  = 1080
onset_point = -108
max_trial = 500
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
#circle_color = ((0.54, 0, 0.46)*255)
circle_color = (148, 0, 211)
#move the stimuli upwards and make it smaller
#psychopy fill.color things check on that
c1 = visual.Circle(win, units = "pix", size = (70), lineColor = "#9932CC",pos = (0,445), fillColor = "#9932CC")
c2 = visual.Circle(win, units = "pix", size = (70), lineColor = '#4B0082',pos = (125,395), fillColor = "#4B0082")
c3 = visual.Circle(win, units = "pix", size = (70), lineColor = '#191970',pos = (175,270), fillColor = "#191970")
c4 = visual.Circle(win, units = "pix", size = (70), lineColor = '#6A5ACD',pos = (125,145), fillColor = "#6A5ACD")
c5 = visual.Circle(win, units = "pix", size = (70), lineColor = '#800080',pos = (0,95), fillColor = "#800080")
c6 = visual.Circle(win, units = "pix", size = (70), lineColor = '#8A2BE2',pos = (-125,145), fillColor = "#8A2BE2")
c7 = visual.Circle(win, units = "pix", size = (70), lineColor = '#DA70D6',pos = (-175,270), fillColor = "#DA70D6")
c8 = visual.Circle(win, units = "pix", size = (70), lineColor = '#BA55D3',pos = (-125,395), fillColor = "#BA55D3")

#find alternative for pixel coding
#Option Boxes they should be bigger
red_pill = visual.Rect(win, width= 150, height=150, fillColor ="red", pos = (885,465), autoDraw = True)
blue_pill = visual.Rect(win, width= 150, height=150, fillColor ="blue", pos = (-885,465), autoDraw = True)
#training Lines
horizon = visual.Line(win,start = (-960,-108), end = (960,-108), lineColor = 'black', autoDraw = True)
win.flip()


mouse = Mouse()

lower_limit = -108
mouse.setVisible(True)


# ... (previous code)

# ... (previous code)

# Main experiment loop
#n trials
for i in range(max_trial):
    out_dict['trial_nbr'].append(i)
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
            # Get current mouse position
            #x,y = mouse.getPos()        
            #save from the beginning
            #mouse_positions.append(mouse.getPos())
            #x,y = mouse.getPos()
            # Check if y-coordinate is below the lower limit        
        mouse_positions.append(mouse.getPos())
        
        if y > -108 and shown == False:
            fixation.draw()
            c1.draw(win)
            c2.draw(win)
            c3.draw(win)
            c4.draw(win)
            c5.draw(win)
            c6.draw(win)
            c7.draw(win)
            c8.draw(win)
            win.flip()
            rt = core.Clock()
            #core.wait(0.2)
            start_time = core.Clock()
            while start_time.getTime() <= stim_duration:
                ms_pos = []
                ms_pos.append(mouse.getPos())
                mouse_positions + ms_pos
            #this should not be core wait it should be timer
            win.flip()
            shown = True
        
        # Stop the experiment when red pill boundary is reached
        if y >= 390 and x >= 810:
            out_dict['rt'].append(rt.getTime())
            out_dict["choice"].append('red')
            out_dict["traj_record"].append(mouse_positions)
            #mouse.setPos((0, -450))
            #7lines below should be gone
            shown = False
            break
        
        # Stop the experiment when blue pill boundary is reached
        elif y >= 390 and x <= -810:
            out_dict['rt'].append(rt.getTime())
            out_dict["choice"].append("blue")
            out_dict["traj_record"].append(mouse_positions)
            shown = False
            break
    out_dict['Experiment Duration'].append(overall_time.getTime())


# Close the window
win.close()

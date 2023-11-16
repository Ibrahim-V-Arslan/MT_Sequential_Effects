# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:48:42 2023

@author: laran
"""

from psychopy import core, visual, event
import math

CIRCLE_SIZE = 10
MOVEMENT_RADIUS = 120
N_CIRCLES = 10
SWITCH_TIME = 0.1

angles = [(i*(360/N_CIRCLES)) for i in range(N_CIRCLES)] # get list of angles

positions = [(MOVEMENT_RADIUS * math.cos(math.radians(angle)), MOVEMENT_RADIUS * math.sin(math.radians(angle))) for angle in angles]

# set up window
win = visual.Window(size = (800,600), units = 'pix') # if you use normalized coordinates the left will be -1 and right 1 (no matter how big or small the screen is)

fixation_cross = visual.TextStim(win, text='+', color='white')
fixation_cross.draw()
fixation_cross.autoDraw = True

circles = []

for position in positions:
    circle = visual.Circle(win, pos = position, radius = CIRCLE_SIZE, fillColor = '#AA3366')
    circles.append(circle)
    circle.autoDraw = True

for circle in circles:
    circle.draw()
 
win.flip()

i = 0

while True:
    
    core.wait(SWITCH_TIME)
    circles[i].fillColor = 'grey'
    circles[i].draw()
    win.flip()
    
    core.wait(SWITCH_TIME)
    circles[i].fillColor = '#AA3366'
    circles[i].draw()
    win.flip()      
    
    if i == (N_CIRCLES - 1):
        i = 0
    else:
        i += 1
    
    key_pressed = event.getKeys(keyList = ['escape'])
    
    if 'escape' in key_pressed:
        break

# close window
win.close()

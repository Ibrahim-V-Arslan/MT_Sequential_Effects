# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:45:01 2023

@author: veoni
"""

from psychopy import visual, event, core


# Initialize window, stimulus, and clock
win = visual.Window(size = (1920,1080), units = ('pix'), fullscr = False, color = (100,100,100), colorSpace='rgb255')
mouse = event.Mouse()
ms_po = []
while -1:
    core.wait(0.001)
    x,y = mouse.getPos()
    ms_po.append((x,y))
    print(mouse.getPos())

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:35:01 2023

@author: veoni
"""



import pandas as pd
from pseudo_color import mypseudorandrange
#from Trials import max_trial
training_trial = 4
max_trial = 16

#First creating input csv for EXPERIMENT

#Control Condition Generator
training_control_values = mypseudorandrange(.5, .1, 8, .001, .001, .1, .9, int(max_trial//4))

# For Blue you will do 1 - value above 

#Easy Condition Generator
training_easy_red_values = mypseudorandrange(.545, .1, 8, .001, .001, .1, .9, int(max_trial/4))

# For Blue you will do 1 - value above 

#Medium Condition Generator
training_medium_red_values = mypseudorandrange(.53, .1, 8, .001, .001, .1, .9, int(max_trial/4))

# For Blue you will do 1 - value above 

#Hard Condition Generator
training_hard_red_values = mypseudorandrange(.52, .1, 8, .001, .001, .1, .9, int(max_trial/4))

# For Blue you will do 1 - value above 


control = []
circle_1 = []
circle_2 = []
circle_3 = []
circle_4 = []
circle_5 = []
circle_6 = []
circle_7 = []
circle_8 = []
for z in range((max_trial//4)):
    
    circle_1.append(training_control_values[z][0])
    circle_2.append(training_control_values[z][1])
    circle_3.append(training_control_values[z][2])
    circle_4.append(training_control_values[z][3])
    circle_5.append(training_control_values[z][4])
    circle_6.append(training_control_values[z][5])
    circle_7.append(training_control_values[z][6])
    circle_8.append(training_control_values[z][7])
for z in range((max_trial//4)):    
    circle_1.append(training_easy_red_values[z][0])
    circle_2.append(training_easy_red_values[z][1])
    circle_3.append(training_easy_red_values[z][2])
    circle_4.append(training_easy_red_values[z][3])
    circle_5.append(training_easy_red_values[z][4])
    circle_6.append(training_easy_red_values[z][5])
    circle_7.append(training_easy_red_values[z][6])
    circle_8.append(training_easy_red_values[z][7])
for z in range((max_trial//4)):    
    circle_1.append(training_medium_red_values[z][0])
    circle_2.append(training_medium_red_values[z][1])
    circle_3.append(training_medium_red_values[z][2])
    circle_4.append(training_medium_red_values[z][3])
    circle_5.append(training_medium_red_values[z][4])
    circle_6.append(training_medium_red_values[z][5])
    circle_7.append(training_medium_red_values[z][6])
    circle_8.append(training_medium_red_values[z][7])
for z in range((max_trial//4)):    
    circle_1.append(training_hard_red_values[z][0])
    circle_2.append(training_hard_red_values[z][1])
    circle_3.append(training_hard_red_values[z][2])
    circle_4.append(training_hard_red_values[z][3])
    circle_5.append(training_hard_red_values[z][4])
    circle_6.append(training_hard_red_values[z][5])
    circle_7.append(training_hard_red_values[z][6])
    circle_8.append(training_hard_red_values[z][7])
    

experiment_df = pd.DataFrame(list(zip(circle_1, circle_2, circle_3, circle_4, circle_5, circle_6, circle_7, circle_8)), columns = ["Circle_1", "Circle_2", "Circle_3",
                                                                                                                                 "Circle_4", "Circle_5", "Circle_6",
                                                                                                                                 "Circle_7","Circle_8",])

condition = []

for i in range(max_trial+1):
    if i <(max_trial//4):
        condition.append("Control")
    elif i > (max_trial//4) and i <=((max_trial//4)*2):
        condition.append("Easy")
    elif i > ((max_trial//4)*2) and i <=((max_trial//4)*3):
        condition.append("Medium")
    elif i > ((max_trial//4)*3) and i <=(max_trial+1):
        condition.append("Hard")

experiment_df["Condition"] = condition
        
stim_color = []

for i in range(max_trial+1):
    if i < (max_trial//4):
        stim_color.append("Control")
    elif i > (max_trial//4) and i <= ((max_trial//4) + ((max_trial//4)//2)):
        stim_color.append("Red")
    elif i > ((max_trial//4) + ((max_trial//4)//2)) and i <= ((max_trial//4)*2):
        stim_color.append("Blue")
    elif i > ((max_trial//4)*2) and i <=(((max_trial//4)*2) + ((max_trial//4)//2)):
        stim_color.append("Red")
    elif i > (((max_trial//4)*2) + ((max_trial//4)//2)) and i <=((max_trial//4)*3):
        stim_color.append("Blue")
    elif i > ((max_trial//4)*3) and i <=(((max_trial//4)*3) + ((max_trial//4)//2)):
        stim_color.append("Red")
    elif i > (((max_trial//4)*3) + ((max_trial//4)//2)) and i <=(max_trial+1):
        stim_color.append("Blue")
   
experiment_df["Stimulus Color"] = stim_color

#df = df.reindex(columns=['C', 'B', 'A', 'D'])

rgb_1 = []
g = 0
xy = 0
for i in experiment_df["Circle_1"]:
    if experiment_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_1.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_1.append((r,g,b))
        print('blue')
        xy+=1
        
rgb_2 = []
g = 0
xy = 0
for i in experiment_df["Circle_2"]:
    if experiment_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_2.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_2.append((r,g,b))
        print('blue')
        xy+=1

rgb_3 = []
g = 0
xy = 0
for i in experiment_df["Circle_3"]:
    if experiment_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_3.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_3.append((r,g,b))
        print('blue')
        xy+=1


rgb_4 = []
g = 0
xy = 0
for i in experiment_df["Circle_4"]:
    if experiment_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_4.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_4.append((r,g,b))
        print('blue')
        xy+=1

rgb_5 = []
g = 0
xy = 0
for i in experiment_df["Circle_5"]:
    if experiment_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_5.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_5.append((r,g,b))
        print('blue')
        xy+=1


rgb_6 = []
g = 0
xy = 0
for i in experiment_df["Circle_6"]:
    if experiment_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_6.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_6.append((r,g,b))
        print('blue')
        xy+=1
        
rgb_7 = []
g = 0
xy = 0
for i in experiment_df["Circle_7"]:
    if experiment_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_7.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_7.append((r,g,b))
        print('blue')
        xy+=1
        
rgb_8 = []
g = 0
xy = 0
for i in experiment_df["Circle_8"]:
    if experiment_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_8.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_8.append((r,g,b))
        print('blue')
        xy+=1
experiment_df["RGB_1"] = rgb_1
experiment_df["RGB_2"] = rgb_2
experiment_df["RGB_3"] = rgb_3
experiment_df["RGB_4"] = rgb_4
experiment_df["RGB_5"] = rgb_5
experiment_df["RGB_6"] = rgb_6
experiment_df["RGB_7"] = rgb_7
experiment_df["RGB_8"] = rgb_8

c_value = []
for i in range(len(experiment_df)):
    if experiment_df["Stimulus Color"].iloc[i] == "Control":
        c_value.append(.5)
    elif experiment_df["Stimulus Color"].iloc[i] == "Red":
        if experiment_df["Condition"].iloc[i] == "Easy":
            c_value.append(.545)
        elif experiment_df["Condition"].iloc[i] == "Medium":
            c_value.append(.530)
        elif experiment_df["Condition"].iloc[i] == "Hard":
            c_value.append(.52)
    elif experiment_df["Stimulus Color"].iloc[i] == "Blue":
        if experiment_df["Condition"].iloc[i] == "Easy":
            c_value.append((1-.545))
        elif experiment_df["Condition"].iloc[i] == "Medium":
            c_value.append((1-.530))
        elif experiment_df["Condition"].iloc[i] == "Hard":
            c_value.append((1-.52))
experiment_df["c_value"] = c_value
experiment_df = experiment_df.sample(frac = 1)
#experiment_df.to_excel("Input_dataset.xlsx")


    
    




#NOW DOING THE SAME THING FOR TRAINING TRIALS



# For Blue you will do 1 - value above 

#Easy Condition Generator
training_easy_red_values = mypseudorandrange(.545, .1, 8, .001, .001, .1, .9, int(training_trial/2))

# For Blue you will do 1 - value above 

#Medium Condition Generator
training_medium_red_values = mypseudorandrange(.530, .1, 8, .001, .001, .1, .9, int(training_trial/2))

# For Blue you will do 1 - value above 



# For Blue you will do 1 - value above 


control = []
circle_1 = []
circle_2 = []
circle_3 = []
circle_4 = []
circle_5 = []
circle_6 = []
circle_7 = []
circle_8 = []
for z in range((training_trial//2)):
    

    
    circle_1.append(training_easy_red_values[z][0])
    circle_2.append(training_easy_red_values[z][1])
    circle_3.append(training_easy_red_values[z][2])
    circle_4.append(training_easy_red_values[z][3])
    circle_5.append(training_easy_red_values[z][4])
    circle_6.append(training_easy_red_values[z][5])
    circle_7.append(training_easy_red_values[z][6])
    circle_8.append(training_easy_red_values[z][7])
for z in range((training_trial//2)):    
    circle_1.append(training_medium_red_values[z][0])
    circle_2.append(training_medium_red_values[z][1])
    circle_3.append(training_medium_red_values[z][2])
    circle_4.append(training_medium_red_values[z][3])
    circle_5.append(training_medium_red_values[z][4])
    circle_6.append(training_medium_red_values[z][5])
    circle_7.append(training_medium_red_values[z][6])
    circle_8.append(training_medium_red_values[z][7])
    


training_df = pd.DataFrame(list(zip(circle_1, circle_2, circle_3, circle_4, circle_5, circle_6, circle_7, circle_8)), columns = ["Circle_1", "Circle_2", "Circle_3",
                                                                                                                                 "Circle_4", "Circle_5", "Circle_6",
                                                                                                                                 "Circle_7","Circle_8",])

condition = []

for i in range(training_trial):
    if i <= (training_trial//2):
        condition.append("Easy")
    else:
        condition.append("Medium")

training_df["Condition"] = condition
        
stim_color = []

for i in range(training_trial+1):
    if i < ((training_trial//2)//2):
        stim_color.append("Red")
    elif i > ((training_trial//2)//2) and i <= ((training_trial//4)*2):
        stim_color.append("Blue")
    elif i > ((training_trial//4)*2) and i <= (((training_trial//4)*2) + ((training_trial//2)//2)):
        stim_color.append("Red")
    elif i > (((training_trial//4)*2) + ((training_trial//2)//2)) and i <= (training_trial):
        stim_color.append("Blue")
    
   
training_df["Stimulus Color"] = stim_color

#df = df.reindex(columns=['C', 'B', 'A', 'D'])

rgb_1 = []
g = 0
xy = 0
for i in training_df["Circle_1"]:
    if training_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_1.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_1.append((r,g,b))
        print('blue')
        xy+=1
        
rgb_2 = []
g = 0
xy = 0
for i in training_df["Circle_2"]:
    if training_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_2.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_2.append((r,g,b))
        print('blue')
        xy+=1

rgb_3 = []
g = 0
xy = 0
for i in training_df["Circle_3"]:
    if training_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_3.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_3.append((r,g,b))
        print('blue')
        xy+=1


rgb_4 = []
g = 0
xy = 0
for i in training_df["Circle_4"]:
    if training_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_4.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_4.append((r,g,b))
        print('blue')
        xy+=1

rgb_5 = []
g = 0
xy = 0
for i in training_df["Circle_5"]:
    if training_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_5.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_5.append((r,g,b))
        print('blue')
        xy+=1


rgb_6 = []
g = 0
xy = 0
for i in training_df["Circle_6"]:
    if training_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_6.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_6.append((r,g,b))
        print('blue')
        xy+=1
        
rgb_7 = []
g = 0
xy = 0
for i in training_df["Circle_7"]:
    if training_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_7.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_7.append((r,g,b))
        print('blue')
        xy+=1
        
rgb_8 = []
g = 0
xy = 0
for i in training_df["Circle_8"]:
    if training_df["Stimulus Color"].iloc[xy] == 'Red':
        r = i*255
        b = ((1-i)*255)
        rgb_8.append((r,g,b))
        print('red')
        xy+=1
    else:
        r = ((1-i)*255)
        b = i*255
        rgb_8.append((r,g,b))
        print('blue')
        xy+=1
training_df["RGB_1"] = rgb_1
training_df["RGB_2"] = rgb_2
training_df["RGB_3"] = rgb_3
training_df["RGB_4"] = rgb_4
training_df["RGB_5"] = rgb_5
training_df["RGB_6"] = rgb_6
training_df["RGB_7"] = rgb_7
training_df["RGB_8"] = rgb_8

c_value = []
for i in range(len(training_df)):
    if training_df["Stimulus Color"].iloc[i] == "Control":
        c_value.append(.5)
    elif training_df["Stimulus Color"].iloc[i] == "Red":
        if training_df["Condition"].iloc[i] == "Easy":
            c_value.append(.545)
        elif training_df["Condition"].iloc[i] == "Medium":
            c_value.append(.530)
        elif training_df["Condition"].iloc[i] == "Hard":
            c_value.append(.52)
    elif training_df["Stimulus Color"].iloc[i] == "Blue":
        if training_df["Condition"].iloc[i] == "Easy":
            c_value.append((1-.545))
        elif training_df["Condition"].iloc[i] == "Medium":
            c_value.append((1-.530))
        elif training_df["Condition"].iloc[i] == "Hard":
            c_value.append((1-.52))
training_df["c_value"] = c_value
training_df = training_df.sample(frac = 1)
#training_df.to_csv("Input_dataset.csv")
        
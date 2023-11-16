# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:33:35 2023

@author: veoni
"""

import matplotlib.pyplot as plt

# Assuming you have recorded mouse positions in the list `mouse_positions`

# Extract x and y coordinates from mouse_positions
x_coords = [pos[0] for pos in out_dict['traj_record'][1]]
y_coords = [pos[1] for pos in out_dict['traj_record'][1]]

# Create a new figure
plt.figure(figsize=(8, 6))

# Plot the mouse trajectory
plt.plot(x_coords, y_coords, label='Mouse Trajectory', color='blue')
plt.scatter(x_coords, y_coords, color='red', s=4, label='Mouse Positions')
plt.hlines(-108, xmin = -800 , xmax =800, colors= 'orange')

# Add labels and title
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Mouse Trajectory')

# Set x-axis limits to show the left side of the screen
plt.xlim(-840, 840)
plt.ylim(-500, 500)  # Assuming max(x_coords) is the rightmost position

# Add legend
plt.legend()

# Show the plot
plt.show()

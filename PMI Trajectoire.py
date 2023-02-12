# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 12:41:40 2022

@author: DECLINE
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set physical parameters
G = 6.674e-11  # Gravitational constant
M_sun = 1.989e30  # Mass of the Sun
M_mercury = 3.285e23
M_venus = 4.867e24
M_earth = 5.972e24
M_mars = 6.39e23
M_jupiter = 1.898e27
M_saturn = 5.684e26
M_uranus = 	8.681e25
M_neptune = 1.024e26

c = 3e8  # Speed of light
r_dust = 1e-6  # Radius of dust particle
q = 4.8e-10  # Charge of dust particle
m = 1e-6  # Mass of dust particle

# Set initial conditions
r_0 = 2e11  # Initial distance from Sun
v_0 = 3e4  # Initial velocity
theta_0 = np.pi/2  # Initial angle (radians)

"""115000, 11200"""
# Set time step and number of steps
dt = 11200  # Time step
n_steps = 5000  # Number of steps

# Initialize arrays to store positions and velocities
r = np.zeros(n_steps+1)
theta = np.zeros(n_steps+1)
v_r = np.zeros(n_steps+1)
v_theta = np.zeros(n_steps+1)

# Set initial positions and velocities
r[0] = r_0
theta[0] = theta_0
v_r[0] = v_0 * np.cos(theta_0)
v_theta[0] = v_0 * np.sin(theta_0)

# Function to update the plot at each time step
def update(num, x, y, line, planets):
        # Compute positions of other planets
    mercury_x = 5.7e10 * np.cos(2*np.pi*num/n_steps)
    mercury_y = 5.7e10 * np.sin(2*np.pi*num/n_steps)
    venus_x = 1.1e11 * np.cos(2*np.pi*num/n_steps)
    venus_y = 1.1e11 * np.sin(2*np.pi*num/n_steps)
    earth_x = 1.5e11 * np.cos(2*np.pi*num/n_steps)
    earth_y = 1.5e11 * np.sin(2*np.pi*num/n_steps)
    mars_x = 2.2e11 * np.cos(2*np.pi*num/n_steps)
    mars_y = 2.2e11 * np.sin(2*np.pi*num/n_steps)
    jupiter_x = 7.78e11 * np.cos(2*np.pi*num/n_steps)
    jupiter_y = 7.78e11 * np.sin(2*np.pi*num/n_steps)
    saturn_x = 1.426e12 * np.cos(2*np.pi*num/n_steps)
    saturn_y = 1.426e12 * np.sin(2*np.pi*num/n_steps) 
    uranus_x = 2.87e12 * np.cos(2*np.pi*num/n_steps)
    uranus_y = 2.87e12 * np.sin(2*np.pi*num/n_steps)
    neptune_x = 4.498e12 * np.cos(2*np.pi*num/n_steps)
    neptune_y = 4.498e12 * np.sin(2*np.pi*num/n_steps)


    # Compute acceleration due to gravity
    a_grav = -G * M_sun / r[num]**2

    # Compute acceleration due to Poynting-Robertson effect
    a_pr = -(c / (4*np.pi*r[num]**2)) * (1 - (v_r[num]/c)) * (q**2 / (m*c))

    # Compute gravitational acceleration due to other planets
    a_mercury = -G * M_mercury * m / (((x[num]-mercury_x)**2 + (y[num]-mercury_y)**2)**0.5)**2
    a_venus = -G * M_venus * m / (((x[num]-venus_x)**2 + (y[num]-venus_y)**2)**0.5)**2
    a_earth = -G * M_earth * m / (((x[num]-earth_x)**2 + (y[num]-earth_y)**2)**0.5)**2
    a_mars = -G * M_mars * m / (((x[num]-mars_x)**2 + (y[num]-mars_y)**2)**0.5)**2
    a_jupiter = -G * M_jupiter * m / (((x[num]-jupiter_x)**2 + (y[num]-jupiter_y)**2)**0.5)**2
    a_saturn = -G * M_saturn * m / (((x[num]-saturn_x)**2 + (y[num]-saturn_y)**2)**0.5)**2
    a_uranus = -G * M_uranus * m / (((x[num]-uranus_x)**2 + (y[num]-uranus_y)**2)**0.5)**2
    a_neptune = -G * M_neptune * m / (((x[num]-neptune_x)**2 + (y[num]-neptune_y)**2)**0.5)**2

    # Update velocities
    v_r[num+1] = v_r[num] + (a_grav + a_pr + a_mercury + a_venus + a_earth + a_mars + a_jupiter + a_saturn + a_uranus + a_neptune) * dt
    v_theta[num+1] = v_theta[num]

    # Update positions
    r[num+1] = r[num] + v_r[num+1] * dt
    theta[num+1] = theta[num] + v_theta[num+1] * dt

    # Convert polar coordinates to Cartesian coordinates
    x[num+1] = r[num+1] * np.cos(theta[num+1])
    y[num+1] = r[num+1] * np.sin(theta[num+1])

    # Update planet positions
    planets[0].set_offsets([mercury_x, mercury_y])
    planets[1].set_offsets([venus_x, venus_y])
    planets[2].set_offsets([earth_x, earth_y])
    planets[3].set_offsets([mars_x, mars_y])
    planets[4].set_offsets([jupiter_x, jupiter_y])
    planets[5].set_offsets([saturn_x, saturn_y])
    planets[6].set_offsets([uranus_x, uranus_y])
    planets[7].set_offsets([neptune_x, neptune_y])
    # Update line data
    line.set_data(x[:num+2], y[:num+2])
    return line, planets[0], planets[1], planets[2], planets[3], planets[4], planets[5], planets[6], planets[7]
                            

# Convert polar coordinates to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Set up figure and axes
fig, ax = plt.subplots()
line, = ax.plot([], [], 'bo-', markersize=0.01)
sun = ax.scatter([0], [0], c='#FFFF00', marker='o', s=300)  # Add Sun to the plot

# Add other planets to the plot
planets = []
planets.append(ax.scatter([], [], c='grey', marker='o', s=20))           # Mercury
planets.append(ax.scatter([], [], c='antiquewhite', marker='o', s=40))   # Venus
planets.append(ax.scatter([], [], c='dodgerblue', marker='o', s=40))     # Earth
planets.append(ax.scatter([], [], c='r', marker='o', s=30))              # Mars
planets.append(ax.scatter([], [], c='orange', marker='o', s=120))        # Jupiter
planets.append(ax.scatter([], [], c='wheat', marker='o', s=100))         # Saturn
planets.append(ax.scatter([], [], c='c', marker='o', s=70))              # Uranus
planets.append(ax.scatter([], [], c='mediumblue', marker='o', s=70))     # Neptune

# Set axis limits
ax.set_xlim(-7.78e11, 7.78e11)
ax.set_ylim(-7.78e11, 7.78e11)


ax.set_xlim(-2.2e11, 2.2e11)
ax.set_ylim(-2.2e11, 2.2e11)
'''
#to Neptune
ax.set_xlim(-4.498e12, 4.498e12)
ax.set_ylim(-4.498e12, 4.498e12)
'''

# Set up animation
ani = animation.FuncAnimation(fig, update, frames=n_steps, fargs=(x, y, line, planets), interval=50, blit=True)

plt.show()


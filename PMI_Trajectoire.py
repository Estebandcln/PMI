# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 12:41:40 2022

@author: DECLINE
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


G = 6.674e-11  # Gravitational constant

# Masses
M_sun = 1.989e30  
M_mercury = 3.285e23
M_venus = 4.867e24
M_earth = 5.972e24
M_mars = 6.39e23
M_jupiter = 1.898e27
M_saturn = 5.684e26
M_uranus = 8.681e25
M_neptune = 1.024e26

# Distances to the Sun
r_mercury = 5.7e10
r_venus = 1.1e11
r_earth = 1.5e11
r_mars = 2.2e11
r_jupiter = 7.78e11
r_saturn = 1.426e12
r_uranus = 2.87e12
r_neptune = 4.498e12

c = 3e8
r_dust = 1e-6  # Radius of dust particle
q = 4.8e-10  # Charge of dust particle
m = 1e-6  # Mass of dust particle

# Initial conditions
r_0 = 2e11  # m
v_0 = 3e4  # m/s
theta_0 = np.pi/2  # Initial angle wrt Sun-particle line (radians)

# Set time step and number of steps
dt = 11200  # Time step
n_steps = 5000  # Number of steps

# Initialize arrays to store positions and velocities
r = np.zeros(n_steps+1)
theta = np.zeros(n_steps+1)
v_r = np.zeros(n_steps+1) # Radial velocity
v_theta = np.zeros(n_steps+1) # Tangential velocity

# Set initial positions and velocities
r[0] = r_0
theta[0] = theta_0
v_r[0] = v_0 * np.cos(theta_0)
v_theta[0] = v_0 * np.sin(theta_0)
                          

# Polar coordinates to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Set up figure and axes
fig, ax = plt.subplots()
line, = ax.plot([], [], 'bo-', markersize=0.01)

sun = ax.scatter([0], [0], c='#FFFF00', marker='o', s=300)
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
# Extend the plot to Neptune
ax.set_xlim(-4.498e12, 4.498e12)
ax.set_ylim(-4.498e12, 4.498e12)
'''


# Function to update the plot at each time step
def update(n, x, y, line, planets):
    
        # Compute positions of other planets
    mercury_x = r_mercury * np.cos(2*np.pi*n/n_steps)
    mercury_y = r_mercury * np.sin(2*np.pi*n/n_steps)
    venus_x = r_venus * np.cos(2*np.pi*n/n_steps)
    venus_y = r_venus * np.sin(2*np.pi*n/n_steps)
    earth_x = r_earth * np.cos(2*np.pi*n/n_steps)
    earth_y = r_earth * np.sin(2*np.pi*n/n_steps)
    mars_x = r_mars * np.cos(2*np.pi*n/n_steps)
    mars_y = r_mars * np.sin(2*np.pi*n/n_steps)
    jupiter_x = r_jupiter * np.cos(2*np.pi*n/n_steps)
    jupiter_y = r_jupiter * np.sin(2*np.pi*n/n_steps)
    saturn_x = r_saturn * np.cos(2*np.pi*n/n_steps)
    saturn_y = r_saturn * np.sin(2*np.pi*n/n_steps) 
    uranus_x = r_uranus * np.cos(2*np.pi*n/n_steps)
    uranus_y = r_uranus * np.sin(2*np.pi*n/n_steps)
    neptune_x = r_neptune * np.cos(2*np.pi*n/n_steps)
    neptune_y = r_neptune * np.sin(2*np.pi*n/n_steps)


    # Compute acceleration due to the gravity of the Sun
    a_sun = -G * M_sun / r[n]**2

    # Compute acceleration due to Poynting-Robertson effect
    a_pr = -(c / (4*np.pi*r[n]**2)) * (1 - (v_r[n]/c)) * (q**2 / (m*c))

    # Compute gravitational acceleration due to other planets
    a_mercury = -G * M_mercury * m / np.sqrt((x[n]-mercury_x)**2 + (y[n]-mercury_y)**2)**2
    a_venus = -G * M_venus * m / np.sqrt((x[n]-venus_x)**2 + (y[n]-venus_y)**2)**2
    a_earth = -G * M_earth * m / np.sqrt((x[n]-earth_x)**2 + (y[n]-earth_y)**2)**2
    a_mars = -G * M_mars * m / np.sqrt((x[n]-mars_x)**2 + (y[n]-mars_y)**2)**2
    a_jupiter = -G * M_jupiter * m / np.sqrt((x[n]-jupiter_x)**2 + (y[n]-jupiter_y)**2)**2
    a_saturn = -G * M_saturn * m / np.sqrt((x[n]-saturn_x)**2 + (y[n]-saturn_y)**2)**2
    a_uranus = -G * M_uranus * m / np.sqrt((x[n]-uranus_x)**2 + (y[n]-uranus_y)**2)**2
    a_neptune = -G * M_neptune * m / np.sqrt((x[n]-neptune_x)**2 + (y[n]-neptune_y)**2)**2

    # Update velocities
    v_r[n+1] = v_r[n] + (a_sun + a_pr + a_mercury + a_venus + a_earth + a_mars + a_jupiter + a_saturn + a_uranus + a_neptune) * dt
    v_theta[n+1] = v_theta[n]

    # Update positions
    r[n+1] = r[n] + v_r[n+1] * dt
    theta[n+1] = theta[n] + v_theta[n+1] * dt

    # Polar coordinates to Cartesian coordinates
    x[n+1] = r[n+1] * np.cos(theta[n+1])
    y[n+1] = r[n+1] * np.sin(theta[n+1])

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
    line.set_data(x[:n+2], y[:n+2])
    
    return line, planets[0], planets[1], planets[2], planets[3], planets[4], planets[5], planets[6], planets[7]
  

# Set up animation
ani = animation.FuncAnimation(fig, update, frames=n_steps, fargs=(x, y, line, planets), interval=50, blit=True)
plt.show()



# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 23:09:13 2023

@author: DECLINE
"""


import numpy as np
import matplotlib.pyplot as plt

#P-R vs. R

plt.figure(1)
 
R=np.linspace(10e9,5e12,100)   # Distance to the Sun (m)
r=np.linspace(1e-6,1e-3,5)     # Particle radius (m)
rho=2.5e3                      # Density of a particle's material (kg/m^3)
Ls=3.828e26                    # Solar luminosity (W)
c=299792458                    # Speed of light (m/s)
G=6.6743e-11                   # Gravitational constant (N*m^2/kg^2)
Ms=1.9885e30                   # Mass of the Sun (kg)

for i in range(len(r)):
    
    PR=[]
    
    for j in range(len(R)):
        
        PR.append(np.sqrt(G*Ms/R[j]**5)*r[i]**2*Ls/(4*c**2))  #N
        
    if i==0:
        plt.plot(R/149.6e9,1e7/(R**2.5),label='$1/R^{2.5}$')
    plt.plot(R/149.6e9,PR,label=str(round(r[i]*1e6,2))+' µm')
    plt.title('Poynting-Robertson Force')
    plt.xlabel('Distance to the Sun (ua)')
    plt.ylabel('Force $F_{PR}$ (N)')
    plt.yscale('log')
    plt.legend()
    plt.grid()

#P-R vs. r
    
plt.figure(2)

R=np.linspace(10e9,5e12,5)   # m
r=np.linspace(1e-6,1e-3,100) # m

for i in range(len(R)):
    
    PR=[]
    
    for j in range(len(r)):
        
        PR.append(np.sqrt(G*Ms/R[i]**5)*r[j]**2*Ls/(4*c**2))  #N
        
    plt.plot(r*1e6,PR,label=str(round(R[i]/149.6e9,2))+' ua')
    plt.title('Poynting-Robertson Force')
    plt.xlabel('Particle radius (µm)')
    plt.ylabel('Force $F_{PR}$ (N)')
    plt.yscale('log')
    plt.legend()
    plt.grid()

#Fg vs. R

plt.figure(3)

R=np.linspace(10e9,5e12,100) #m
r=np.linspace(1e-6,1e-3,5)   #m
  
for i in range(len(r)):
    
    Fg=[]
    
    for j in range(len(R)):
        
        m=np.pi*(4/3)*r[i]**3*rho  #kg
        Fg.append(G*Ms*m/R[j]**2)  #N
    if i==0:
        plt.plot(R/149.6e9,1e6/R**2,label='$1/R^2$')
    plt.plot(R/149.6e9,Fg,label=str(round(r[i]*1e6,2))+' µm')
    plt.title('Gravitational Force')
    plt.xlabel('Distance to the Sun (ua)')
    plt.ylabel('Force $F_g$ (N)')
    plt.yscale('log')
    plt.legend()
    plt.grid()

#Fg vs. r

plt.figure(4)

R=np.linspace(10e9,5e12,5)   #m
r=np.linspace(1e-6,1e-3,100) #m

for i in range(len(R)):
    
    Fg=[]
    
    for j in range(len(r)):
        
        m=np.pi*(4/3)*r[j]**3*rho  #kg
        Fg.append(G*Ms*m/R[i]**2)  #N

    plt.plot(r*1e6,Fg,label=str(round(R[i]/149.6e9,2))+' ua')
    plt.title('Gravitational Force')
    plt.xlabel('Particle radius (µm)')
    plt.ylabel('Force $F_g$ (N)')
    plt.yscale('log')
    plt.legend()
    plt.grid()


#beta from previous values
    
plt.figure(5)

beta=[]
for i in range(len(PR)):
    beta.append(PR[i]/Fg[i])    #We're missing a factor ~1e7

plt.plot(r*1e6,beta)
plt.axhline(y=0.1,label='$beta=0.1$',c='k',linewidth=1)
plt.axhline(y=0.5,label='$beta=0.5$',c='k',linewidth=1)
plt.title('$beta=F_r/F_g$')
plt.xlabel('Particle radius ($µm$)')
plt.ylabel('beta')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid()

#beta from its formula (ideal material Q=1)

plt.figure(6)

beta=[]
r=np.linspace(1e-6,1e-3,8)   # Particle radius (cm)
rho=2.5                      # Density of a particle's material (g/cm^3)
Ls=3.828e33                  # Solar luminosity (erg/s)
c=29979245800                # Speed of light (cm/s)
G=6.6743e-8                  # Gravitational constant (dyn*cm^2/g^2)
Ms=1.9885e33                 # Mass of the Sun (g)
Q=1                          # Ideal material

for i in range(len(r)):
    
    beta.append(3*Ls*Q/(np.pi*16*G*Ms*c*rho*r[i]))
    
plt.plot(r*1e6,beta,label='ideal material (Q=1)')
plt.axhline(y=0.1,label='$beta=0.1$',c='k',linewidth=1)
plt.axhline(y=0.5,label='$beta=0.5$',c='k',linewidth=1)
plt.title('$beta=F_r/F_g$')
plt.xlabel('Particle radius ($µm$)')
plt.ylabel('beta')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid()

"""
#truc
plt.figure(7)
R=np.linspace(10e9,5e12,5)  #m
r=np.linspace(1e-6,1,20)  #m
beta=np.linspace(0.1,1)
rho=2.5e3                    #kg/m^3
Ls=1361                      #W/m^2
c=299792458                  #m/s
G=6.6743e-11                 #N*m^2/kg^2
Ms=1.9885e30                 #kg

for i in range(len(R)):
    PR=[]
    for j in r:
        PR.append(np.sqrt(G*Ms/R[i]**5)*j**2*Ls/(4*c**2))  #N

    plt.plot(r,PR,label=str(round(R[i]/149.6e9,2))+' ua')
    plt.title('Poynting-Robertson Force')
    plt.xlabel('Particle radius (m)')
    plt.ylabel('Force (N)')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid()    
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 23:09:13 2023

@author: DECLINE
"""


import numpy as np
import matplotlib.pyplot as plt


#P-R vs. r
 
        
R=np.linspace(10e9,5e12,5)   #m
r=np.linspace(1e-6,1e-4,100) #m

rho=2.5e3                    #kg/m^3
Ls=3.828e26                  #W
c=299792458                  #m/s
G=6.6743e-11                 #N*m^2/kg^2
Ms=1.9885e30                 #kg

for i in range(len(R)):
    
    PR=[]
    
    for j in range(len(r)):
        
        plt.figure(1)
        
        PR.append(np.sqrt(G*Ms/R[i]**5)*r[j]**2*Ls/(4*c**2))  #N
        
    plt.plot(r*1e6,PR,label=str(round(R[i]/149.6e9,2))+' ua')
    plt.title('Poynting-Robertson Force')
    plt.xlabel('Particle radius (µm)')
    plt.ylabel('Force $F_{PR}$ (N)')
    plt.yscale('log')
    plt.legend()
    plt.grid()

#P-R vs. R
 
        
R=np.linspace(10e9,5e12,100)   #m
r=np.linspace(1e-6,1e-4,5) #m

rho=2.5e3                    #kg/m^3
Ls=3.828e26                  #W
c=299792458                  #m/s
G=6.6743e-11                 #N*m^2/kg^2
Ms=1.9885e30                 #kg

for i in range(len(r)):
    
    PR=[]
    
    for j in range(len(R)):
        
        plt.figure(2)
        
        PR.append(np.sqrt(G*Ms/R[j]**5)*r[i]**2*Ls/(4*c**2))  #N
        
    if i==0:
        plt.plot(R/149.6e9,1e7/(R**2.5),label='$1/R^{2.5}$')
    plt.plot(R/149.6e9,PR,label=str(round(r[i]*1e9,2))+' ua')
    plt.title('Poynting-Robertson Force')
    plt.xlabel('Particle radius (µm)')
    plt.ylabel('Force $F_{PR}$ (N)')
    plt.yscale('log')
    plt.legend()
    plt.grid()




#Fg vs. r

R=np.linspace(10e9,5e12,5)   #m
r=np.linspace(1e-6,1e-4,100) #m

rho=2.5e3                    #kg/m^3
Ls=3.828e26                  #W
c=299792458                  #m/s
G=6.6743e-11                 #N*m^2/kg^2
Ms=1.9885e30                 #kg

    
for i in range(len(R)):
    
    Fg=[]
    
    for j in range(len(r)):
        
        plt.figure(3)
        
        m=np.pi*(4/3)*r[j]**3*rho  #kg
        Fg.append(G*Ms*m/R[i]**2)  #N

    plt.plot(r*1e6,Fg,label=str(round(R[i]/149.6e9,2))+' ua')
    
    plt.title('Gravitational Force')
    plt.xlabel('Particle radius (µm)')
    plt.ylabel('Force $F_g$ (N)')
    plt.yscale('log')
    plt.legend()
    plt.grid()




#Fg vs. R


R=np.linspace(10e9,5e12,100) #m
r=np.linspace(1e-6,1e-4,5)   #m

rho=2.5e3                    #kg/m^3
Ls=3.828e26                  #W
c=299792458                  #m/s
G=6.6743e-11                 #N*m^2/kg^2
Ms=1.9885e30                 #kg

    
for i in range(len(r)):
    
    Fg=[]
    
    for j in range(len(R)):
        
        plt.figure(4)
        
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




beta=[]

Ls=3.828e33                  #erg/s
c=29979245800                #cm/s
G=6.6743e-8                  #dyn*cm^2/g^2
Ms=1.9885e33                 #g
Q=1
r=np.linspace(1e-6,1e-3,8)  #cm
rho=2.5                     #g/cm^3

for i in range(len(r)):
    
    beta.append(3*Ls*Q/(np.pi*16*G*Ms*c*rho*r[i]))
    
plt.figure(5)
plt.plot(beta,r*1e6,label='ideal material (Q=1)')
plt.axvline(x=0.1,label='$beta=0.1$',linewidth=1)
plt.axvline(x=0.5,label='$beta=0.5$',linewidth=1)
plt.title('$beta=F_r/F_g$')
plt.ylabel('Particle radius ($µm$)')
plt.xlabel('beta')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid()










"""

#truc
plt.figure(6)
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




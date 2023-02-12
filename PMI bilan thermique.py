# -*- coding: utf-8 -*-
"""
Created on Fri Dec 9 17:56:05 2022

@author: DECLINE
"""

import matplotlib.pyplot as plt


h=36e-3                              # height (m)
L=56e-3                              # width (m)
l=51e-3                              # length (m)
sol=[]
colour=['black','white','gold','chromium','copper']
S=2*L*l+2*L*h+2*l*h                  # total area (m2)
Si=[L*l,L*h,l*h]                     # all the different surfaces (m2)
Spstr=['L*l','L*h','l*h']
phi0=1361                            # Solar flux (W/m2)
sigma=5.6704*10**(-8)
black=[]
white=[]
gold=[]
chromium=[]
copper=[]
oxcopper=[]
abso=[0.99,0.15,0.3,0.4,0.18]         # absorptivity
emis=[0.9,0.98,0.03,0.07,0.03]        # emissivity

for i in range(len(Spstr)):
    
    GEO=[]
    GEOdeg=[]
    
    for j in range(len(colour)):
        
        alpha_s=abso[j]
        epsilon=emis[j]
        phi_s=phi0*Si[i]                    # solar power received by surface 
        energy_s=phi_s*alpha_s 
        #GEO and beyond (no infrared)
        TGEO=(energy_s/(sigma*epsilon*S))**(1/4)-273.15  # final temperature (°C)
        GEOdeg.append(''+str(round(TGEO,3))+' °C')
        GEO.append(round(TGEO,3))
        if j==0:
            black.append(GEO[j])
        if j==1:
            white.append(GEO[j])
        if j==2:
            gold.append(GEO[j])
        if j==3:
            chromium.append(GEO[j])
        if j==4:
            copper.append(GEO[j])

        
        
    sol.append(''+str(GEOdeg)+' surface '+str(Spstr[i]))


print(colour)
print('GEO and beyond :')
print(sol)

plt.figure(1)
plt.title('Temperature of each surface')
plt.plot(Spstr,black,c='black',label='Black')
plt.plot(Spstr,white,c='c',label='White')
plt.plot(Spstr,gold,c='gold',label='Gold')
plt.plot(Spstr,chromium,c='lightgrey',label='Chromium')
plt.plot(Spstr,copper,c='#B87333',label='Copper')
plt.xlabel('Surface considered')
plt.ylabel('Temperature in °C')
plt.legend()
plt.grid()
plt.show()



















"""
h=36e-3                              # height (m)
L=56e-3                              # width (m)
l=51e-3                              # length (m)
sol=[]
colour=['black','white','gold','chromium','copper','oxidized copper']
S=2*L*l+2*L*h+2*l*h                  # total area (m2)
Si=[L*l,L*h,l*h]                     # all the different surfaces (m2)
Spstr=['L*l','L*h','l*h']
phi0=1361                            # Solar flux (W/m2)
sigma=5.6704*10**(-8)
black=[]
white=[]
gold=[]
chromium=[]
copper=[]
oxcopper=[]
abso=[0.99,0.15,0.3,0.4,0.18,0.7]         # absorptivity
emis=[0.9,0.98,0.03,0.07,0.03,0.45]       # emissivity

for i in range(len(Spstr)):
    
    GEO=[]
    GEOdeg=[]
    
    for j in range(len(colour)):
        
        alpha_s=abso[j]
        epsilon=emis[j]
        phi_s=phi0*Si[i]
        energy_s=phi_s*alpha_s            # solar energy 
        #GEO and beyond (no infrared)
        TGEO=(energy_s/(sigma*epsilon*S))**(1/4)-273.15  # final temperature (°C)
        GEOdeg.append(''+str(round(TGEO,3))+' °C')
        GEO.append(round(TGEO,3))
        if j==0:
            black.append(GEO[j])
        if j==1:
            white.append(GEO[j])
        if j==2:
            gold.append(GEO[j])
        if j==3:
            chromium.append(GEO[j])
        if j==4:
            copper.append(GEO[j])
        if j==5:
            oxcopper.append(GEO[j])
        
        
    sol.append(''+str(GEOdeg)+' surface '+str(Spstr[i]))


print(colour)
print('GEO and beyond :')
print(sol)

plt.figure(1)
plt.title('Temperature of each surface')
plt.plot(Spstr,black,c='black',label='Black')
plt.plot(Spstr,white,c='c',label='White')
plt.plot(Spstr,gold,c='gold',label='Gold')
plt.plot(Spstr,chromium,c='lightgrey',label='Chromium')
plt.plot(Spstr,copper,c='#B87333',label='Copper')
plt.plot(Spstr,oxcopper,c='#4E7566',label='Oxidized copper')
plt.xlabel('Surface considered')
plt.ylabel('Temperature in °C')
plt.legend()
plt.grid()
plt.show()



fig, ax = plt.subplots()
for i in range(3):
    for j in Spstr:
        if j==Spstr[0] and i==0:
            ax.plot(Spstr,black,c='black',label='Black')
            ax.plot(Spstr,white,c='c',label='White')
            ax.plot(Spstr,gold,c='gold',label='Gold')
            ax.set_title('Temperature of each surface depending on its hue')
            ax.set_xlabel=('Surface considered')
            ax.set_ylabel=('Temperature in °C')
            ax.legend()
            ax.grid()
            plt.show()
        else:
            plt.plot(Spstr,black,c='black')
            plt.plot(Spstr,white,c='c')
            plt.plot(Spstr,gold,c='gold')
            plt.show()

#LEO et GEO

h=30e-3
L=50e-3
l=45e-3
sol=[]
LEO=[]
GEO=[]
c=['black','white','gold']
sol.append(c)
d=0.5                                                    #m
S=2*L*l+2*L*h+2*l*h                                      #m2
Sp=L*l                                                   #m2
Phi_s=1360                                               #W/m2
albedo=0.3
Phi_e=238                                                #W/m2
sigma=5.67*10**(-8)

absorptivity=[0.95,0.15,0.3]
emissivity=[0.9,0.98,0.03]
for i in range(3):
    alpha_s=absorptivity[i]
    em=emissivity[i]
    energy_s=Sp*Phi_s*alpha_s
    energy_a=energy_s*albedo
    energy_t=Sp*em*Phi_e
    energy=energy_t+energy_a+energy_s
    #GEO and beyond (no infrared)
    TGEO=(energy_s/(sigma*em*S))**(1/4)-273.15     #°C
    GEO.append(''+str(round(TGEO,3))+' °C')
    #Orbite basse (IR)
    TLEO=(energy/(sigma*em*S))**(1/4)-273.15       #°C
    LEO.append(''+str(round(TLEO,3))+' °C')

sol.append(LEO)
sol.append(GEO)

print(sol[0])
print('En LEO :')
print(sol[1])
print('En GEO :')
print(sol[2])



#pour une sphère

sol=[]
LEO=[]
GEO=[]
c=['black','white','gold']
sol.append(c)
d=0.5               #m
S=4*np.pi*(d/2)**2         #m2
Sp=S/4              #m2
Phi_s=1360             #W/m2
albedo=0.3
Phi_e=238           #W/m2
sigma=5.67*10**(-8)

absorptivity=[0.95,0.15,0.3]
emissivity=[0.9,0.85,0.03]
for i in range(3):
    alpha_s=absorptivity[i]
    em=emissivity[i]
    energy_s=Sp*Phi_s*alpha_s
    energy_a=energy_s*albedo
    energy_t=Sp*em*Phi_e
    energy=energy_t+energy_a+energy_s
    #GEO and beyond (no infrared)
    TGEO=(energy_s/(sigma*em*S))**(1/4)-273.15     #°C
    GEO.append(round(TGEO,3))
    #Orbite basse (IR)
    TLEO=(energy/(sigma*em*S))**(1/4)-273.15       #°C
    LEO.append(round(TLEO,3))

sol.append(LEO)
sol.append(GEO)

print(sol[0])
print(sol[1])
print(sol[2])

"""
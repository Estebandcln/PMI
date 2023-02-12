# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:27:23 2022

@author: DECLINE
"""
import matplotlib.pyplot as plt
import numpy as np

rho_p=10                   # particules/m**3
rho=10**(-6)               # particules/m**3
y=20*10**(-3)              # m
y_l=2*10**(-3)             # largeur du laser (diviser les résultats par 10)


# v = 2500 m/s (57 400 km)

x=25*10**(-3)                         #m
S=x*y                                 #m**2
t=np.arange(0,157788000/2629800,1)    #mois
v=2500                                #m/s

flux=[]
n=[]
nsomme=[]

for i in range(len(t)):
    flux.append(S*v*rho*2629800)           #particules/mois
    n.append(flux[i]*(t[1]-t[0]))          #particules
    if i==0:
        nsomme.append(n[i])                #particules
    else:
        nsomme.append(n[i]+nsomme[i-1])    #particules


plt.figure(1,dpi=300)
plt.title('Detected particles')
plt.plot(t,nsomme)
plt.axvline(x=18,c='r',linestyle='--')
plt.xlabel('Mission duration (months)')
plt.ylabel('Particles number $N_p$')
plt.grid()
plt.axvline(x=12,c='c',linestyle='--')
plt.axvline(x=18,c='r',linestyle='--')
plt.axvline(x=24,c='c',linestyle='--')
plt.axvline(x=36,c='c',linestyle='--')
plt.axvline(x=48,c='c',linestyle='--')
plt.axvline(x=60,c='c',linestyle='--')
plt.show()




# v = 1390 m/s (200 000 km de la Terre)



hi=50000*10**3             # m
hf=384400*10**3            # m
t=4.7336*10**7             # s
v=2500                     # m/s

x=[]
S=[]
flux=[]
n=[]
nsomme=[]
for i in range(30):
    x.append(i+1)                       # mm
    S.append(x[i]*y*10**(-3))           # m**2
    flux.append(S[i]*v*rho)             # particules/s
    n.append(flux[i]*t)                 # particules

plt.figure(1,dpi=300)
plt.title('Detected particles during 1.5 years')
plt.plot(S,n)
plt.xlabel('Inlet surface ($m^2$)')
plt.ylabel('Particles number $N_p$')
plt.grid()




# v = 1001 - 2659 m/s (50 000 - 384 400 km) - linéaire

x=25*10**(-3)                             # m
S=x*y                                     # m**2
t=np.arange(0,157788000/2629800,1)        # mois, pas d'un mois
v=np.linspace(1001,2659,8)                # m/s

for i in range(len(v)):
    flux=[]
    n=[]
    tliste=[]
    for j in range(len(t)):
        tliste.append(t[j])                    #mois
        flux.append(S*rho*v[i]*2629800)        #particules/mois
        n.append(flux[j]*tliste[j])            #particules
    
    plt.figure(2,dpi=300)
    plt.title('Detected particles')
    plt.xlabel('Mission duration (months)')
    plt.ylabel('Particles number $N_p$')
    plt.grid()
    plt.plot(t,n,label='v='+str(round(v[i]))+' m/s')
    plt.legend()
    plt.axvline(x=12,c='c',linestyle='--')
    plt.axvline(x=18,c='r',linestyle='--')
    plt.axvline(x=24,c='c',linestyle='--')
    plt.axvline(x=36,c='c',linestyle='--')
    plt.axvline(x=48,c='c',linestyle='--')
    plt.axvline(x=60,c='c',linestyle='--')
    
 
# v = 1001 - 2659 m/s (50 000 - 384 400 km) - linéaire

x=25*10**(-3)                         #m
S=x*y                                 #m**2
t=np.arange(0,157788000/2629800,1)    #mois
v=np.linspace(2659,1001,len(t))       #m/s, à 50 000km et 384 400km

flux=[]
n=[]
nsomme=[]

for i in range(len(v)):
    flux.append(S*v[i]*rho*2629800)        #particules/mois
    n.append(flux[i]*(t[1]-t[0]))          #particules
    if i==0:
        nsomme.append(n[i])                #particules
    else:
        nsomme.append(n[i]+nsomme[i-1])    #particules
 
plt.figure(3,dpi=300)
plt.title('Detected particles')
plt.plot(t,nsomme)
plt.axvline(x=18,c='r',linestyle='--')
plt.xlabel('Mission duration (months)')
plt.ylabel('Particles number $N_p$')
plt.grid()
plt.axvline(x=12,c='c',linestyle='--')
plt.axvline(x=18,c='r',linestyle='--')
plt.axvline(x=24,c='c',linestyle='--')
plt.axvline(x=36,c='c',linestyle='--')
plt.axvline(x=48,c='c',linestyle='--')
plt.axvline(x=60,c='c',linestyle='--')


# v = 1001 - 2659 m/s (50 000 - 384 400 km) - logarithmique

x=25*10**(-3)                         #m
S=x*y                                 #m**2
t=np.arange(0,157788000/2629800,1)    #mois
v=np.geomspace(2659,1001,len(t))      #m/s, à 50 000km et 384 400km, pas linéaire

flux=[]
n=[]
nsomme=[]

for i in range(len(v)):
    flux.append(S*v[i]*rho*2629800)        #particules/mois
    n.append(flux[i]*(t[1]-t[0]))          #particules
    if i==0:
        nsomme.append(n[i])                #particules
    else:
        nsomme.append(n[i]+nsomme[i-1])    #particules


plt.figure(4,dpi=300)
plt.title('Detected particles')
plt.plot(t,nsomme)
plt.axvline(x=18,c='r',linestyle='--')
plt.xlabel('Mission duration (months)')
plt.ylabel('Particles number $N_p$')
plt.grid()
plt.axvline(x=12,c='c',linestyle='--')
plt.axvline(x=18,c='r',linestyle='--')
plt.axvline(x=24,c='c',linestyle='--')
plt.axvline(x=36,c='c',linestyle='--')
plt.axvline(x=48,c='c',linestyle='--')
plt.axvline(x=60,c='c',linestyle='--')

"""


# Même scénario, nombre de protons

x=25*10**(-3)                         #m
S=x*y                                 #m**2
t=np.arange(0,157788000/2629800,1)    #mois
v=np.geomspace(2659,1001,len(t))      #m/s, à 50 000km et 384 400km, pas linéaire

flux=[]
n=[]
nsomme=[]

for i in range(len(v)):
    flux.append(S*v[i]*rho_p*2629800)      #protons/mois
    n.append(flux[i]*(t[1]-t[0]))          #protons
    if i==0:
        nsomme.append(n[i])                #protons
    else:
        nsomme.append(n[i]+nsomme[i-1])    #protons


plt.figure(5,dpi=300)
plt.title('Protons détectés')
plt.plot(t,nsomme)
plt.axvline(x=18,c='r',linestyle='--')
plt.xlabel('Mission duration (months)')
plt.ylabel('Nombre de protons $N_p$')
plt.grid()
plt.axvline(x=12,c='c',linestyle='--')
plt.axvline(x=18,c='r',linestyle='--')
plt.axvline(x=24,c='c',linestyle='--')
plt.axvline(x=36,c='c',linestyle='--')
plt.axvline(x=48,c='c',linestyle='--')
plt.axvline(x=60,c='c',linestyle='--')

"""
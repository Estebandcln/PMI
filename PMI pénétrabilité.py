# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:54:55 2023

@author: DECLINE
"""

import numpy as np
import matplotlib.pyplot as plt


"""

#v=26 km/s

d=np.linspace(0,10e-4,20)                              #cm
rho=2.5                                                #g/cm3
v=26                                                   #km/s  
P=[]

for i in d:
    P.append(0.53*(i**1.06)*(rho**0.5)*(v**(2/3)))     #cm

plt.plot(d*1e4,P)
plt.title('Pénétrabilité des particules')
plt.xlabel('Taille des particules ($µm$)')
plt.ylabel('Pénétrabilité ($cm$)')
"""


"""

#pour plusieurs vitesses mais est faux

d=np.linspace(0,10e-4,8)                               #cm
rho=2.5                                                #g/cm3
v=np.linspace(1,26,8)                                  #km/s  


for i in range(len(d)):
    P=[]
    for j in v:
        P.append(0.53*(d[i]**1.06)*(rho**0.5)*(j**(2/3)))     #cm

    plt.plot(d*1e4,P,label='v='+str(round(v[i],2))+' $km/s$')
    plt.title('Pénétrabilité des particules')
    plt.xlabel('Taille des particules ($µm$)')
    plt.ylabel('Pénétrabilité ($cm$)')
    plt.legend()
    plt.grid()
    
    

"""

#pour plusieurs vitesses

d=np.linspace(0,10e-4,20)                              #cm
rho=2.5                                                #g/cm3
v=np.linspace(1,26,8)                                  #km/s  


for i in v:
    P=[]
    for j in d:
        P.append(0.53*(j**1.06)*(rho**0.5)*(i**(2/3)))     #cm

    plt.plot(d*1e4,P,label='v='+str(round(i,2))+' $km/s$')
    plt.title('Pénétrabilité des particules')
    plt.xlabel('Taille des particules ($µm$)')
    plt.ylabel('Pénétrabilité ($cm$)')
    plt.legend()
    plt.grid()



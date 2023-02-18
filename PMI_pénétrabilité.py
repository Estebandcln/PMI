# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:54:55 2023

@author: DECLINE
"""

import numpy as np
import matplotlib.pyplot as plt



#P vs. v


plt.figure(1)


d=np.linspace(1e-5,1e-3,5)                             #cm
rho=2.5                                                #g/cm3
v=np.linspace(5,26,100)                                #km/s  


for i in range(len(d)):
    P=[]
    for j in v:
        P.append(530*(d[i]**1.06)*(rho**0.5)*(j**(2/3)))     #mm

    plt.plot(v,P,label='d='+str(round(d[i]*1e4,2))+' $µm$')
    plt.title('Pénétrabilité des particules')
    plt.xlabel('Vitesse des particules ($km/s$)')
    plt.ylabel('Pénétrabilité ($mm$)')
    plt.legend()
    plt.grid()
    
    

#P vs. d


plt.figure(2)


d=np.linspace(1e-5,1e-3,50)                            #cm
rho=2.5                                                #g/cm3
v=np.linspace(5,26,6)                                  #km/s  


for i in v:
    P=[]
    for j in d:
        P.append(530*(j**1.06)*(rho**0.5)*(i**(2/3)))     #mm

    plt.plot(d*1e4,P,label='v='+str(round(i,2))+' $km/s$')
    plt.title('Pénétrabilité des particules')
    plt.xlabel('Taille des particules ($µm$)')
    plt.ylabel('Pénétrabilité ($mm$)')
    plt.legend()
    plt.grid()



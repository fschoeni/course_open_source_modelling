# -*- coding: utf-8 -*-
"""
Created on Fri May 8 17:25:00 2020

@author: schoeniger
"""

# Importieren der benötigten Module
import numpy as np
import matplotlib.pyplot as plt

# Parameter nicht als globale Variablen definieren, sondern in der Funktion

# Definieren der Funktion Yamamura
def yamamura(theta, Y_0 = 0.11, f = 1.9, b = 0.19):
    '''Yamamura equation to calculate the sputtering yield'''
    return Y_0*(np.cos(theta))**(-f)*np.exp(b*(1-1/np.cos(theta)))


# Plotten der Funktion
xvals = np.linspace(0., 90.)
yvals = yamamura(np.radians(xvals))

plt.title('Sputtering yield according to the Yamamura formula')
plt.plot(xvals, yvals, 'r+-', label='Yamamura(theta)')
plt.legend()

# Definieren der Funktion 
def roses(b, theta):
    '''Exponential expression'''
    return np.exp(b*(1-1/np.cos(theta)))

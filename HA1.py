# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 17:25:00 2018

@author: schoeniger
"""

# Importieren der benötigten Module
import numpy as np
import matplotlib.pyplot as plt

# Parameter nicht als globale Variablen definieren, sondern in der Funktion

# Definieren der Funktion
def yamamura(theta, Y_0 = 0.11, f = 1.9, b = 0.19):
    '''Yamamura equation to calculate the sputtering yield'''
 
    Y = Y_0*(np.cos(theta))**(-f)*np.exp(b*(1-1/np.cos(theta)))
    return Y

# Plotten der Funktion
xvals = np.linspace(0., 90.)
yvals = yamamura(np.radians(xvals))

plt.title('Sputtering yield according to the Yamamura formula')
plt.plot(xvals, yvals, 'r+-', label='Yamamura(theta)')
plt.legend()
plt.show()

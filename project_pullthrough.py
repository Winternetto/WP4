# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:52:48 2020

@author: Tiia
"""

import numpy as np

def CalcArea(Dfo, Dfi):
    A = np.pi * ((Dfo/2)**2 - (Dfi/2)**2)
    
    return A

def CalcStress(A, F): # It is really this simple right? Lol
    sigma = F / A # safety factor for Saint Venant??
    
    return sigma


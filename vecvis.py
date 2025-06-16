#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 23:50:02 2025

@author: John Doe
"""

import matplotlib.pyplot as plt
import numpy as np
import linalglib

class Vecvis:
    def __init__(self, *args):
        self.vecs = args
    
    def plot_triangle(self):
        plt.plot(self.vecs[0].vec, self.vecs[1].vec)
        plt.show()
    
    def normvis_2D(self):
        for i in range(len(self.vecs)):
            if len(self.vecs[i].vec) != 2:
                raise Exception("Please use 2D vectors only.")
                
        theta = np.linspace(0, 2*np.pi)
        
        xline = np.zeros(10)
        yline = np.linspace(-1,1,10)
        
        figure, axes = plt.subplots(1)
        
        axes.plot(xline,yline,'k-')
        axes.plot(yline,xline,'k-')
        axes.plot(np.cos(theta), np.sin(theta), 'r-')
        
        legend = []
        for i in range(len(self.vecs)):
            normvec = self.vecs[i].normalize()
            axes.plot([0,normvec.vec[0]], [0,normvec.vec[1]], label=str(normvec.rnd()))
            print("Plotting norm of " + str(self.vecs[i].vec) + ", which is " + str(normvec))
            legend.append(str(normvec.rnd()))
        
        axes.legend()
        axes.set_aspect(1)
        
        plt.title('Normalized Vectors on the Unit Circle')
        plt.grid()
        plt.show()

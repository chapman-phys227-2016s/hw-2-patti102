#! /usr/bin/env python

"""
File: read_2columns.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module plots the points of two lists of data, as well as generating plots with the 1st, 2nd, and 3rd order
polynomial approximations also included.

"""

import numpy as np
from matplotlib.pyplot import *
    
def pendulum_prep(filename='pendulum.dat'):
    """Orders the file data into two seperate arrays and removes the first line."""
    pendulum_data = np.loadtxt(filename, dtype=np.float, skiprows=1) #skip first row so as to avoid headings
    return pendulum_data[:, 0], pendulum_data[:, 1]

def pendulum_plotter(filename='pendulum.dat'):
    """Plots the data from the pendulum_prep function."""
    info = pendulum_prep(filename)
    plot(info[0], info[1], 'bo')
    xlabel('Length')
    ylabel('Time')
    title('Period of Pendulum Oscillation')
    show()
    
def pendulum_poly_prep(filename='pendulum.dat'):
    """Creates the coefficient functions from the pendulum_prep data"""
    info = pendulum_prep(filename)
    coeffs = []
    for n in xrange(3):
        coeffs.append(np.poly1d(np.polyfit(info[0], info[1], n+1)))
    return coeffs

def poly_plotter():
    """Makes plots of the original function and of the 1st, 2nd, and 3rd order polynomial approximations."""
    ori = pendulum_prep()
    polys = pendulum_poly_prep()
    plot(ori[0], ori[1], 'ko')
    for n in range(3):
        fit = polys[n](ori[0])
        plot(ori[0], fit, '-')
        legend('P123', loc=4)
    xlabel('Length')
    ylabel('Time')
    title('1st, 2nd, and 3rd Degree Aprx. for Pendulum P Periods')

def test_poly_prep_constant():
    """Ensures that the pendulum_poly_prep returns an appropriate approximation coefficient for the 1st order fit
    of a straight line at y=2"""
    info = pendulum_poly_prep('constant.dat')
    apt = (info[0][0] - 0.5 < 1e-3)
    msg = 'Improperly prepared coeffients.'
    assert apt

def test_pendulum_prep():
    """Ensures that the prepdulum_prep function properly separates and indexes the file data."""
    info = pendulum_prep()
    apt = (info[0][-1] - 1 < 1e-6) and (info[1][-1] - 2 < 1e-6)
    msg = 'Pendulum lists improperly formed.'
    assert apt, msg
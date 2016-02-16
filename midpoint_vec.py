#! /usr/bin/env python

"""
File: read_2columns.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module demonstrates three different iteration techniques, lists and loops, 
vectorization with default summation, and vectorization wtih numpy sumation, 
through the implementation of a midpoint integration function.

"""

import numpy as np

def midpointint(f, a, b, n):
    """Uses lists and for loop to iterate through a midpoint integration function"""
    h = (b - a) / float(n)
    sum = 0
    for i in range(n):
        sum = sum + h * f(a - (h /2) + (i+1) * h)
    return sum

def midpointvecdefault(f, a, b, n):
    """Uses arrays and default summation for a midpoint integration function"""
    h = (b - a) / float(n)
    info = np.array([h * f(a - (h /2) + (i+1) * h) for i in range(n)])
    return sum(info)

def midpointvec(f, a, b, n):
    """Uses arrays and numpy summation for a midpoint integration function"""
    h = (b - a) / float(n)
    info = np.array([h * f(a - (h /2) + (i+1) * h) for i in range(n)])
    return np.sum(info)

def x_func(i):
    """The function x, for implementation in other functions."""
    return i

def test_midpointint_triangle():
    """Ensures proper integration of the straight line x from 1 to 3."""
    apt = (abs((midpointint(x_func, 1, 3, 1000)) - 4) <1e-6)
    msg = 'Unsuccessful integration.'
    assert apt, msg

def test_midpointvecdefault_triangle():
    """Ensures proper integration of the straight line x from 1 to 3."""
    apt = (abs(midpointvecdefault(x_func, 1, 3, 1000) - 4) <1e-6)
    msg = 'Unsuccessful integration.'
    assert apt, msg
    
def test_midpointvec_triangle():
    """Ensures proper integration of the straight line x from 1 to 3."""
    apt = (abs(midpointvec(x_func, 1, 3, 1000) - 4) <1e-6)
    msg = 'Unsuccessful integration.'
    assert apt, msg
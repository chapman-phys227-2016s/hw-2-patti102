#! /usr/bin/env python

"""
File: read_2columns.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module 

"""

import numpy as np
import math
from matplotlib.pylab import *

import Lagrange_poly1 as p1
import Lagrange_poly2 as p2

def multigrapher():
    legender1 = ['F2', '2', 'F4', '4', 'F6', '6', 'F10', '10']
    n_list = [2, 4, 6, 10]
    figure(1)
    p2.graph2(np.abs, n_list, -2, 2, legender1)
    legender2 = ['F13', '13', 'F20', '20']
    n_list2 = [13, 20]
    figure(2)
    p2.graph2(np.abs, n_list2, -2, 2, legender2)
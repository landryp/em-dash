#!/usr/bin/env python

import numpy as np

# physical constants

c = 2.998e10
G = 6.67e-8
Msol = 1.988e33

# symmetric mass ratio

def eta(m1,m2):

    q = m2/m1

    return q/(1.+q)**2

# neutron star compactness

def C(m,R):

    return G*m*Msol/(1e5*c**2*R)
    
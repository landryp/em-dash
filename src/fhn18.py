#!/usr/bin/env python

import numpy as np
from src.utils import *

# innermost stable circular orbit for Kerr black hole

def Z1(chi):

    return 1. + (1. - chi**2)**(1./3.)*((1. + chi)**(1./3.) + (1. - chi)**(1./3.))

def Z2(chi):

    return np.sqrt(3.*chi**2 + Z1(chi)**2)

def R_ISCO(m,chi): # in km

    return G*m*Msol*(3. + Z2(chi) - np.sign(chi)*np.sqrt((3. - Z1(chi))*(3. + Z1(chi) + 2.*Z2(chi))))/(1e5*c**2)

# Foucart+ 2018 fitting formula for remnant mass from neutron star--black hole merger, in units of neutron star baryonic mass

def F_remnant(m1,m2,chi1,RNS,alpha=0.406,beta=0.139,gamma=0.255,delta=1.761):
    
    F = alpha*eta(m1,m2)**(-1./3.)*(1. - 2.*C(m2,RNS)) - beta*c**2*1e5*R_ISCO(m1,chi1)*C(m2,RNS)/(G*m1*Msol*eta(m1,m2)) + gamma

    return np.where(F > 0., F**delta, 0.)
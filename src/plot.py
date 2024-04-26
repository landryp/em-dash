#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from src.fhn18 import F_remnant

# contour plot

def remnant_mass_contour_plot(mBHgrid,mNSgrid,chiBHs,RNS,F_threshold,mBHrange=None,mNSrange=None,qrange=None,model=F_remnant,ngrid=100,shade=0.05,fade=0.5):

    m1s = np.linspace(mBHgrid[0],mBHgrid[1],ngrid)
    m2s = np.linspace(mNSgrid[0],mNSgrid[1],ngrid)
    
    mBHs,mNSs = np.meshgrid(m1s,m2s)

    for chiBH in chiBHs:
    
        Fs = model(mBHs,mNSs,chiBH,RNS)
    
        cs = plt.contour(mNSs,mBHs,Fs,[F_threshold,1.],colors='k',linewidths=0.5,zorder=-1)
        plt.contourf(mNSs,mBHs,Fs,[F_threshold,1.],colors='k',alpha=shade,zorder=-3)
    
        plt.clabel(cs, cs.levels, inline=True, fmt={c: '{0:.1f}'.format(chiBH) for c in cs.levels}, fontsize=10,zorder=-1)

    if mBHrange is None: mBHrange = mBHgrid
    if mNSrange is None: mNSrange = mNSgrid
    if qrange is None: qrange = (0.04,1.)

    plt.fill_between(m2s,min(mBHgrid[1],mBHrange[1]),m2s/qrange[0],facecolor='white',edgecolor=None,alpha=fade,zorder=-2)
    plt.fill_between(m2s[m2s < mNSrange[0]],max(mBHgrid[0],mBHrange[0]),m2s[m2s < mNSrange[0]]/qrange[0],facecolor='white',edgecolor=None,alpha=fade,zorder=-2)
    plt.fill_between(m2s[m2s > mNSrange[1]],max(mBHgrid[0],mBHrange[0]),m2s[m2s > mNSrange[1]]/qrange[0],facecolor='white',edgecolor=None,alpha=fade,zorder=-2)

    plt.xlim(mNSgrid[0],mNSgrid[1])
    plt.ylim(max(mBHgrid[0],mBHrange[0]),min(mBHgrid[1],mBHrange[1]))
    plt.xlabel(r'$m_{NS}\;[M_\odot]$',fontsize=16)
    plt.ylabel(r'$m_{BH}\;[M_\odot]$',fontsize=16)

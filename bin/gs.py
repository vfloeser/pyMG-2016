#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse.linalg as spLA


from project.poisson1d import Poisson1D
from project.gauss_seidel import GaussSeidel


#k-th Fourier-Mode
def fourierMode(k,x):
    return np.sin(np.pi * k * x)


if __name__ == "__main__":
    N=63
    p=Poisson1D(N)

    gs = GaussSeidel(p.A, 1.)

    xv = np.array([ i * p.dx for i in range(p.ndofs)])

    #second fourier mode
    w2=lambda x: fourierMode(2,x)
    #16-th fourier mode
    w16=lambda x: fourierMode(16,x)
    #mean of second and 16-th fourier mode
    w=lambda x: (w2(x)+w16(x))/2.

    w2sol1=gs.smooth(p.rhs,w2(xv))
    w2sol10=np.copy(w2sol1)

    w16sol1=gs.smooth(p.rhs,w16(xv))
    w16sol10=np.copy(w16sol1)

    wsol1=gs.smooth(p.rhs,w(xv))
    wsol10=np.copy(wsol1)

    for i in range(9):
        w2sol10=gs.smooth(p.rhs,w2sol10)
        w16sol10=gs.smooth(p.rhs,w16sol10)
        wsol10=gs.smooth(p.rhs,wsol10)

    plt.figure(1)
    plt.plot(w2sol1,"b-")
    plt.plot(w2sol10,"r-")
    plt.figure(2)
    plt.plot(w16sol1,"b-")
    plt.plot(w16sol10,"r-")
    plt.figure(3)
    plt.plot(wsol1,"b-")
    plt.plot(wsol10,"r-")
    plt.show()
    plt.close()
    

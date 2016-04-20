#!/usr/bin/env python
import numpy as np
import scipy.linalg as LA
import scipy.sparse.linalg as spLA
import matplotlib.pyplot as plt

from project.helmholtz1d import Helmholtz1D
from project.weighted_jacobi import WeightedJacobi
# from project.gauss_seidel import GaussSeidel
from project.linear_transfer import LinearTransfer

from project.mymultigrid import MyMultigrid

if __name__ == "__main__":

    ntests = 1
    ndofs = 15
    niter_list = []
    for n in range(ntests):
        for sigma in range(-50,51):
            nlevels = int(np.log2(ndofs+1))

            # No. 2
            prob = Helmholtz1D(ndofs=ndofs, sigma=sigma)

            mymg = MyMultigrid(ndofs=ndofs, nlevels=nlevels)
            mymg.attach_transfer(LinearTransfer)
            mymg.attach_smoother(WeightedJacobi,prob.A,omega=2.0/3.0)
            # mymg.attach_smoother(GaussSeidel,prob.A)

            k = 6
            xvalues = np.array([(i+1) * prob.dx for i in range(prob.ndofs)])
            prob.rhs = (np.pi*k)**2 * np.sin(np.pi*k*xvalues)

            uex = spLA.spsolve(prob.A, prob.rhs)

            res = 1
            niter = 0
            err = []
            u = np.zeros(uex.size)
            while res > 1E-10 and niter < 10:
                niter += 1
                u = mymg.do_v_cycle(u, prob.rhs, 2, 2, 0)
                res = LA.norm(prob.A.dot(u)-prob.rhs, np.inf)
                err.append(LA.norm(u-uex, np.inf))
                #print(niter,res,err[-1])

            niter_list.append(niter)

        plt.subplot(121)
        plt.title("sigma aus [-50,0]")
        plt.plot(range(-50,1),niter_list[:51])
        plt.subplot(122)
        plt.title("sigma aus [0,50]")
        plt.plot(range(0,51),niter_list[50:])
        plt.tight_layout()
        plt.show()

#Imports
import numpy as np
import math
from math import sqrt
from math import pow
import scipy
from scipy.linalg import svd

#Functions#
def calc_SV(EigVals):
    """
    Calculating the Singular Values....
    """

    SnglrMtrx = []
    size = np.size(EigVals)

    for i in range(size):
        if (EigVals[i] != 0):
            SnglrMtrx = np.append(SnglrMtrx,math.sqrt(EigVals[i]))
        else:
            pass
    return(SnglrMtrx)

def TSF(A,V,U,EV):
    """
    Trahans sign checker
    """

    AxV = A @ V
    diagEV = np.diag(EV)
    UxEV = U @ diagEV
    same_sign = np.sign((AxV)[0]*(UxEV[0]))
    V = V*same_sign.reshape(1, -1)

    return(V)

def calc_svd(InputMtrx):
    """
    Richard Sucks
    """

    #Basic matrix declarations
    mtrxA = InputMtrx
    mtrxAT = np.transpose(mtrxA)
    ATxA = mtrxAT @ mtrxA
    AxAT = mtrxA @ mtrxAT
    mtrxSize = [len(mtrxA), len(mtrxA[0])]

    #Getting the Eigen Values/Vectors & Singular Values
    eigvalsV, eigvecsV = scipy.linalg.eig(ATxA)
    eigvalsU, eigvecsU = scipy.linalg.eig(AxAT)

    #Depending on the dimensions of the matrix the more 
    # accurate the SVD
    if (mtrxSize[0] >= mtrxSize[1]):
        eigvals = eigvalsV
    elif (mtrxSize[0] < mtrxSize[1]):
        eigvals = eigvalsU

    eigvals = np.append(eigvals,0)
    #Sort the eigen values/vectors in descending order
    eigvals = sorted(eigvals, reverse = True)  
    snglrvals = calc_SV(eigvals)

    #Sum Matrix
    mtrxS = np.diag(snglrvals)

    #V Matrix
    mtrxV = eigvecsV

    #U mtrx
    mtrxU = eigvecsU

    invA = None
    #Getting the matrix inverse if it Exists
    mtrxSInv = np.diag(1.0/snglrvals)
    try:
        mtrxInv = (mtrxV @ mtrxSInv) @ mtrxU.T
    except ValueError:
        print("Error: This matrix does not have an inverse")
    else:
        invA = mtrxInv

    #Getting the Condition Number
    CndtnK = (np.max(snglrvals))/(np.min(snglrvals))

    TSF(mtrxA, mtrxV, mtrxU, eigvecsU)
    return(mtrxU, mtrxS, mtrxV, CndtnK, invA)


InputMtrx = [[3,2,2],[2,3,-2]]
mtrxU, mtrxS, mtrxV, K, invA = calc_svd(InputMtrx)
print("Your condition number is: " , K)
print("Your matrix SVD is: " , "\n U: ", mtrxU, "\n S: ", mtrxS, "\n VT:", mtrxV.T)

U, s, VT = svd(InputMtrx)
print("U: " , U)
print("S: " , s)
print("VT: " , VT)
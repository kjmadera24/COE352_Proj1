#Imports
import numpy as np
import math
import scipy
import Proj_1_Final
from Proj_1_Final import calc_svd

#Functions
def calc_SpringMassSys(springNums, massNums, bndCond):
    #Variable Declarations
    mtrxf = 9.81 * np.array(massNums)
    mtrxKsize = len(springNums)-1
    mtrxK = np.zeros((mtrxKsize, mtrxKsize))
    
    #Two Fixed Ends
    if (bndCond == 2):
        for i in range(mtrxKsize):
            for j in range(mtrxKsize):
                if i == j:
                    mtrxK[i, j] = sum(springNums[i:i+1])
                elif (j == i-1 or j == i+1):
                    mtrxK[i, j] = -springNums[i+1]

    #One Fixed End
    elif (bndCond == 1):
        for i in range(mtrxKsize):
            for j in range(mtrxKsize):
                if (i == mtrxKsize and j == mtrxKsize):
                    mtrxK[i,j] == springNums[i]
                elif (i == j):
                    mtrxK[i, j] = sum(springNums[i:i+1])
                elif (j == i-1 or j == i+1):
                    mtrxK[i, j] = -springNums[i+1]

    #No Fixed Ends
    elif (bndCond == 0):
        for i in range(mtrxKsize):
            for j in range(mtrxKsize):
                if (i == 0 and j == 0):
                    mtrxK[i,j] == springNums[i]
                elif (i == mtrxKsize and j == mtrxKsize):
                    mtrxK[i,j] == springNums[i]
                elif (i == j):
                    mtrxK[i, j] = sum(springNums[i:i+1])
                elif (j == i-1 or j == i+1):
                    mtrxK[i, j] = -springNums[i+1]

    #Calculate the SVD of the K matrix
    mtrxU, mtrxS, mtrxV, CndtnNum, mtrxInv = calc_svd(mtrxK)
    
    #Calculating the Equilibrium displacements in Ku=f
    mtrxu = mtrxInv @ mtrxf

    #Calculating the Elongations and Internal Stresses
    deltaL = np.zeros(mtrxKsize)
    mtrxW = np.zeros(mtrxKsize - 1)
    
    for i in range(mtrxKsize - 1):
        deltaL = np.append(deltaL, mtrxu[i+1] - mtrxu[i])
        mtrxW = np.append(mtrxW, mtrxK[i]*deltaL[i])

    #Calculating the Condition number
    snglrvals = np.diag(mtrxS)
    CndtnK = (np.max(snglrvals))/(np.min(snglrvals))

    return(mtrxu, deltaL, mtrxW, CndtnK)

print("An array with the the spring constants, the masses, and whether you would like 0,1 or 2 fixed ends")
InputMtrx = eval(input("Ex: [[2,3,4], [1,2], 1] respectfully. "))

EquilDisp, DeltaElong, IntrnlStress, CndtnNum = calc_SpringMassSys(InputMtrx[0], InputMtrx[1], InputMtrx[2])

print("Your spring-mass system values are:")
print("Equilibrium displacements: " , EquilDisp)
print("Elongations: " ,  DeltaElong)
print("Internal Stresses: " , IntrnlStress)
print("Condition Number: " , CndtnNum)
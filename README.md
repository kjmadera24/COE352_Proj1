# COE352_Proj1
This repository is for my COE352 project 1 making an SVD callable function and a user-input function for calculating a spring-mass system!!

## Proj1_pt1.py

### Description <a name="description"></a>
This code performs Singular Value Decomposition (SVD) on a given matrix and calculates the singular values, the left singular vectors (U), the diagonal matrix of singular values (S), the right singular vectors (V), the condition number of the matrix, and the inverse of the matrix if it exists. 
<p>
SVD is a fundamental linear algebra technique used in data analysis, dimensionality reduction, and various scientific applications.

### Usage <a name="usage"></a>
In order to use this code you need to download it and edit the InputMtrx variable at the bottom of the code to any matrix youd like to get the SVD from. The code reads this input as an array so, when inputting your matrix you must assure it is as an array of arrays 
<p>
**As an example, with this matrix ` [[3,2,2],[2,3,-2]] `
  <p>
**You will get an output that looks something like this**
  <p>
> <p> Error: This matrix does not have an inverse </p>
> <p> Your condition number is:  1.6666666666666665
> <p> Your matrix SVD is:
> <p> U:  [[ 0.70710678 -0.70710678]
> <p>     [ 0.70710678  0.70710678]]
> <p> S:  [[5. 0.]
> <p>     [0. 3.]]
> <p> VT: [[-7.07106781e-01 -7.07106781e-01 -4.55680392e-17]
> <p>     [-6.66666667e-01  6.66666667e-01  3.33333333e-01]
> <p>     [ 2.35702260e-01 -2.35702260e-01  9.42809042e-01]]
> <p> U:  [[-0.70710678 -0.70710678]
> <p>     [-0.70710678  0.70710678]]
> <p> S:  [5. 3.]
> <p> VT:  [[-7.07106781e-01 -7.07106781e-01 -6.47932334e-17]
> <p>      [-2.35702260e-01  2.35702260e-01 -9.42809042e-01]
> <p>      [-6.66666667e-01  6.66666667e-01  3.33333333e-01]]
    
### Functions <a name="functions"></a>

#### Function: calc_SV <a name="function-calc_sv"></a>
This function calculates the singular values from the inputted eigenvalues.

#####Parameters:
EigVals: A list of eigenvalues.

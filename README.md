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
Heres an example [[3,2,2],[2,3,-2]]
    
### Functions <a name="functions"></a>

#### calc_SV <a name="function-calc_sv"></a>
This function calculates the singular values from the inputted eigenvalues.

##### Parameters:
EigVals: The list of eigenvalues calulated in the calc_svd function.

##### Returns:
SnglrMtrx: The list of singular values.

#### TSF <a name="function-tsf"></a>
This function performs truncation and sign flipping to ensure that the singular vectors are aligned correctly.

##### Parameters:
* A: The input matrix.
* V: Right singular vectors.
* U: Left singular vectors.
* EV: Eigenvalues.

##### Returns:
* V: The updated V matrix with corrected signs.

#### calc_svd <a name="function-calc_svd"></a>
This is the main function that calculates the SVD of the input matrix.

##### Parameters:
* InputMtrx: The input matrix to perform SVD on.

##### Returns:
* mtrxU: Left singular vectors.
* mtrxS: Diagonal matrix of singular values.
* mtrxV: Right singular vectors.
* CndtnK: Condition number of the matrix.
* invA: Inverse of the matrix (if it exists).

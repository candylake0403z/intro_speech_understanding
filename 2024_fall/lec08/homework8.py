import numpy as np

def dft_matrix(N):
    '''
    Create a DFT transform matrix, W, of size N.
    
    @param:
    N (scalar): number of columns in the transform matrix
    
    @result:
    W (NxN array): a matrix of dtype='complex' whose (k,n)^th element is:
           W[k,n] = cos(2*np.pi*k*n/N) - j*sin(2*np.pi*k*n/N)
           Equivalent to W[k,n] = exp(-2j * np.pi * k * n / N)
    '''
    k = np.arange(N).reshape((N, 1))  # Column vector of indices
    n = np.arange(N)                 # Row vector of indices
    exponent = -2j * np.pi * k * n / N
    W = np.exp(exponent)             # Compute the complex exponential
    return W

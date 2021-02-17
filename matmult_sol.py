# Program to multiply two matrices using Numpy arrays 
import numpy as np

@profile
def  matnumpy():

    N = 250 

    # NxN matrix 
    X = np.zeros(shape = (250, 250) , dtype = np.int64) 
    X  = np.random.randint(0, 101, size = (N, N))

    # Nx(N+1) matrix 
    Y = np.zeros(shape = (250, 250 + 1) , dtype = np.int64) 
    Y  = np.random.randint(0, 101, size = (N, N + 1))
    
    # result is Nx(N+1)     
    result = np.zeros(shape = (250, N + 1) , dtype = np.int64) 
    result = np.matmul(X, Y) 

    for r in result: 
        print(r) 
    
matnumpy()
# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

from mat import *
from vec import *
from cancer_data import *
from matutil import *

## Task 1 ##
def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    return Vec(u.D,{k:1 if u[k]>=0 else -1 for k in u.D} ) 

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w 
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> fraction_wrong(A, b, w)
        0.3333333333333333
    '''
    hypothesis_vec=signum(A*w)
    frac_wrong=sum([1 if hypothesis_vec[k]!=b[k] else 0 for k in b.D])/len(b.D)
    return frac_wrong


## Task 3 ##
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> loss(A, b, w)
        317
    '''
    hypothesis_vec=(A*w);
    loss_vec=hypothesis_vec-b;
    loss_func=sum([loss_vec[x]*loss_vec[x] for x in loss_vec.D])
    return loss_func
    

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> find_grad(A, b, w) == Vec({'B', 'A'},{'B': -290, 'A': 60})
        True
    '''
    A_rows=mat2rowdict(A)
    grad_vec=sum([(A_rows[y]*w - b[y])*2*A_rows[y] for y in b.D])
    return grad_vec

## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    Example:
        >>> A = Mat(({'a','b','c'},{'A','B'}), {('a','A'):-4, ('a','B'):3, ('b','A'):1, ('b','B'):8, ('c','A'):5, ('c','B'):2})
        >>> b = Vec({'a','b','c'}, {'a':1, 'b':-1,'c':1})
        >>> w = Vec({'A','B'}, {'A':1, 'B':-2})
        >>> sigma = .1
        >>> gradient_descent_step(A, b, w, sigma) == Vec({'B', 'A'},{'B': 27.0, 'A': -5.0})
        True
    '''
    w=w-(sigma*find_grad(A,b,w))
    return w
## Ungraded task ##
def gradient_descent(A, b, w, sigma, T):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
        - T: number of iterations to run
    Output: hypothesis vector obtained after T iterations of gradient descent.
    '''
    pass

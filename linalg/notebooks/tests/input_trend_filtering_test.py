import numpy as np
import matplotlib.pyplot as plt
import time

def second_difference_matrix(N):
    '''
    Creates the second-difference matrix D such that the second difference of a vector u is D*u.

    Parameters:

    N: Number of data points
    m: number if inputs u(k) in R^m
    '''
    D2 = np.eye(N) - 2*np.eye(N, k=1) + np.eye(N, k=2)
    #delete non-comlete rows
    D2 = D2[:-2, :]
    return D2

def obsv(A, C, n):
    '''
    Create the extended observability matrix used in the data equation.

    Parameters:

    A : numpy.ndarray
        The state matrix of the state-space system
    C : numpy.ndarray
        The observation matrix of the state-space system
    n : float
        number of measurements

    Returns:

    O : numpy.ndarray, shape(n, number of state variables)
        The extended observability matrix
    '''
    O = C
    for k in range(1, n):
        O = np.vstack((O, C @ np.linalg.matrix_power(A, k)))

    return O

def Gamma(A,B,C,N):
    '''
    Create the impulse response matrix used in the data equation.

    Parameters:

    A : numpy.ndarray
        The state matrix of the state-space system
    B : numpy.ndarray
        The input matrix of the state-space system
    C : numpy.ndarray
        The observation matrix of the state-space system
    n : float
        number of measurements

    Returns:

    gamma : numpy.ndarray, shape(n*number of state variables, n*number of state variables)
        The impulse response matrix
    '''
    mat_list = []
    n = (C@B).shape[0]
    m = (C@B).shape[1]
    for i in range(N): # generate row
        tmp = []
        for j in range(N): # loop through A^j*B
            if j <= i:
                tmp.append(C@np.linalg.matrix_power(A,i-j)@B)
        if i < N-1:
            tmp.append(np.zeros((n, m*(N-1-i))))
        mat_list.append(tmp)
        G = np.block(mat_list)
        #add zero row and column
        n,m = (C@B).shape
        ng,mg = G.shape
        G = np.append(np.zeros((n,mg)),G,axis=0)
        G = np.append(G,np.zeros((n+ng,m)),axis=1)
        G = G[:-1, :-1] #CHECK THIS!
    return G


def prbs31(code):
    '''code for generating a prbs'''
    for i in range(32):
        next_bit = ~((code>>30) ^ (code>>27))&0x01
        code = ((code<<1) | next_bit) & 0xFFFFFFFF
    return code

###########################
''' create state soace system
x(k+1) = Ax(k) + Bu(k)
y(k) = Cx(k)
'''
A = np.array([[0.76, 0.89],[-0.45, 0.72]])
B = np.array([[.24],[.45]])
C = np.array([[1,0]])

###########################
# Generate data
#number of data points
N = 200

#imitialization
x = np.array([[0],[0]])
y = C@x

#input signal
uk = 0
u = np.array([0])
# weighted random walk
for k in range(N-1):
    r = np.random.uniform(0,1,1)
    if r < 0.1:
        uk += 1
    elif r > 1 - 0.1:
        uk -= 1
    else:
        pass
    u = np.append(u,uk)

#simulate
for k in range(N-1):
    x = A@x + B*u[k]
    y = np.append(y,C@x)

print("...............")
#compute matrices Gamma end Delta_2
lam = 0.01
t = time.time()
G = Gamma(A,B,C,N)
elapsed = time.time() - t
print("elapsed time, Gamma:", elapsed, "seconds")

t = time.time()
D2 = second_difference_matrix(N)
elapsed = time.time() - t
print("elapsed time, Delta_2:", elapsed, "seconds")

t = time.time()
M = np.linalg.inv(G.T@G + lam*D2.T@D2)@G.T
elapsed = time.time() - t
print("elapsed time, M:", elapsed, "seconds")

#####
# matrix-vector multiplication
t = time.time()
uhat = M@y
elapsed = time.time() - t
print("elapsed time, M*y:", elapsed, "seconds")
print("...............")

#####
plt.plot(u)
plt.plot(uhat)
plt.show()

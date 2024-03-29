# No additional 3rd party external libraries are allowed
from typing import final
import numpy as np

def relu(x):
    '''Returns input variable in the same shape passed through ReLu function.'''
    return np.maximum(x, 0)

def relu_grad(z):
    '''Returns gradient of the ReLu activation function.'''
    z[z<=0] = 0
    z[z>0] = 1
    return z

def sigmoid(x):
    '''Returns input variable in the same shape passed through Sigmoid function.'''
    return 1/(1 + np.exp(-x))
    
def sigmoid_grad(z):
    '''Returns gradient of the Sigmoid activation function. 
    Parameters:
    - z: output of the sigmoid layer.'''
    return z * (1 - z)

def softmax(x):
    '''Softmax activation function.'''
    #The final probability vector
    final_probability = np.zeros((x.shape[0],x.shape[1]))
    #Iterate over each vector in the inpux, calculate exponent of each value 
    #in the vecor and normalize it. Then, update the final_probability.
    for i in range(0,x.shape[0]):
        vector = x[i]
        exp=np.exp(vector)
        probability=exp/np.sum(exp)
        final_probability[i]=probability
    return final_probability
    
def softmax_grad(z):
    '''Gradient of the softmax activation function.'''
    #Create a jacobean matrix of the n x n size where n is the length of the input
    #vector z.
    jacobian_m = np.zeros((len(z[0]),len(z[0])))
    #Iterate over each position in the Jacobian vector and perform calculations.
    for i in range(len(jacobian_m)):
        for j in range(len(jacobian_m)):
            if i == j:
                jacobian_m[i][j] = z[0][i] * (1 - z[0][i])
            else: 
                jacobian_m[i][j] = -z[0][i] * z[0][j]
    return jacobian_m

def tanh(x):
    '''Hypoerbolic tangent activation function.'''
    return (2/(1 + np.exp(-2*x)))-1

def tanh_grad(z):
    '''Gradient of Hypoerbolic tangent activation function.'''
    return 1 - tanh(z)**2

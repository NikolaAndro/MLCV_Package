# No additional 3rd party external libraries are allowed
import numpy as np

def dropout(b, p, mode='test'):
    '''
    Output : should return a tuple containing 
     - b : b is the output of batch norm layern.
     - p : Dropout param
     - mode : 'test' or 'train'
     - mask : 
        - in train mode, it is the dropout mask
        - in test mode, mask will be None.
    
    sample output: (b_drop=, p=0.5, mode='test',mask=None)
    '''
    # TODO Implement logic for both 'test' and 'train' modes.
    if mode == 'train':
        # Mask for the dropout. List of binomial distribution in size of x.
        # mask = [int(np.random.binomial(n=1, p=p, size=1)) for q in range(len(z))]
        mask = np.random.binomial(1, p, size=b.shape) 
        # For every distribution == 1 in hte mask, make that element of x = 0.
        # z_drop = [0 if mask[index] == 1 else z[index] for index in range(len(z))]
        b_drop = b * mask

    elif mode == 'test':
        # No mask in testing mode since we want to keep all the nodes active. 
        # What we need to do is to make it matches the training phase expectation, so we scale the layer output with p.
        mask = None
        b_drop = b * p
    
    return b_drop, p, mode, mask

def dropout_grad(z, mask, mode='train'):
    '''Gradient of the dropout.'''
    e = 0.001

    if mode == 'train':
        # + e ?   where   e = 0.001
        grad_w_wrt_b = np.dot((1/mask) * np.identity(len(mask)), z)
    
    return grad_w_wrt_b
    # elif mode == 'test':
    #     raise NotImplementedError("Gradiant of Dropout - Test Not Implemented")
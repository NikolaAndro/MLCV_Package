# No additional 3rd party external libraries are allowed
import numpy as np
# tqdm - package used to shoe a progress bar when loops executing
# tqdm - "progress" in arabic and obriviation for  "Te Quiero DeMaciado" 
# in Spanish (I love you so much)
from tqdm import tqdm 

def async_sgd(model, x_train_batches, y_train_batches, lr=0.1, R=100):
    '''
    Compute gradient estimate of emp loss on each minibatch in parallel using GPU blocks/threads
    use the most recent gradient estimate computed on a single minibatch to update the weights asynchronously.
    '''
    # setup
    w_r_minus_1 = []
    gamma_beta_minus_1 = []
    for index, layer in enumerate(model.layers):
        w_r_minus_1.append(layer.W)
        if index != 3:
            gamma_beta_minus_1.append([layer.gamma, layer.beta])

    w_r_minus_1 = np.array(w_r_minus_1)
    gamma_beta_minus_1 = np.array(gamma_beta_minus_1)

    #Run epochs
    for r in range(R):
        #iterate over minibatches
        for x_minibatch, y_minibatch in tqdm(zip(x_train_batches, y_train_batches)):

            if model.use_batchnorm:
                del_L_N_of_w_r_min_1, del_L_N_of_gamma_and_beta_min_1 = model.emp_loss_grad(x_minibatch, y_minibatch)
                # Update the gamma and beta
                gamma_beta = gamma_beta_minus_1 - lr * del_L_N_of_gamma_and_beta_min_1
            else:
                del_L_N_of_w_r_min_1 = model.emp_loss_grad(x_minibatch, y_minibatch)

            # Update the weights
            w_r = w_r_minus_1 - lr * del_L_N_of_w_r_min_1

            w_r_minus_1 = w_r
    
    for i in range(4):
        model.layers[i].W = w_r[i]
        if model.use_batchnorm and i != 3:
            model.layers[i].gamma = gamma_beta[i][0]
            model.layers[i].beta = gamma_beta[i][1]

    return model

            





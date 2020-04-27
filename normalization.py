#############################################
# normalization
#############################################    

def train_normalize(x):
    train_mean = np.mean(x)
    train_std = np.std(x)
    normalize = (x - train_mean)/train_std
    
    return normalize, train_mean, train_std

def test_normalize(test, train_mean, train_std):
    return (test - train_mean)/train_std


def return_value(pred, train_mean, train_std): 

    y_hat_list = list()
    for i in pred:
        y_hat = train_mean + i * train_std
        y_hat_list.append(y_hat)
        
    return y_hat_list

def return_values(pred, train_mean, train_std, y_list): 
    
    y_hat_list = list()
    for l, i in enumerate(y_list):
        y_hat = train_mean[i] + pred[l] * train_std[i]
        y_hat_list.append(y_hat)
        
    return y_hat_list
    
    

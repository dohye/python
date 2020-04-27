
def mean_squared_error(pred, y):
    mse = np.mean((y - pred)**2)
    return mse

def mean_absolute_diviation(pred, y):
    mad = np.mean(np.abs(y - pred))
    return mad

def R_square(pred, y):
    y_mean = np.array(np.mean(y))
    SSR = np.sum((pred - y)**2)
    TSS = np.sum((y - y_mean)**2)
    R_square = 1 - SSR/TSS
    return R_square

def mean_absolute_percentage_error(pred, y):
    y, pred = np.array(y), np.array(pred)
    mape = np.mean(np.abs((y - pred)/y)) * 100
    return mape
    

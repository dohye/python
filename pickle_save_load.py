# data save & load (pickle)

def save_obj(obj, output):
    with open(output, 'wb')as f_out:
        pickle.dump(obj, f_out)

def load_obj(output):
    return pickle.load(open(output, 'rb'))
    

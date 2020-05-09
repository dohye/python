import pickle

pickle.dump(변수명, open('저장할 파일 이름', 'wb')) #pickle.dump(train_examples, open('train_all_examples.tlp', 'wb'))
pickle.load(open('파일 이름', 'rb')) #train_examples = pickle.load(open('train_all_examples.tlp', 'rb'))

def save_obj(obj, output):
    with open(output, 'wb') as f_out:
        pickle.dump(obj, f_out)
        
def load_obj(output):
    return pickle.load(open(output, 'rb'))

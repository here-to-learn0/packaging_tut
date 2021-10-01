import pickle as pkl

def loading_pkl(path):
    with open(path, 'rb') as f:
        data = pkl.load(f)
    return data

 

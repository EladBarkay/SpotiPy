import pickle


def save(obj, path):
    pickle.dump(obj, open(path, 'wb'), pickle.HIGHEST_PROTOCOL)


def load(path):
    return pickle.load(open(path, 'rb'))
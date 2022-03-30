import os


class Vocab:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise ValueError('Vocab name should be string')

        self.name = name
        self.obj2index, self.index2obj = {}, {}

    def get_store_path(self, store_dir):
        return os.path.join(store_dir, 'tok.{}.dat'.format(self.name))

    def load(self, store_dir: str, as_path=False):
        store_path = store_dir if as_path else self.get_store_path(store_dir)

        self.obj2index, self.index2obj = {}, {}
        with open(store_path, 'r') as f:
            objs = f.read().split('\n')[:-1]
        for index, obj in enumerate(objs):
            self.obj2index[obj] = index
            self.index2obj[index] = obj

        return self

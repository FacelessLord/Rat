from typing import Generic, TypeVar, Dict

K = TypeVar('K')
V = TypeVar('V')


class readonlydict(Dict[K, V]):
    def __init__(self, dictionary: Dict[K, V]):
        super().__init__(dictionary)

    def __setitem__(self, key, value):
        raise KeyError('Dict is readonly')

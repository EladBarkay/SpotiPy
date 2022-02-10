import typing


class SpotipyGenericObj:
    id: str
    name: str

    def __init__(self, _id: str, name: str):
        self.id = _id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, SpotipyGenericObj):
            return self.id == other.id and self.name == other.name
        return self == other

    def __repr__(self):
        return str(self.__dict__)
import typing


class SpotipyGenericObj:
    id: str
    name: str

    def __init__(self, _id: str, name: str):
        self.id = _id
        self.name = name
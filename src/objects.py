# common types
class Color:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b


class Country:
    def __init__(self, *, color: Color):
        self.color = color


class FocusTree:
    ...

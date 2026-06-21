# common types
class Color:
    def __init__(self, r: int, g: int, b: int):
        # TODO: bounds checking
        self.r = r
        self.g = g
        self.b = b

    def __str__(self) -> str:
        return f"{{ {self.r} {self.g} {self.b} }}"


# .mod settings as a class
class Mod:
    ...


class Country:
    def __init__(self, *, name, tag=None, color=Color(255, 0, 255)):
        self.name = name
        self.tag = tag if tag is not None else name[:3].upper()

        self.color = color
        # unimplemented stuff (TODO)
        use_legacy_ai_pp_spend = False
        graphical_culture = 0
        graphical_culture_2d = 0


class FocusTree:
    ...

from pymunk import vec2d

class Moveable:
    def move(self, offset):
        raise NotImplementedError("Not implemented")
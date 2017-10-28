import operator


class CoordinateSystem:
    def __init__(self, position = (0, 0), scale = 1.0):
        self.position = position
        self.scale = scale

    def screen_to_world(self, vertex):
        return tuple(map(lambda x,y: (x + y) * self.scale, vertex, self.position))

    def world_to_screen(self, vertex):
        return tuple(map(lambda x,y: x/self.scale - y, vertex, self.position))

    def screen_to_world_scalar(self, scalar):
        return scalar * self.scale

    def world_to_screen_scalar(self, scalar):
        return scalar / self.scale

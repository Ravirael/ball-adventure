from coordinate_system import CoordinateSystem


class VerticesGetter:
    def __init__(self, shape, coordinate_system = CoordinateSystem()):
        self.shape = shape
        self.coordinate_system = coordinate_system

    def __call__(self):
        return [
            self.coordinate_system.world_to_screen(v.rotated(self.shape.body.angle) + self.shape.body.position)
            for v in self.shape.get_vertices()
        ]

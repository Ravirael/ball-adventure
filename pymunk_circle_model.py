from circle_model import CircleModel


class PymunkCircleModel(CircleModel):
    def __init__(self, pymunk_circle, coordinate_system):
        self.coordinate_system = coordinate_system
        self.shape = pymunk_circle

    def center(self):
        return self.coordinate_system.world_to_screen(self.shape.body.position)

    def radius(self):
        return self.coordinate_system.world_to_screen_scalar(self.shape.radius)

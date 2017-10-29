from circle_model import CircleModel


class ConstCircleModel(CircleModel):
    def __init__(self, position, radius, coordinate_system):
        self.coordinate_system = coordinate_system
        self.positon = position
        self.radius = radius

    def center(self):
        return self.coordinate_system.world_to_screen(self.position)

    def radius(self):
        return self.coordinate_system.world_to_screen_scalar(self.radius)

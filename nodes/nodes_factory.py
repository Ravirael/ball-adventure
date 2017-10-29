import pymunk

from collision_types import CollisionType
from nodes.circle import Circle
from nodes.polygon import Polygon
from nodes.target import Target
from pymunk_circle_model import PymunkCircleModel
from vertices_getter import VerticesGetter


class NodesFactory:
    def __init__(self, space, coordinate_system):
        self.space = space
        self.coordinate_system = coordinate_system

    def create_rect(
            self,
            width: int,
            height: int,
            body_type = pymunk.Body.KINEMATIC,
            position: (int, int) = (0, 0),
            elasticity: float = 1.0
    ) -> (Polygon, pymunk.Poly):
        body = pymunk.Body(1, 16000, body_type)
        body.position = position
        half_width = width/2
        half_height = height/2
        vertices = [
            (- half_width, - half_height),
            (half_width, - half_height),
            (half_width, half_height),
            (- half_width, half_height)
            ]
        pymunk_poly = pymunk.Poly(body, vertices)
        pymunk_poly.elasticity = elasticity
        self.space.add(body, pymunk_poly)
        return Polygon(VerticesGetter(pymunk_poly, self.coordinate_system)), pymunk_poly

    def create_circle(
            self,
            radius: int,
            position: (int, int) = (0, 0),
            body_type = pymunk.Body.DYNAMIC,
            elasticity: float = 1.0
    ) -> (Circle, pymunk.Circle):
        body = pymunk.Body(1, 16000, body_type)
        body.position = position
        circle = pymunk.Circle(body, radius)
        circle.elasticity = elasticity
        self.space.add(body, circle)
        return Circle(PymunkCircleModel(circle, self.coordinate_system)), circle

    def create_target(self) -> (Target, pymunk.Circle):
        body = pymunk.Body(1, 16000)
        body.body_type = pymunk.Body.STATIC
        circle = pymunk.Circle(body, 50)
        circle.elasticity = 1.0
        circle.collision_type = CollisionType.TARGET
        circle.sensor = True
        self.space.add(body, circle)
        model = PymunkCircleModel(circle, self.coordinate_system)
        return Target(model), circle
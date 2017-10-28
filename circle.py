import pygame
import pygame.gfxdraw
import pymunk

from pymun_circle_model import CircleModel
from scene_node import SceneNode
from vertices_getter import VerticesGetter


class Circle(SceneNode):
    def __init__(self, circle_model, draw_function = pygame.gfxdraw.circle, color = (255, 255, 255, 255)):
        self.circle_model = circle_model
        self.color = color
        self.draw_function = draw_function
        self.position = self.circle_model.center()
        self.radius = self.circle_model.radius()

    def update(self, dt):
        self.position = tuple(map(int, self.circle_model.center()))
        self.radius = int(self.circle_model.radius())

    def draw(self, screen):
        x, y = self.position
        self.draw_function(screen, int(x), int(y), int(self.radius), self.color)

    def circle(space, body, radius, coordinate_system):
        circle = pymunk.Circle(body, radius)
        circle.elasticity = 1.0
        space.add(body, circle)
        return Circle(CircleModel(circle, coordinate_system)), circle

    # def rectangle(space, body, size):
    #     return Polygon.rectangle(space=space, body=body, width=size[0], height=size[1])
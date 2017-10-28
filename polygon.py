import pygame
import pygame.gfxdraw
import pymunk

from scene_node import SceneNode
from vertices_getter import VerticesGetter


class Polygon(SceneNode):
    def __init__(self, vertices_getter, draw_function = pygame.gfxdraw.polygon, color = (255, 255, 255, 255)):
        self.__vertices_getter = vertices_getter
        self.__vertices = vertices_getter()
        self.color = color
        self.draw_function = draw_function

    def update(self, dt):
        self.__vertices = self.__vertices_getter()

    def draw(self, screen):
        self.draw_function(screen, self.__vertices, self.color)

    def rectangle(space, body, width, height, coordinate_system):
        half_width = width/2
        half_height = height/2
        vertices = [
            (- half_width, - half_height),
            (half_width, - half_height),
            (half_width, half_height),
            (- half_width, half_height)
            ]
        pymunk_poly = pymunk.Poly(body, vertices)
        pymunk_poly.elasticity = 1.0
        space.add(body, pymunk_poly)
        return (Polygon(VerticesGetter(pymunk_poly, coordinate_system)), pymunk_poly)

    # def rectangle(space, body, size):
    #     return Polygon.rectangle(space=space, body=body, width=size[0], height=size[1])
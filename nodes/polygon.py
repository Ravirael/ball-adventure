import pygame
import pygame.gfxdraw
from nodes.scene_node import SceneNode


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

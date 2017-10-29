from math import sin

import pygame
import pygame.gfxdraw

from nodes.circle import Circle
from nodes.scene_node import SceneNode


class Target(SceneNode):
    def __init__(self, circle_model):
        self.circle = Circle(circle_model=circle_model, draw_function=self.draw_handler, color=(255, 0, 255, 255))
        self.time = 0
        self.multiplier = 1

    def update(self, dt):
        self.circle.update(dt)
        self.time += dt
        self.multiplier = 1 + sin(self.time * 4) * 0.15

    def draw(self, screen):
        self.circle.draw(screen)

    def draw_handler(self, screen, x, y, radius, color):
        pygame.gfxdraw.circle(screen, x, y, int(self.multiplier * radius), color)

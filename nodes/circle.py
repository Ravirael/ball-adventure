import pygame
import pygame.gfxdraw
from nodes.scene_node import SceneNode


class Circle(SceneNode):
    def __init__(self, circle_model, draw_function = pygame.gfxdraw.filled_circle, color = (0, 0, 255, 255)):
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

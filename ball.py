import pygame
import pymunk

from scene_node import SceneNode


class Ball(SceneNode):
    def __init__(self, space):
        self.radius = 50
        self.body = pymunk.Body(1, 16000)
        self.body.position = 500.0, 100.0
        poly = pymunk.Circle(self.body, self.radius)  # Create a box shape and attach to body
        poly.elasticity = 1.0
        space.add(self.body, poly)

    def update(self, dt):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), tuple(map(lambda x: int(x), self.body.position)), self.radius)


import math

import pygame.gfxdraw

from nodes.scene_node import SceneNode


class PulsingCircle(SceneNode):
    def __init__(self, position, radius, amplitude, time_scale, time, color = (255, 255, 255, 255)):
        self.amplitude = amplitude
        self.time_scale = time_scale
        self.color = color
        self.position = tuple(map(int, position))
        self.radius = int(radius)
        self.multiplier = 1
        self.time = time

    def update(self, dt):
        self.time += dt
        self.multiplier = 1 + self.amplitude * (1 + math.sin(self.time * self.time_scale))/2

    def draw(self, screen):
        x, y = self.position
        pygame.gfxdraw.filled_circle(screen, int(x), int(y), int(self.radius * self.multiplier), self.color)
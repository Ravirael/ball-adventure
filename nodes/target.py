from math import sin

import pygame
import pygame.gfxdraw

from nodes.scene_node import SceneNode


def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect


class Target(SceneNode):
    def __init__(self, circle_model):
        self.circle = circle_model
        self.image = pygame.image.load("star.png")
        self.angle = 0

    def update(self, dt):
        self.angle += 90 * dt
        if self.angle > 360: self.angle -= 360

    def draw(self, screen):
        rect = self.image.get_rect()
        rect.center = self.circle.center()
        image, rect = rot_center(self.image, rect, self.angle)
        screen.blit(image, rect)

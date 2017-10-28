import pygame
import pymunk

from scene_node import SceneNode


class Wall(SceneNode):
    def __init__(self, space):
        self.radius = 50
        self.body = pymunk.Body(1, 16000, pymunk.Body.STATIC)
        self.body.position = 500.0, 400.0
        self.rect = pygame.Rect(self.body.position[0], self.body.position[1], 500, 50)
        poly = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))  # Create a box shape and attach to body
        poly.elasticity = 1.0
        self.body.angle = 45
        space.add(self.body, poly)

    def update(self, dt):
        #self.rect.centerx = self.body.position.x
        #self.rect.centery = self.body.position.y
        pass

    def draw(self, screen):
        surface = pygame.Surface(size = self.rect.size)
        pygame.draw.rect(surface, pygame.Color("white"), self.rect)
        pygame.transform.rotate(surface, self.body.angle)
        screen.blit(surface, (self.body.position.x, self.body.position.y))




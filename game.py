import pygame
import sys

from clock import Clock

class Game:
    def __init__(self,scene,width=1280,height=720):
        self.time_per_frame = 1.0/60.0
        self.screen = pygame.display.set_mode((width, height))
        self.scene = scene

    def run(self):
        clock = Clock()
        time_since_last_update = 0.0

        while True:
            elapsed = clock.restart()
            time_since_last_update += elapsed
            while time_since_last_update > self.time_per_frame:
                time_since_last_update -= self.time_per_frame
                self.process_events()
                self.update(self.time_per_frame)
            self.screen.fill(pygame.Color("black"))
            self.draw()
            pygame.display.flip()

    def update(self, dt):
        self.scene.update(dt)

    def draw(self):
        self.scene.draw(self.screen)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.scene.handle(event)
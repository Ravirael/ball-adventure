import pygame

from angle import Angle
from event_handlers.event_handler import EventHandler


class RotationHandler(EventHandler):
    def __init__(self, shape, coordinate_system, rotation = Angle.from_degrees(15)):
        self.shape = shape
        self.rotation = rotation
        self.coordinate_system = coordinate_system

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if self.shape.point_query(self.coordinate_system.screen_to_world(event.pos))[0] < 0:
                self.shape.body.angle += self.rotation
                return True
        return False


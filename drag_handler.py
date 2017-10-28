import pygame

from event_handler import EventHandler


class DragHandler(EventHandler):
    def __init__(self, shape, coordinate_system):
        self.shape = shape
        self.drag_started = False
        self.coordinate_system = coordinate_system

    def handle(self, event):
        print(self)
        if self.drag_started:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.drag_started = False
            elif event.type == pygame.MOUSEMOTION:
                position = (event.rel[0] * self.coordinate_system.scale, event.rel[1] * self.coordinate_system.scale)
                self.shape.body.position += position
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.shape.point_query(self.coordinate_system.screen_to_world(event.pos))[0] < 0:
                self.drag_started = True

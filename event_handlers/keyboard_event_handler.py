import pygame

from event_handlers.event_handler import EventHandler


class KeyboardEventHandler(EventHandler):
    def __init__(self, key_code: int, handler):
        self.key_code = key_code
        self.handler = handler

    def handle(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.KEYDOWN and event.key == self.key_code:
            self.handler()
            return True
        return False

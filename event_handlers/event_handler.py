import pygame


class EventHandler:
    def handle(self, event: pygame.event.Event) -> bool:
        raise NotImplementedError("EventHandler needs to implement handle method!")

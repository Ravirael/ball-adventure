import pygame
import random
from scene.scene import Scene
from scene.scenes import ScenesController


class WinScene(Scene):
    possible_texts = [
        "EPIC WIN!",
        "FANTASTIC!",
        "AWESOME!",
        "WOW!",
        "THAT'S NEAT!",
        "TERRIFIC!"
    ]

    def __init__(self, underlying_scene: Scene, scene_controller: ScenesController):
        self.underlying_scene = underlying_scene
        self.scene_controller = scene_controller
        font = pygame.font.SysFont("monospace", bold=True, size=96)
        self.text = font.render(random.choice(WinScene.possible_texts), 1, (0,255,255))

    def update(self, dt):
        self.underlying_scene.update(dt)

    def handle(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.KEYDOWN:
            self.scene_controller.pop()

    def draw(self, screen: pygame.Surface):
        self.underlying_scene.draw(screen)
        screen_width, screen_height = screen.get_size()
        text_width, text_height = self.text.get_size()
        screen.blit(self.text, (screen_width//2 - text_width//2, screen_height//2 - text_height//2))
import pygame

from event_handlers.keyboard_event_handler import KeyboardEventHandler
from scene.scene import Scene
from scene.scenes import ScenesController


class LevelSelectionScene(Scene):
    file_path = "level"

    def __init__(self, scene_controller: ScenesController):
        self.scene_controller = scene_controller
        with open(LevelSelectionScene.file_path) as file:
            self.current_level = int(file.read())
        self.selected_level = self.current_level
        self.font = pygame.font.SysFont("monospace", bold=True, size=96)
        self.level_text = None
        self.levels = []
        self.update_level_text()
        self.event_handlers = []
        self.event_handlers.append(
            KeyboardEventHandler(key_code=pygame.K_RIGHT, handler=self.select_next_level)
        )
        self.event_handlers.append(
            KeyboardEventHandler(key_code=pygame.K_LEFT, handler=self.select_prev_level)
        )
        self.event_handlers.append(
            KeyboardEventHandler(key_code=pygame.K_RETURN, handler=self.start_level)
        )

    def update_level_text(self):
        self.level_text = self.font.render(f"<< Level {self.selected_level} >>", 1, (0,255,255))

    def select_next_level(self):
        self.selected_level = self.selected_level + 1
        if self.selected_level > self.current_level:
            self.selected_level = 0
        self.update_level_text()

    def select_prev_level(self):
        self.selected_level = self.selected_level - 1
        if self.selected_level < 0:
            self.selected_level = self.current_level
        self.update_level_text()

    def level_won(self, level_number):
        if level_number == self.current_level and level_number < len(self.levels) - 1:
            self.current_level = self.current_level + 1
            self.selected_level = self.current_level
            self.update_level_text()
            with open(LevelSelectionScene.file_path, "w") as file:
                file.write(str(self.current_level))

    def start_level(self):
        self.scene_controller.push(self.levels[self.selected_level](self.selected_level, self.scene_controller, self.level_won))

    def draw(self, screen):
        screen_width, screen_height = screen.get_size()
        text_width, text_height = self.level_text.get_size()
        screen.blit(self.level_text, (screen_width//2 - text_width//2, screen_height//2 - text_height//2))

    def handle(self, event: pygame.event.Event) -> bool:
        for handler in self.event_handlers:
            if handler.handle(event):
                return True
        return False

    def update(self, dt):
        pass
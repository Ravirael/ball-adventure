import pymunk

from coordinate_system import CoordinateSystem
from event_handlers.event_handler import EventHandler
from nodes.scene_node import SceneNode
from scene.scene import Scene


class SetupScene(Scene):
    def __init__(
            self,
            coordinate_system: CoordinateSystem,
            space: pymunk.Space,
            nodes: [SceneNode],
            event_handlers: [EventHandler],
            ball_body: pymunk.Body
    ):
        self.coordinate_system = coordinate_system
        self.nodes = nodes
        self.event_handlers = event_handlers
        self.ball_body = ball_body
        self.space = space
        self.initial_ball_position = ball_body.position

    def handle(self, event):
        for handler in self.event_handlers:
            if handler.handle(event):
                return True
        return False

    def draw(self, screen):
        for node in self.nodes:
            node.draw(screen)

    def update(self, dt):
        self.space.step(dt)
        self.ball_body.position = self.initial_ball_position
        self.ball_body.velocity = (0, 0)
        for node in self.nodes:
            node.update(dt)

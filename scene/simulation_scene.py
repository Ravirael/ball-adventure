import pygame
import pymunk

from nodes.scene_node import SceneNode
from scene.scene import Scene
from scene.scenes import ScenesController


class SimulationScene(Scene):
    def __init__(self, space: pymunk.Space, nodes: [SceneNode], ball_body: pymunk.Body, scene_controller: ScenesController):
        self.space = space
        self.nodes = nodes
        self.ball_body = ball_body
        self.ball_initial_position = ball_body.position
        self.scene_controller = scene_controller

    def handle(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            self.reset()

    def draw(self, screen):
        for node in self.nodes:
            node.draw(screen)

    def update(self, dt):
        self.space.step(dt)
        for node in self.nodes:
            node.update(dt)
        if self.ball_body.position[1] > 4000:
            self.reset()

    def reset(self):
        self.ball_body.position = self.ball_initial_position
        self.ball_body.velocity = (0, 0)
        self.scene_controller.pop()

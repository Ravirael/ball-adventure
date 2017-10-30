import pygame
import pymunk

from angle import Angle
from collision_types import CollisionType
from coordinate_system import CoordinateSystem
from event_handlers.drag_handler import DragHandler
from event_handlers.keyboard_event_handler import KeyboardEventHandler
from event_handlers.rotation_handler import RotationHandler
from nodes.nodes_factory import NodesFactory
from nodes.circle import Circle
from scene.scene import Scene
from scene.scenes import Scenes
from scene.setup_scene import SetupScene
from scene.simulation_scene import SimulationScene
from scene.win_scene import WinScene


class LevelBuilder:

    def __init__(self, level_number, scene_controller):
        self.level_number = level_number
        self.scene_controller = scene_controller
        self.space = pymunk.Space()
        self.space.gravity = 0, 800
        self.coordinate_system = CoordinateSystem()
        self.nodes = []
        self.event_handlers = []
        self.nodes_factory = NodesFactory(space=self.space, coordinate_system=self.coordinate_system)
        self.win_callback = lambda x: None

        ball, circle = self.nodes_factory.create_ball(radius=16)
        self.ball_body = circle.body
        self.nodes.append(ball)

        self.event_handlers += [
        KeyboardEventHandler(
            key_code=pygame.K_SPACE,
            handler=lambda: self.scene_controller.push(
                SimulationScene(
                    ball_body=self.ball_body,
                    nodes=self.nodes,
                    space=self.space,
                    scene_controller=self.scene_controller
                )
            )
        ),
        KeyboardEventHandler(
            key_code=pygame.K_ESCAPE,
            handler=lambda: self.scene_controller.pop()
        )
        ]

        self.target, self.target_shape = self.nodes_factory.create_target()
        self.nodes.append(self.target)
        handler = self.space.add_collision_handler(CollisionType.BALL, CollisionType.TARGET)
        handler.pre_solve = self.on_win

    def set_win_callback(self, callback):
        self.win_callback = callback

    def on_win(self, x, y, z):
        game_scene = self.scene_controller.pop()
        game_scene.update_physics = False
        self.scene_controller.pop() #poping setup scene
        self.scene_controller.push(WinScene(game_scene, self.scene_controller))
        self.win_callback(self.level_number)
        return True

    def set_ball_position(self, position: (int, int)):
        self.ball_body.position = position

    def set_target_position(self, position: (int, int)):
        self.target_shape.body.position = position

    def create_static_obstacle(self, position: (int, int), size: (int, int), rotation: Angle = Angle.from_degrees(0), elasticity: float = 1.0):
        width, height = size
        node, shape = self.nodes_factory.create_rect(
            width=width,
            height=height,
            body_type=pymunk.Body.STATIC,
            position=position,
            rotation=rotation,
            elasticity=elasticity
        )
        self.nodes.append(node)

    def create_draggable_obstacle(self, position: (int, int), size: (int, int), rotation: Angle = Angle.from_degrees(0), elasticity: float = 1.0):
        width, height = size
        node, shape = self.nodes_factory.create_rect(
            width=width,
            height=height,
            body_type=pymunk.Body.KINEMATIC,
            position=position,
            elasticity=elasticity
        )
        node.color = (0, 255, 255, 255)
        shape.body.angle = rotation
        self.event_handlers.append(DragHandler(shape=shape, coordinate_system=self.coordinate_system))
        self.event_handlers.append(RotationHandler(shape=shape, coordinate_system=self.coordinate_system))
        self.nodes.append(node)

    def create_level(self) -> Scene:
        return SetupScene(
            ball_body=self.ball_body,
            space=self.space,
            nodes=self.nodes,
            event_handlers=self.event_handlers,
            coordinate_system=self.coordinate_system
        )

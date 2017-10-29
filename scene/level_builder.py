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


class LevelBuilder:

    def __init__(self):
        self.scene_controller = Scenes()
        self.space = pymunk.Space()
        self.space.gravity = 0, 800
        self.coordinate_system = CoordinateSystem()
        self.nodes = []
        self.event_handlers = []
        self.nodes_factory = NodesFactory(space=self.space, coordinate_system=self.coordinate_system)

        ball, circle = self.nodes_factory.create_circle(radius=20, body_type=pymunk.Body.DYNAMIC)
        circle.collision_type = CollisionType.BALL
        self.ball_body = circle.body

        self.nodes.append(ball)

        self.event_handlers += [KeyboardEventHandler(
            key_code=pygame.K_SPACE,
            handler=lambda: self.scene_controller.push(
                SimulationScene(
                    ball_body=self.ball_body,
                    nodes=self.nodes,
                    space=self.space,
                    scene_controller=self.scene_controller
                )
            )
        )]

        self.target, self.target_shape = self.nodes_factory.create_target()
        self.nodes.append(self.target)



        #self.space.add_collision_handler(CollisionType.BALL, CollisionType.TARGET)
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
            elasticity=elasticity
        )
        shape.body.angle = rotation
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
        shape.body.angle = rotation
        self.event_handlers.append(DragHandler(shape=shape, coordinate_system=self.coordinate_system))
        self.event_handlers.append(RotationHandler(shape=shape, coordinate_system=self.coordinate_system))
        self.nodes.append(node)

    def create_level(self) -> Scene:
        self.scene_controller.push(
            SetupScene(
                ball_body=self.ball_body,
                space=self.space,
                nodes=self.nodes,
                event_handlers=self.event_handlers,
                coordinate_system=self.coordinate_system
            )
        )
        return self.scene_controller
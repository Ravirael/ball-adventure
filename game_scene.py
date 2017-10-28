import pymunk

from angle import Angle
from ball import Ball
from coordinate_system import CoordinateSystem
from drag_handler import DragHandler
from drawable import Drawable
from polygon import Polygon
from circle import Circle
from rotation_handler import RotationHandler
from updatable import Updatable
from wall import Wall


class GameScene(Updatable, Drawable):
    def __init__(self):
        self.coordinate_system = CoordinateSystem(position=(-200, 0), scale=2)
        self._space = pymunk.Space()
        self._space.gravity = 0,800
        #self._nodes = [Ball(self._space)]

        body = pymunk.Body(1, 16000)
        body.position = 500.0, 100.0
        ball, circle = Circle.circle(self._space, body, 50, self.coordinate_system)
        self._nodes = [ball]

        body = pymunk.Body(1, 16000, pymunk.Body.KINEMATIC)
        body.position = 500.0, 400.0
        body.angle = Angle.from_degrees(45)
        poly, shape = Polygon.rectangle(space=self._space, body=body, width=500, height=30, coordinate_system=self.coordinate_system)
        self._nodes.append(poly)

        self._event_handlers = []
        self._event_handlers = [DragHandler(shape, self.coordinate_system)]

        body = pymunk.Body(1, 16000, pymunk.Body.KINEMATIC)
        body.position = 900.0, 400.0
        body.angle = Angle.from_degrees(-45)
        poly, shape = Polygon.rectangle(space=self._space, body=body, width=500, height=30, coordinate_system=self.coordinate_system)
        self._nodes.append(poly)

        self._event_handlers += [DragHandler(shape, self.coordinate_system)]
        self._event_handlers += [RotationHandler(shape, self.coordinate_system)]


    def draw(self, screen):
        [node.draw(screen) for node in self._nodes]

    def update(self, dt):
        self._space.step(dt)
        [node.update(dt) for node in self._nodes]

    def handle(self, event):
        print(event)
        [handler.handle(event) for handler in self._event_handlers]


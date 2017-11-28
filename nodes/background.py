from nodes.pulsing_circle import PulsingCircle
from nodes.scene_node import SceneNode
import random


class Background(SceneNode):

    def __init__(self):
        alpha = 15
        color_pool = [
            (255, 0, 0, alpha),
            (255, 0, 128, alpha),
            (255, 0, 255, alpha)
        ]
        self.children = []
        rng = random.Random()
        for i in range(0, 100):
            circle = PulsingCircle(
                position=(rng.randint(0, 1280), rng.randint(0, 720)),
                radius=rng.randint(10, 50),
                amplitude=rng.randint(1, 4),
                time_scale=rng.randint(10, 100)/100.0,
                time=rng.randint(0, 100),
                color=rng.choice(color_pool)
            )
            self.children.append(circle)

    def draw(self, screen):
        [child.draw(screen) for child in self.children]

    def update(self, dt):
        [child.update(dt) for child in self.children]
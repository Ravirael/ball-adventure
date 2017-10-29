import pygame

from angle import Angle
from game import Game
from level_generator import LevelDefinition
from scene.level_builder import LevelBuilder
from scene.level_selection import LevelSelectionScene
from scene.scenes import Scenes


pygame.init()

scene_controller = Scenes()
level_selection_scene = LevelSelectionScene(scene_controller)

level0 = LevelDefinition()
level0.static_objects = [
    {
        "position": (300, 500),
        "size": (400, 20)
    }
]
level0.draggable_objects = [
    {
        "position": (800, 500),
        "size": (400, 20),
        "rotation": Angle.from_degrees(90)
    }
]
level0.ball_position = (200, 200)
level0.target_position = (800, 400)

level_selection_scene.levels = [level0.create]

scene_controller.push(level_selection_scene)

game = Game(scene_controller)

game.run()
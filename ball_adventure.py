import pygame

from angle import Angle
from game import Game
from level_generator import LevelDefinition
from levels.levels import levels
from scene.level_builder import LevelBuilder
from scene.level_selection import LevelSelectionScene
from scene.scenes import Scenes


pygame.init()

scene_controller = Scenes()
level_selection_scene = LevelSelectionScene(scene_controller)

level_selection_scene.levels = [level.create for level in levels]

scene_controller.push(level_selection_scene)

game = Game(scene_controller)

game.run()
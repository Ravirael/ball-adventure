from angle import Angle
from scene.level_builder import LevelBuilder
from scene.level_selection import LevelSelectionScene
from scene.scenes import ScenesController


class LevelDefinition:
    def __init__(self):
        self.static_objects = []
        self.draggable_objects = []
        self.ball_position = (0, 0)
        self.target_position = (0,0)

    def create(self, level_number, scene_controller, win_callback):
        builder = LevelBuilder(level_number, scene_controller)
        builder.set_ball_position(self.ball_position)
        builder.set_target_position(self.target_position)

        for obstacle in self.static_objects:
            builder.create_static_obstacle(
                **obstacle
            )

        for obstacle in self.draggable_objects:
            builder.create_draggable_obstacle(
                **obstacle
            )

        builder.set_win_callback(win_callback)
        return builder.create_level()

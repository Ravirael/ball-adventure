from angle import Angle
from level_generator import LevelDefinition


level0 = LevelDefinition()
level0.draggable_objects = [
    {
        "position": (1000, 500),
        "size": (50, 20),
        "rotation": Angle.from_degrees(90)
    }
]
level0.ball_position = (400, 200)
level0.target_position = (800, 400)

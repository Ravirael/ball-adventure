from angle import Angle
from level_generator import LevelDefinition


level1 = LevelDefinition()
level1.draggable_objects = [
    {
        "position": (1000, 500),
        "size": (50, 20),
        "rotation": Angle.from_degrees(90)
    }
]
level1.static_objects = [
    {
        "position": (600, 500),
        "size": (400, 20),
        "rotation": Angle.from_degrees(90)
    }
]
level1.ball_position = (400, 200)
level1.target_position = (800, 400)

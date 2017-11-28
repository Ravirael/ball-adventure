from angle import Angle
from level_generator import LevelDefinition


level4 = LevelDefinition()
level4.draggable_objects = [
    {
        "position": (1000, 500),
        "size": (50, 20),
        "rotation": Angle.from_degrees(90)
    },
    {
        "position": (1040, 500),
        "size": (50, 20),
        "rotation": Angle.from_degrees(90)
    }
]
level4.static_objects = [
    {
        "position": (200, 75),
        "size": (800, 20),
        "rotation": Angle.from_degrees(30)
    },
    {
        "position": (800, 500),
        "size": (500, 20),
        "rotation": Angle.from_degrees(90)
    }
]
level4.ball_position = (200, 40)
level4.target_position = (200, 110)

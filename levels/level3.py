from angle import Angle
from level_generator import LevelDefinition


level3 = LevelDefinition()
level3.draggable_objects = [
    {
        "position": (1000, 500),
        "size": (50, 20),
        "rotation": Angle.from_degrees(90)
    },
    {
        "position": (1040, 500),
        "size": (50, 20),
        "rotation": Angle.from_degrees(90)
    },
    {
        "position": (1080, 500),
        "size": (50, 20),
        "rotation": Angle.from_degrees(90)
    }
]
level3.static_objects = [
    {
        "position": (600, 250),
        "size": (600, 20),
        "rotation": Angle.from_degrees(90)
    },
    {
        "position": (800, 450),
        "size": (600, 20),
        "rotation": Angle.from_degrees(90)
    },
    {
        "position": (840, 150),
        "size": (100, 20)
    }
]
level3.ball_position = (200, 50)
level3.target_position = (850, 200)

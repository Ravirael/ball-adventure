from angle import Angle
from level_generator import LevelDefinition


level2 = LevelDefinition()
level2.draggable_objects = [
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
level2.static_objects = [
    {
        "position": (600, 200),
        "size": (500, 20),
        "rotation": Angle.from_degrees(90)
    }
]
level2.ball_position = (400, 200)
level2.target_position = (700, 250)

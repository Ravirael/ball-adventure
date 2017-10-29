from angle import Angle
from game import Game
from scene.level_builder import LevelBuilder
from scene.scenes import Scenes

builder = LevelBuilder()
builder.set_ball_position((200, 200))
builder.set_target_position((400, 400))
builder.create_static_obstacle(
    position=(300, 500),
    size=(400, 20)
)
builder.create_draggable_obstacle(
    position=(500, 500),
    size=(400, 20),
    rotation=Angle.from_degrees(90)
)
builder.set_target_position((900, 400))
scene = Scenes()
game = Game(builder.create_level())

game.run()
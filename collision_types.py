from enum import IntEnum, unique


@unique
class CollisionType(IntEnum):
    BALL = 2,
    OBSTACLE = 3,
    TARGET = 4

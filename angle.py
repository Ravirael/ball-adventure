import math


class Angle(float):
    def __new__(cls, value, *args, **kwargs):
        return super(Angle, cls).__new__(cls, value)

    def to_degrees(self):
        return math.degrees(self)

    def to_radians(self):
        return self

    def from_degrees(degrees):
        return Angle(math.radians(degrees))

    def from_radians(radians):
        return Angle(radians)


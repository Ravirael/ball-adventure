from scene.scene import Scene


class ScenesController:
    def push(self, scene: Scene):
        raise NotImplementedError()

    def pop(self):
        raise NotImplementedError()

    def remove(self, scene: Scene):
        raise NotImplementedError()


class Scenes(Scene, ScenesController):
    def __init__(self):
        self.__scenes = []

    def handle(self, event):
        self.__scenes[-1].handle(event)

    def draw(self, screen):
        self.__scenes[-1].draw(screen)

    def update(self, dt):
        self.__scenes[-1].update(dt)

    def push(self, scene):
        self.__scenes.append(scene)

    def pop(self):
        return self.__scenes.pop()

    def remove(self, scene):
        return self.__scenes.remove(scene)

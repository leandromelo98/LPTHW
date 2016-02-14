# from python import exit and radom integer generator modules
from sys import exit
from random import randint

# class that has-a function "enter" that takes self parameter
class Scene(object):

    def enter(self):
        print "Unconfigured scene. Subclass it and implement enter()."
        exit(1)


# class with:
class Engine(object):

    # has-a _init_ that takes self and scene_map parameters;
    def __init__(self, scene_map):
        self.scene_map = scene_map

    # has-a function "play" that takes self as a parameter
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # print this out the last scene
        current_scene.enter()


# make a class "Death" that is-a "Scene" which has function "enter" with self parameter
class Death(Scene):

    quips = [
        "The scythe of death has reached you. Adios...",
         "Do better next time!",
         "You can do better than that! Come on!",
         "Our highly esteemed hero...Please try again and save the world!",
         "The icy cold clammy hand from underground dragged you to death...Bye...",
         "Hades has invited you to his kingdom where no one can escape back out again",
         "Welcome to eternal Tartarus...."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        pass


class LaserWeaponArmory(Scene):

    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

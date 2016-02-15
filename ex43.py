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
         "The icy cold clammy hand from underground dragged you to death..."
         "Bye...",
         "Hades has invited you to his kingdom where no one can escape back out",
         "Welcome to eternal Tartarus...."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


# make a class "CentralCorridor" that is-a "Scene" that has a function "enter"
class CentralCorridor(Scene):

    def enter(self):
        print "Hey Hercules!"
        print "The Titans of the Tartarus have invaded the Olympus!"
        print "Other gods have been killed or escaped. Even taken captive!"
        print "You are the chosen one to save the Olympus and your"
        print "mission is to get the 'Lightning Bolt' from Zeus's room,"
        print "strike the Titans with it,"
        print "and rescue the helpless gods and goddesses to the "
        print "top of the Olympus."
        print "\n"
        print "You are running down the streets of Oedipus"
        print "to head toward Mount Olympus."
        print "On the way to Olympus, you meet a one-eyed Cyclops."
        print "He approached you with green slimy skin, grinding his teeth,"
        print "drooling, and one eye."
        print "He's blocking the way to the Olympus. What would you do?"
        print "You have a sword and a shield that Athena gave you as gifts."
        print "Will you [fight him] or [run away] or [tell a joke] ?"

        action = raw_input("> ")

        if "run" in action:
            print "With your fastest run, you tried to escape!
            print "You ran as hard as you can!"
            print "The hungry Cyclops's not gonna miss you cuz he's hugggrryyy."
            print "While you ran a yard he ran a mile.
            print "Within a single blink of your eyes"
            print "he's in front of you.\n"
            print "'Hey, boy,' said he.\n"
            print "'Wut, wut is it!? What do you want from me!?,
            print "said Hercules.\n"
            print "'I'm going to eat you like a piece of cake."
            print "Yum,' replied the Cyclops.\n"
            print "Without letting you reply, he eats you. You are dead.  "
            return 'death'
        elif "fight" in action:
            print "Like the world's strongest demi-god, you fight."
            print "You draw your sword and dash toward him,"
            print "THUMP! You got his back.You first blind him with your sword."
            print "The cool blade creates an intersection with his neck."
            print "PSHSHSHSH."
            print "The spring of blood soaksyou."
            print "The big nuisance is down! You can proceed to Mount Olympus"
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'laser_weapon_armory'
        elif "tell" in action:
            print "You try to tell the Cyclops joke you know:"
            print "\n 'Wait, what languages does he speak?...hmmm...'\n "
            print "While you were thinking,"
            print "a humongous hand reached out to you."
            print "Grabbbb!!!!Squeeze!!!Too strong!!!!!"
            print "You can't move. Then, he swallowed you.\nDeath."
            return 'death'
        else:
            print "NO OTHER CHOICE. TRY AGAIN"
            return 'central_corridor'


# make a class "LaserWeaponArmory" that is-a "Scene" with a function "enter"
class LaserWeaponArmory(Scene):

    def enter(self):
        print "Here you are at the Mount Olympus."
        print "You see no one in the Counicl Square of the Olympus."
        print "You see no one in the room of Zeus."
        print "However, you see a golden chest."
        print "What will you do?"
        print "Will you [strike the chest] or [open the chest] or [move on]"

        do_what = raw_input("> ")

        if "strike" in do_what:
            print "Clang!....Nothing happened. Maybe too weak!"
            print "You got mad and striked the chest multiple times"
            print "Clang!"*4
            print "You striked the chest %d times." % (randint(1, 10000))
            print "You were too loud."
            print "The furious Titans came and dragged you to Tartarus."
            return 'death'
        elif "open" in do_what:
            print "All you had to do was just simply open!"
            print "You grabbed Zeus's Lightning Bolt"
            print "Now...."
            print "Hercules on the RESCUE!!!!"
            return 'the_bridge'
        elif "move" in do_what:
            print "When you came out, the Titans were walking by Zeus's room."
            print "They saw you and came after you."
            print "The cold blade of them went through your tummy."
            print "You DIED."
            return 'death'
        else:
            print "What you gonna do? Try again."
            return 'laser_weapon_armory'


# make a class "TheBridge" that is-a "Scene" with function "enter"
class TheBridge(Scene):

    def enter(self):
        print "Now with your Lightning Bolt, you came out of the room."
        print "You see those evil Titans trying to swallow the Olympus gods."
        print "You are so mad right now."
        print "What action do you take now?!"
        print "Will you [strike Titans with Lightning] or [strike the gods] or"
        print "[run away] ?"

        action = raw_input("> ")

        if "Titans" in action or "titans" in action:
            print "With your Pikachu Lightning Bolt, you strike the Titans!\n"
            print "'Pikachu, bolt attack!' roared Hercules.\n"
            print "The Titans fell down. They died because of electric shock"
            print "The cloaks of the gods and the goddesses"
            print "were made of rubber (inductor)"
            print "so they survived from the flowing electricity.\n"
            return 'escape_pod'

        elif "god" in action:
            print "The cloaks of the gods and the goddesses"
            print "were made of rubber (inductor)"
            print "so they survived from the flowing electricity.\n"
            print "Because you were foolish to attack your allies"
            print "instead of attacking the enemies,"
            print "your enemies swallowed your allies.\n"
            print "Now, they are coming after you"
            print "THUMP " * 8
            print "\nROOOOOOOOAAAAAAAAR\n"
            print "They got you! (Smiley Face)"
            return 'death'

        elif "run" in action:
            print "You abandoned the gods and the Olympus"
            print "You such a coward."
            print "The Titans killed every gods."
            print "Since the ferocious Titans are ruling the world as gods,"
            print "The earth committed suicide by destroying itself with its own"
            print "gravitational force."
            print "It became a blackhole, and everyone died."
            return 'death'

        else:
            print "NO OTHER CHOICE. TRY AGAIN!"
            return "the_bridge"


# make a class "EscapePod" that is-a "Scene" with function "enter"
class EscapePod(Scene):

    def enter(self):
        print "Now that all gods are saved,"
        print "you have go to the gate of Tartarus and close it again."
        print "You rush down the mountain desperately trying to make it to"
        print "the gate of Tartarus before the Titans regenerate
        print "and reappear on Olympus. You reach down to"
        print "the gate of Tartarus. When you were about to shut the gate,"
        print "you saw your mom in Tartarus."
        print "\nYou can hardly believe that she's in there,
        print "and you start to weep."
        print "What would you do?"
        print "Would you [shut the gate] for the world's sake? or"
        print "Would you [go in to meet your mom] for your sake?"

        hesitate = raw_input("> ")

        if "shut" in hesitate:
            print "You ignored your mom and shut the gate"
            print "You hear her cry,"
            print "but that's okay because you are such a nice son."
            print "GOOD JOB shutting your own mom off for the world's sake."
            print "Wheeeee~~~~You saved the world!"
            return 'finished'
        else:
            print "You jump into pod and met your mom."
            print "You approached her to hug her...."
            print "......"
            print "BUT THEN!!"
            print "She suddenly disappeared!"
            print "Oh man! It was a hallucination!"
            print "Since you failed to shut the gate,"
            print "the Titans conquered the world."
            print "Plus, you died."
            return 'death'


# make a class "running" that is-a "Scene"
class Running(Scene):

    def enter(self):
        print "You are being chased!"
        print "You are running!"
        print "Running" * (randint(1, 9))
        print "But eventually you were caught."
        print "You died"
        return 'death'


# make a class "Finished" that is-a "Scene"
class Finished(Scene):

    def enter(self):
        print "You saved the world!"
        print "Hurray! Victory is yours!"
        return 'finished'


# make a class "Map" that has-a:
class Map(object):

    # attribute
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
        'running': Running()
    }

    # _init_ with self and start_scene parameters
    def __init__(self, start_scene):
        self.start_scene = start_scene

    # function "next_scene" that takes self and scene_name parameters
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    # function "opening_scene" with self
    def opening_scene(self):
        return self.next_scene(self.start_scene)


# set "a_map" to an instance of class "Map" with central_corridor parameter
a_map = Map('central_corridor')
# set "a_game" to an instance of class "Engine" with "a_map" parameter
a_game = Engine(a_map)
# from class "a_game" get function "play" and run it!
a_game.play()

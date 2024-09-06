# Polymorphism allows methods to do different things based on the object it is acting upon.

class Bird:
    def make_sound(self):
        return "Chirp!"

class Parrot(Bird):
    def make_sound(self):
        return "Squawk!"

class Sparrow(Bird):
    def make_sound(self):
        return "Tweet!"

def animal_sound(animal):
    print(animal.make_sound())

parrot = Parrot()
sparrow = Sparrow()

animal_sound(parrot)  # Output: Squawk!
animal_sound(sparrow)  # Output: Tweet!
# Inheritance allows a class to inherit attributes and methods from another class.

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "Some sound"

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__("Cat")
        self.name = name
        self.age = age

    def make_sound(self):
        return f"{self.name} says Meow!"

cat1 = Cat("Whiskers", 2)
print(cat1.make_sound())  # Output: Whiskers says Meow!
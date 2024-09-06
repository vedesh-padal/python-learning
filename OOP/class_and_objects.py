# Classes are blueprints for creating objects (instances). Objects are instances of classes.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())  # Output: Buddy says Woof!
print(dog2.bark())  # Output: Max says Woof!
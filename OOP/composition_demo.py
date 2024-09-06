# Composition is a design principle where a class is composed of one or more objects from other classes.

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine()  # Car has an Engine

    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"

my_car = Car("Toyota", "Corolla")
print(my_car.start())  # Output: Toyota Corolla: Engine started
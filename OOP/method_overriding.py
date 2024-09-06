# Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass.

class Vehicle:
    def start(self):
        return "Vehicle is starting"

class Motorcycle(Vehicle):
    def start(self):
        return "Motorcycle is starting with a roar!"

vehicle = Vehicle()
motorcycle = Motorcycle()

print(vehicle.start())  # Output: Vehicle is starting
print(motorcycle.start())  # Output: Motorcycle is starting with a roar!
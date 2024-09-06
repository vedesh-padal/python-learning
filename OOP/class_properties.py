# Properties allow you to manage the access to an attribute through getter and setter methods.

class Person:
    def __init__(self, name):
        self._name = name  # Protected attribute

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError("Name must be a string")

person = Person("Alice")
print(person.name)  # Output: Alice
person.name = "Bob"
print(person.name)  # Output: Bob
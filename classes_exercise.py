# classes_exercise.py

"""
1. Create a class according to the following requirements:
It's name is Vehicle and it has the following attributes/methods:
Attributes/properties:
  name: str
  max_speed: int
  capacity: int
Methods:
    vroom() -> None
        Prints "Vroom" max_speed times
2. Create a child/subclass of Vehicle called Bus with the following methods:
Methods:
    fare(age: float) -> None
        Prints "The fare of the bus ride is {}."
            Price depends on age:
                0-17 years - Free
                18-60 years - $5
                61+ years - Free
"""

class Vehicle():
    def __init__(self):
        self.name = ""
        self.max_speed = max_speed
        self.capacity = capacity

    def vroom(self) -> None:
        return self.max_speed * 10

class Bus(Vehicle):
    def __init__(self, age):
        super().__init__()
        self.age = age

    def fare(self, age: float) -> None:
        if age < 18:
            print("The fare of the bus ride is $0")
        if age > 17 and age < 61:
            print("The fare of the bus ride is $5")
        if age > 60:
            print("The fare of the bus ride is $0")

bus = Vehicle("Bus", 10, 300)
bus.age = 13

a = Bus(29)
a.fare()


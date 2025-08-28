class Car:
    def move(self): print("Driving 🚗")

class Plane:
    def move(self): print("Flying ✈️")

class Dog:
    def move(self): print("Running 🐕")
    
class Bird:
    def move(self): print("Flapping wings 🐦")

class Boat:
    def move(self): print("Sailing 🚤")

class Fish:
    def move(self): print("Swimming 🐟")

class Python:
    def move(self): print("Slithering 🐍") 
# Polymorphic loop
for mover in [Car(), Plane(), Dog(), Bird(), Boat(), Fish()]:
    mover.move()
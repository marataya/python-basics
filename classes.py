import math
from tokenize import Name

class Orientation:
    pi = 3.14

    def __init__(self, x_pos, y_pos, degrees):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_dir, self.y_dir = self.getUnitVectorFromDegrees(degrees)

    @staticmethod
    def getUnitVectorFromDegrees(degrees):
        radians = (degrees/180) * Orientation.pi
        return math.sin(radians), -math.cos(radians)

    def getNextPos(self):
        return self.x_pos + self.x_dir, self.y_pos + self.y_dir

class Dog:
    _legs = 4

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " says Bark!")

    def getLegs(self):
        return self._legs


class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: Yap yap yap!')
    def wagTail(self):
        print('Wagging')


dog = Chihuahua('Roxy')

print(dog.speak())
print(Dog.speak(dog))
print(dog.wagTail())





orientation = Orientation(5, 5, 75)

print(orientation.getNextPos())

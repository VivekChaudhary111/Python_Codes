import random

class Dice:
    def __init__(self):
        self.sides = 6

    def roll(self):
        return random.randint(1, self.sides)
c1= Dice()
print(c1.roll())
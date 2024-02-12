# Design a class hierarchy for a zoo. Create a base class Animal with attributes like name,
# species, and age. Then, create derived classes for specific types of animals, such as Lion,
# Elephant, and Giraffe. Implement methods to display information specific to each type of
# animal.

class Animal:
    def __init__(self,name, species, age):
        self.name = name
        self.species = species
        self.age = age
    def display_info(self):
        return f'\nName: {self.name}\nspecies: {self.species}\nAge: {self.age}\n'


class Lion(Animal):
    def __init__(self,name, species, age):
        super().__init__(name, species, age)
        print("\nLion is the king of forest.")

class Elephant(Animal):
        def __init__(self,name, species, age):
            super().__init__(name, species, age)
            print("\nElephant is the largest animal.")
class Giraffe(Animal):
        def __init__(self,name, species, age):
            super().__init__(name, species, age)   
            print("\nGiraffe is the tallest animal.")
obj1 = Lion('Lion1', 'Asiatic', 10)
obj2 = Elephant('Elephant1', 'White', 15)
obj3 = Giraffe('Giraffe', 'African', 13)
print(obj1.display_info())

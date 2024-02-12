class shape:
    def __init__(self,side1, side2):
        self.side1 = side1
        self.side2 = side2
    def area(self):
        return self.side1 * self.side2
    def perimeter(self):
        return 2 * (self.side1 + self.side2)
    def length_diagonal(self):
        return (self.side1 **2 + self.side2 **2) ** 0.5

class Rectangle(shape):
    def __init__(self,length, breadth):
        super().__init__(length, breadth)
    
class Square(shape):
    def __init__(self, side):
        super().__init__(side, side)

# driver code      
l = int(input('Enter the length of the rectangle:'))
b = int(input('Enter the breadth of the rectangle:'))
rec = Rectangle(l,b)
area = rec.area()
peri = rec.perimeter()
diag = rec.length_diagonal()
print(f'Area of rectangle with given dimensions {l} and {b} is {area}')
print(f'Perimeter of rectangle with given dimensions {l} and {b} is {peri}')
print(f'Length of Diagonal of rectangle with given dimensions {l} and {b} is {round(diag, 2)}')
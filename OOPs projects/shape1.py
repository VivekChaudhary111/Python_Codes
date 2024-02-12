class Shape:
    def __init__(self):
        pass
    def square_area(self, x):
        print(f"Area of square: {x**2}")
    def rectangle_area(self, a, b):
        print(f"Area of rectangle: {a*b}")
    def circle_area(self, r):
        print(f"Area of circle: {3.14*(r**2)}")

areas = Shape()
areas.circle_area(37)
areas.rectangle_area(54,33)
areas.square_area(45)
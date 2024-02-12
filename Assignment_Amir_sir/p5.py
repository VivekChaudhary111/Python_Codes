class Car:
    def __init__(self, maker, model, color, park_time: float):
        self.maker = maker
        self.model = model
        self.color = color
        self.park_time = park_time
    def display_cars(self):
        print(f'''Maker: {self.maker}
Model: {self.model}
Color: {self.color}
Parking time(in hours): {self.park_time}''')
    
    def calc_rent_charges(self):
        base_charges = 50
        self.rental_charges = self.park_time*50 + base_charges
        print(f"Rental Charges: {self.rental_charges}")

car1 = Car('Mercedes', 'Benz', 'White', 2.5)
car2 = Car('BMW', 'competition', 'Black', 5)

car1.display_cars()
car1.calc_rent_charges()

car2.display_cars()
car2.calc_rent_charges()
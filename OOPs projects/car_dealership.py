class Car:
    def __init__(self, maker, name, model, year, price):
        self.maker = maker
        self.name = name
        self.model = model
        self.year = year
        self.price = price
        self.available = True
    def display_car(self):
        return f'''Maker: {self.maker}
Car Name: {self.name}
Model: {self.model}
Year: {self.year}
Price: {self.price}'''


class Dealership:
    def __init__(self, name):
        self.name = name
        self.inventory = []
    def add_car_to_inventory(self, car):
        self.inventory.append(car)
    def display_available_cars(self): 
        count = 1
        for car in self.inventory:
            if car.available:
                print(count)
                print(car.display_car())
                print('------\n')
                count+=1
    def sell_car(self, c, index):
        if 0 < index <= len(self.inventory) and self.inventory[index-1].available:
            c.purchase(self.inventory[index-1])
            return self.inventory[index-1]
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_car = []
    def purchase(self, car):
        self.purchased_car.append(car)
        car.available = False    


# Main code
car1 = Car('Honda','Delta', 'xtar',2015, 1200000)
car2 = Car('Tata','Harrier','xtech',2012, 2330000)
car3 = Car('BMW','Competition','M3',2013, 3000000)



d1 = Dealership('Varshney Motors')
d1.add_car_to_inventory(car1)
d1.add_car_to_inventory(car2)
d1.add_car_to_inventory(car3)

d1.display_available_cars()
custname = input("Enter the Customer name: ")
cnum =int(input(f"Enter the car number [1-{len(d1.inventory)}]"))
c1 = Customer(custname)
ret = d1.sell_car(c1, cnum)
if ret:
    print(f'{c1.name} purchased car\n{ret.display_car()}')
else:
    print('Car is not available')

print('\nAvailable cars after selling:')
d1.display_available_cars()
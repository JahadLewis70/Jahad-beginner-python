#Rental car
class vehicle:
    def calculate_rent(self, days):
        pass

class car(vehicle):
    def __init__(self, brand, daily_rate):
        self.brand = brand
        self.daily_rate = daily_rate
    def calculate_rent(self, days):
        return self.daily_rate * days + 50

class luxury(vehicle):
    def __init__(self, brand, daily_rate):
        self.brand = brand
        self.daily_rate = daily_rate
    def calculate_rent(self, days):
        return (self.daily_rate * days) + 100

car1 = car("Toyota", 50)
lux1 = luxury("BMW", 100)

class car2(vehicle):
    def calculate_rent(self, brand, daily_rate):
        self.brand = "Honda"
        self.daily_rate = 50
        return (self.daily_rate * daily_rate) + 50

class lux2(vehicle):
    def calculate_rent(self, brand, daily_rate):
        self.brand = "Lambo"
        self.daily_rate = 200
        return (self.daily_rate * daily_rate) + 200


print(car1.calculate_rent(5))
print(lux1.calculate_rent(10))


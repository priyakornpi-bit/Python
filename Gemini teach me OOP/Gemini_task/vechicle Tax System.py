from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @abstractmethod
    def get_vehicle_type(self):
        pass

    @abstractmethod
    def get_fuel_type(self):
        pass

    @abstractmethod
    def calculate_tax(self):
        pass

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
        print(f"Vehicle Type: {self.get_vehicle_type()}")
        print(f"Fuel Type: {self.get_fuel_type()}")
        print(f"Tax: {self.calculate_tax()}")

class Car(Vehicle):
    def __init__(self,brand, year):
        super().__init__(brand, year)

    def get_vehicle_type(self):
        return "Car"
    
    def get_fuel_type(self):
        return "Gasoline"
    
    def calculate_tax(self):
        return 2000
    
class ElectriCar(Vehicle):
    def __init__(self,brand, year):
        super().__init__(brand, year)

    def get_vehicle_type(self):
        return "Electric_Car"
    
    def get_fuel_type(self):
        return "Electricity"
    
    def calculate_tax(self):
        return 500
    
class NiggaAum(Vehicle):
    def __init__(self,brand,year):
        super.__init__()
        self.brand = brand
        self.year = year
    
    def get_vehicle_type(self):
        return "Electric_Car"
    
    def get_fuel_type(self):
        return "Electricity"
    
    def calculate_tax(self):
        return 500
    


# Example usage
v1 = Car("Toyota", 2020)
v2 = ElectriCar("Tesla", 2023)

v1.display_info()
v2.display_info()
from abc import ABC, abstractmethod

class Vehicle:
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
    print(f"Type: {self.get_vehicle_type()}")
    print(f"Fuel: {self.get_fuel_type()}")
    print(f"Tax: {self.calculate_tax()} THB")

class car:
    def __init__(self, brand, year, engine_cc):
        super().__init__(brand, year)
        self.enigine_cc = engine_cc

    def get_vechile_type(self):
        return "Car"
    
    def get_fuel_type(self):
        return "97  เต็มถัง"
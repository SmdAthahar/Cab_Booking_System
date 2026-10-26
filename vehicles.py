# Parent class

class Vehicle:

    def __init__(self, vehicle_number, brand, driver_name, price_per_km):

        self.vehicle_number = vehicle_number
        self.brand = brand
        self.driver_name = driver_name
        self.price_per_km = price_per_km



class Car(Vehicle):

    def __init__(self, vehicle_number, brand, driver_name, price_per_km):

        super().__init__(vehicle_number, brand, driver_name, price_per_km)



class Bike(Vehicle):

    def __init__(self, vehicle_number, brand, driver_name, price_per_km):

        super().__init__(vehicle_number, brand, driver_name, price_per_km)
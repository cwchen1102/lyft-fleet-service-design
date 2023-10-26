from car_factory import CarFactory
from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class calliopeFactory(CarFactory):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(current_date, last_service_date)
    def get_car(self):
        return Car(self.engine, self.battery)

class glissadeFactory(CarFactory):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(current_date, last_service_date)
    def get_car(self):
        return Car(self.engine, self.battery)

class palindromeFactory(CarFactory):
    def __init__(self, current_date, last_service_date, warning_light_is_on):
        self.engine = SternmanEngine(warning_light_is_on)
        self.battery = SpindlerBattery(current_date, last_service_date)
    def get_car(self):
        return Car(self.engine, self.battery)

class rorschachFactory(CarFactory):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = NubbinBattery(current_date, last_service_date)
    def get_car(self):
        return Car(self.engine, self.battery)

class thovexFactory(CarFactory):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = NubbinBattery(current_date, last_service_date)
    def get_car(self):
        return Car(self.engine, self.battery)    
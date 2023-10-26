from abc import ABC, abstractmethod

class CarFactory(ABC):
    @abstractmethod
    def get_car(self):
        pass
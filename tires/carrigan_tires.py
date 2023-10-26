from service import Service

class CarriganTires(Service):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        service = False
        for num in self.tire_wear:
            if num >= 0.9:
                service = True
                break      
        return service
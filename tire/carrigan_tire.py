class Carrigan_Tire(Battery):
    def __init__(self, tires_list: List[float]):
        self.tires_list = tires_list

    def needs_service(self):
       return any(tire >= 0.9 for tire in self.tires_list)
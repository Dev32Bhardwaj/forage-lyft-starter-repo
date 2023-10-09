class Octoprime_Tire(Battery):
    def __init__(self, tires_list: List[float]):
        self.tires_list = tires_list

    def needs_service(self):
       return sum(self.tires_list) >= 3
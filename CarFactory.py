import datetime.date as date
import car.Car as Car
from engine import *
from battery import *
from tire import *

class CarFactory:
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_list: List[float]):
        return Car(CapuletEngine(current_mileage,last_service_mileage), Spindler_Battery(last_service_date,current_date), Carrigan_Tire(tires_list))
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_list: List[float]):
        return Car(WilloughbyEngine(current_mileage,last_service_mileage), Spindler_Battery(last_service_date,current_date), Octoprime_Tire(tires_list))
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, tires_list: List[float]):
        return Car(SternmanEngine(warning_light_on), Spindler_Battery(last_service_date,current_date), Carrigan_Tire(tires_list))
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_list: List[float]):
        return Car(WilloughbyEngine(current_mileage,last_service_mileage), Nubbin_Battery(last_service_date,current_date), Octoprime_Tire(tires_list))
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_list: List[float]):
        return Car(CapuletEngine(current_mileage,last_service_mileage), Nubbin_Battery(last_service_date,current_date), Carrigan_Tire(tires_list))
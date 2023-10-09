# from abc import ABC, abstractmethod
import battery
import engine
import Serviceable
import tire

class Car(Serviceable.Serviceable):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self) -> bool:
        return self.battery.needs_service() or self.engine.needs_service() or self.tire.needs_service()
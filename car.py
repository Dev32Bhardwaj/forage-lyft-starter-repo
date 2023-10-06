# from abc import ABC, abstractmethod
import battery
import engine
import Serviceable

class Car(Serviceable.Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    def needs_service(self) -> bool:
        return self.battery.needs_service() or self.engine.needs_service()
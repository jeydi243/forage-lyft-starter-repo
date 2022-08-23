from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: battery):
        self.engine = engine
        self.battery = battery

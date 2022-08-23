from xmlrpc.client import DateTime

from car import Car


class CarFactory:
    def create_calliope(
        current_date: DateTime, last_service_date: DateTime, current_mileage: int, service_mileage: int
    ) -> Car:
        pass

    def create_glissage(
        current_date: DateTime, last_service_date: DateTime, current_mileage: int, service_mileage: int
    ) -> Car:
        pass

    def create_palindrome(current_date: DateTime, last_service_date: DateTime, warning_light_on: bool) -> Car:
        pass

    def create_rorschach(
        current_date: DateTime, last_service_date: DateTime, current_mileage: int, service_mileage: int
    ) -> Car:
        pass

    def create_thovex(
        current_date: DateTime, last_service_date: DateTime, current_mileage: int, service_mileage: int
    ) -> Car:
        pass

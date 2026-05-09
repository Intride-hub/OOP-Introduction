from base import Car
from models import ElectricCar, TruckCar, SportCar


class Fleet:
    def __init__(self):
        self._cars: list[Car] = []
        self._id_set: set = set()

    def add(self, car: Car):
        if not isinstance(car, Car):
            raise TypeError("Можно добавлять только объекты класса Car или его потомков")
        if car.id in self._id_set:
            raise ValueError(f"Автомобиль с id={car.id} уже есть в автопарке")
        self._cars.append(car)
        self._id_set.add(car.id)

    def remove(self, car: Car):
        if car in self._cars:
            self._cars.remove(car)
            self._id_set.discard(car.id)
        else:
            raise ValueError("Машины нет в автопарке")

    def get_all(self):
        return self._cars.copy()

    def find_by_id(self, car_id: int):
        for car in self._cars:
            if car.id == car_id:
                return car
        return None

    def find_by_brand(self, brand: str):
        return [c for c in self._cars if c.brand.lower() == brand.lower()]

    def __len__(self):
        return len(self._cars)

    def __iter__(self):
        return iter(self._cars)

    def __getitem__(self, index: int):
        return self._cars[index]

    def sort_by_speed(self, reverse: bool = False):
        self._cars.sort(key=lambda c: c.speed, reverse=reverse)

    def get_only_electric(self) -> "Fleet":
        """Вернуть подкоэ с только электромобилями."""
        result = Fleet()
        for car in self._cars:
            if isinstance(car, ElectricCar):
                result._cars.append(car)
                result._id_set.add(car.id)
        return result

    def get_only_trucks(self) -> "Fleet":
        """Вернуть подпарк только из грузовиков."""
        result = Fleet()
        for car in self._cars:
            if isinstance(car, TruckCar):
                result._cars.append(car)
                result._id_set.add(car.id)
        return result

    def get_only_sport(self) -> "Fleet":
        """Вернуть подпарк только из спорткаров."""
        result = Fleet()
        for car in self._cars:
            if isinstance(car, SportCar):
                result._cars.append(car)
                result._id_set.add(car.id)
        return result

    def get_cars_with_engine_on(self) -> "Fleet":
        result = Fleet()
        for car in self._cars:
            if car.engine_on:
                result._cars.append(car)
                result._id_set.add(car.id)
        return result

    def get_cars_with_low_fuel(self, threshold: int) -> "Fleet":
        result = Fleet()
        for car in self._cars:
            if car.fuel < threshold:
                result._cars.append(car)
                result._id_set.add(car.id)
        return result

    def __repr__(self):
        return f"Fleet({len(self)} cars)"

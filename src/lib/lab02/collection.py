from model import Car

class Fleet:
    def __init__(self):
        self._cars = []          
        self._id_set = set()     

    # Методы оценки 3
    def add(self, car: Car):
        if not isinstance(car, Car):
            raise TypeError("Можно добавлять только объекты класса Car")
        if car.id in self._id_set:
            raise ValueError(f"Автомобиль с id={car.id} уже есть в автопарке")
        self._cars.append(car)
        self._id_set.add(car.id)

    def remove(self, car: Car):
        if not isinstance(car, Car):
            raise TypeError("Можно удалять только объекты класса Car")
        if car in self._cars:
            self._cars.remove(car)
            self._id_set.discard(car.id)
        else:
            return ValueError('нет машины в списке')

    def get_all(self):
        return self._cars.copy()

    #  Методы оценки 4
    def find_by_id(self, car_id: int):
        for car in self._cars:
            if car.id == car_id:
                return car
        return None

    def find_by_brand(self, brand: str):
        brand_lower = brand.lower()
        return [car for car in self._cars if car.brand.lower() == brand_lower]

    def __len__(self):
        return len(self._cars)

    def __iter__(self):
        return iter(self._cars)

    #  Методы оценки 5 
    def __getitem__(self, index: int):
        return self._cars[index]

    def remove_at(self, index: int):
        if 0 <= index < len(self._cars):
            car = self._cars.pop(index)
            self._id_set.discard(car.id)
        else:
            raise IndexError("Индекс за пределами автопарка")

    def sort_by_speed(self, reverse: bool = False):
        self._cars.sort(key=lambda car: car.speed, reverse=reverse)

    def sort_by_brand(self, reverse: bool = False):
        self._cars.sort(key=lambda car: car.brand.lower(), reverse=reverse)

    def get_cars_with_engine_on(self):
        new_fleet = Fleet()
        for car in self._cars:
            if car.engine_on:
                new_fleet._cars.append(car)
                new_fleet._id_set.add(car.id)
        return new_fleet

    def get_cars_with_low_fuel(self, threshold: int):
        new_fleet = Fleet()
        for car in self._cars:
            if car.fuel < threshold:
                new_fleet._cars.append(car)
                new_fleet._id_set.add(car.id)
        return new_fleet

    def __repr__(self):
        return f"Fleet({len(self)} cars)"
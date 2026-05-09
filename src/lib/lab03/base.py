import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from lib.lab01.validators import _validate_brand, _validate_speed, _validate_capacity, _validate_fuel


class Car:
    """Базовый класс автомобиля (из ЛР-1, расширенная версия из ЛР-2)."""

    category = "Transport"

    def __init__(self, car_id: int, brand: str, speed: int, capacity: int, fuel: int):
        self._id = car_id
        self._brand = _validate_brand(brand)
        self._speed = _validate_speed(speed)
        self._capacity = _validate_capacity(capacity)
        self._fuel = _validate_fuel(fuel)
        self._engine_on = False

    # ---------- свойства ----------

    @property
    def id(self):
        return self._id

    @property
    def brand(self):
        return self._brand

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = _validate_speed(value)

    @property
    def capacity(self):
        return self._capacity

    @property
    def fuel(self):
        return self._fuel

    @property
    def engine_on(self):
        return self._engine_on

    # ---------- бизнес-методы ----------

    def start_engine(self):
        if self._fuel <= 0:
            raise RuntimeError("Двигатель не может быть запущен: нет топлива")
        self._engine_on = True

    def stop_engine(self):
        self._engine_on = False

    def drive(self, distance: int):
        if not self._engine_on:
            raise RuntimeError("Двигатель не запущен")
        fuel_needed = distance // 10
        if fuel_needed > self._fuel:
            raise RuntimeError("Недостаточно топлива для поездки")
        self._fuel -= fuel_needed

    # ---------- общий интерфейс (переопределяется в потомках) ----------

    def display(self) -> str:
        """Единый интерфейс отображения объекта. Полиморфный метод."""
        status = "заведён" if self._engine_on else "заглушен"
        return (
            f"[Car] {self.brand} (id={self.id}): "
            f"{self.speed} км/ч, {self.fuel} л, двигатель {status}"
        )

    def calculate(self) -> float:
        """Общий интерфейс расчёта стоимости/потенциала. Полиморфный метод."""
        return float(self._speed * self._capacity)

    # ---------- магические методы ----------

    def __str__(self):
        return self.display()

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, brand='{self._brand}', "
            f"speed={self._speed}, capacity={self._capacity}, fuel={self._fuel})"
        )

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return self.id == other.id
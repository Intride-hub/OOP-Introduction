import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from interfaces import Printable, Comparable, Diagnosable


# ──────────────────────────────────────────────
# Вспомогательные компоненты
# ──────────────────────────────────────────────

class Engine:
    def __init__(self, horsepower: int, oil_level: int = 100):
        self.horsepower = horsepower
        self.oil_level = oil_level
        self.is_running = False
        self.health = 100

    def start(self) -> None:
        self.is_running = True

    def stop(self) -> None:
        self.is_running = False

    def diagnose(self) -> dict:
        return {
            "horsepower": self.horsepower,
            "oil_level": self.oil_level,
            "is_running": self.is_running,
            "health": self.health,
        }


class FuelTank:
    def __init__(self, capacity: int, fuel_level: int):
        self.capacity = capacity
        self.fuel_level = fuel_level

    def consume(self, amount: int) -> None:
        self.fuel_level = max(0, self.fuel_level - amount)

    def refuel(self, amount: int) -> None:
        self.fuel_level = min(self.capacity, self.fuel_level + amount)

    def diagnose(self) -> dict:
        return {"capacity": self.capacity, "fuel_level": self.fuel_level}


class BrakeSystem:
    def __init__(self, pad_wear: int = 0):
        self.pad_wear = pad_wear

    def apply_brakes(self) -> None:
        print("Торможение выполнено.")

    def diagnose(self) -> dict:
        return {
            "pad_wear": self.pad_wear,
            "status": "ok" if self.pad_wear < 90 else "critical",
        }


# ──────────────────────────────────────────────
# Классы с интерфейсами
# ──────────────────────────────────────────────

class Car(Printable, Comparable, Diagnosable):
    """Автомобиль. Comparable по мощности двигателя."""

    def __init__(self, brand: str, model: str, engine: Engine,
                 fuel_tank: FuelTank, brakes: BrakeSystem):
        self.brand = brand
        self.model = model
        self._engine = engine
        self._fuel_tank = fuel_tank
        self._brakes = brakes
        self.speed = 0

    def to_string(self) -> str:
        return (f"Car({self.brand} {self.model}, "
                f"{self._engine.horsepower} л.с., "
                f"топливо={self._fuel_tank.fuel_level}/{self._fuel_tank.capacity} л)")

    def compare_to(self, other: "Car") -> int:
        a, b = self._engine.horsepower, other._engine.horsepower
        return (a > b) - (a < b)

    def diagnose(self) -> dict:
        return {
            "engine": self._engine.diagnose(),
            "fuel_tank": self._fuel_tank.diagnose(),
            "brakes": self._brakes.diagnose(),
        }

    def start(self) -> None:
        self._engine.start()
        print(f"{self.brand} {self.model} заведён.")

    def drive(self, distance: int) -> None:
        self._fuel_tank.consume(distance // 10 + 1)
        self.speed = 60
        print(f"{self.brand} {self.model} проехал {distance} км.")

    def stop(self) -> None:
        self._brakes.apply_brakes()
        self.speed = 0
        self._engine.stop()
        print(f"{self.brand} {self.model} остановлен.")


class ElectricCar(Printable, Comparable, Diagnosable):
    """Электромобиль. Comparable по запасу хода."""

    def __init__(self, brand: str, model: str, battery_kwh: float, km_range: int):
        self.brand = brand
        self.model = model
        self.battery_kwh = battery_kwh
        self.km_range = km_range
        self.charge_pct = 100

    def to_string(self) -> str:
        return (f"ElectricCar({self.brand} {self.model}, "
                f"{self.battery_kwh} кВт·ч, "
                f"запас={self.km_range} км, заряд={self.charge_pct}%)")

    def compare_to(self, other: "ElectricCar") -> int:
        a, b = self.km_range, other.km_range
        return (a > b) - (a < b)

    def diagnose(self) -> dict:
        return {
            "battery_kwh": self.battery_kwh,
            "km_range": self.km_range,
            "charge_pct": self.charge_pct,
        }

    def charge(self, pct: int) -> None:
        self.charge_pct = min(100, self.charge_pct + pct)
        print(f"{self.brand} {self.model} заряжен до {self.charge_pct}%.")


class Truck(Printable, Comparable, Diagnosable):
    """Грузовик. Comparable по грузоподъёмности."""

    def __init__(self, brand: str, model: str, engine: Engine,
                 fuel_tank: FuelTank, payload_ton: float):
        self.brand = brand
        self.model = model
        self._engine = engine
        self._fuel_tank = fuel_tank
        self.payload_ton = payload_ton

    def to_string(self) -> str:
        return (f"Truck({self.brand} {self.model}, "
                f"{self._engine.horsepower} л.с., "
                f"грузоподъёмность={self.payload_ton} т)")

    def compare_to(self, other: "Truck") -> int:
        a, b = self.payload_ton, other.payload_ton
        return (a > b) - (a < b)

    def diagnose(self) -> dict:
        return {
            "engine": self._engine.diagnose(),
            "fuel_tank": self._fuel_tank.diagnose(),
            "payload_ton": self.payload_ton,
        }


# ──────────────────────────────────────────────
# Коллекция
# ──────────────────────────────────────────────

class VehicleCollection:
    """Коллекция с поддержкой фильтрации по интерфейсу."""

    def __init__(self):
        self._items: list = []

    def add(self, vehicle) -> None:
        self._items.append(vehicle)

    def get_all(self) -> list:
        return list(self._items)

    def get_printable(self) -> list:
        return [v for v in self._items if isinstance(v, Printable)]

    def get_comparable(self) -> list:
        return [v for v in self._items if isinstance(v, Comparable)]

    def get_diagnosable(self) -> list:
        return [v for v in self._items if isinstance(v, Diagnosable)]

    def print_all(self) -> None:
        for item in self.get_printable():
            print(item.to_string())

    def diagnose_all(self) -> None:
        for item in self.get_diagnosable():
            label = item.to_string() if isinstance(item, Printable) else repr(item)
            print(f"\n[Диагностика] {label}")
            for k, v in item.diagnose().items():
                print(f"  {k}: {v}")

    def sort_by_compare(self) -> list:
        items = self.get_comparable()
        for i in range(1, len(items)):
            key = items[i]
            j = i - 1
            while j >= 0:
                try:
                    if items[j].compare_to(key) > 0:
                        items[j + 1] = items[j]
                        j -= 1
                    else:
                        break
                except Exception:
                    break
            items[j + 1] = key
        return items

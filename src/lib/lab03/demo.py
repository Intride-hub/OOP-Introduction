import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from base import Car
from models import ElectricCar, TruckCar, SportCar
from collection import Fleet




 
def separator(title: str):
    print(f"\n{'=' * 55}")
    print(f"  {title}")
    print('=' * 55)


# ──────────────────────────────────────────────
# Сценарий 1: Создание объектов и вывод display()
# ──────────────────────────────────────────────
separator("Сценарий 1 — Создание объектов, display()")

bmw = Car(1, "BMW", 200, 5, 60)
tesla = ElectricCar(2, "Tesla", 250, 5, 10, battery_capacity=100.0, charge_level=80.0)
scania = TruckCar(3, "Scania", 120, 2, 200, payload=20000, trailer_attached=True)
ferrari = SportCar(4, "Ferrari", 320, 2, 80, top_speed=400, turbo=True)

for vehicle in [bmw, tesla, scania, ferrari]:
    print(vehicle.display())

# ──────────────────────────────────────────────
# Сценарий 2: Полиморфизм — один метод calculate()
# ──────────────────────────────────────────────
separator("Сценарий 2 — Полиморфный calculate()")

cars = [bmw, tesla, scania, ferrari]
for vehicle in cars:
    print(f"{vehicle.brand:12s} → calculate() = {vehicle.calculate()}")

# ──────────────────────────────────────────────
# Сценарий 3: isinstance() — проверка типов
# ──────────────────────────────────────────────
separator("Сценарий 3 — isinstance() проверка типов")

for vehicle in cars:
    print(
        f"{vehicle.brand:12s}: "
        f"Car={isinstance(vehicle, Car)}, "
        f"ElectricCar={isinstance(vehicle, ElectricCar)}, "
        f"TruckCar={isinstance(vehicle, TruckCar)}, "
        f"SportCar={isinstance(vehicle, SportCar)}"
    )

# ──────────────────────────────────────────────
# Сценарий 4: Работа коллекции Fleet + фильтрация
# ──────────────────────────────────────────────
separator("Сценарий 4 — Fleet: добавление и фильтрация")

fleet = Fleet()
for vehicle in cars:
    fleet.add(vehicle)

print(f"Всего в автопарке: {len(fleet)} машин")

print("\n-- Только электромобили --")
for v in fleet.get_only_electric():
    print(" ", v.display())

print("\n-- Только грузовики --")
for v in fleet.get_only_trucks():
    print(" ", v.display())

print("\n-- Только спорткары --")
for v in fleet.get_only_sport():
    print(" ", v.display())

# ──────────────────────────────────────────────
# Сценарий 5: Полиморфизм без if/type — единый список
# ──────────────────────────────────────────────
separator("Сценарий 5 — Полиморфизм без условий")

print("Вызываем display() для каждого объекта через единый список:")
for vehicle in fleet:
    print(" ", vehicle.display())

print("\nВызываем calculate() для каждого объекта через единый список:")
for vehicle in fleet:
    print(f"  {vehicle.brand:12s}: {vehicle.calculate()}")

# ──────────────────────────────────────────────
# Сценарий 6: Уникальные методы дочерних классов
# ──────────────────────────────────────────────
separator("Сценарий 6 — Уникальные методы потомков")

print("Tesla: заряжаем батарею +15%")
print(f"  До зарядки:  заряд {tesla.charge_level:.1f}%")
tesla.charge(15)
print(f"  После зарядки: заряд {tesla.charge_level:.1f}%")

print("\nScania: прицепляем/отцепляем прицеп")
print(f"  До: {scania.display()}")
scania.detach_trailer()
print(f"  После отцепки: {scania.display()}")

print("\nFerrari: включаем турбо (уже включено), repr:")

print(f"  {repr(ferrari)}")

print(f"  {repr(ferrari)}")


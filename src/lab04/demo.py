from models import (
    Car, ElectricCar, Truck,
    Engine, FuelTank, BrakeSystem,
    VehicleCollection,
)
from interfaces import Printable, Comparable, Diagnosable


# ──────────────────────────────────────────────
# Универсальные функции через интерфейс
# ──────────────────────────────────────────────

def print_all(items: list) -> None:
    """Выводит объекты через интерфейс Printable."""
    for item in items:
        print(" ", item.to_string())


def find_max(items: list):
    """Возвращает наибольший объект через Comparable."""
    if not items:
        return None
    champion = items[0]
    for item in items[1:]:
        if champion.compare_to(item) < 0:
            champion = item
    return champion


def run_diagnostics(items: list) -> None:
    """Диагностика через интерфейс Diagnosable."""
    for item in items:
        label = item.to_string() if isinstance(item, Printable) else repr(item)
        print(f"  [{label}]")
        for k, v in item.diagnose().items():
            print(f"    {k}: {v}")


def sort_by_interface(items: list) -> list:
    """Сортировка через compare_to без isinstance внутри."""
    items = list(items)
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


# ──────────────────────────────────────────────
# Объекты
# ──────────────────────────────────────────────

car1   = Car("Toyota", "Camry", Engine(150), FuelTank(60, 50), BrakeSystem(10))
car2   = Car("BMW", "M5",       Engine(600), FuelTank(70, 65), BrakeSystem(20))
tesla  = ElectricCar("Tesla", "Model S", 100.0, 600)
byd    = ElectricCar("BYD",   "Han",      76.9, 550)
truck1 = Truck("Volvo", "FH16",  Engine(750), FuelTank(300, 250), 25.0)
truck2 = Truck("KAMAZ", "65201", Engine(400), FuelTank(250, 200), 20.0)


# ══ Сценарий 1: вывод через Printable ════════════════════════════
print("=" * 60)
print("Сценарий 1: вывод через интерфейс Printable")
print("=" * 60)
print_all([car1, car2, tesla, byd, truck1, truck2])


# ══ Сценарий 2: сортировка через Comparable ═══════════════════
print()
print("=" * 60)
print("Сценарий 2: сортировка Car по мощности через Comparable")
print("=" * 60)
for c in sort_by_interface([car2, car1]):
    print(" ", c.to_string())
print("Самый мощный:", find_max([car1, car2]).to_string())


# ══ Сценарий 3: диагностика через Diagnosable ═════════════════
print()
print("=" * 60)
print("Сценарий 3: диагностика через Diagnosable")
print("=" * 60)
run_diagnostics([car1, tesla, truck1])


# ══ Сценарий 4: isinstance-проверки ══════════════════════════
print()
print("=" * 60)
print("Сценарий 4: isinstance-проверки")
print("=" * 60)
for obj in [car1, tesla, truck1]:
    print(f"  {obj.to_string()}")
    print(f"    Printable:   {isinstance(obj, Printable)}")
    print(f"    Comparable:  {isinstance(obj, Comparable)}")
    print(f"    Diagnosable: {isinstance(obj, Diagnosable)}")


# ══ Сценарий 5: VehicleCollection ═══════════════════════════
print()
print("=" * 60)
print("Сценарий 5: VehicleCollection + фильтрация по интерфейсу")
print("=" * 60)

col = VehicleCollection()
for v in [car1, car2, tesla, byd, truck1, truck2]:
    col.add(v)

print("\n--- print_all() ---")
col.print_all()

print("\n--- diagnose_all() ---")
col.diagnose_all()

print("\n--- Лучший электромобиль по запасу хода ---")
ev_list = [v for v in col.get_comparable() if isinstance(v, ElectricCar)]
print(" ", find_max(ev_list).to_string())

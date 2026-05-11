# ЛР-4 — Интерфейсы и абстрактные классы (ABC)

## 1. Цель работы

Изучить механизм **абстрактных базовых классов (ABC)**. Освоить:
- создание интерфейсов через `ABC` и `@abstractmethod`;
- множественную реализацию интерфейсов;
- использование интерфейса как типа в функциях и коллекциях;
- полиморфизм без `if/isinstance` внутри бизнес-логики.

---

## 2. Описание интерфейсов

Файл: `interfaces.py`

| Интерфейс | Метод | Назначение |
|---|---|---|
| `Printable` | `to_string() -> str` | Строковое представление |
| `Comparable` | `compare_to(other) -> int` | Сравнение (-1 / 0 / 1) |
| `Diagnosable` | `diagnose() -> dict` | Техническое состояние |

---

## 3. Реализация в классах

Файл: `models.py`

| Класс | Интерфейсы | Особенность `compare_to` |
|---|---|---|
| `Car` | `Printable`, `Comparable`, `Diagnosable` | По мощности двигателя (л.с.) |
| `ElectricCar` | `Printable`, `Comparable`, `Diagnosable` | По запасу хода (км) |
| `Truck` | `Printable`, `Comparable`, `Diagnosable` | По грузоподъёмности (т) |

`VehicleCollection` расширяет коллекцию методами `get_printable()`, `get_comparable()`, `get_diagnosable()`, `print_all()`, `diagnose_all()`, `sort_by_compare()`.

---

## 4. Демонстрация

Файл `demo.py` содержит **5 сценариев**:

| Сценарий | Что демонстрирует |
|---|---|
| 1 | Вывод всех объектов через `Printable` |
| 2 | Сортировка `Car` через `Comparable` + `find_max` |
| 3 | Диагностика через `Diagnosable` |
| 4 | `isinstance`-проверки по всем интерфейсам |
| 5 | `VehicleCollection`: фильтрация, диагностика, лучший электромобиль |

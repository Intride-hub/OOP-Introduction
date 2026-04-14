# src/lib/lab02/demo.py

from model import Car
from collection import Fleet


def print_section(title: str):
    print("=" * 70)
    print(f"  {title}")
    print("=" * 70)


def print_subsection(title: str):
    print(f"\n--- {title} ---")


def scenario_1():
  
    print_section("СЦЕНАРИЙ 1: БАЗОВЫЕ ОПЕРАЦИИ С КОЛЛЕКЦИЕЙ")

    print_subsection("Создание автомобилей")
    car1 = Car(201, "Toyota Camry", 210, 5, 55)
    car2 = Car(202, "Honda Accord", 200, 5, 48)
    car3 = Car(203, "Ford Mustang", 280, 4, 35)
    car4 = Car(204, "Tesla Model 3", 260, 5, 90)

    print(f"  Созданы автомобили:")
    print(f"    {car1}")
    print(f"    {car2}")
    print(f"    {car3}")
    print(f"    {car4}")

    print_subsection("Добавление в коллекцию")
    fleet = Fleet()
    fleet.add(car1)
    fleet.add(car2)
    fleet.add(car3)
    fleet.add(car4)
    print(f"  Все автомобили добавлены в автопарк")


    print_subsection("Вывод всех элементов коллекции")
    print(f"  Всего автомобилей: {len(fleet)}")
    for i, car in enumerate(fleet, 1):
        print(f"    {i}. {car}")

    print_subsection("Проверка: добавление объекта неправильного типа")
    try:
        fleet.add("Это не автомобиль, а строка")
        print("  ❌ ОШИБКА: Неправильный объект был добавлен!")
    except TypeError as e:
        print(f"  ✅ Проверка типа сработала: {e}")

    try:
        fleet.add(12345)
        print("  ❌ ОШИБКА: Число было добавлено!")
    except TypeError as e:
        print(f"  ✅ Проверка типа сработала: {e}")

    print_subsection("Удаление элемента")
    print(f"  Удаляем автомобиль: {car2}")
    fleet.remove(car2)
    print(f"  Автомобиль удалён")

    print_subsection("Повторный вывод коллекции после удаления")
    print(f"  Всего автомобилей: {len(fleet)}")
    for i, car in enumerate(fleet, 1):
        print(f"    {i}. {car}")

    print_subsection("Проверка: удаление несуществующего элемента")
    print(f"  Пытаемся удалить уже удалённый автомобиль: {car2}")
    fleet.remove(car2) 
    print(f"  ✅ Удаление отработало корректно, коллекция не изменилась")
    print(f"  Текущий размер: {len(fleet)} автомобилей")

    return fleet


def scenario_2(fleet: Fleet):
    print_section("СЦЕНАРИЙ 2: ПОИСК, ИТЕРАЦИЯ И ОГРАНИЧЕНИЯ")

    car5 = Car(205, "BMW X5", 250, 5, 70)
    car6 = Car(206, "Audi Q7", 240, 7, 65)
    car7 = Car(207, "BMW M3", 290, 4, 40)
    fleet.add(car5)
    fleet.add(car6)
    fleet.add(car7)

    print_subsection("Текущий состав коллекции")
    for i, car in enumerate(fleet, 1):
        print(f"    {i}. {car}")
    print(f"  Всего: {len(fleet)} автомобилей")

    print_subsection("Поиск по id")
    search_ids = [203, 999, 205]
    for sid in search_ids:
        result = fleet.find_by_id(sid)
        if result:
            print(f"  Поиск id={sid}: ✅ {result}")
        else:
            print(f"  Поиск id={sid}: ❌ не найден")

    print_subsection("Поиск по марке")
    search_brands = ["BMW", "Toyota", "Lada"]
    for brand in search_brands:
        results = fleet.find_by_brand(brand)
        if results:
            print(f"  Поиск '{brand}': найдено {len(results)} шт.")
            for car in results:
                print(f"      - {car}")
        else:
            print(f"  Поиск '{brand}': ❌ не найдено")

    print_subsection("Использование len()")
    print(f"  Размер коллекции: {len(fleet)}")
    print(f"  (вызывается fleet.__len__())")

    print_subsection("Использование for")
    print("  Автомобили с запасом топлива > 50 л:")
    for car in fleet:
        if car.fuel > 50:
            print(f"    - {car.brand}: {car.fuel} л")

    print("\n  Статистика по скоростям:")
    speeds = [car.speed for car in fleet]
    print(f"    Максимальная скорость: {max(speeds)} км/ч")
    print(f"    Минимальная скорость: {min(speeds)} км/ч")
    print(f"    Средняя скорость: {sum(speeds) / len(speeds):.0f} км/ч")

    print_subsection("Ограничение на дубликаты (по id)")
    print("  Пытаемся добавить автомобиль с существующим id=201")
    duplicate_car = Car(201, "Lada Vesta", 180, 5, 50)

    try:
        fleet.add(duplicate_car)
        print("  ❌ ОШИБКА: Дубликат добавлен!")
    except ValueError as e:
        print(f"  ✅ Ограничение сработало: {e}")

    print(f"\n  Размер коллекции не изменился: {len(fleet)} автомобилей")

    return fleet


def scenario_3(fleet: Fleet):
    print_section("СЦЕНАРИЙ 3: ИНДЕКСАЦИЯ, СОРТИРОВКА И ФИЛЬТРАЦИЯ")

    print_subsection("Индексация коллекции")
    print(f"  Первый автомобиль: {fleet[0]}")
    print(f"  Второй автомобиль: {fleet[1]}")
    print(f"  Последний автомобиль: {fleet[-1]}")
    print(f"  Предпоследний автомобиль: {fleet[-2]}")


    print_subsection("Сортировка по скорости (по возрастанию)")
    fleet.sort_by_speed()
    print("  После сортировки по скорости:")
    for i, car in enumerate(fleet, 1):
        print(f"    {i}. {car.brand}: {car.speed} км/ч")

    print_subsection("Сортировка по скорости (по убыванию)")
    fleet.sort_by_speed(reverse=True)
    print("  Топ-3 самых быстрых автомобиля:")
    for i, car in enumerate(fleet[:3], 1):
        print(f"    {i}. {car.brand}: {car.speed} км/ч")

    print_subsection("Подготовка к фильтрации")
    fleet[0].start_engine()    
    fleet[2].start_engine()  
    fleet[4].start_engine()  

    print("  Запущены двигатели у:")
    for car in fleet:
        if car.engine_on:
            print(f"    - {car.brand} (готов к поездке)")

    print_subsection("Фильтрация: автомобили с заведённым двигателем")
    running_cars = fleet.get_cars_with_engine_on()
    print(f"  Найдено {len(running_cars)} автомобиля(ей):")
    for car in running_cars:
        print(f"    - {car}")

    print_subsection("Фильтрация: автомобили с малым запасом топлива (< 50 л)")
    low_fuel_cars = fleet.get_cars_with_low_fuel(50)
    print(f"  Найдено {len(low_fuel_cars)} автомобиля(ей):")
    for car in low_fuel_cars:
        print(f"    - {car.brand}: {car.fuel} л")

    print_subsection("Удаление по индексу")
    print(f"  Текущий размер коллекции: {len(fleet)}")
    print(f"  Удаляем автомобиль с индексом 2: {fleet[2]}")
    fleet.remove_at(2)
    print(f"  После удаления, размер коллекции: {len(fleet)}")
    print("  Оставшиеся автомобили:")

    for i, car in enumerate(fleet, 1):
        print(f"    {i}. {car}")

    return fleet


def main():
    fleet = scenario_1()
    fleet = scenario_2(fleet)
    fleet = scenario_3(fleet)
    
if __name__ == "__main__":
    main()
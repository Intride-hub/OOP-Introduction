from model import car

print("=== Создание машины ===")
car1 = car("Toyota", 120, 5, 50)
print(car1)

print("=== Сравнение машин ===")
car2 = car("Toyota", 120, 5, 30)
print(car1 == car2)

print("=== Ошибка валидации ===")
try:
    bad_car = car("", -100, 0, -5)
except Exception as e:
    print("Error:", e)

print("=== Ошибка состояния ===")
try:
    car3 = car("BMW", 200, 4, 0)
    car3.start_engine()
except Exception as e:
    print("Error:", e)

print("=== Работа setter ===")
car1.speed = 150
print(car1)

print("=== Атрибут класса ===")
print(car.category)
print(car1.category)

print("=== Работа состояния ===")
car1.start_engine()
car1.drive(50)
print("Fuel left:", car1.fuel)

car1.__repr__
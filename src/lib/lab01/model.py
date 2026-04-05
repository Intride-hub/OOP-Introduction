from validators import _validate_brand, _validate_speed, _validate_capacity, _validate_fuel


class car():
    category = "Transport"

    def __init__(self, brand: str, speed: int, capacity: int, fuel: int):
        self._brand = _validate_brand(brand)
        self._speed = _validate_speed(speed)
        self._capacity = _validate_capacity(capacity)
        self._fuel = _validate_fuel(fuel)
        self._engine_on =False
    
   
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
    
    def __str__(self):
        return f"{self.brand} : {self.speed} km/h : {self.fuel} L"
    
    def __repr__(self):
        return f"Car(brand='{self._brand}', speed={self._speed}, capacity={self._capacity}, fuel={self._fuel})"
    
    def __eq__(self, other):
        if not isinstance(other, car):
            return False
        return self._brand == other._brand and self._speed == other._speed
    
    

    def start_engine(self):
        if self._fuel <= 0:
            raise RuntimeError("не может быть запущен, нет топлива")
        self._engine_on = True

    def stop_engine(self):
        self._engine_on = False

    def drive(self, distance):
        if not self._engine_on:
            raise RuntimeError("двигатель включен")

        fuel_needed = distance // 10

        if fuel_needed > self._fuel:
            raise RuntimeError("недостаточно топлива")

        self._fuel -= fuel_needed


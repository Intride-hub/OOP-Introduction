class car():
    category = "Transport"

    def __init__(self, brand: str, speed: int, capacity: int, fuel: int):
        self._brand = self._validate_brand(brand)
        self._speed = self._validate_speed(speed)
        self._capacity = self._validate_capacity(capacity)
        self._fuel = self._validate_fuel(fuel)
        self._engine_on =False
    


    def _validate_brand(self,brand):
        if not isinstance(brand, str) or brand.strip() == '':
            raise ValueError("должно быть строкой, не должно быть пустым")
        return brand 
    
    def _validate_speed(self,speed):
        if not isinstance(speed, int) or speed<0:
            raise ValueError('скорость не может быть меньше 0')       
        return speed 
    
    def _validate_capacity(self, capacity):
        if not isinstance(capacity, int) or capacity<0:
            raise ValueError('вместимость > 0')
        return capacity
    
    def _validate_fuel(self, fuel):
        if not isinstance(fuel, int) or fuel <0:
            raise ValueError('топливо>0')
        return fuel
    
    @property
    def brand(self):
        return self._brand
    
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        self._speed = self._validate_speed(value)

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
    
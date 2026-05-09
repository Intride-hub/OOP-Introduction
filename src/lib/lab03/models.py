from base import Car


class ElectricCar(Car):
    """
    Электромобиль — дочерний класс Car.
    Новые атрибуты: battery_capacity (кВт·ч), charge_level (%).
    """

    def __init__(
        self,
        car_id: int,
        brand: str,
        speed: int,
        capacity: int,
        fuel: int,
        battery_capacity: float,
        charge_level: float,
    ):
        super().__init__(car_id, brand, speed, capacity, fuel)
        if battery_capacity <= 0:
            raise ValueError("Ёмкость батареи должна быть > 0")
        if not (0 <= charge_level <= 100):
            raise ValueError("Уровень заряда должен быть от 0 до 100")
        self._battery_capacity = battery_capacity
        self._charge_level = charge_level

    @property
    def battery_capacity(self):
        return self._battery_capacity

    @property
    def charge_level(self):
        return self._charge_level

    def charge(self, amount: float):
        """Зарядить батарею на amount процентов."""
        self._charge_level = min(100.0, self._charge_level + amount)

    def display(self) -> str:
        status = "заведён" if self.engine_on else "заглушен"
        return (
            f"[ElectricCar] {self.brand} (id={self.id}): "
            f"{self.speed} км/ч, батарея {self._battery_capacity} кВт·ч, "
            f"заряд {self._charge_level:.1f}%, двигатель {status}"
        )

    def calculate(self) -> float:
        """Оценка запаса хода: battery_capacity * charge_level / 10."""
        return round(self._battery_capacity * self._charge_level / 10, 2)


class TruckCar(Car):
    """
    Грузовик — дочерний класс Car.
    Новые атрибуты: payload (грузоподъёмность, кг), trailer_attached (прицеп).
    """

    def __init__(
        self,
        car_id: int,
        brand: str,
        speed: int,
        capacity: int,
        fuel: int,
        payload: int,
        trailer_attached: bool = False,
    ):
        super().__init__(car_id, brand, speed, capacity, fuel)
        if payload <= 0:
            raise ValueError("Грузоподъёмность должна быть > 0")
        self._payload = payload
        self._trailer_attached = trailer_attached

    @property
    def payload(self):
        return self._payload

    @property
    def trailer_attached(self):
        return self._trailer_attached

    def attach_trailer(self):
        """Прицепить прицеп."""
        self._trailer_attached = True

    def detach_trailer(self):
        """Отцепить прицеп."""
        self._trailer_attached = False

    def display(self) -> str:
        status = "заведён" if self.engine_on else "заглушен"
        trailer = "с прицепом" if self._trailer_attached else "без прицепа"
        return (
            f"[TruckCar] {self.brand} (id={self.id}): "
            f"{self.speed} км/ч, грузоп. {self._payload} кг, "
            f"{trailer}, двигатель {status}"
        )

    def calculate(self) -> float:
        """Стоимостной потенциал: payload * speed."""
        bonus = 1.2 if self._trailer_attached else 1.0
        return round(self._payload * self.speed * bonus, 2)


class SportCar(Car):
    """
    Спортивный автомобиль — дочерний класс Car.
    Новые атрибуты: turbo (турбонаддув), top_speed (максимальная скорость).
    """

    def __init__(
        self,
        car_id: int,
        brand: str,
        speed: int,
        capacity: int,
        fuel: int,
        top_speed: int,
        turbo: bool = False,
    ):
        super().__init__(car_id, brand, speed, capacity, fuel)
        if top_speed <= 0:
            raise ValueError("Максимальная скорость должна быть > 0")
        self._top_speed = top_speed
        self._turbo = turbo

    @property
    def top_speed(self):
        return self._top_speed

    @property
    def turbo(self):
        return self._turbo

    def activate_turbo(self):
        """Включить турбонаддув."""
        self._turbo = True

    def display(self) -> str:
        status = "заведён" if self.engine_on else "заглушен"
        turbo_str = "TURBO" if self._turbo else "без турбо"
        return (
            f"[SportCar] {self.brand} (id={self.id}): "
            f"{self.speed} км/ч, макс. {self._top_speed} км/ч, "
            f"{turbo_str}, двигатель {status}"
        )

    def calculate(self) -> float:
        """Спортивный рейтинг: top_speed * (2 if turbo else 1)."""
        multiplier = 2.0 if self._turbo else 1.0
        return round(self._top_speed * multiplier, 2)
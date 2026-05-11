from abc import ABC, abstractmethod


class Printable(ABC):
    """Интерфейс: объект умеет представить себя в виде строки."""

    @abstractmethod
    def to_string(self) -> str:
        """Возвращает строковое представление объекта."""
        ...


class Comparable(ABC):
    """Интерфейс: объект умеет сравнивать себя с другим."""

    @abstractmethod
    def compare_to(self, other: "Comparable") -> int:
        """
        Возвращает:
          -1 — если self < other
           0 — если self == other
           1 — если self > other
        """
        ...


class Diagnosable(ABC):
    """Интерфейс: объект умеет вернуть диагностическую информацию."""

    @abstractmethod
    def diagnose(self) -> dict:
        """Возвращает словарь с техническим состоянием объекта."""
        ...

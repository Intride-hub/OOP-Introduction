from abc import ABC, abstractmethod


class Printable(ABC):
    """Интерфейс: объект умеет представить себя в виде строки."""

    @abstractmethod
    def to_string(self) -> str:
        ...


class Comparable(ABC):
    """Интерфейс: объект умеет сравнивать себя с другим."""

    @abstractmethod
    def compare_to(self, other: "Comparable") -> int:
        """Возвращает: -1 | 0 | 1"""
        ...


class Diagnosable(ABC):
    """Интерфейс: объект умеет вернуть техническое состояние."""

    @abstractmethod
    def diagnose(self) -> dict:
        ...

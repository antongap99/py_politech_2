from typing import List


class PhysicalObject:
    """
    Абстрактный класс, который репрезентует физический объект.

    Attributes:
        mass (float): Массой физического объекта в килограммах.
        volume (float): Объем физического объекта в метрах в кубе.
        coordinates: coordinates (Tuple[float, float, float]) Координаты объекта

    Methods:
        move(self, destination: float) -> float:
            передвигает физический объект на заданное расстояние

        measure_temperature(self) -> float:
            измеряет температуру объекта

        interact_with_environment(self, time_interval: int) -> List[str]:
            взаимодействие с объектом
    """

    def __init__(self, mass: float, volume: float):
        """
        Объявление  PhysicalObject с переданной массой (mass) и объемом (volume).

        Args:
            mass (float): Массой физического объекта в килограммах.
            volume (float): Объем физического объекта в метрах в кубе.

        Raises:
            ValueError: Если масса отрицательна
        """
        self.mass = mass
        self.volume = volume
        if mass <= 0 or volume <= 0:
            raise ValueError("Mass and volume must be positive values.")

    def move(self, destination: str) -> float:
        """
        Переместите физический объект в указанное место назначения.

         Args:
         пункт назначения (str): пункт назначения, в который нужно переместить объект.

         Returns:
         float:  Результат перемещения.

        Examples:
            >>> obj = PhysicalObject(5.0, 2.0)
            >>> obj.move("Room 101")
            'Object moved to Room 101 successfully.'
        """
        return f'Object moved to {destination} successfully.'

    def measure_temperature(self) -> float:
        """
        Измерьте температуру физического объекта.

        Returns:
         float: Температура объекта в градусах Цельсия.
        Examples:
            >>> obj = PhysicalObject(5.0, 2.0)
            >>> obj.measure_temperature()
            25.0
        """
        # Placeholder implementation, actual implementation would involve temperature measurement
        return 25.0

    def interact_with_environment(self, time_interval: int) -> List[str]:
        """
        Имитировать взаимодействие физического объекта с окружающей средой в течение заданного интервала времени.

         Args:
         time_interval (int): Интервал времени для моделирования взаимодействия в секундах.

         Returns:
         List[str]: Список сообщений, описывающих взаимодействия во время моделирования.
        Simulate the interaction of the physical object with the environment over a given time interval.

        Examples:
            >>> obj = PhysicalObject(5.0, 2.0)
            >>> obj.interact_with_environment(10)
            ['Object exchanged heat with surroundings.', 'Object experienced external forces.']
        """
        return ['Object exchanged heat with surroundings.', 'Object experienced external forces.']


if __name__ == "__main__":
    doctest.testmod()

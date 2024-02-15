from typing import Union


# Базовый класс
class ElectronicDevice:
    def __init__(self, brand: str, model: str, price: float):
        """
        Конструктор базового класса ElectronicDevice.

        :param brand: Бренд устройства.
        :param model: Модель устройства.
        :param price: Цена устройства в долларах.
        """
        self._brand = brand
        self._model = model
        self._price = price

    @property
    def brand(self) -> str:
        """
        Свойство для получения бренда устройства.

        :return: Бренд устройства.
        """
        return self._brand

    @property
    def model(self) -> str:
        """
        Свойство для получения модели устройства.

        :return: Модель устройства.
        """
        return self._model

    @property
    def price(self) -> float:
        """
        Свойство для получения цены устройства.

        :return: Цена устройства в долларах.
        """
        return self._price

    def display_info(self) -> str:
        """
        Метод для отображения информации о устройстве.

        :return: Строка с информацией о бренде, модели и цене устройства.
        """
        return f"{self.brand} {self.model} - ${self.price}"

    def power_on(self) -> None:
        """
        Метод для включения устройства.

        Обычная реализация для базового класса, так как у каждого устройства
        может быть свой способ включения, но у них всегда есть какой-то общий
        функционал при включении.
        """
        print(f"{self.display_info()} is powered on.")


# Дочерниый класс

class Smartphone(ElectronicDevice):
    def __init__(self, brand: str, model: str, price: float, os: str):
        """
        Конструктор дочернего класса Smartphone.

        :param brand: Бренд смартфона.
        :param model: Модель смартфона.
        :param price: Цена смартфона в долларах.
        :param os: Операционная система смартфона.
        """
        super().__init__(brand, model, price)
        self._os = os

    @property
    def os(self) -> str:
        """
        Свойство для получения операционной системы смартфона.

        :return: Операционная система смартфона.
        """
        return self._os

    def make_call(self, number: str) -> None:
        """
        Метод для совершения звонка смартфоном.

        Перегруженный метод, так как здесь добавляется дополнительный функционал
        по сравнению с базовым классом.

        :param number: Номер телефона для звонка.
        """
        print(f"{self.display_info()} is making a call to {number}.")

    def power_on(self) -> None:
        """
        Перегруженный метод для включения смартфона.

        Добавлен вызов родительского метода и дополнительный функционал,
        специфичный для смартфона.

        """
        super().power_on()
        print(f"{self.model} is ready to use with {self.os}.")


phone = Smartphone('xiaomi', 'redmi note', 12000, 'android')
device = ElectronicDevice('xiaomi', 'redmi note', 12000)

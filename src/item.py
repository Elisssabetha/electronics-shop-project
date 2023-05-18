import csv
import os.path

PATH = os.path.join('..', 'src', 'items.csv')


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            raise ValueError('слишком длинное название')

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open(PATH, encoding='Windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                if len(list(csv.reader(csvfile))[0]) != 3:
                    raise InstantiateCSVError(f'Файл {PATH} поврежден')
                for item in reader:
                    if len(item['name']) < 10:
                        cls(item['name'], item['price'], item['quantity'])
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {PATH}')
            # print(f'Отсутствует файл {PATH}')


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @staticmethod
    def string_to_number(number):
        return int(float(number))

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise AttributeError

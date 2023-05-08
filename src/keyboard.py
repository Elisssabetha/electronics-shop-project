from src.item import Item


class KeyboardLanguage:
    def __init__(self):
        self.first_language = 'EN'
        self.second_language = 'RU'

    def change_lang(self):
        self.first_language, self.second_language = self.second_language, self.first_language
        Keyboard.__language = self.first_language
        return self


class Keyboard(Item, KeyboardLanguage):

    @property
    def language(self):
        return self.__language

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = self.first_language

    def change_lang(self):
        super().change_lang()
        self.__language = self.first_language
        return self








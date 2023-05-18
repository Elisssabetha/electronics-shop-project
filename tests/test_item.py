"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
import os

import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def class_example_fixture():
    return Item("Монитор", 15000, 6)


def test_calculate_total_price(class_example_fixture):
    assert class_example_fixture.calculate_total_price() == 90000


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name():
    item1 = Item('Монитор', 15000, 6)
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'
    # item1.name = 'суперСмартфон'
    # assert item1.name == 'суперСмартфон'
    with pytest.raises(ValueError):
        item1.name = 'суперсмартфон'


def test_repr():
    item1 = Item('Монитор', 15000, 6)
    assert repr(item1) == "Item('Монитор', 15000, 6)"


def test_str():
    item1 = Item('Монитор', 15000, 6)
    assert str(item1) == 'Монитор'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

    with pytest.raises(AttributeError):
        var = item1 + 5 == 25


def test_instantiate_from_csv():
    file = os.path.join('..', 'src', 'itms.csv')
    with pytest.raises(FileNotFoundError):
        with open(file, encoding='Windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)



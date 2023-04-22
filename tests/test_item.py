"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


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
    class_example_fixture.name = 'Смартфон'
    assert class_example_fixture.name == 'Смартфон'

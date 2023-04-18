"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
@pytest.fixture
def class_example_fixture():
    return Item("Монитор", 15000, 6)
def test_calculate_total_price(class_example_fixture):
    assert class_example_fixture.calculate_total_price() == 90000


import pytest

from src.phone import Phone


def test_init():
    phone1 = Phone("iPhone 11", 50000, 10, 1)
    assert phone1.name == 'iPhone 11'
    assert phone1.price == 50000
    assert phone1.quantity == 10
    assert phone1.number_of_sim == 1


def test_repr():
    phone1 = Phone("iPhone 11", 50000, 10, 1)
    assert repr(phone1) == "Phone('iPhone 11', 50000, 10, 1)"


def test_str():
    phone1 = Phone("iPhone 11", 50000, 10, 1)
    assert str(phone1) == 'iPhone 11'


def test_number_of_sim():
    phone1 = Phone("iPhone 11", 50000, 10, 1)
    phone1.number_of_sim = 2
    assert phone1.number_of_sim == 2

    with pytest.raises(ValueError):
        phone1.number_of_sim = 0

    with pytest.raises(ValueError):
        phone1.number_of_sim = 2.5

    with pytest.raises(ValueError):
        phone1.number_of_sim = -1






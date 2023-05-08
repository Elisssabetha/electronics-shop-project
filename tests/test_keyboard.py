from src.keyboard import Keyboard
import pytest

kb = Keyboard('Dark Project KD87A', 1000, 10)

def test_init():
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 1000
    assert kb.quantity == 10
    assert kb.language == 'EN'


def test_change_lang():
    assert kb.language == 'EN'
    kb.change_lang()
    assert kb.language == 'RU'


with pytest.raises(AttributeError):
    kb.language = 'DE'




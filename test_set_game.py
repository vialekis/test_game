import pytest
import set_game

def test_generator():
    for i in set_game.generator_cards(set_game.NUMBERS, set_game.SYMBOLS, set_game.SHADINGS, set_game.COLORS):
        assert isinstance(i,set_game.Card)

# def test_check_set():
#     assert set_game.check_set(set_game.generator_cards(set_game.NUMBERS, set_game.SYMBOLS, set_game.SHADINGS, set_game.COLORS))

def test_check_true():
    cards = set_game.check_set_true()
    for i in cards:
        assert set_game.check_set(i)

def test_check_false():
    cards = set_game.check_set_false()
    for i in cards:
        assert not set_game.check_set(i)

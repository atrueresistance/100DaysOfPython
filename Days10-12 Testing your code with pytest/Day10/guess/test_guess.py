from unittest.mock import patch
import pytest
import random
from Day10GuessRandom import get_random_number, Game


@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17


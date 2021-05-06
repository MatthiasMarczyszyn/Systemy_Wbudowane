import pytest

import Lab2


def test_char_counter_string():

    assert Lab2.char_counter_string("kupa") == {'k': 1, 'u': 1, 'p': 1, 'a': 1}

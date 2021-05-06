import pytest

import RPNCalculator as RPN

def test_RPNCalculator():
    assert RPN.RPNCalulator("3,3+") == 6
    assert RPN.RPNCalulator("3,3/") == 1
    assert RPN.RPNCalulator("3,3*") == 9
    assert RPN.RPNCalulator("3,3-") == 0
    assert RPN.RPNCalulator("5,3,2*+") == 11
    assert RPN.RPNCalulator("9,4/1,2+-") == -1
    assert RPN.RPNCalulator("1,2+3*6+2,3+/") == 3
    assert RPN.RPNCalulator("9,4+1-9,5/*7,2,8/--") == 5
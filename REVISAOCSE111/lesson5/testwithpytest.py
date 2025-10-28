from learningPytest import func, func2

import pytest

def test_func():

    assert func(3) == 8 

def test_func2():

    assert func2(15, 20) == 35
    assert func2(10, 15) == 25
    assert func2(0, 0) == 0


pytest.main(["-v", "--tb=line", "-rN", __file__])
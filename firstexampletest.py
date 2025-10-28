import pytest

def incremento(x):
    return (x) + 1

def test_incremento():
    assert incremento(3) == 5

pytest.main(["-v", "--tb=line", "-rN", __file__])

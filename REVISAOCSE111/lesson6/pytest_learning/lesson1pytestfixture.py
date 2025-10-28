import pytest

@pytest.fixture

def numbers():
    a = 10
    b = 20
    c = 25
    return [a, b, c] #retorna uma lista cujo indice sempre começa com 0 onde 0 = a, 1 = b e 2 = c

def test_method1(numbers):
    x = 10
    assert numbers[0] == x

def test_method2(numbers):
    y = 20
    assert numbers[1] == y

def test_method3(numbers):
    z = 25
    assert numbers[2] == z

pytest.main(["-v", "--tb=line", "-rN", __file__])

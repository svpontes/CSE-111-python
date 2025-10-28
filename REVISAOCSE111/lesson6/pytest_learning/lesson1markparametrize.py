import pytest
#---------------------------------->x   y   z     x   y   z
@pytest.mark.parametrize("x,y,z", [(10, 20,200),(20, 40, 800)])

def test_method1(x, y, z):
    assert x*y == z # assert 10 * 20 == 200  e assert 20 * 40 == 800
    assert z/y == x # assert 200/20 == 10 e assert 800/40 == 20
    


pytest.main(["-v", "--tb=line", "-rN", __file__])
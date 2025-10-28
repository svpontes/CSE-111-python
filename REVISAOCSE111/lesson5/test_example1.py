from example1 import cels_from_fahr
from pytest import approx
import pytest

def test_cels_from_fahr():

    assert cels_from_fahr(-28.5) == approx(-33.611111111111114)
    assert cels_from_fahr(0) == approx(-17.77778)
    assert cels_from_fahr(32) == approx(0)
    assert cels_from_fahr(70) == approx(21.1111)

pytest.main(["-v", "--tb=line", "-rN", __file__])
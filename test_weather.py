from weather import celsius_from_frh
import pytest
from pytest import approx

def test_celsius_from_fahr():
    assert celsius_from_frh(70) == approx(21.1111)

pytest.main(["-v", "--tb=line", "-rN", __file__])
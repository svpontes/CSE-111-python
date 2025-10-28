from can_size2_test import compute_cost_efficiency, compute_storage_efficiency, compute_surface_area, compute_volume
from pytest import approx
import pytest

def test_f():

    assert compute_volume(6.85, 10.16) == approx(1496.94036)

if __name__ == "__main__":
    
    pytest.main(["-v", "--tb=line", "-rN", __file__])

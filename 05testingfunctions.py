# test_weather.py

from test_sample import func
from pytest import approx
import pytest

def test_answer_func():

    assert func(3) == 5
      
pytest.main(["-v", "--tb=line", "-rN", __file__])
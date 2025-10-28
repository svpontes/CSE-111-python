from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():

    assert make_full_name ("Sally-Christina", "Brown Jhonson;") == "Brown Jhonson; Sally-Christina"

def test_extract_family_name():

    assert extract_family_name("Brown Jhonson; Sally-Christina") == "Brown Jhonson"

def test_extract_given_name():
    
    assert extract_given_name("Brown Jhonson; Sally-Christina") == "Sally-Christina"

pytest.main(["-v", "--tb=line", "-rN", __file__])
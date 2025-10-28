from address import extract_city, extract_state, extract_zipcode
import pytest

def extract_city():

    assert extract_city("525 South Center St, Rixburg, ID 83460") == "Rixburg"

def extract_state():

    assert extract_state("252 South Center St, Rixburg, ID 83460") == "ID"

pytest.main(["-v", "--tb=line", "-rN", __file__])

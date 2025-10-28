from  prefix import prefix
import pytest
def test_prefix():

    """
    verify if the prefix function works just fine
    """

    assert prefix("incovienient","inconsivalble") == "inco"
    assert prefix("plesume", "pleasure") == "ple"
    assert prefix("","") ==""
    assert prefix("casa","")==""

pytest.main(["-v", "--tb=line","-rN", __file__])
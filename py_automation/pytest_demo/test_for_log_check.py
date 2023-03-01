import pytest
from pytest_demo.Basefile_logging import Baseclass


@pytest.mark.usefixtures("dataload")
class Test_check3(Baseclass):
    def test_profile(self, dataload):
        log = self.getlogger()
        log.debug(dataload[0])
        print(dataload)

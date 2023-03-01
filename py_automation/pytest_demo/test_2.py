import pytest

from pytest_demo.Basefile_logging import Baseclass


class TestOne(Baseclass):

    def test_assert(self):
        log = self.getlogger()
        str = "hi"
        log.info("str:"+str)
        assert str == "hi"
        log.info("string match")

# @pytest.mark.smoke #marking the test method for custom mark 'smoke'
# def test_calc_mul():
#     a=9
#     b=4
#     print(a*b)

#pytest file name should start wih test_ or end with _test
#pytest script containing methods or function call and it is call test method it should named as testXXX
#all the method inside the scritpt start with test ,so that pytest will recognize
import pytest


def testfirstprogram(test_setup):
    print("Hello pytest")

@pytest.mark.xfail
def test_calc_add(test_setup):
    a=8
    b=3
    print(a+b)

@pytest.mark.smoke
def test_calc_div(test_setup):
   a=6
   b=2
   print(a//b)
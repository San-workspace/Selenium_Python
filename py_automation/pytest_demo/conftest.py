import pytest

@pytest.fixture()
def test_setup():
    print("i ill execute initially")
    yield
    print("i will execute finally")

@pytest.fixture()
def dataload():
    print("user profile")
    return("San", "deepu")

@pytest.fixture(params=(("chrome","San"),("firefox","msys"),("IE","QA")))
def crossbrowser(request):
    return request.param
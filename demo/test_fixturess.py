import pytest


@pytest.fixture()
def setup():
    print("this is before")
    yield
    print("this is after")

def test_case1(setup):
    print("this is test case 1")

def test_case2(setup):
    print("this is test case 2")
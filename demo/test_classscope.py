import pytest


@pytest.fixture(scope="class")
def setup():
    print("this is setup")

@pytest.mark.usefixtures("setup")
class TestDemo:
    def test_m1(self):
        print("this is test m1")
    def test_m2(self):
        print("this is test m2")
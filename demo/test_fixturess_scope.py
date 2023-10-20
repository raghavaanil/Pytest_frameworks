import pytest


@pytest.fixture(scope="function")
def login():
    print("this is login")


def test_case3(login):
    print("this is testcase 3")

def test_case4(login):
    print("this is testcase 4")
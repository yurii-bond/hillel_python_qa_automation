import pytest
from Lessons.lecture_18.app import calc


@pytest.fixture(scope='function')
def calculator():
    return calc.Calculator()


@pytest.fixture(scope='function')
def _calculator():
    return calc.Calculator()


@pytest.fixture(scope="function")
def _calc():
    print('Fixture object created from subdirectory')
    return calc.Calculator()
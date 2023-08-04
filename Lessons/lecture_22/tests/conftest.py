import pytest
from Lessons.lecture_18.app import calc


@pytest.fixture(scope="function")
def _calc():
    print('Fixture object created')
    return calc.Calculator()


@pytest.fixture(scope="function")
def _calc_():
    print('Fixture object created')
    return calc.Calculator()


@pytest.fixture
def calc_link():
    print('Return link to a Calculator class')
    return calc.Calculator


@pytest.fixture
def calc_link_call(calc_link):
    print('Make a call on a Calculator Class link. Creating Calculator Class object.')
    return calc_link()
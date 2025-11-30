import pytest
from target_functions import *

@pytest.mark.parametrize('kwargs', [
    {'a': -100, 'b': -100},
    {'a': -100, 'b': -90},
    {'a': -86, 'b': -100},
    {'a': -89, 'b': 0},
    {'a': 34, 'b': 100},
])
def test_add(kwargs):
    # Generated test for add
    try:
        add(**kwargs)
    except Exception as e:
        pytest.fail(f'Function add raised exception: {e}')

@pytest.mark.parametrize('kwargs', [
    {'a': -96.53434246737147, 'b': 36.290365391022874},
    {'a': 56.875011234332305, 'b': -56.384381894225164},
    {'a': -100.0, 'b': -46.34350303839258},
    {'a': 56.875011234332305, 'b': 100.0},
    {'a': 56.875011234332305, 'b': -46.34350303839258},
])
def test_divide(kwargs):
    # Generated test for divide
    try:
        divide(**kwargs)
    except Exception as e:
        pytest.fail(f'Function divide raised exception: {e}')

@pytest.mark.parametrize('kwargs', [
    {'name': '0z8c5'},
    {'name': '0z8c5'},
    {'name': 'ul'},
    {'name': '0z8c5'},
    {'name': 'ul'},
])
def test_greet(kwargs):
    # Generated test for greet
    try:
        greet(**kwargs)
    except Exception as e:
        pytest.fail(f'Function greet raised exception: {e}')

@pytest.mark.parametrize('kwargs', [
    {'age': 20},
    {'age': 60},
    {'age': 88},
    {'age': 20},
    {'age': 43},
])
def test_check_age(kwargs):
    # Generated test for check_age
    try:
        check_age(**kwargs)
    except Exception as e:
        pytest.fail(f'Function check_age raised exception: {e}')


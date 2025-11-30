import pytest
from target_functions import *

@pytest.mark.parametrize('kwargs', [
    {'_is_valid': True, 'a': 61, 'b': 0},
    {'_is_valid': True, 'a': 54, 'b': 100},
    {'_is_valid': True, 'a': -34, 'b': -29},
    {'_is_valid': True, 'a': 100, 'b': 38},
    {'_is_valid': True, 'a': -34, 'b': -30},
    {'_is_valid': False, 'a': 200, 'b': 100},
    {'_is_valid': False, 'a': -101, 'b': 100},
    {'_is_valid': False, 'b': 101, 'a': 0},
    {'_is_valid': False, 'b': 101, 'a': -90},
])
def test_add(kwargs):
    # Generated test for add
    is_valid = kwargs.pop('_is_valid', True)
    
    if is_valid:
        try:
            add(**kwargs)
        except Exception as e:
            pytest.fail(f'Function add raised exception on valid input: {e}')
    else:
        # Expect failure
        with pytest.raises(Exception):
            add(**kwargs)

@pytest.mark.parametrize('kwargs', [
    {'_is_valid': True, 'a': 49.27535269018955, 'b': -100.0},
    {'_is_valid': True, 'a': 59.62836068650975, 'b': -75.9497743182788},
    {'_is_valid': True, 'a': -69.25509674836456, 'b': 51.76955465395952},
    {'_is_valid': True, 'a': -100.0, 'b': 100.0},
    {'_is_valid': True, 'a': -100.0, 'b': -48.33943839493931},
    {'_is_valid': False, 'a': -100.1, 'b': -62.01223514743348},
    {'_is_valid': False, 'a': -100.1, 'b': 51.76955465395952},
    {'_is_valid': False, 'b': -100.1, 'a': 49.27535269018955},
    {'_is_valid': False, 'b': -200.0, 'a': 59.62836068650975},
])
def test_divide(kwargs):
    # Generated test for divide
    is_valid = kwargs.pop('_is_valid', True)
    
    if is_valid:
        try:
            divide(**kwargs)
        except Exception as e:
            pytest.fail(f'Function divide raised exception on valid input: {e}')
    else:
        # Expect failure
        with pytest.raises(Exception):
            divide(**kwargs)

@pytest.mark.parametrize('kwargs', [
    {'_is_valid': True, 'name': '6omh'},
    {'_is_valid': True, 'name': 'otr'},
    {'_is_valid': True, 'name': '6omh'},
    {'_is_valid': True, 'name': '8dp'},
    {'_is_valid': True, 'name': '99ct'},
    {'_is_valid': False, 'name': 'bbbbbbbbbbbbbbb'},
    {'_is_valid': False, 'name': 'bbbbbbbbbbbbbbb'},
])
def test_greet(kwargs):
    # Generated test for greet
    is_valid = kwargs.pop('_is_valid', True)
    
    if is_valid:
        try:
            greet(**kwargs)
        except Exception as e:
            pytest.fail(f'Function greet raised exception on valid input: {e}')
    else:
        # Expect failure
        with pytest.raises(Exception):
            greet(**kwargs)

@pytest.mark.parametrize('kwargs', [
    {'_is_valid': True, 'age': 59},
    {'_is_valid': True, 'age': -1},
    {'_is_valid': True, 'age': 130},
    {'_is_valid': True, 'age': 24},
    {'_is_valid': True, 'age': 43},
    {'_is_valid': False, 'age': 230},
    {'_is_valid': False, 'age': 131},
])
def test_check_age(kwargs):
    # Generated test for check_age
    is_valid = kwargs.pop('_is_valid', True)
    
    if is_valid:
        try:
            check_age(**kwargs)
        except Exception as e:
            pytest.fail(f'Function check_age raised exception on valid input: {e}')
    else:
        # Expect failure
        with pytest.raises(Exception):
            check_age(**kwargs)


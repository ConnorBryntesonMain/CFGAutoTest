# CFG Report for target_functions

## Function: `add`

### Parameter: `a`
- **Start Symbol**: `S`
- **Reasoning**: Integer type. Range: [-100, 100]. Samples generated uniformly.
- **Productions**:
    - `S -> -70`
    - `S -> -100`
    - `S -> 61`
    - `S -> -34`
    - `S -> -90`
    - `S -> 54`
    - `S -> 0`
    - `S -> 100`

### Parameter: `b`
- **Start Symbol**: `S`
- **Reasoning**: Integer type. Range: [-100, 100]. Samples generated uniformly.
- **Productions**:
    - `S -> -100`
    - `S -> -21`
    - `S -> 38`
    - `S -> 84`
    - `S -> -30`
    - `S -> 0`
    - `S -> 100`
    - `S -> -29`

## Function: `divide`

### Parameter: `a`
- **Start Symbol**: `S`
- **Reasoning**: Float type. Range: [-100.0, 100.0]. Samples generated uniformly.
- **Productions**:
    - `S -> 59.62836068650975`
    - `S -> -100.0`
    - `S -> -69.25509674836456`
    - `S -> 49.27535269018955`
    - `S -> 77.15390976574338`
    - `S -> -81.50393830739493`
    - `S -> 100.0`

### Parameter: `b`
- **Start Symbol**: `S`
- **Reasoning**: Float type. Range: [-100.0, 100.0]. Samples generated uniformly.
- **Productions**:
    - `S -> -75.9497743182788`
    - `S -> 51.76955465395952`
    - `S -> -62.01223514743348`
    - `S -> -100.0`
    - `S -> 17.839400248147072`
    - `S -> 100.0`
    - `S -> -48.33943839493931`

## Function: `greet`

### Parameter: `name`
- **Start Symbol**: `S`
- **Reasoning**: String type. Max Length: 5. Charset: alphanumeric. Samples generated randomly.
- **Productions**:
    - `S -> "otr"`
    - `S -> "99ct"`
    - `S -> "6omh"`
    - `S -> "wb"`
    - `S -> "8dp"`

## Function: `check_age`

### Parameter: `age`
- **Start Symbol**: `S`
- **Reasoning**: Integer type. Range: [-1, 130]. Samples generated uniformly.
- **Productions**:
    - `S -> 19`
    - `S -> 120`
    - `S -> 59`
    - `S -> 24`
    - `S -> 130`
    - `S -> -1`
    - `S -> 64`
    - `S -> 43`

## Detected Bugs / Test Results

```
============================= test session starts ==============================
platform linux -- Python 3.13.7, pytest-9.0.1, pluggy-1.6.0 -- /home/cjb/Documents/Code/CFGAutoTest/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/cjb/Documents/Code/CFGAutoTest
collecting ... collected 32 items

examples/target_functions_test.py::test_add[kwargs0] PASSED              [  3%]
examples/target_functions_test.py::test_add[kwargs1] PASSED              [  6%]
examples/target_functions_test.py::test_add[kwargs2] PASSED              [  9%]
examples/target_functions_test.py::test_add[kwargs3] PASSED              [ 12%]
examples/target_functions_test.py::test_add[kwargs4] PASSED              [ 15%]
examples/target_functions_test.py::test_add[kwargs5] FAILED              [ 18%]
examples/target_functions_test.py::test_add[kwargs6] FAILED              [ 21%]
examples/target_functions_test.py::test_add[kwargs7] FAILED              [ 25%]
examples/target_functions_test.py::test_add[kwargs8] FAILED              [ 28%]
examples/target_functions_test.py::test_divide[kwargs0] PASSED           [ 31%]
examples/target_functions_test.py::test_divide[kwargs1] PASSED           [ 34%]
examples/target_functions_test.py::test_divide[kwargs2] PASSED           [ 37%]
examples/target_functions_test.py::test_divide[kwargs3] PASSED           [ 40%]
examples/target_functions_test.py::test_divide[kwargs4] PASSED           [ 43%]
examples/target_functions_test.py::test_divide[kwargs5] FAILED           [ 46%]
examples/target_functions_test.py::test_divide[kwargs6] FAILED           [ 50%]
examples/target_functions_test.py::test_divide[kwargs7] FAILED           [ 53%]
examples/target_functions_test.py::test_divide[kwargs8] FAILED           [ 56%]
examples/target_functions_test.py::test_greet[kwargs0] PASSED            [ 59%]
examples/target_functions_test.py::test_greet[kwargs1] PASSED            [ 62%]
examples/target_functions_test.py::test_greet[kwargs2] PASSED            [ 65%]
examples/target_functions_test.py::test_greet[kwargs3] PASSED            [ 68%]
examples/target_functions_test.py::test_greet[kwargs4] PASSED            [ 71%]
examples/target_functions_test.py::test_greet[kwargs5] FAILED            [ 75%]
examples/target_functions_test.py::test_greet[kwargs6] FAILED            [ 78%]
examples/target_functions_test.py::test_check_age[kwargs0] PASSED        [ 81%]
examples/target_functions_test.py::test_check_age[kwargs1] FAILED        [ 84%]
examples/target_functions_test.py::test_check_age[kwargs2] FAILED        [ 87%]
examples/target_functions_test.py::test_check_age[kwargs3] PASSED        [ 90%]
examples/target_functions_test.py::test_check_age[kwargs4] PASSED        [ 93%]
examples/target_functions_test.py::test_check_age[kwargs5] PASSED        [ 96%]
examples/target_functions_test.py::test_check_age[kwargs6] PASSED        [100%]

=================================== FAILURES ===================================
______________________________ test_add[kwargs5] _______________________________

kwargs = {'a': 200, 'b': 100}

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
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:26: Failed
______________________________ test_add[kwargs6] _______________________________

kwargs = {'a': -101, 'b': 100}

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
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:26: Failed
______________________________ test_add[kwargs7] _______________________________

kwargs = {'a': 0, 'b': 101}

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
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:26: Failed
______________________________ test_add[kwargs8] _______________________________

kwargs = {'a': -90, 'b': 101}

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
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:26: Failed
_____________________________ test_divide[kwargs5] _____________________________

kwargs = {'a': -100.1, 'b': -62.01223514743348}

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
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:51: Failed
_____________________________ test_divide[kwargs6] _____________________________

kwargs = {'a': -100.1, 'b': 51.76955465395952}

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
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:51: Failed
_____________________________ test_divide[kwargs7] _____________________________

kwargs = {'a': 49.27535269018955, 'b': -100.1}

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
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:51: Failed
_____________________________ test_divide[kwargs8] _____________________________

kwargs = {'a': 59.62836068650975, 'b': -200.0}

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
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:51: Failed
_____________________________ test_greet[kwargs5] ______________________________

kwargs = {'name': 'bbbbbbbbbbbbbbb'}

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
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:74: Failed
_____________________________ test_greet[kwargs6] ______________________________

kwargs = {'name': 'bbbbbbbbbbbbbbb'}

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
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:74: Failed
___________________________ test_check_age[kwargs1] ____________________________

kwargs = {'age': -1}

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
>               check_age(**kwargs)

examples/target_functions_test.py:92: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

age = -1

    def check_age(age: int):
        """Checks if age is valid."""
        if age < 0:
>           raise ValueError("Age cannot be negative")
E           ValueError: Age cannot be negative

examples/target_functions.py:18: ValueError

During handling of the above exception, another exception occurred:

kwargs = {'age': -1}

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
>               pytest.fail(f'Function check_age raised exception on valid input: {e}')
E               Failed: Function check_age raised exception on valid input: Age cannot be negative

examples/target_functions_test.py:94: Failed
___________________________ test_check_age[kwargs2] ____________________________

kwargs = {'age': 130}

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
>               check_age(**kwargs)

examples/target_functions_test.py:92: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

age = 130

    def check_age(age: int):
        """Checks if age is valid."""
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 120:
>           raise ValueError("Age too high")
E           ValueError: Age too high

examples/target_functions.py:20: ValueError

During handling of the above exception, another exception occurred:

kwargs = {'age': 130}

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
>               pytest.fail(f'Function check_age raised exception on valid input: {e}')
E               Failed: Function check_age raised exception on valid input: Age too high

examples/target_functions_test.py:94: Failed
=========================== short test summary info ============================
FAILED examples/target_functions_test.py::test_add[kwargs5] - Failed: DID NOT...
FAILED examples/target_functions_test.py::test_add[kwargs6] - Failed: DID NOT...
FAILED examples/target_functions_test.py::test_add[kwargs7] - Failed: DID NOT...
FAILED examples/target_functions_test.py::test_add[kwargs8] - Failed: DID NOT...
FAILED examples/target_functions_test.py::test_divide[kwargs5] - Failed: DID ...
FAILED examples/target_functions_test.py::test_divide[kwargs6] - Failed: DID ...
FAILED examples/target_functions_test.py::test_divide[kwargs7] - Failed: DID ...
FAILED examples/target_functions_test.py::test_divide[kwargs8] - Failed: DID ...
FAILED examples/target_functions_test.py::test_greet[kwargs5] - Failed: DID N...
FAILED examples/target_functions_test.py::test_greet[kwargs6] - Failed: DID N...
FAILED examples/target_functions_test.py::test_check_age[kwargs1] - Failed: F...
FAILED examples/target_functions_test.py::test_check_age[kwargs2] - Failed: F...
======================== 12 failed, 20 passed in 0.08s =========================


```

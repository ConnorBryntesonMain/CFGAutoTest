# CFG Report for target_functions

## Function: `add`

### Parameter: `a`
- **Start Symbol**: `S`
- **Reasoning**: Integer type. Range: [-100, 100]. Samples generated uniformly.
- **Productions**:
    - `S -> 57`
    - `S -> -40`
    - `S -> 48`
    - `S -> 100`
    - `S -> 30`
    - `S -> -100`
    - `S -> 0`
    - `S -> -41`

### Parameter: `b`
- **Start Symbol**: `S`
- **Reasoning**: Integer type. Range: [-100, 100]. Samples generated uniformly.
- **Productions**:
    - `S -> -66`
    - `S -> 58`
    - `S -> 100`
    - `S -> 98`
    - `S -> -100`
    - `S -> 0`
    - `S -> 76`

## Function: `divide`

### Parameter: `a`
- **Start Symbol**: `S`
- **Reasoning**: Float type. Range: [-100.0, 100.0]. Samples generated uniformly.
- **Productions**:
    - `S -> 16.200943935103496`
    - `S -> 1.8280843846884665`
    - `S -> -100.0`
    - `S -> -68.43709266255145`
    - `S -> -93.34848181008897`
    - `S -> 10.594161950805955`
    - `S -> 100.0`

### Parameter: `b`
- **Start Symbol**: `S`
- **Reasoning**: Float type. Range: [-100.0, 100.0]. Samples generated uniformly.
- **Productions**:
    - `S -> 54.732899862884864`
    - `S -> -61.88974481834286`
    - `S -> -100.0`
    - `S -> -40.09754562579464`
    - `S -> 78.7975274514229`
    - `S -> -25.661652515310436`
    - `S -> 100.0`

## Function: `greet`

### Parameter: `name`
- **Start Symbol**: `S`
- **Reasoning**: String type. Max Length: 5. Charset: alphanumeric. Samples generated randomly.
- **Productions**:
    - `S -> "6csid"`
    - `S -> "5yz1"`
    - `S -> "euuw"`
    - `S -> "dk1l"`
    - `S -> "0"`

## Function: `check_age`

### Parameter: `age`
- **Start Symbol**: `S`
- **Reasoning**: Integer type. Range: [-1, 130]. Samples generated uniformly.
- **Productions**:
    - `S -> 47`
    - `S -> 28`
    - `S -> 41`
    - `S -> 88`
    - `S -> 0`
    - `S -> -1`
    - `S -> 64`
    - `S -> 130`

## Function: `solve_quadratic`

### Parameter: `a`
- **Start Symbol**: `S`
- **Reasoning**: Float type. Range: [-10.0, 10.0]. Samples generated uniformly.
- **Productions**:
    - `S -> 10.0`
    - `S -> 8.437785602473667`
    - `S -> 7.96289970187734`
    - `S -> -2.0414739940551936`
    - `S -> -10.0`
    - `S -> 6.7728000163553865`
    - `S -> 7.855719411846987`

### Parameter: `b`
- **Start Symbol**: `S`
- **Reasoning**: Float type. Range: [-10.0, 10.0]. Samples generated uniformly.
- **Productions**:
    - `S -> -7.23788688170665`
    - `S -> 10.0`
    - `S -> 2.8954299458492976`
    - `S -> 1.3209488265010663`
    - `S -> 5.861797996569907`
    - `S -> -9.518278041164281`
    - `S -> -10.0`

### Parameter: `c`
- **Start Symbol**: `S`
- **Reasoning**: Float type. Range: [-10.0, 10.0]. Samples generated uniformly.
- **Productions**:
    - `S -> -0.18210431935722227`
    - `S -> 10.0`
    - `S -> -6.407219104304205`
    - `S -> -7.039896007606603`
    - `S -> -10.0`
    - `S -> -4.235904262307624`
    - `S -> -9.662920836907734`

## Function: `process_order`

### Parameter: `quantity`
- **Start Symbol**: `S`
- **Reasoning**: Integer type. Range: [1, 100]. Samples generated uniformly.
- **Productions**:
    - `S -> 50`
    - `S -> 70`
    - `S -> 100`
    - `S -> 6`
    - `S -> 39`
    - `S -> 1`
    - `S -> 3`

### Parameter: `price`
- **Start Symbol**: `S`
- **Reasoning**: Float type. Range: [0.1, 1000.0]. Samples generated uniformly.
- **Productions**:
    - `S -> 1000.0`
    - `S -> 359.59221383006803`
    - `S -> 0.1`
    - `S -> 718.2201298591339`
    - `S -> 707.1327348965718`
    - `S -> 35.81692138573593`
    - `S -> 982.5090119586471`

### Parameter: `member`
- **Start Symbol**: `S`
- **Reasoning**: Boolean type. Values: True, False.
- **Productions**:
    - `S -> True`
    - `S -> False`

## Function: `validate_username`

### Parameter: `username`
- **Start Symbol**: `S`
- **Reasoning**: String type. Max Length: 15. Charset: alphanumeric. Samples generated randomly.
- **Productions**:
    - `S -> "z"`
    - `S -> "8"`
    - `S -> "glpatd"`
    - `S -> "q9fkdmmlrukv"`
    - `S -> "2q0evs5pqxs3c"`

## Detected Bugs / Test Results

**Status**: Unknown Status

| Test Case | Line | Failure Reason |
| :--- | :--- | :--- |
| `test_add[kwargs5]` | 26 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_add[kwargs6]` | 26 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_add[kwargs7]` | 26 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_add[kwargs8]` | 26 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_divide[kwargs5]` | 51 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_divide[kwargs6]` | 51 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_divide[kwargs7]` | 51 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_divide[kwargs8]` | 51 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_greet[kwargs5]` | 74 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_greet[kwargs6]` | 74 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_check_age[kwargs3]` | 92 | ValueError: Age too high |
| `test_solve_quadratic[kwargs1]` | 119 | ValueError: Discriminant is negative, no real roots. |
| `test_solve_quadratic[kwargs2]` | 119 | ValueError: Discriminant is negative, no real roots. |
| `test_solve_quadratic[kwargs5]` | 124 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_solve_quadratic[kwargs6]` | 124 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_solve_quadratic[kwargs7]` | 124 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_solve_quadratic[kwargs8]` | 124 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_process_order[kwargs7]` | 151 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_process_order[kwargs9]` | 151 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_process_order[kwargs10]` | 151 | Failed: DID NOT RAISE <class 'Exception'> |
| `test_validate_username[kwargs0]` | 169 | ValueError: Username too short. |
| `test_validate_username[kwargs2]` | 169 | ValueError: Username too short. |


<details>
<summary>Raw Test Output</summary>

```
============================= test session starts ==============================
platform linux -- Python 3.13.7, pytest-9.0.1, pluggy-1.6.0 -- /home/cjb/Documents/Code/CFGAutoTest/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/cjb/Documents/Code/CFGAutoTest
collecting ... collected 61 items

examples/target_functions_test.py::test_add[kwargs0] PASSED              [  1%]
examples/target_functions_test.py::test_add[kwargs1] PASSED              [  3%]
examples/target_functions_test.py::test_add[kwargs2] PASSED              [  4%]
examples/target_functions_test.py::test_add[kwargs3] PASSED              [  6%]
examples/target_functions_test.py::test_add[kwargs4] PASSED              [  8%]
examples/target_functions_test.py::test_add[kwargs5] FAILED              [  9%]
examples/target_functions_test.py::test_add[kwargs6] FAILED              [ 11%]
examples/target_functions_test.py::test_add[kwargs7] FAILED              [ 13%]
examples/target_functions_test.py::test_add[kwargs8] FAILED              [ 14%]
examples/target_functions_test.py::test_divide[kwargs0] PASSED           [ 16%]
examples/target_functions_test.py::test_divide[kwargs1] PASSED           [ 18%]
examples/target_functions_test.py::test_divide[kwargs2] PASSED           [ 19%]
examples/target_functions_test.py::test_divide[kwargs3] PASSED           [ 21%]
examples/target_functions_test.py::test_divide[kwargs4] PASSED           [ 22%]
examples/target_functions_test.py::test_divide[kwargs5] FAILED           [ 24%]
examples/target_functions_test.py::test_divide[kwargs6] FAILED           [ 26%]
examples/target_functions_test.py::test_divide[kwargs7] FAILED           [ 27%]
examples/target_functions_test.py::test_divide[kwargs8] FAILED           [ 29%]
examples/target_functions_test.py::test_greet[kwargs0] PASSED            [ 31%]
examples/target_functions_test.py::test_greet[kwargs1] PASSED            [ 32%]
examples/target_functions_test.py::test_greet[kwargs2] PASSED            [ 34%]
examples/target_functions_test.py::test_greet[kwargs3] PASSED            [ 36%]
examples/target_functions_test.py::test_greet[kwargs4] PASSED            [ 37%]
examples/target_functions_test.py::test_greet[kwargs5] FAILED            [ 39%]
examples/target_functions_test.py::test_greet[kwargs6] FAILED            [ 40%]
examples/target_functions_test.py::test_check_age[kwargs0] PASSED        [ 42%]
examples/target_functions_test.py::test_check_age[kwargs1] PASSED        [ 44%]
examples/target_functions_test.py::test_check_age[kwargs2] PASSED        [ 45%]
examples/target_functions_test.py::test_check_age[kwargs3] FAILED        [ 47%]
examples/target_functions_test.py::test_check_age[kwargs4] PASSED        [ 49%]
examples/target_functions_test.py::test_check_age[kwargs5] PASSED        [ 50%]
examples/target_functions_test.py::test_check_age[kwargs6] PASSED        [ 52%]
examples/target_functions_test.py::test_solve_quadratic[kwargs0] PASSED  [ 54%]
examples/target_functions_test.py::test_solve_quadratic[kwargs1] FAILED  [ 55%]
examples/target_functions_test.py::test_solve_quadratic[kwargs2] FAILED  [ 57%]
examples/target_functions_test.py::test_solve_quadratic[kwargs3] PASSED  [ 59%]
examples/target_functions_test.py::test_solve_quadratic[kwargs4] PASSED  [ 60%]
examples/target_functions_test.py::test_solve_quadratic[kwargs5] FAILED  [ 62%]
examples/target_functions_test.py::test_solve_quadratic[kwargs6] FAILED  [ 63%]
examples/target_functions_test.py::test_solve_quadratic[kwargs7] FAILED  [ 65%]
examples/target_functions_test.py::test_solve_quadratic[kwargs8] FAILED  [ 67%]
examples/target_functions_test.py::test_solve_quadratic[kwargs9] PASSED  [ 68%]
examples/target_functions_test.py::test_solve_quadratic[kwargs10] PASSED [ 70%]
examples/target_functions_test.py::test_process_order[kwargs0] PASSED    [ 72%]
examples/target_functions_test.py::test_process_order[kwargs1] PASSED    [ 73%]
examples/target_functions_test.py::test_process_order[kwargs2] PASSED    [ 75%]
examples/target_functions_test.py::test_process_order[kwargs3] PASSED    [ 77%]
examples/target_functions_test.py::test_process_order[kwargs4] PASSED    [ 78%]
examples/target_functions_test.py::test_process_order[kwargs5] PASSED    [ 80%]
examples/target_functions_test.py::test_process_order[kwargs6] PASSED    [ 81%]
examples/target_functions_test.py::test_process_order[kwargs7] FAILED    [ 83%]
examples/target_functions_test.py::test_process_order[kwargs8] PASSED    [ 85%]
examples/target_functions_test.py::test_process_order[kwargs9] FAILED    [ 86%]
examples/target_functions_test.py::test_process_order[kwargs10] FAILED   [ 88%]
examples/target_functions_test.py::test_validate_username[kwargs0] FAILED [ 90%]
examples/target_functions_test.py::test_validate_username[kwargs1] PASSED [ 91%]
examples/target_functions_test.py::test_validate_username[kwargs2] FAILED [ 93%]
examples/target_functions_test.py::test_validate_username[kwargs3] PASSED [ 95%]
examples/target_functions_test.py::test_validate_username[kwargs4] PASSED [ 96%]
examples/target_functions_test.py::test_validate_username[kwargs5] PASSED [ 98%]
examples/target_functions_test.py::test_validate_username[kwargs6] PASSED [100%]

=================================== FAILURES ===================================
______________________________ test_add[kwargs5] _______________________________

kwargs = {'a': 101, 'b': 76}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': 100, 'b': -100},
        {'_is_valid': True, 'a': -100, 'b': 76},
        {'_is_valid': True, 'a': -40, 'b': 98},
        {'_is_valid': True, 'a': 30, 'b': 0},
        {'_is_valid': True, 'a': 30, 'b': 76},
        {'_is_valid': False, 'a': 101, 'b': 76},
        {'_is_valid': False, 'a': 200, 'b': 0},
        {'_is_valid': False, 'b': 200, 'a': 30},
        {'_is_valid': False, 'b': 101, 'a': 100},
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

kwargs = {'a': 200, 'b': 0}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': 100, 'b': -100},
        {'_is_valid': True, 'a': -100, 'b': 76},
        {'_is_valid': True, 'a': -40, 'b': 98},
        {'_is_valid': True, 'a': 30, 'b': 0},
        {'_is_valid': True, 'a': 30, 'b': 76},
        {'_is_valid': False, 'a': 101, 'b': 76},
        {'_is_valid': False, 'a': 200, 'b': 0},
        {'_is_valid': False, 'b': 200, 'a': 30},
        {'_is_valid': False, 'b': 101, 'a': 100},
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

kwargs = {'a': 30, 'b': 200}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': 100, 'b': -100},
        {'_is_valid': True, 'a': -100, 'b': 76},
        {'_is_valid': True, 'a': -40, 'b': 98},
        {'_is_valid': True, 'a': 30, 'b': 0},
        {'_is_valid': True, 'a': 30, 'b': 76},
        {'_is_valid': False, 'a': 101, 'b': 76},
        {'_is_valid': False, 'a': 200, 'b': 0},
        {'_is_valid': False, 'b': 200, 'a': 30},
        {'_is_valid': False, 'b': 101, 'a': 100},
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

kwargs = {'a': 100, 'b': 101}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': 100, 'b': -100},
        {'_is_valid': True, 'a': -100, 'b': 76},
        {'_is_valid': True, 'a': -40, 'b': 98},
        {'_is_valid': True, 'a': 30, 'b': 0},
        {'_is_valid': True, 'a': 30, 'b': 76},
        {'_is_valid': False, 'a': 101, 'b': 76},
        {'_is_valid': False, 'a': 200, 'b': 0},
        {'_is_valid': False, 'b': 200, 'a': 30},
        {'_is_valid': False, 'b': 101, 'a': 100},
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

kwargs = {'a': -100.1, 'b': -100.0}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': 16.200943935103496, 'b': 100.0},
        {'_is_valid': True, 'a': 10.594161950805955, 'b': -40.09754562579464},
        {'_is_valid': True, 'a': 1.8280843846884665, 'b': -61.88974481834286},
        {'_is_valid': True, 'a': 10.594161950805955, 'b': -40.09754562579464},
        {'_is_valid': True, 'a': -93.34848181008897, 'b': 100.0},
        {'_is_valid': False, 'a': -100.1, 'b': -100.0},
        {'_is_valid': False, 'a': -200.0, 'b': -61.88974481834286},
        {'_is_valid': False, 'b': 200.0, 'a': -100.0},
        {'_is_valid': False, 'b': 200.0, 'a': -68.43709266255145},
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

kwargs = {'a': -200.0, 'b': -61.88974481834286}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': 16.200943935103496, 'b': 100.0},
        {'_is_valid': True, 'a': 10.594161950805955, 'b': -40.09754562579464},
        {'_is_valid': True, 'a': 1.8280843846884665, 'b': -61.88974481834286},
        {'_is_valid': True, 'a': 10.594161950805955, 'b': -40.09754562579464},
        {'_is_valid': True, 'a': -93.34848181008897, 'b': 100.0},
        {'_is_valid': False, 'a': -100.1, 'b': -100.0},
        {'_is_valid': False, 'a': -200.0, 'b': -61.88974481834286},
        {'_is_valid': False, 'b': 200.0, 'a': -100.0},
        {'_is_valid': False, 'b': 200.0, 'a': -68.43709266255145},
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

kwargs = {'a': -100.0, 'b': 200.0}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': 16.200943935103496, 'b': 100.0},
        {'_is_valid': True, 'a': 10.594161950805955, 'b': -40.09754562579464},
        {'_is_valid': True, 'a': 1.8280843846884665, 'b': -61.88974481834286},
        {'_is_valid': True, 'a': 10.594161950805955, 'b': -40.09754562579464},
        {'_is_valid': True, 'a': -93.34848181008897, 'b': 100.0},
        {'_is_valid': False, 'a': -100.1, 'b': -100.0},
        {'_is_valid': False, 'a': -200.0, 'b': -61.88974481834286},
        {'_is_valid': False, 'b': 200.0, 'a': -100.0},
        {'_is_valid': False, 'b': 200.0, 'a': -68.43709266255145},
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

kwargs = {'a': -68.43709266255145, 'b': 200.0}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': 16.200943935103496, 'b': 100.0},
        {'_is_valid': True, 'a': 10.594161950805955, 'b': -40.09754562579464},
        {'_is_valid': True, 'a': 1.8280843846884665, 'b': -61.88974481834286},
        {'_is_valid': True, 'a': 10.594161950805955, 'b': -40.09754562579464},
        {'_is_valid': True, 'a': -93.34848181008897, 'b': 100.0},
        {'_is_valid': False, 'a': -100.1, 'b': -100.0},
        {'_is_valid': False, 'a': -200.0, 'b': -61.88974481834286},
        {'_is_valid': False, 'b': 200.0, 'a': -100.0},
        {'_is_valid': False, 'b': 200.0, 'a': -68.43709266255145},
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

kwargs = {'name': 'aaaaaa'}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'name': '0'},
        {'_is_valid': True, 'name': '6csid'},
        {'_is_valid': True, 'name': '6csid'},
        {'_is_valid': True, 'name': 'dk1l'},
        {'_is_valid': True, 'name': 'euuw'},
        {'_is_valid': False, 'name': 'aaaaaa'},
        {'_is_valid': False, 'name': 'aaaaaa'},
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

kwargs = {'name': 'aaaaaa'}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'name': '0'},
        {'_is_valid': True, 'name': '6csid'},
        {'_is_valid': True, 'name': '6csid'},
        {'_is_valid': True, 'name': 'dk1l'},
        {'_is_valid': True, 'name': 'euuw'},
        {'_is_valid': False, 'name': 'aaaaaa'},
        {'_is_valid': False, 'name': 'aaaaaa'},
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
___________________________ test_check_age[kwargs3] ____________________________

kwargs = {'age': 130}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'age': 64},
        {'_is_valid': True, 'age': 28},
        {'_is_valid': True, 'age': 64},
        {'_is_valid': True, 'age': 130},
        {'_is_valid': True, 'age': 41},
        {'_is_valid': False, 'age': -101},
        {'_is_valid': False, 'age': -2},
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
        {'_is_valid': True, 'age': 64},
        {'_is_valid': True, 'age': 28},
        {'_is_valid': True, 'age': 64},
        {'_is_valid': True, 'age': 130},
        {'_is_valid': True, 'age': 41},
        {'_is_valid': False, 'age': -101},
        {'_is_valid': False, 'age': -2},
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
________________________ test_solve_quadratic[kwargs1] _________________________

kwargs = {'a': -10.0, 'b': 2.8954299458492976, 'c': -7.039896007606603}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': -2.0414739940551936, 'b': -9.518278041164281, 'c': -4.235904262307624},
        {'_is_valid': True, 'a': -10.0, 'b': 2.8954299458492976, 'c': -7.039896007606603},
        {'_is_valid': True, 'a': 7.96289970187734, 'b': 2.8954299458492976, 'c': 10.0},
        {'_is_valid': True, 'a': 7.855719411846987, 'b': 10.0, 'c': -6.407219104304205},
        {'_is_valid': True, 'a': 6.7728000163553865, 'b': -7.23788688170665, 'c': -7.039896007606603},
        {'_is_valid': False, 'a': 110.0, 'b': 2.8954299458492976, 'c': -10.0},
        {'_is_valid': False, 'a': 10.1, 'b': -9.518278041164281, 'c': -0.18210431935722227},
        {'_is_valid': False, 'b': -110.0, 'a': 10.0, 'c': -7.039896007606603},
        {'_is_valid': False, 'b': -110.0, 'a': 8.437785602473667, 'c': -9.662920836907734},
        {'_is_valid': False, 'c': 110.0, 'a': 8.437785602473667, 'b': -7.23788688170665},
        {'_is_valid': False, 'c': 110.0, 'a': 6.7728000163553865, 'b': 1.3209488265010663},
    ])
    def test_solve_quadratic(kwargs):
        # Generated test for solve_quadratic
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
>               solve_quadratic(**kwargs)

examples/target_functions_test.py:119: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

a = -10.0, b = 2.8954299458492976, c = -7.039896007606603

    def solve_quadratic(a: float, b: float, c: float):
        """
        Solves the quadratic equation ax^2 + bx + c = 0.
        Returns a tuple of roots.
        """
        import math
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
    
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
>           raise ValueError("Discriminant is negative, no real roots.")
E           ValueError: Discriminant is negative, no real roots.

examples/target_functions.py:34: ValueError

During handling of the above exception, another exception occurred:

kwargs = {'a': -10.0, 'b': 2.8954299458492976, 'c': -7.039896007606603}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': -2.0414739940551936, 'b': -9.518278041164281, 'c': -4.235904262307624},
        {'_is_valid': True, 'a': -10.0, 'b': 2.8954299458492976, 'c': -7.039896007606603},
        {'_is_valid': True, 'a': 7.96289970187734, 'b': 2.8954299458492976, 'c': 10.0},
        {'_is_valid': True, 'a': 7.855719411846987, 'b': 10.0, 'c': -6.407219104304205},
        {'_is_valid': True, 'a': 6.7728000163553865, 'b': -7.23788688170665, 'c': -7.039896007606603},
        {'_is_valid': False, 'a': 110.0, 'b': 2.8954299458492976, 'c': -10.0},
        {'_is_valid': False, 'a': 10.1, 'b': -9.518278041164281, 'c': -0.18210431935722227},
        {'_is_valid': False, 'b': -110.0, 'a': 10.0, 'c': -7.039896007606603},
        {'_is_valid': False, 'b': -110.0, 'a': 8.437785602473667, 'c': -9.662920836907734},
        {'_is_valid': False, 'c': 110.0, 'a': 8.437785602473667, 'b': -7.23788688170665},
        {'_is_valid': False, 'c': 110.0, 'a': 6.7728000163553865, 'b': 1.3209488265010663},
    ])
    def test_solve_quadratic(kwargs):
        # Generated test for solve_quadratic
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
                solve_quadratic(**kwargs)
            except Exception as e:
>               pytest.fail(f'Function solve_quadratic raised exception on valid input: {e}')
E               Failed: Function solve_quadratic raised exception on valid input: Discriminant is negative, no real roots.

examples/target_functions_test.py:121: Failed
________________________ test_solve_quadratic[kwargs2] _________________________

kwargs = {'a': 7.96289970187734, 'b': 2.8954299458492976, 'c': 10.0}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': -2.0414739940551936, 'b': -9.518278041164281, 'c': -4.235904262307624},
        {'_is_valid': True, 'a': -10.0, 'b': 2.8954299458492976, 'c': -7.039896007606603},
        {'_is_valid': True, 'a': 7.96289970187734, 'b': 2.8954299458492976, 'c': 10.0},
        {'_is_valid': True, 'a': 7.855719411846987, 'b': 10.0, 'c': -6.407219104304205},
        {'_is_valid': True, 'a': 6.7728000163553865, 'b': -7.23788688170665, 'c': -7.039896007606603},
        {'_is_valid': False, 'a': 110.0, 'b': 2.8954299458492976, 'c': -10.0},
        {'_is_valid': False, 'a': 10.1, 'b': -9.518278041164281, 'c': -0.18210431935722227},
        {'_is_valid': False, 'b': -110.0, 'a': 10.0, 'c': -7.039896007606603},
        {'_is_valid': False, 'b': -110.0, 'a': 8.437785602473667, 'c': -9.662920836907734},
        {'_is_valid': False, 'c': 110.0, 'a': 8.437785602473667, 'b': -7.23788688170665},
        {'_is_valid': False, 'c': 110.0, 'a': 6.7728000163553865, 'b': 1.3209488265010663},
    ])
    def test_solve_quadratic(kwargs):
        # Generated test for solve_quadratic
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
>               solve_quadratic(**kwargs)

examples/target_functions_test.py:119: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

a = 7.96289970187734, b = 2.8954299458492976, c = 10.0

    def solve_quadratic(a: float, b: float, c: float):
        """
        Solves the quadratic equation ax^2 + bx + c = 0.
        Returns a tuple of roots.
        """
        import math
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
    
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
>           raise ValueError("Discriminant is negative, no real roots.")
E           ValueError: Discriminant is negative, no real roots.

examples/target_functions.py:34: ValueError

During handling of the above exception, another exception occurred:

kwargs = {'a': 7.96289970187734, 'b': 2.8954299458492976, 'c': 10.0}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': -2.0414739940551936, 'b': -9.518278041164281, 'c': -4.235904262307624},
        {'_is_valid': True, 'a': -10.0, 'b': 2.8954299458492976, 'c': -7.039896007606603},
        {'_is_valid': True, 'a': 7.96289970187734, 'b': 2.8954299458492976, 'c': 10.0},
        {'_is_valid': True, 'a': 7.855719411846987, 'b': 10.0, 'c': -6.407219104304205},
        {'_is_valid': True, 'a': 6.7728000163553865, 'b': -7.23788688170665, 'c': -7.039896007606603},
        {'_is_valid': False, 'a': 110.0, 'b': 2.8954299458492976, 'c': -10.0},
        {'_is_valid': False, 'a': 10.1, 'b': -9.518278041164281, 'c': -0.18210431935722227},
        {'_is_valid': False, 'b': -110.0, 'a': 10.0, 'c': -7.039896007606603},
        {'_is_valid': False, 'b': -110.0, 'a': 8.437785602473667, 'c': -9.662920836907734},
        {'_is_valid': False, 'c': 110.0, 'a': 8.437785602473667, 'b': -7.23788688170665},
        {'_is_valid': False, 'c': 110.0, 'a': 6.7728000163553865, 'b': 1.3209488265010663},
    ])
    def test_solve_quadratic(kwargs):
        # Generated test for solve_quadratic
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
                solve_quadratic(**kwargs)
            except Exception as e:
>               pytest.fail(f'Function solve_quadratic raised exception on valid input: {e}')
E               Failed: Function solve_quadratic raised exception on valid input: Discriminant is negative, no real roots.

examples/target_functions_test.py:121: Failed
________________________ test_solve_quadratic[kwargs5] _________________________

kwargs = {'a': 110.0, 'b': 2.8954299458492976, 'c': -10.0}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': -2.0414739940551936, 'b': -9.518278041164281, 'c': -4.235904262307624},
        {'_is_valid': True, 'a': -10.0, 'b': 2.8954299458492976, 'c': -7.039896007606603},
        {'_is_valid': True, 'a': 7.96289970187734, 'b': 2.8954299458492976, 'c': 10.0},
        {'_is_valid': True, 'a': 7.855719411846987, 'b': 10.0, 'c': -6.407219104304205},
        {'_is_valid': True, 'a': 6.7728000163553865, 'b': -7.23788688170665, 'c': -7.039896007606603},
        {'_is_valid': False, 'a': 110.0, 'b': 2.8954299458492976, 'c': -10.0},
        {'_is_valid': False, 'a': 10.1, 'b': -9.518278041164281, 'c': -0.18210431935722227},
        {'_is_valid': False, 'b': -110.0, 'a': 10.0, 'c': -7.039896007606603},
        {'_is_valid': False, 'b': -110.0, 'a': 8.437785602473667, 'c': -9.662920836907734},
        {'_is_valid': False, 'c': 110.0, 'a': 8.437785602473667, 'b': -7.23788688170665},
        {'_is_valid': False, 'c': 110.0, 'a': 6.7728000163553865, 'b': 1.3209488265010663},
    ])
    def test_solve_quadratic(kwargs):
        # Generated test for solve_quadratic
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
                solve_quadratic(**kwargs)
            except Exception as e:
                pytest.fail(f'Function solve_quadratic raised exception on valid input: {e}')
        else:
            # Expect failure
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:124: Failed
________________________ test_solve_quadratic[kwargs6] _________________________

kwargs = {'a': 10.1, 'b': -9.518278041164281, 'c': -0.18210431935722227}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': -2.0414739940551936, 'b': -9.518278041164281, 'c': -4.235904262307624},
        {'_is_valid': True, 'a': -10.0, 'b': 2.8954299458492976, 'c': -7.039896007606603},
        {'_is_valid': True, 'a': 7.96289970187734, 'b': 2.8954299458492976, 'c': 10.0},
        {'_is_valid': True, 'a': 7.855719411846987, 'b': 10.0, 'c': -6.407219104304205},
        {'_is_valid': True, 'a': 6.7728000163553865, 'b': -7.23788688170665, 'c': -7.039896007606603},
        {'_is_valid': False, 'a': 110.0, 'b': 2.8954299458492976, 'c': -10.0},
        {'_is_valid': False, 'a': 10.1, 'b': -9.518278041164281, 'c': -0.18210431935722227},
        {'_is_valid': False, 'b': -110.0, 'a': 10.0, 'c': -7.039896007606603},
        {'_is_valid': False, 'b': -110.0, 'a': 8.437785602473667, 'c': -9.662920836907734},
        {'_is_valid': False, 'c': 110.0, 'a': 8.437785602473667, 'b': -7.23788688170665},
        {'_is_valid': False, 'c': 110.0, 'a': 6.7728000163553865, 'b': 1.3209488265010663},
    ])
    def test_solve_quadratic(kwargs):
        # Generated test for solve_quadratic
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
                solve_quadratic(**kwargs)
            except Exception as e:
                pytest.fail(f'Function solve_quadratic raised exception on valid input: {e}')
        else:
            # Expect failure
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:124: Failed
________________________ test_solve_quadratic[kwargs7] _________________________

kwargs = {'a': 10.0, 'b': -110.0, 'c': -7.039896007606603}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': -2.0414739940551936, 'b': -9.518278041164281, 'c': -4.235904262307624},
        {'_is_valid': True, 'a': -10.0, 'b': 2.8954299458492976, 'c': -7.039896007606603},
        {'_is_valid': True, 'a': 7.96289970187734, 'b': 2.8954299458492976, 'c': 10.0},
        {'_is_valid': True, 'a': 7.855719411846987, 'b': 10.0, 'c': -6.407219104304205},
        {'_is_valid': True, 'a': 6.7728000163553865, 'b': -7.23788688170665, 'c': -7.039896007606603},
        {'_is_valid': False, 'a': 110.0, 'b': 2.8954299458492976, 'c': -10.0},
        {'_is_valid': False, 'a': 10.1, 'b': -9.518278041164281, 'c': -0.18210431935722227},
        {'_is_valid': False, 'b': -110.0, 'a': 10.0, 'c': -7.039896007606603},
        {'_is_valid': False, 'b': -110.0, 'a': 8.437785602473667, 'c': -9.662920836907734},
        {'_is_valid': False, 'c': 110.0, 'a': 8.437785602473667, 'b': -7.23788688170665},
        {'_is_valid': False, 'c': 110.0, 'a': 6.7728000163553865, 'b': 1.3209488265010663},
    ])
    def test_solve_quadratic(kwargs):
        # Generated test for solve_quadratic
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
                solve_quadratic(**kwargs)
            except Exception as e:
                pytest.fail(f'Function solve_quadratic raised exception on valid input: {e}')
        else:
            # Expect failure
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:124: Failed
________________________ test_solve_quadratic[kwargs8] _________________________

kwargs = {'a': 8.437785602473667, 'b': -110.0, 'c': -9.662920836907734}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'a': -2.0414739940551936, 'b': -9.518278041164281, 'c': -4.235904262307624},
        {'_is_valid': True, 'a': -10.0, 'b': 2.8954299458492976, 'c': -7.039896007606603},
        {'_is_valid': True, 'a': 7.96289970187734, 'b': 2.8954299458492976, 'c': 10.0},
        {'_is_valid': True, 'a': 7.855719411846987, 'b': 10.0, 'c': -6.407219104304205},
        {'_is_valid': True, 'a': 6.7728000163553865, 'b': -7.23788688170665, 'c': -7.039896007606603},
        {'_is_valid': False, 'a': 110.0, 'b': 2.8954299458492976, 'c': -10.0},
        {'_is_valid': False, 'a': 10.1, 'b': -9.518278041164281, 'c': -0.18210431935722227},
        {'_is_valid': False, 'b': -110.0, 'a': 10.0, 'c': -7.039896007606603},
        {'_is_valid': False, 'b': -110.0, 'a': 8.437785602473667, 'c': -9.662920836907734},
        {'_is_valid': False, 'c': 110.0, 'a': 8.437785602473667, 'b': -7.23788688170665},
        {'_is_valid': False, 'c': 110.0, 'a': 6.7728000163553865, 'b': 1.3209488265010663},
    ])
    def test_solve_quadratic(kwargs):
        # Generated test for solve_quadratic
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
                solve_quadratic(**kwargs)
            except Exception as e:
                pytest.fail(f'Function solve_quadratic raised exception on valid input: {e}')
        else:
            # Expect failure
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:124: Failed
_________________________ test_process_order[kwargs7] __________________________

kwargs = {'member': False, 'price': 1000.1, 'quantity': 1}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'quantity': 1, 'price': 982.5090119586471, 'member': True},
        {'_is_valid': True, 'quantity': 100, 'price': 1000.0, 'member': False},
        {'_is_valid': True, 'quantity': 1, 'price': 359.59221383006803, 'member': False},
        {'_is_valid': True, 'quantity': 70, 'price': 707.1327348965718, 'member': False},
        {'_is_valid': True, 'quantity': 3, 'price': 359.59221383006803, 'member': True},
        {'_is_valid': False, 'quantity': 200, 'price': 1000.0, 'member': True},
        {'_is_valid': False, 'quantity': 0, 'price': 1000.0, 'member': False},
        {'_is_valid': False, 'price': 1000.1, 'quantity': 1, 'member': False},
        {'_is_valid': False, 'price': 0.0, 'quantity': 50, 'member': False},
        {'_is_valid': False, 'member': 'None', 'quantity': 1, 'price': 982.5090119586471},
        {'_is_valid': False, 'member': 'None', 'quantity': 3, 'price': 982.5090119586471},
    ])
    def test_process_order(kwargs):
        # Generated test for process_order
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
                process_order(**kwargs)
            except Exception as e:
                pytest.fail(f'Function process_order raised exception on valid input: {e}')
        else:
            # Expect failure
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:151: Failed
_________________________ test_process_order[kwargs9] __________________________

kwargs = {'member': 'None', 'price': 982.5090119586471, 'quantity': 1}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'quantity': 1, 'price': 982.5090119586471, 'member': True},
        {'_is_valid': True, 'quantity': 100, 'price': 1000.0, 'member': False},
        {'_is_valid': True, 'quantity': 1, 'price': 359.59221383006803, 'member': False},
        {'_is_valid': True, 'quantity': 70, 'price': 707.1327348965718, 'member': False},
        {'_is_valid': True, 'quantity': 3, 'price': 359.59221383006803, 'member': True},
        {'_is_valid': False, 'quantity': 200, 'price': 1000.0, 'member': True},
        {'_is_valid': False, 'quantity': 0, 'price': 1000.0, 'member': False},
        {'_is_valid': False, 'price': 1000.1, 'quantity': 1, 'member': False},
        {'_is_valid': False, 'price': 0.0, 'quantity': 50, 'member': False},
        {'_is_valid': False, 'member': 'None', 'quantity': 1, 'price': 982.5090119586471},
        {'_is_valid': False, 'member': 'None', 'quantity': 3, 'price': 982.5090119586471},
    ])
    def test_process_order(kwargs):
        # Generated test for process_order
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
                process_order(**kwargs)
            except Exception as e:
                pytest.fail(f'Function process_order raised exception on valid input: {e}')
        else:
            # Expect failure
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:151: Failed
_________________________ test_process_order[kwargs10] _________________________

kwargs = {'member': 'None', 'price': 982.5090119586471, 'quantity': 3}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'quantity': 1, 'price': 982.5090119586471, 'member': True},
        {'_is_valid': True, 'quantity': 100, 'price': 1000.0, 'member': False},
        {'_is_valid': True, 'quantity': 1, 'price': 359.59221383006803, 'member': False},
        {'_is_valid': True, 'quantity': 70, 'price': 707.1327348965718, 'member': False},
        {'_is_valid': True, 'quantity': 3, 'price': 359.59221383006803, 'member': True},
        {'_is_valid': False, 'quantity': 200, 'price': 1000.0, 'member': True},
        {'_is_valid': False, 'quantity': 0, 'price': 1000.0, 'member': False},
        {'_is_valid': False, 'price': 1000.1, 'quantity': 1, 'member': False},
        {'_is_valid': False, 'price': 0.0, 'quantity': 50, 'member': False},
        {'_is_valid': False, 'member': 'None', 'quantity': 1, 'price': 982.5090119586471},
        {'_is_valid': False, 'member': 'None', 'quantity': 3, 'price': 982.5090119586471},
    ])
    def test_process_order(kwargs):
        # Generated test for process_order
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
                process_order(**kwargs)
            except Exception as e:
                pytest.fail(f'Function process_order raised exception on valid input: {e}')
        else:
            # Expect failure
>           with pytest.raises(Exception):
                 ^^^^^^^^^^^^^^^^^^^^^^^^
E           Failed: DID NOT RAISE <class 'Exception'>

examples/target_functions_test.py:151: Failed
_______________________ test_validate_username[kwargs0] ________________________

kwargs = {'username': '8'}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'username': '8'},
        {'_is_valid': True, 'username': 'q9fkdmmlrukv'},
        {'_is_valid': True, 'username': 'z'},
        {'_is_valid': True, 'username': '2q0evs5pqxs3c'},
        {'_is_valid': True, 'username': 'glpatd'},
        {'_is_valid': False, 'username': 'bbbbbbbbbbbbbbbbbbbbbbbbb'},
        {'_is_valid': False, 'username': 'aaaaaaaaaaaaaaaa'},
    ])
    def test_validate_username(kwargs):
        # Generated test for validate_username
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
>               validate_username(**kwargs)

examples/target_functions_test.py:169: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

username = '8'

    def validate_username(username: str):
        """
        Validates a username.
        """
        if len(username) < 5:
>           raise ValueError("Username too short.")
E           ValueError: Username too short.

examples/target_functions.py:63: ValueError

During handling of the above exception, another exception occurred:

kwargs = {'username': '8'}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'username': '8'},
        {'_is_valid': True, 'username': 'q9fkdmmlrukv'},
        {'_is_valid': True, 'username': 'z'},
        {'_is_valid': True, 'username': '2q0evs5pqxs3c'},
        {'_is_valid': True, 'username': 'glpatd'},
        {'_is_valid': False, 'username': 'bbbbbbbbbbbbbbbbbbbbbbbbb'},
        {'_is_valid': False, 'username': 'aaaaaaaaaaaaaaaa'},
    ])
    def test_validate_username(kwargs):
        # Generated test for validate_username
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
                validate_username(**kwargs)
            except Exception as e:
>               pytest.fail(f'Function validate_username raised exception on valid input: {e}')
E               Failed: Function validate_username raised exception on valid input: Username too short.

examples/target_functions_test.py:171: Failed
_______________________ test_validate_username[kwargs2] ________________________

kwargs = {'username': 'z'}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'username': '8'},
        {'_is_valid': True, 'username': 'q9fkdmmlrukv'},
        {'_is_valid': True, 'username': 'z'},
        {'_is_valid': True, 'username': '2q0evs5pqxs3c'},
        {'_is_valid': True, 'username': 'glpatd'},
        {'_is_valid': False, 'username': 'bbbbbbbbbbbbbbbbbbbbbbbbb'},
        {'_is_valid': False, 'username': 'aaaaaaaaaaaaaaaa'},
    ])
    def test_validate_username(kwargs):
        # Generated test for validate_username
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
>               validate_username(**kwargs)

examples/target_functions_test.py:169: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

username = 'z'

    def validate_username(username: str):
        """
        Validates a username.
        """
        if len(username) < 5:
>           raise ValueError("Username too short.")
E           ValueError: Username too short.

examples/target_functions.py:63: ValueError

During handling of the above exception, another exception occurred:

kwargs = {'username': 'z'}

    @pytest.mark.parametrize('kwargs', [
        {'_is_valid': True, 'username': '8'},
        {'_is_valid': True, 'username': 'q9fkdmmlrukv'},
        {'_is_valid': True, 'username': 'z'},
        {'_is_valid': True, 'username': '2q0evs5pqxs3c'},
        {'_is_valid': True, 'username': 'glpatd'},
        {'_is_valid': False, 'username': 'bbbbbbbbbbbbbbbbbbbbbbbbb'},
        {'_is_valid': False, 'username': 'aaaaaaaaaaaaaaaa'},
    ])
    def test_validate_username(kwargs):
        # Generated test for validate_username
        is_valid = kwargs.pop('_is_valid', True)
    
        if is_valid:
            try:
                validate_username(**kwargs)
            except Exception as e:
>               pytest.fail(f'Function validate_username raised exception on valid input: {e}')
E               Failed: Function validate_username raised exception on valid input: Username too short.

examples/target_functions_test.py:171: Failed
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
FAILED examples/target_functions_test.py::test_check_age[kwargs3] - Failed: F...
FAILED examples/target_functions_test.py::test_solve_quadratic[kwargs1] - Fai...
FAILED examples/target_functions_test.py::test_solve_quadratic[kwargs2] - Fai...
FAILED examples/target_functions_test.py::test_solve_quadratic[kwargs5] - Fai...
FAILED examples/target_functions_test.py::test_solve_quadratic[kwargs6] - Fai...
FAILED examples/target_functions_test.py::test_solve_quadratic[kwargs7] - Fai...
FAILED examples/target_functions_test.py::test_solve_quadratic[kwargs8] - Fai...
FAILED examples/target_functions_test.py::test_process_order[kwargs7] - Faile...
FAILED examples/target_functions_test.py::test_process_order[kwargs9] - Faile...
FAILED examples/target_functions_test.py::test_process_order[kwargs10] - Fail...
FAILED examples/target_functions_test.py::test_validate_username[kwargs0] - F...
FAILED examples/target_functions_test.py::test_validate_username[kwargs2] - F...
======================== 22 failed, 39 passed in 0.17s =========================


```
</details>

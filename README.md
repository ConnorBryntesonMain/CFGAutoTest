# CFG Auto Test Generator

A tool that generates automated test cases for Python functions by modeling valid inputs as a **Context Free Grammar (CFG)**.

## Overview

This project automates the process of testing function robustness. Instead of manually writing test cases, you define the "rules" for valid inputs (e.g., "an integer between -10 and 10"). The tool converts these rules into a formal grammar and uses it to generate:
1.  **Valid Inputs**: To verify the function works as expected.
2.  **Invalid Inputs**: To verify the function correctly rejects bad data (Negative Testing).
3.  **Pytest Suite**: An executable test file.
4.  **CFG Report**: A detailed report of the grammar and detected bugs.

## Why use a Context Free Grammar (CFG)?

Using a CFG for test generation offers several theoretical and practical advantages over simple random testing (fuzzing):

1.  **Formal Definition of Validity**: A CFG provides a precise, mathematical way to define what constitutes a "valid" input. If an input can be derived from the grammar, it is valid; otherwise, it is not.
2.  **Structured Generation**: Unlike random fuzzing which generates noise, a CFG allows us to generate highly structured data. While our current examples (int, str) are simple, a CFG can easily model complex recursive structures like JSON objects, mathematical expressions, or code snippets.
3.  **Boundary Analysis**: By manipulating the grammar, we can systematically generate inputs that are "almost" valid (e.g., one character too long, one number out of range), which are often the source of edge-case bugs.
4.  **Completeness**: Theoretically, a CFG allows us to reason about the coverage of the input space. We can ensure we have generated samples from every "production rule" of the grammar.

## How It Works

### 1. Input Analysis
The tool determines the bounds for function parameters in two ways:
*   **Configuration (`config.json`)**: Explicit rules provided by the user (e.g., `min`, `max`, `charset`).
*   **Inference**: If no config is present, it inspects Python type hints (`int`, `float`, `str`) to assign default reasonable bounds.

### 2. CFG Generation
The `CFGGenerator` converts these bounds into a grammar.
*   **Valid CFG**: Productions generate values within bounds.
    *   *Example*: `S -> -10 | 0 | 10` (simplified)
*   **Invalid CFG**: Productions generate values outside bounds.
    *   *Example*: `S -> -11 | 11`

### 3. Test Generation
The `TestGenerator` "walks" the CFG to produce concrete input values. It creates a mix of:
*   **Positive Cases**: Inputs derived from the Valid CFG. Expectation: Function runs successfully.
*   **Negative Cases**: Inputs derived from the Invalid CFG. Expectation: Function raises an Exception.

### 4. Execution & Reporting
*   **Pytest**: A `.py` file is generated using `pytest.mark.parametrize` to run all cases.
*   **Report**: The tool runs the tests and generates a Markdown report detailing the CFG structure and any failures (bugs).

## Usage

### Prerequisites
```bash
pip install pytest
```

### Running the Tool
```bash
python3 main.py <target_file.py> [--config <config.json>]
```

**Example:**
```bash
python3 main.py examples/target_functions.py --config examples/config.json
```

### Output
*   `[target]_test.py`: The generated pytest file.
*   `[target]_cfg_report.md`: Report containing:
    *   The generated grammar (productions).
    *   **Test Results Summary**: A concise table showing passed/failed tests.
    *   **Detailed Failures**: Line numbers and specific error messages for each bug found.

## Features

### 1. Negative Testing
The tool automatically generates "invalid" inputs (e.g., integers out of range, strings too long) to verify that your function correctly raises exceptions. If your function accepts these invalid inputs, the test will fail, alerting you to a missing validation check.

### 2. Bug Detection & Reporting
The generated report doesn't just show the grammar; it runs the tests and reports the results. It highlights:
*   **Logic Bugs**: When valid inputs cause crashes.
*   **Validation Gaps**: When invalid inputs are accepted.
*   **Constraint Mismatches**: When the config allows values that the code rejects (or vice versa).

### 3. Complex Function Support
Handles functions with:
*   Multiple parameters (`int`, `float`, `str`, `bool`).
*   Cross-parameter constraints (e.g., quadratic equations).
*   Business logic (e.g., order processing).

## Configuration Format
```json
{
    "function_name": {
        "parameter_name": {
            "type": "int",
            "min": 0,
            "max": 100
        }
    }
}
```
Supported types: `int`, `float`, `str`.

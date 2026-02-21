# Python Calculator App

A simple command-line calculator application that performs basic arithmetic operations.

## Features

- Addition, subtraction, multiplication, and division operations
- Handle user input for numbers and operations
- Display results clearly after each calculation
- Loop to allow multiple calculations without restarting
- Error handling for invalid inputs or division by zero

## Installation

1. Make sure you have Python installed on your system (Python 3.6 or higher recommended)
2. Clone or download this repository

## Usage

1. Navigate to the directory containing the calculator app:

   ```
   cd calculator_app
   ```

2. Run the calculator:

   ```
   python main.py
   ```

3. Enter mathematical expressions when prompted (e.g., "3 + 2", "10 \* 5", "20 / 4")

4. Type 'quit', 'exit', or 'q' to exit the program

## Supported Operations

- Addition (+)
- Subtraction (-)
- Multiplication (\*)
- Division (/)

## Examples

```
Enter calculation: 3 + 2
Result: 5

Enter calculation: 10 * 5
Result: 50

Enter calculation: 20 / 4
Result: 5.0

Enter calculation: 3 - -2
Result: 5
```

## Error Handling

The calculator handles various error conditions gracefully:

- Division by zero
- Invalid operands (non-numeric values)
- Missing operands after operators
- Empty expressions
- Invalid operators

Example error messages:

```
Enter calculation: 10 / 0
Result: Error: Division by zero.

Enter calculation: 5 + abc
Result: Error: Operand must be a number.
```

## Notes

- Spaces between numbers and operators are optional
- Negative numbers are supported (e.g., "5 + -3")
- Operations are performed from left to right
- The calculator does not currently support parentheses or order of operations

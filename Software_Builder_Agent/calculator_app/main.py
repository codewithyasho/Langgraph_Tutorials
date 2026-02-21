import re


def calculate(expression):
    """Calculate the result of a mathematical expression."""
    # Tokenize the expression
    tokens = re.findall(r'-?\d+|[+\-*/]', expression)
    if len(tokens) == 0:
        return "Error: Empty expression"

    # The first token must be a number
    try:
        result = int(tokens[0])
    except ValueError:
        return "Error: The first token must be a number."

    i = 1
    while i < len(tokens):
        if i+1 >= len(tokens):
            return "Error: Missing operand after operator."

        operator = tokens[i]
        try:
            operand = int(tokens[i+1])
        except ValueError:
            return "Error: Operand must be a number."

        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            if operand == 0:
                return "Error: Division by zero."
            result /= operand
        else:
            return "Error: Unknown operator."

        i += 2

    return result


def main():
    """Main function to run the calculator."""
    print("Welcome to the Python Calculator App!")
    print("Enter expressions like '3 + 2' or '5 * 4'")
    print("Type 'quit' to exit the program")

    while True:
        # Get user input
        expression = input("\nEnter calculation: ").strip()

        # Check if user wants to quit
        if expression.lower() in ['quit', 'exit', 'q']:
            print("Thank you for using the calculator. Goodbye!")
            break

        # Handle empty input
        if not expression:
            print("Please enter a valid expression.")
            continue

        # Calculate and display result
        result = calculate(expression)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()

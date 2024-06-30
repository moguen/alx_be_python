def get_number(prompt):
    while True:
        try:
            return float(input(prompt))  # Check for the input prompt for the first and second number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    # Prompt for user input for the first and second number
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    # Prompt for user input for the operation
    operation = input("Choose the operation (+, -, *, /): ").strip()

    # Match case statement for operations
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")  # Output result message
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")  # Output result message
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")  # Output result message
        case "/":
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}.")  # Output result message
            else:
                print("Cannot divide by zero.")  # Output result message for division by zero
        case _:
            print("Invalid operation. Please choose from (+, -, *, /).")  # Output result message for invalid operation

if __name__ == "__main__":
    main()

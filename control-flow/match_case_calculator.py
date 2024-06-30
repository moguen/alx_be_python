def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def main():
    num1 = get_number("Enter the first number : ")
    num2 = get_number("Enter the second number: ")

    operation = input("choose the operation (+, -, *, /): ").strip()

    match operation:
        case"+":
            result =num1 + num2
            print(f"the result is {result}.")
        case"-":
            result = num1 - num2
            print(f"the result is {result}.")
        case"*":
            result = num1 * num2
            print(f"the result is {result}.")
        case"/":
            if num2 != 0:
                result = num1/num2
                print(f"the result is {result}.")
            else:
                print("cannot devide by 0")
        case _:
            print("Invalid operation. Please choose from (+, -, *, /).")
if __name__=="__main__":
    main()


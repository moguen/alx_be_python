def calculator():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("choose the opration (+, *, -, /): ")
    
    match operation:
      case"+":
       result = num1 + num2
       print (f"the result is {result}.")
      case"-":
       result = num1 - num2
       print(f"the result is{result}.")
      case"*":
       result = num1 * num2
       print(f"the result is {result}.")
      case"/":
       if num2 ==0:
        print("cannot devide by zero")
       else:
        result = num1 / num2
        print(f"the result is {result}.")
calculator()


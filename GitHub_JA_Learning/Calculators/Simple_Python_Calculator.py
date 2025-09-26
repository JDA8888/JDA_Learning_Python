# Python Calculator
while True:
    operator = input("Enter an operator (+ - * / ) or type 'quit' to exit: ")

    # Exit condition (case-insensitive)
    if operator.lower() == "quit":
        print("Thanks for using the calculator! Goodbye 👋")
        break

    # Ask for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid number entered. Please try again.")
        continue

    # Perform the operation
    if operator == "+":
        result = num1 + num2
        print("Result:", result)
    elif operator == "-":
        result = num1 - num2
        print("Result:", result)
    elif operator == "*":
        result = num1 * num2
        print("Result:", result)
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print(f"{operator} is not a valid operator.")
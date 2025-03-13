num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
math_operation = input("Enter the operation (+, -, *, /): ")
if math_operation == '+':
    result = num1 + num2
elif math_operation == '-':
    result = num1 - num2
elif math_operation == '*':
    result = num1 * num2
elif math_operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")

print(f"{num1} {math_operation} {num2} = {result}")
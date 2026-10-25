def calculator(num1, num2, operation):
 if operation == "+":
    result = num1 + num2    
 elif operation == "-":
    result = num1 - num2
 elif operation == "*":
    result = num1 * num2
 elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
 else:
    result = "Error: Invalid operation"
 return result    



print ("Welcome to the calculator program")
print("Enter first number: ")
print("Enter second number: ")
print("Enter operation (+, -, *, /): ")
calculator(20,10,"+")
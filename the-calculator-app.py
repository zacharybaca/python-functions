"""Task 1: Create functions for each arithmetic operation.
Task 2: Implement user input to receive numbers and an operation choice.
Task 3: Ensure your program can handle division by zero and other potential errors."""

# Task 1
def add(num1, num2):
    print('The Sum of Your Two Values is: ', num1 + num2)

def subtract(num1, num2):
    print('The Difference Between Your Two Values is: ', num1 - num2)

def multiply(num1, num2):
    print('The Product of Your Two Values is: ', num1 * num2)

def divide(num1, num2):
    if num2 != 0:
        print(f'{num2} is Divisible by {num1} This Many Times: ', num1 / num2)
    else:
        print('Cannot Divide By Zero')
        number_one = int(input("Please Input a Value for Your First Number: "))
        number_two = int(input("Please Input a Value for Your Second Number: "))
        divide(number_one, number_two)

# Task 2
number_one = int(input("Please Input a Value for Your First Number: "))
number_two = int(input("Please Input a Value for Your Second Number: "))
operation_choice = input("Would You Like to Add, Subtract, Multiply, or Divide Your Two Values? ").lower()

# Task 3
def calculate(operation, num1, num2):
    if operation == "add" and type(num1) is int and type(num2) is int:
        add(num1,num2)
    elif operation == "subtract" and type(num1) is int and type(num2) is int:
        subtract(num1,num2)
    elif operation == "multiply" and type(num1) is int and type(num2) is int:
        multiply(num1,num2)
    elif operation == "divide" and type(num1) is int and type(num2) is int:
        divide(num1,num2)
    elif type(num1) is not int and type(num2) is not int:
        print('Please Enter Valid Integers')
        number_one = int(input("Please Input a Value for Your First Number: "))
        number_two = int(input("Please Input a Value for Your Second Number: "))
        calculate(operation, number_one, number_two)
    elif operation != "add" or operation != "subtract" or operation != "multiply" or operation != "divide":
        print('Please Enter a Valid Operation')
        operation_choice = input("Would You Like to Add, Subtract, Multiply, or Divide Your Two Values? ")
        calculate(operation_choice, num1, num2)
    else:
        raise Exception("Unknown Error")
        
calculate(operation_choice, number_one, number_two)


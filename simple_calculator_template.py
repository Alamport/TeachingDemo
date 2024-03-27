"""
Topics covered:
- functions
- conditional statements
- recursion
- loops
"""

def addition(num1, num2):
        return num1 + num2

def subtraction(num1, num2):
        return num1 - num2

def multiplication(num1, num2):
        return num1 * num2

def division(num1, num2):
        return num1 / num2

def power(num1, num2):
        return num1**num2

################################################################################
# ADDITIONAL FUNCTIONS
# def square_root(num):
#         return num**(1/2)

# def square(num):
#         return num**2
################################################################################

def mod(num1, num2):
        return num1 % num2

################################################################################
def factorial(num):
        product = 1
        for num in range (1, num):
                product *= num
        return product

def factorial_while(num):
        product = 1
        while num > 1:
                product *= num
                num -= 1
        return product
################################################################################

def main():
        num1 = int(input("Input the first number: "))
        operation = input("Input the operation (+|-|*|/|**|sqrt|square): ")
        num2 = int(input("Input the second number: "))

        operations(num1, num2, operation)
        
def operations(num1, num2, operation):
        if operation == '+':
                print(addition(num1, num2))
        elif operation == '-':
                print(subtraction(num1, num2))
        elif operation == '*':
                print(multiplication(num1, num2))
        elif operation == '/':
                print(division(num1, num2))
        elif operation == "**":
                print(power(num1, num2))
        elif operation == "fact":
                print(factorial(num1))
        # elif operation == "square":
        #         print(square(num1))
        # elif operation == "sqrt":
        #         print(square_root(num1))
        else:
                operation = input("Invalid operation, try another operation (+|-|*|/|**): ")
                operations(num1, num2, operation)

main()